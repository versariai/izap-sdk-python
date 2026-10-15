"""Exceptions raised by the SDK."""

from __future__ import annotations

from typing import Any

import httpx

_MAX_TEXT_MESSAGE = 500


class IzapError(Exception):
    """Base class for every exception the SDK raises."""


class IzapApiError(IzapError):
    """The API answered with a 4xx or 5xx status.

    Attributes:
        status: The HTTP status code.
        code: The machine-readable error code when the API sent one, from ``detail.code``
            or, on some 5xx responses, a top-level ``code``.
        message: A human-readable summary of the error.
        detail: The raw ``detail`` value: a string, a ``{"code", "message", ...}`` object,
            or the list of validation errors a 422 carries. ``None`` when the body had none.
        body: The decoded JSON body, or ``None`` when the body was not JSON.
        response: The underlying ``httpx.Response``.
    """

    status: int
    code: str | None
    message: str
    detail: Any
    body: Any
    response: httpx.Response

    def __init__(self, response: httpx.Response) -> None:
        self.response = response
        self.status = response.status_code
        self.body = _json_body(response)
        self.detail, self.code, self.message = _describe(self.body, response)
        code = f" {self.code}" if self.code else ""
        super().__init__(f"HTTP {self.status}{code}: {self.message}")


def _json_body(response: httpx.Response) -> Any:
    try:
        return response.json()
    except ValueError:
        return None


def _string(value: Any) -> str | None:
    return value if isinstance(value, str) and value else None


def _validation_summary(errors: list[Any]) -> str:
    parts = []
    for error in errors:
        if not isinstance(error, dict):
            continue
        location = ".".join(str(part) for part in error.get("loc", []))
        message = _string(error.get("msg")) or "invalid"
        parts.append(f"{location}: {message}" if location else message)
    return "; ".join(parts)


def _describe(body: Any, response: httpx.Response) -> tuple[Any, str | None, str]:
    """Split a FastAPI error body into ``(detail, code, message)``."""
    fallback = response.reason_phrase or "Request failed"
    if not isinstance(body, dict):
        text = response.text.strip()
        return None, None, text[:_MAX_TEXT_MESSAGE] if text else fallback

    detail = body.get("detail")
    top_level_code = _string(body.get("code"))
    if isinstance(detail, str):
        return detail, top_level_code, detail or fallback
    if isinstance(detail, dict):
        code = _string(detail.get("code")) or top_level_code
        return detail, code, _string(detail.get("message")) or code or fallback
    if isinstance(detail, list):
        return detail, top_level_code, _validation_summary(detail) or fallback
    return detail, top_level_code, _string(body.get("message")) or fallback
