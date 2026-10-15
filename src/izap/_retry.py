"""Retries for idempotent requests that hit 429, 502, 503 or 504."""

from __future__ import annotations

import math
import random
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime

import httpx

RETRY_STATUSES = frozenset({429, 502, 503, 504})
IDEMPOTENT_METHODS = frozenset({"GET", "HEAD", "OPTIONS", "PUT", "DELETE"})
INITIAL_DELAY = 0.5
MAX_DELAY = 8.0
MAX_RETRY_AFTER = 60.0


def is_retryable(request: httpx.Request) -> bool:
    return request.method.upper() in IDEMPOTENT_METHODS


def retry_after_seconds(response: httpx.Response) -> float | None:
    """Seconds the server asked us to wait, from a delta-seconds or HTTP-date ``Retry-After``."""
    value = response.headers.get("retry-after")
    if value is None:
        return None
    value = value.strip()
    try:
        seconds = float(value)
    except ValueError:
        try:
            when = parsedate_to_datetime(value)
        except (TypeError, ValueError, IndexError):
            return None
        if when.tzinfo is None:
            when = when.replace(tzinfo=UTC)
        seconds = (when - datetime.now(UTC)).total_seconds()
    if not math.isfinite(seconds):
        return None
    return max(seconds, 0.0)


def backoff(attempt: int) -> float:
    """Exponential backoff with jitter: 0.5s, 1s, 2s, ... capped at 8s, each scaled by 50-100%."""
    return min(MAX_DELAY, INITIAL_DELAY * 2**attempt) * (0.5 + random.random() / 2)


def next_delay(response: httpx.Response, attempt: int, max_retries: int) -> float | None:
    """How long to wait before retrying ``response``, or ``None`` to stop and return it.

    A ``Retry-After`` longer than ``MAX_RETRY_AFTER`` stops retrying rather than waiting
    that long inside a request call.
    """
    if attempt >= max_retries or response.status_code not in RETRY_STATUSES:
        return None
    retry_after = retry_after_seconds(response)
    if retry_after is None:
        return backoff(attempt)
    return retry_after if retry_after <= MAX_RETRY_AFTER else None
