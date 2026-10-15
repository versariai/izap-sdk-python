from __future__ import annotations

import asyncio
import json
from uuid import uuid4

import httpx
import pytest

import izap
from izap import AsyncClient, Client, IzapApiError
from izap.api.api_tokens import introspect_token
from izap.api.businesses import get_current_business
from izap.api.messages import send_chat_message
from izap.api.whatsapp_templates import list_whats_app_templates
from izap.models import CreateMessageIn, PrincipalResponse, TemplateListResponse

from .conftest import TOKEN, Recorder, make_client

BUSINESS_ID = "8f0b9e2a-1c3d-4e5f-8a9b-0c1d2e3f4a5b"
OTHER_BUSINESS_ID = "2b3c4d5e-6f70-4182-93a4-b5c6d7e8f901"
TEMPLATE = {
    "id": str(uuid4()),
    "business_id": BUSINESS_ID,
    "name": "order_ready",
    "body_text": "Your order {{1}} is ready",
    "status": "approved",
    "created": "2026-09-01T12:00:00Z",
    "modified": "2026-09-02T12:00:00Z",
}


def templates_response() -> httpx.Response:
    return httpx.Response(200, json={"templates": [TEMPLATE], "total_count": 1})


class TestAuthentication:
    def test_sends_the_token_as_a_bearer_credential(self) -> None:
        recorder = Recorder(templates_response())

        list_whats_app_templates.sync(client=make_client(recorder))

        assert recorder.requests[0].headers["authorization"] == f"Bearer {TOKEN}"

    def test_identifies_the_sdk(self) -> None:
        recorder = Recorder(templates_response())

        list_whats_app_templates.sync(client=make_client(recorder))

        assert recorder.requests[0].headers["user-agent"] == f"izap-python/{izap.__version__}"

    def test_requires_a_token(self) -> None:
        with pytest.raises(ValueError, match="token"):
            Client("")

    def test_repr_does_not_leak_the_token(self) -> None:
        client = make_client(Recorder(templates_response()), business_id=BUSINESS_ID)

        assert TOKEN not in repr(client)
        assert BUSINESS_ID in repr(client)


class TestBusinessScope:
    def test_sends_the_business_id_header_when_set(self) -> None:
        recorder = Recorder(templates_response())

        list_whats_app_templates.sync(client=make_client(recorder, business_id=BUSINESS_ID))

        assert recorder.requests[0].headers["business-id"] == BUSINESS_ID

    def test_omits_the_business_id_header_when_unset(self) -> None:
        recorder = Recorder(templates_response())

        list_whats_app_templates.sync(client=make_client(recorder))

        assert "business-id" not in recorder.requests[0].headers

    def test_a_per_call_business_id_overrides_the_client(self) -> None:
        recorder = Recorder(templates_response())

        list_whats_app_templates.sync(
            client=make_client(recorder, business_id=BUSINESS_ID), business_id=OTHER_BUSINESS_ID
        )

        assert recorder.requests[0].headers["business-id"] == OTHER_BUSINESS_ID

    def test_the_business_id_argument_wins_over_a_header_of_the_same_name(self) -> None:
        recorder = Recorder(templates_response())
        client = make_client(recorder, business_id=BUSINESS_ID, headers={"business-id": OTHER_BUSINESS_ID})

        list_whats_app_templates.sync(client=client)

        assert recorder.requests[0].headers["business-id"] == BUSINESS_ID

    def test_with_business_returns_a_rescoped_copy(self) -> None:
        recorder = Recorder(templates_response())
        client = make_client(recorder, business_id=BUSINESS_ID)

        rescoped = client.with_business(OTHER_BUSINESS_ID)
        list_whats_app_templates.sync(client=rescoped)

        assert (client.business_id, rescoped.business_id) == (BUSINESS_ID, OTHER_BUSINESS_ID)
        assert recorder.requests[0].headers["business-id"] == OTHER_BUSINESS_ID
        assert recorder.requests[0].headers["authorization"] == f"Bearer {TOKEN}"

    def test_current_business_endpoints_are_scoped_by_header_not_path(self) -> None:
        recorder = Recorder(httpx.Response(404, json={"detail": "Business not found"}))

        with pytest.raises(IzapApiError):
            get_current_business.sync(client=make_client(recorder, business_id=BUSINESS_ID))

        request = recorder.requests[0]
        assert request.url.path == "/api/v1/businesses/current"
        assert BUSINESS_ID not in str(request.url)
        assert request.headers["business-id"] == BUSINESS_ID


class TestEndpoints:
    def test_parses_the_success_model(self) -> None:
        recorder = Recorder(templates_response())

        result = list_whats_app_templates.sync(client=make_client(recorder, business_id=BUSINESS_ID), status="approved")

        assert isinstance(result, TemplateListResponse)
        assert result.total_count == 1
        assert result.templates[0].name == "order_ready"
        request = recorder.requests[0]
        assert (request.method, request.url.host, request.url.path) == (
            "GET",
            "api.izap.ai",
            "/api/v1/whatsapp_templates",
        )
        assert request.url.params["status"] == "approved"

    def test_posts_a_json_body(self) -> None:
        chat_id = uuid4()
        user_message = {
            "id": str(uuid4()),
            "content": "Your order is on its way",
            "no_reply": True,
            "timestamp": "2026-09-14T12:00:00Z",
            "status": None,
            "error_code": None,
            "error_reason": None,
            "sender_user_id": None,
        }
        recorder = Recorder(httpx.Response(200, json={"user_message": user_message}))

        sent = send_chat_message.sync(
            chat_id, client=make_client(recorder), body=CreateMessageIn(content="Your order is on its way")
        )

        assert sent is not None
        assert sent.user_message.content == "Your order is on its way"
        request = recorder.requests[0]
        assert (request.method, request.url.path) == ("POST", f"/api/v1/chats/{chat_id}/messages")
        assert json.loads(request.content) == {"content": "Your order is on its way"}

    def test_async_client_calls_asyncio_endpoints(self) -> None:
        recorder = Recorder(httpx.Response(200, json={"kind": "personal_access_token"}))
        transport = httpx.MockTransport(recorder)

        async def call() -> PrincipalResponse | None:
            async with AsyncClient(TOKEN, business_id=BUSINESS_ID, async_transport=transport) as client:
                return await introspect_token.asyncio(client=client)

        principal = asyncio.run(call())

        assert principal is not None
        assert principal.kind == "personal_access_token"
        assert recorder.requests[0].headers["business-id"] == BUSINESS_ID

    def test_honours_a_custom_base_url(self) -> None:
        recorder = Recorder(httpx.Response(200, json={"kind": "personal_access_token"}))

        introspect_token.sync(client=make_client(recorder, base_url="https://staging.example.com/"))

        assert str(recorder.requests[0].url) == "https://staging.example.com/api/v1/auth/token/introspect"


class TestConfiguration:
    def test_defaults(self) -> None:
        client = Client(TOKEN)

        assert izap.DEFAULT_BASE_URL == "https://api.izap.ai"
        assert client.max_retries == 2
        assert client.get_httpx_client().timeout == httpx.Timeout(30.0)
        assert str(client.get_httpx_client().base_url) == "https://api.izap.ai"

    @pytest.mark.parametrize(
        ("timeout", "expected"),
        [(5.0, httpx.Timeout(5.0)), (httpx.Timeout(2.0, read=9.0), httpx.Timeout(2.0, read=9.0))],
    )
    def test_custom_timeout(self, timeout: float | httpx.Timeout, expected: httpx.Timeout) -> None:
        assert Client(TOKEN, timeout=timeout).get_async_httpx_client().timeout == expected

    def test_rejects_negative_max_retries(self) -> None:
        with pytest.raises(ValueError, match="max_retries"):
            Client(TOKEN, max_retries=-1)

    def test_with_headers_keeps_the_rest_of_the_configuration(self) -> None:
        recorder = Recorder(templates_response())
        client = make_client(recorder, business_id=BUSINESS_ID, max_retries=5)

        traced = client.with_headers({"x-trace-id": "abc"})
        list_whats_app_templates.sync(client=traced)

        headers = recorder.requests[0].headers
        assert (headers["x-trace-id"], headers["business-id"]) == ("abc", BUSINESS_ID)
        assert traced.max_retries == 5

    def test_with_timeout(self) -> None:
        assert Client(TOKEN).with_timeout(httpx.Timeout(1.0)).get_httpx_client().timeout == httpx.Timeout(1.0)

    def test_with_cookies_is_not_supported(self) -> None:
        with pytest.raises(NotImplementedError):
            Client(TOKEN).with_cookies({"session": "x"})
