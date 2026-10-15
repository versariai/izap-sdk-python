from __future__ import annotations

import asyncio
from uuid import uuid4

import httpx
import pytest

from izap import IzapApiError, IzapError
from izap.api.messages import send_chat_message
from izap.models import CreateMessageIn

from .conftest import Recorder, make_client


def raised_by(response: httpx.Response) -> IzapApiError:
    client = make_client(Recorder(response), max_retries=0)
    with pytest.raises(IzapApiError) as caught:
        client.get_httpx_client().get("/api/v1/whatsapp_templates")
    return caught.value


class TestErrorBodies:
    def test_string_detail(self) -> None:
        error = raised_by(httpx.Response(404, json={"detail": "Chat not found"}))

        assert (error.status, error.code, error.message, error.detail) == (
            404,
            None,
            "Chat not found",
            "Chat not found",
        )
        assert str(error) == "HTTP 404: Chat not found"

    def test_structured_detail(self) -> None:
        detail = {"code": "plan_limit_event_webhooks", "message": "Your plan does not include event webhooks."}
        error = raised_by(httpx.Response(403, json={"detail": detail}))

        assert error.code == "plan_limit_event_webhooks"
        assert error.message == "Your plan does not include event webhooks."
        assert error.detail == detail
        assert str(error) == "HTTP 403 plan_limit_event_webhooks: Your plan does not include event webhooks."

    def test_structured_detail_without_a_message_falls_back_to_the_code(self) -> None:
        error = raised_by(httpx.Response(409, json={"detail": {"code": "already_connected"}}))

        assert (error.code, error.message) == ("already_connected", "already_connected")

    def test_top_level_code_on_a_server_error(self) -> None:
        error = raised_by(httpx.Response(503, json={"detail": "Upstream unavailable", "code": "whatsapp_unavailable"}))

        assert (error.status, error.code, error.message) == (503, "whatsapp_unavailable", "Upstream unavailable")

    def test_validation_errors(self) -> None:
        detail = [
            {"loc": ["body", "content"], "msg": "Field required", "type": "missing"},
            {"loc": ["query", "page"], "msg": "Input should be greater than 0", "type": "greater_than"},
        ]
        error = raised_by(httpx.Response(422, json={"detail": detail}))

        assert error.message == "body.content: Field required; query.page: Input should be greater than 0"
        assert error.detail == detail

    def test_non_json_body(self) -> None:
        error = raised_by(httpx.Response(500, text="Internal Server Error"))

        assert (error.body, error.detail, error.code, error.message) == (None, None, None, "Internal Server Error")

    def test_empty_body_uses_the_reason_phrase(self) -> None:
        error = raised_by(httpx.Response(401))

        assert error.message == "Unauthorized"

    def test_keeps_the_response(self) -> None:
        error = raised_by(httpx.Response(400, json={"detail": "bad"}, headers={"x-trace": "abc"}))

        assert error.response.headers["x-trace"] == "abc"
        assert isinstance(error, IzapError)


class TestRaisedFromEndpoints:
    def test_sync_endpoint_raises_instead_of_returning_the_error_model(self) -> None:
        detail = [{"loc": ["body", "content"], "msg": "Field required", "type": "missing"}]
        client = make_client(Recorder(httpx.Response(422, json={"detail": detail})))

        with pytest.raises(IzapApiError) as caught:
            send_chat_message.sync(uuid4(), client=client, body=CreateMessageIn(content=""))

        assert caught.value.status == 422

    def test_async_endpoint_raises(self) -> None:
        client = make_client(Recorder(httpx.Response(404, json={"detail": "Chat not found"})))

        async def call() -> None:
            async with client:
                await send_chat_message.asyncio(uuid4(), client=client, body=CreateMessageIn(content="hi"))

        with pytest.raises(IzapApiError, match="Chat not found"):
            asyncio.run(call())
