from __future__ import annotations

import asyncio
import time
from typing import Any

import httpx
import pytest

from izap import Client

TOKEN = "izap_pat_test_0123456789"


class Recorder:
    """A ``MockTransport`` handler that replays queued responses and records each request.

    Once a single response is left it is replayed for every further request. Each reply
    is a fresh copy: httpx binds a sent response's stream to the client that sent it.
    """

    def __init__(self, *responses: httpx.Response) -> None:
        self.responses = list(responses)
        self.requests: list[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        request.read()
        self.requests.append(request)
        template = self.responses.pop(0) if len(self.responses) > 1 else self.responses[0]
        return httpx.Response(template.status_code, headers=template.headers, content=template.read())


def make_client(recorder: Recorder, **kwargs: Any) -> Client:
    transport = httpx.MockTransport(recorder)
    return Client(TOKEN, transport=transport, async_transport=transport, **kwargs)


@pytest.fixture
def sleeps(monkeypatch: pytest.MonkeyPatch) -> list[float]:
    """Record retry waits instead of sleeping through them."""
    recorded: list[float] = []

    async def fake_async_sleep(delay: float) -> None:
        recorded.append(delay)

    monkeypatch.setattr(time, "sleep", recorded.append)
    monkeypatch.setattr(asyncio, "sleep", fake_async_sleep)
    return recorded
