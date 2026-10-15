"""Regenerate ``tests/fixtures/webhook_vectors.json`` with the backend's own signer.

The vectors are signed by ``aizap.services.webhook.webhook_delivery_service`` rather
than by this SDK, so the tests prove the SDK verifies what the server actually sends.
Needs the backend environment; run from the monorepo root:

    cd backend && set -a && . .buildkite/ci-test.env && set +a && \
        PYTHONPATH=. uv run --no-sync python ../sdk/python/scripts/webhook_vectors.py
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from types import SimpleNamespace
from typing import Any

from aizap.models.webhook_endpoint import (
    HEADER_EVENT,
    HEADER_ID,
    HEADER_SIGNATURE,
    HEADER_SIGNATURE_V2,
    HEADER_TIMESTAMP,
)
from aizap.services.webhook.webhook_delivery_service import (
    build_message_received_payload,
    serialize_payload,
    sign,
    sign_v2,
)

OUTPUT = Path(__file__).resolve().parent.parent / "tests" / "fixtures" / "webhook_vectors.json"

CASES: list[dict[str, Any]] = [
    {
        "name": "ascii",
        "secret": "izap_whsec_Q2hhbmdlTWVCZWZvcmVTaGlwcGluZ1RoaXNTZWNyZXQ",
        "timestamp": 1789430400,
        "delivery_id": "7b0c9a62-5f1e-4d3b-9a0e-2f6c1d8e4a01",
        "business_id": "8f0b9e2a-1c3d-4e5f-8a9b-0c1d2e3f4a5b",
        "conversation_id": "c3a1f6d0-2b4c-4d6e-8f0a-1b2c3d4e5f60",
        "message_id": "8a2e1c40-3d5f-4a7b-9c1d-2e3f4a5b6c7d",
        "chat_id": "b91d4a5e-6f70-4812-9a3b-4c5d6e7f8091",
        "text": "What are your hours?",
        "sender": "+15551234567",
        "created": datetime(2026, 9, 12, 10, 0, 0, 123456, tzinfo=UTC),
    },
    {
        "name": "non_ascii",
        "secret": "izap_whsec_T2zDoSwgc2VncmVkbyBkZSB0ZXN0ZSDwn5qA",
        "timestamp": 1789434000,
        "delivery_id": "1d4f7a2b-8c9e-4f01-a2b3-c4d5e6f70812",
        "business_id": "8f0b9e2a-1c3d-4e5f-8a9b-0c1d2e3f4a5b",
        "conversation_id": None,
        "message_id": "5e6f7081-92a3-4b4c-8d5e-6f708192a3b4",
        "chat_id": None,
        "text": 'Olá! Qual o horário de amanhã? 🚀 "entrega" \\ ção',
        "sender": "+5511987654321",
        "created": datetime(2026, 9, 12, 13, 45, 7, tzinfo=UTC),
    },
    {
        "name": "empty_text",
        "secret": "izap_whsec_c2hvcnQ",
        "timestamp": 1789437600,
        "delivery_id": "0a1b2c3d-4e5f-4061-8728-394a5b6c7d8e",
        "business_id": "2b3c4d5e-6f70-4182-93a4-b5c6d7e8f901",
        "conversation_id": "9f8e7d6c-5b4a-4938-8271-605f4e3d2c1b",
        "message_id": "6c5b4a39-2817-4f6e-9d5c-4b3a29180f7e",
        "chat_id": "3a29180f-7e6d-4c5b-8a49-3827160f5e4d",
        "text": None,
        "sender": "+15550000000",
        "created": datetime(2026, 9, 12, 23, 59, 59, 999999, tzinfo=UTC),
    },
]


def build_vector(case: dict[str, Any]) -> dict[str, Any]:
    message = SimpleNamespace(
        id=case["message_id"],
        chat_id=case["chat_id"],
        message=case["text"],
        sender=case["sender"],
        created=case["created"],
    )
    payload = build_message_received_payload(
        message,
        business_id=case["business_id"],
        conversation_id=case["conversation_id"],
        sender_type="consumer",
    )
    body = serialize_payload(payload)
    timestamp = str(case["timestamp"])
    return {
        "name": case["name"],
        "secret": case["secret"],
        "body": body,
        "headers": {
            HEADER_ID: case["delivery_id"],
            HEADER_EVENT: payload["event"],
            HEADER_TIMESTAMP: timestamp,
            HEADER_SIGNATURE: sign(case["secret"], timestamp, body),
            HEADER_SIGNATURE_V2: sign_v2(case["secret"], case["delivery_id"], timestamp, body),
        },
    }


def main() -> None:
    document = {
        "source": "aizap.services.webhook.webhook_delivery_service.sign / serialize_payload",
        "vectors": [build_vector(case) for case in CASES],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
