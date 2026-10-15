from __future__ import annotations

import asyncio
import time
from email.utils import formatdate

import httpx
import pytest

from izap import AsyncClient, IzapApiError

from .conftest import Recorder, make_client

OK = httpx.Response(200, json={"ok": True})


class TestRetriedRequests:
    @pytest.mark.parametrize("status", [429, 502, 503, 504])
    def test_retries_an_idempotent_request_on_a_retryable_status(self, status: int, sleeps: list[float]) -> None:
        recorder = Recorder(httpx.Response(status), OK)

        response = make_client(recorder).get_httpx_client().get("/api/v1/transmissions")

        assert response.status_code == 200
        assert len(recorder.requests) == 2
        assert len(sleeps) == 1

    @pytest.mark.parametrize("method", ["GET", "HEAD", "OPTIONS", "PUT", "DELETE"])
    def test_retries_every_idempotent_method(self, method: str, sleeps: list[float]) -> None:
        recorder = Recorder(httpx.Response(503), httpx.Response(204))

        response = make_client(recorder).get_httpx_client().request(method, "/api/v1/whatsapp_templates/t")

        assert response.status_code == 204
        assert [r.method for r in recorder.requests] == [method, method]

    def test_resends_the_same_body(self, sleeps: list[float]) -> None:
        recorder = Recorder(httpx.Response(502), OK)

        make_client(recorder).get_httpx_client().put("/api/v1/chats/c/status", json={"status": "closed"})

        assert [r.content for r in recorder.requests] == [b'{"status":"closed"}'] * 2

    def test_backs_off_exponentially_with_jitter(self, sleeps: list[float]) -> None:
        recorder = Recorder(httpx.Response(503), httpx.Response(503), httpx.Response(503), OK)

        make_client(recorder, max_retries=3).get_httpx_client().get("/api/v1/transmissions")

        assert len(sleeps) == 3
        for attempt, delay in enumerate(sleeps):
            assert 0.25 * 2**attempt <= delay <= 0.5 * 2**attempt

    def test_gives_up_after_max_retries(self, sleeps: list[float]) -> None:
        recorder = Recorder(httpx.Response(503, json={"detail": "busy"}))

        with pytest.raises(IzapApiError) as caught:
            make_client(recorder, max_retries=2).get_httpx_client().get("/api/v1/transmissions")

        assert caught.value.status == 503
        assert len(recorder.requests) == 3
        assert len(sleeps) == 2


class TestRequestsNotRetried:
    @pytest.mark.parametrize("method", ["POST", "PATCH", "TRACE"])
    def test_never_retries_a_non_idempotent_method(self, method: str, sleeps: list[float]) -> None:
        recorder = Recorder(httpx.Response(503))

        with pytest.raises(IzapApiError):
            make_client(recorder).get_httpx_client().request(method, "/api/v1/chats/c/messages", json={"content": "hi"})

        assert len(recorder.requests) == 1
        assert sleeps == []

    @pytest.mark.parametrize("status", [400, 401, 403, 404, 409, 422, 500])
    def test_does_not_retry_other_errors(self, status: int, sleeps: list[float]) -> None:
        recorder = Recorder(httpx.Response(status))

        with pytest.raises(IzapApiError):
            make_client(recorder).get_httpx_client().get("/api/v1/transmissions")

        assert len(recorder.requests) == 1
        assert sleeps == []

    def test_zero_max_retries_disables_retries(self, sleeps: list[float]) -> None:
        recorder = Recorder(httpx.Response(503))

        with pytest.raises(IzapApiError):
            make_client(recorder, max_retries=0).get_httpx_client().get("/api/v1/transmissions")

        assert len(recorder.requests) == 1


class TestRetryAfter:
    def test_waits_the_seconds_the_server_asks_for(self, sleeps: list[float]) -> None:
        recorder = Recorder(httpx.Response(429, headers={"Retry-After": "3"}), OK)

        make_client(recorder).get_httpx_client().get("/api/v1/transmissions")

        assert sleeps == [3.0]

    def test_waits_until_an_http_date(self, sleeps: list[float]) -> None:
        retry_at = formatdate(time.time() + 10, usegmt=True)
        recorder = Recorder(httpx.Response(503, headers={"Retry-After": retry_at}), OK)

        make_client(recorder).get_httpx_client().get("/api/v1/transmissions")

        assert len(sleeps) == 1
        assert 8.0 <= sleeps[0] <= 10.0

    def test_stops_when_the_server_asks_for_longer_than_a_minute(self, sleeps: list[float]) -> None:
        recorder = Recorder(httpx.Response(429, headers={"Retry-After": "120"}), OK)

        with pytest.raises(IzapApiError) as caught:
            make_client(recorder).get_httpx_client().get("/api/v1/transmissions")

        assert caught.value.status == 429
        assert len(recorder.requests) == 1
        assert sleeps == []

    @pytest.mark.parametrize("value", ["soon", "nan", "inf", ""])
    def test_falls_back_to_backoff_on_an_unusable_header(self, value: str, sleeps: list[float]) -> None:
        recorder = Recorder(httpx.Response(503, headers={"Retry-After": value}), OK)

        make_client(recorder).get_httpx_client().get("/api/v1/transmissions")

        assert len(sleeps) == 1
        assert 0.25 <= sleeps[0] <= 0.5


class TestAsyncRetries:
    def test_retries_through_the_async_client(self, sleeps: list[float]) -> None:
        recorder = Recorder(httpx.Response(504), httpx.Response(429, headers={"Retry-After": "1"}), OK)
        transport = httpx.MockTransport(recorder)

        async def call() -> httpx.Response:
            async with AsyncClient("izap_pat_test", async_transport=transport) as client:
                return await client.get_async_httpx_client().get("/api/v1/transmissions")

        assert asyncio.run(call()).status_code == 200
        assert len(recorder.requests) == 3
        assert sleeps[1] == 1.0

    def test_async_client_does_not_retry_post(self, sleeps: list[float]) -> None:
        recorder = Recorder(httpx.Response(503))
        transport = httpx.MockTransport(recorder)

        async def call() -> None:
            async with AsyncClient("izap_pat_test", async_transport=transport) as client:
                await client.get_async_httpx_client().post("/api/v1/transmissions/preview", json={})

        with pytest.raises(IzapApiError):
            asyncio.run(call())
        assert len(recorder.requests) == 1
