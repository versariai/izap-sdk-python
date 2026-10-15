"""The configured clients every generated endpoint function accepts."""

from __future__ import annotations

import asyncio
import time
from collections.abc import Mapping
from typing import Any

import httpx

from ._errors import IzapApiError
from ._generated.client import AuthenticatedClient
from ._retry import is_retryable, next_delay
from ._version import __version__

DEFAULT_BASE_URL = "https://api.izap.ai"
DEFAULT_TIMEOUT = 30.0
DEFAULT_MAX_RETRIES = 2
BUSINESS_ID_HEADER = "business-id"
USER_AGENT = f"izap-python/{__version__}"


class _RetryingHttpxClient(httpx.Client):
    """``httpx.Client`` that retries idempotent requests and raises ``IzapApiError`` on 4xx/5xx."""

    def __init__(self, *, max_retries: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._max_retries = max_retries

    def send(self, request: httpx.Request, **kwargs: Any) -> httpx.Response:
        max_retries = self._max_retries if is_retryable(request) else 0
        if max_retries:
            request.read()
        attempt = 0
        while True:
            response = super().send(request, **kwargs)
            delay = next_delay(response, attempt, max_retries)
            if delay is None:
                break
            response.close()
            time.sleep(delay)
            attempt += 1
        if response.is_error:
            response.read()
            raise IzapApiError(response)
        return response


class _RetryingAsyncHttpxClient(httpx.AsyncClient):
    """``httpx.AsyncClient`` that retries idempotent requests and raises ``IzapApiError`` on 4xx/5xx."""

    def __init__(self, *, max_retries: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._max_retries = max_retries

    async def send(self, request: httpx.Request, **kwargs: Any) -> httpx.Response:
        max_retries = self._max_retries if is_retryable(request) else 0
        if max_retries:
            await request.aread()
        attempt = 0
        while True:
            response = await super().send(request, **kwargs)
            delay = next_delay(response, attempt, max_retries)
            if delay is None:
                break
            await response.aclose()
            await asyncio.sleep(delay)
            attempt += 1
        if response.is_error:
            await response.aread()
            raise IzapApiError(response)
        return response


class Client(AuthenticatedClient):
    """An authenticated iZap API client.

    Pass it to any endpoint function in :mod:`izap.api`, as ``.sync()`` / ``.sync_detailed()``
    or ``.asyncio()`` / ``.asyncio_detailed()``::

        from izap import Client
        from izap.api.whatsapp_templates import list_whats_app_templates

        with Client("izap_pat_...", business_id="...") as client:
            templates = list_whats_app_templates.sync(client=client)

    Args:
        token: A personal access token (``izap_pat_...``), sent as ``Authorization: Bearer``.
        business_id: Sent as the ``business-id`` header, selecting the business that
            business-scoped endpoints act on. Endpoints that don't act on a business
            (e.g. token and account-creation endpoints) ignore it.
        base_url: The API origin.
        max_retries: Retries for idempotent requests (GET, HEAD, OPTIONS, PUT, DELETE) answered
            with 429, 502, 503 or 504. Waits honour ``Retry-After``, otherwise back off
            exponentially. ``0`` disables retries.
        timeout: Seconds, or an ``httpx.Timeout``, for each attempt.
        headers: Extra headers sent with every request.
        transport: A custom sync ``httpx`` transport, e.g. ``httpx.HTTPTransport(proxy=...)``.
        async_transport: A custom async ``httpx`` transport for the ``asyncio`` functions.

    Every 4xx/5xx response raises :class:`izap.IzapApiError`.
    """

    def __init__(
        self,
        token: str,
        *,
        business_id: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        max_retries: int = DEFAULT_MAX_RETRIES,
        timeout: float | httpx.Timeout | None = DEFAULT_TIMEOUT,
        headers: Mapping[str, str] | None = None,
        transport: httpx.BaseTransport | None = None,
        async_transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        if not token:
            raise ValueError("token is required: create a personal access token in User Settings -> API Keys")
        if max_retries < 0:
            raise ValueError("max_retries must be 0 or greater")

        default_headers = {"User-Agent": USER_AGENT, **(headers or {})}
        if business_id:
            default_headers[BUSINESS_ID_HEADER] = business_id

        super().__init__(
            base_url=base_url.rstrip("/"),
            token=token,
            headers=default_headers,
            timeout=timeout if isinstance(timeout, httpx.Timeout) else httpx.Timeout(timeout),
        )
        self._options: dict[str, Any] = {
            "business_id": business_id,
            "base_url": base_url,
            "max_retries": max_retries,
            "timeout": timeout,
            "headers": dict(headers or {}),
            "transport": transport,
            "async_transport": async_transport,
        }

    @property
    def business_id(self) -> str | None:
        return self._options["business_id"]

    @property
    def max_retries(self) -> int:
        return self._options["max_retries"]

    def _httpx_kwargs(self) -> dict[str, Any]:
        return {
            "max_retries": self.max_retries,
            "base_url": self._base_url,
            "headers": {**self._headers, self.auth_header_name: f"{self.prefix} {self.token}"},
            "cookies": self._cookies,
            "timeout": self._timeout,
            "verify": self._verify_ssl,
            "follow_redirects": self._follow_redirects,
        }

    def get_httpx_client(self) -> httpx.Client:
        if self._client is None:
            self._client = _RetryingHttpxClient(transport=self._options["transport"], **self._httpx_kwargs())
        return self._client

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        if self._async_client is None:
            self._async_client = _RetryingAsyncHttpxClient(
                transport=self._options["async_transport"], **self._httpx_kwargs()
            )
        return self._async_client

    def _copy(self, **changes: Any) -> Client:
        return type(self)(self.token, **{**self._options, **changes})

    def with_headers(self, headers: dict[str, str]) -> Client:
        """A new client that also sends ``headers``."""
        return self._copy(headers={**self._options["headers"], **headers})

    def with_timeout(self, timeout: httpx.Timeout) -> Client:
        """A new client with a different timeout."""
        return self._copy(timeout=timeout)

    def with_cookies(self, cookies: dict[str, str]) -> Client:
        raise NotImplementedError("The iZap API authenticates with a bearer token; it does not use cookies.")

    def with_business(self, business_id: str | None) -> Client:
        """A new client that acts on ``business_id``."""
        return self._copy(business_id=business_id)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(base_url={self._base_url!r}, business_id={self.business_id!r})"


class AsyncClient(Client):
    """:class:`Client` under the name async code expects.

    The same object drives both the sync and the ``asyncio`` endpoint functions; use it
    as ``async with AsyncClient(...) as client`` so the async connection pool is closed.
    """
