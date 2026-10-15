"""Verify iZap webhook deliveries.

Every delivery carries ``izap-webhook-signature: v1=<hex>``, where ``<hex>`` is the
HMAC-SHA256 of ``"{izap-webhook-timestamp}.{raw body}"`` keyed with the endpoint's
signing secret (``izap_whsec_...``). Deliveries also carry a stronger
``izap-webhook-signature-v2: v2=<hex>``, the HMAC-SHA256 of
``"{izap-webhook-id}.{izap-webhook-timestamp}.{raw body}"`` under the same secret: it
additionally covers the delivery id, closing a gap in v1 where a captured delivery could
be replayed under a new id within the timestamp tolerance. See
https://devs.izap.ai/en/api-reference/webhooks.

    event = izap.webhooks.verify(request_body_bytes, request.headers, secret)

``verify`` requires ``izap-webhook-signature-v2`` by default (the stronger check).
Pass ``allow_v1=True`` to accept a v1-only delivery when that header is absent, for
senders from before v2 existed. A captured delivery always includes both headers, so
falling back whenever v2 is missing would let a replay strip v2 and reuse the v1 HMAC
under a new id.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import re
import time
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from ._errors import IzapError

SIGNATURE_HEADER = "izap-webhook-signature"
SIGNATURE_HEADER_V2 = "izap-webhook-signature-v2"
TIMESTAMP_HEADER = "izap-webhook-timestamp"
ID_HEADER = "izap-webhook-id"
EVENT_HEADER = "izap-webhook-event"
DEFAULT_TOLERANCE = 300

_SIGNATURE_PREFIX = "v1="
_SIGNATURE_PREFIX_V2 = "v2="
# Bounded so a hostile value cannot make int()/float() raise past WebhookVerificationError.
_TIMESTAMP = re.compile(r"[0-9]{1,12}", re.ASCII)


class WebhookVerificationError(IzapError, ValueError):
    """The delivery is not authentic, is outside the tolerance window, or is malformed.

    Answer it with a 4xx and do not process it.
    """


@dataclass(frozen=True)
class WebhookEvent:
    """A verified delivery.

    Attributes:
        id: The ``izap-webhook-id`` header. Stable across retries and resends of the same
            event, so use it as the idempotency key. v2 covers this id; v1 does not.
        type: The event type from the signed body, e.g. ``message.received``.
        timestamp: The signed ``izap-webhook-timestamp``, in Unix seconds.
        data: The parsed body.
    """

    id: str
    type: str
    timestamp: int
    data: dict[str, Any]


def _as_bytes(payload: bytes | str) -> bytes:
    return payload.encode() if isinstance(payload, str) else bytes(payload)


def sign(payload: bytes | str, secret: str, timestamp: int | str) -> str:
    """The ``izap-webhook-signature`` (v1) value for ``payload``; useful to test your own receiver."""
    signed = f"{timestamp}.".encode() + _as_bytes(payload)
    return _SIGNATURE_PREFIX + hmac.new(secret.encode(), signed, hashlib.sha256).hexdigest()


def sign_v2(payload: bytes | str, secret: str, delivery_id: str, timestamp: int | str) -> str:
    """The ``izap-webhook-signature-v2`` value for ``payload``; useful to test your own receiver.

    ``delivery_id`` must be exactly the value sent in ``izap-webhook-id``.
    """
    signed = f"{delivery_id}.{timestamp}.".encode() + _as_bytes(payload)
    return _SIGNATURE_PREFIX_V2 + hmac.new(secret.encode(), signed, hashlib.sha256).hexdigest()


def _header(headers: Mapping[str, str], name: str) -> str:
    value = headers.get(name)
    if not value:
        raise WebhookVerificationError(f"missing {name} header")
    return value


def verify(
    payload: bytes | str,
    headers: Mapping[str, str],
    secret: str,
    tolerance: int = DEFAULT_TOLERANCE,
    *,
    allow_v1: bool = False,
) -> WebhookEvent:
    """Check a delivery's signature and freshness, and return the parsed event.

    Requires the v2 signature (``izap-webhook-signature-v2``) by default, since it also
    covers the delivery id. Pass ``allow_v1=True`` to fall back to v1
    (``izap-webhook-signature``) when that header is absent, for senders from before v2
    existed. When both are present, v2 alone decides: a v2 mismatch fails verification
    even if v1 would have matched. ``izap-webhook-id`` is required on both paths because
    ``WebhookEvent.id`` is always taken from that header.

    Args:
        payload: The raw request body exactly as received, before any JSON parsing.
        headers: The request headers; names are matched case-insensitively.
        secret: The endpoint's signing secret (``izap_whsec_...``).
        tolerance: Maximum age, in seconds, between the signed timestamp and now.
        allow_v1: Accept a v1-only delivery when ``izap-webhook-signature-v2`` is absent.
            ``izap-webhook-id`` is still required so ``WebhookEvent.id`` is always set.

    Raises:
        WebhookVerificationError: A header is missing or malformed, the signature does not
            match, the timestamp is outside ``tolerance``, or the body is not a JSON object.
    """
    if not secret:
        raise ValueError("secret is required")
    if tolerance < 0:
        raise ValueError("tolerance must be 0 or greater")

    lowered = {name.lower(): value for name, value in headers.items()}
    timestamp_header = _header(lowered, TIMESTAMP_HEADER)
    delivery_id = _header(lowered, ID_HEADER)
    if not _TIMESTAMP.fullmatch(timestamp_header):
        raise WebhookVerificationError(f"malformed {TIMESTAMP_HEADER} header")

    body = _as_bytes(payload)
    # Presence, not truthiness: a blanked v2 header must not downgrade to the v1 check.
    if SIGNATURE_HEADER_V2 in lowered:
        signature_v2_header = lowered[SIGNATURE_HEADER_V2]
        expected = sign_v2(body, secret, delivery_id, timestamp_header).encode()
        candidates = (part.strip() for part in signature_v2_header.split(","))
        prefix = _SIGNATURE_PREFIX_V2
    elif allow_v1:
        signature_header = _header(lowered, SIGNATURE_HEADER)
        expected = sign(body, secret, timestamp_header).encode()
        candidates = (part.strip() for part in signature_header.split(","))
        prefix = _SIGNATURE_PREFIX
    else:
        raise WebhookVerificationError(f"missing {SIGNATURE_HEADER_V2} header")
    if not any(
        hmac.compare_digest(expected, candidate.encode()) for candidate in candidates if candidate.startswith(prefix)
    ):
        raise WebhookVerificationError("signature does not match")

    timestamp = int(timestamp_header)
    if abs(time.time() - timestamp) > tolerance:
        raise WebhookVerificationError(f"timestamp is more than {tolerance}s from now")

    try:
        data = json.loads(body)
    except (UnicodeDecodeError, ValueError) as exc:
        raise WebhookVerificationError("body is not valid JSON") from exc
    if not isinstance(data, dict):
        raise WebhookVerificationError("body is not a JSON object")

    event_type = data.get("event")
    if not isinstance(event_type, str):
        event_type = lowered.get(EVENT_HEADER, "")
    return WebhookEvent(id=delivery_id, type=event_type, timestamp=timestamp, data=data)


__all__ = [
    "DEFAULT_TOLERANCE",
    "EVENT_HEADER",
    "ID_HEADER",
    "SIGNATURE_HEADER",
    "SIGNATURE_HEADER_V2",
    "TIMESTAMP_HEADER",
    "WebhookEvent",
    "WebhookVerificationError",
    "sign",
    "sign_v2",
    "verify",
]
