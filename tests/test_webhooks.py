"""Webhook verification against vectors signed by the backend's own signer.

``fixtures/webhook_vectors.json`` comes from ``scripts/webhook_vectors.py``, which calls
``aizap.services.webhook.webhook_delivery_service.sign`` and ``sign_v2``, so these tests
pin the SDK to what the server actually sends (both signature headers, since the backend
sends both on every delivery) rather than to the SDK's own idea of the contract.
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

import pytest

from izap import IzapError, webhooks
from izap.webhooks import WebhookVerificationError

VECTORS: list[dict[str, Any]] = json.loads(
    (Path(__file__).parent / "fixtures" / "webhook_vectors.json").read_text(encoding="utf-8")
)["vectors"]


def timestamp_of(vector: dict[str, Any]) -> int:
    return int(vector["headers"][webhooks.TIMESTAMP_HEADER])


def without_v2(headers: dict[str, str]) -> dict[str, str]:
    """``headers`` as if the delivery predated v2, or a receiver stripped the unknown header."""
    return {name: value for name, value in headers.items() if name != webhooks.SIGNATURE_HEADER_V2}


def flipped(signature: str) -> str:
    """``signature`` with its first hex digit changed, to forge a signature that does not match."""
    prefix, digest = signature.split("=", 1)
    return f"{prefix}=" + ("0" if digest[0] != "0" else "1") + digest[1:]


@pytest.fixture
def now(monkeypatch: pytest.MonkeyPatch) -> Any:
    def freeze(at: float) -> None:
        monkeypatch.setattr(time, "time", lambda: at)

    return freeze


@pytest.fixture
def vector(now: Any) -> dict[str, Any]:
    now(timestamp_of(VECTORS[0]))
    return VECTORS[0]


class TestBackendVectors:
    @pytest.mark.parametrize("vector", VECTORS, ids=[v["name"] for v in VECTORS])
    def test_verifies_what_the_backend_signed(self, vector: dict[str, Any], now: Any) -> None:
        now(timestamp_of(vector))
        event = webhooks.verify(vector["body"].encode(), vector["headers"], vector["secret"])

        assert event.id == vector["headers"][webhooks.ID_HEADER]
        assert event.type == "message.received"
        assert event.timestamp == timestamp_of(vector)
        assert event.data == json.loads(vector["body"])

    @pytest.mark.parametrize("vector", VECTORS, ids=[v["name"] for v in VECTORS])
    def test_signs_like_the_backend(self, vector: dict[str, Any]) -> None:
        signature = webhooks.sign(vector["body"].encode(), vector["secret"], timestamp_of(vector))

        assert signature == vector["headers"][webhooks.SIGNATURE_HEADER]

    def test_accepts_the_body_as_text(self, vector: dict[str, Any]) -> None:
        event = webhooks.verify(vector["body"], vector["headers"], vector["secret"])

        assert event.data["event"] == "message.received"

    def test_matches_header_names_case_insensitively(self, vector: dict[str, Any]) -> None:
        headers = {name.title(): value for name, value in vector["headers"].items()}

        assert webhooks.verify(vector["body"], headers, vector["secret"]).id == vector["headers"][webhooks.ID_HEADER]


class TestSignature:
    def test_rejects_a_tampered_body(self, vector: dict[str, Any]) -> None:
        body = vector["body"].replace("What are your hours?", "What are your prices?")

        with pytest.raises(WebhookVerificationError, match="signature"):
            webhooks.verify(body, vector["headers"], vector["secret"])

    def test_rejects_the_wrong_secret(self, vector: dict[str, Any]) -> None:
        with pytest.raises(WebhookVerificationError, match="signature"):
            webhooks.verify(vector["body"], vector["headers"], "izap_whsec_not_the_right_one")

    def test_rejects_a_signature_bound_to_another_timestamp(self, vector: dict[str, Any]) -> None:
        headers = {**vector["headers"], webhooks.TIMESTAMP_HEADER: str(timestamp_of(vector) + 1)}

        with pytest.raises(WebhookVerificationError, match="signature"):
            webhooks.verify(vector["body"], headers, vector["secret"])

    def test_rejects_a_forged_v1_signature_when_v2_is_absent(self, vector: dict[str, Any]) -> None:
        headers = without_v2(vector["headers"])
        forged = flipped(headers[webhooks.SIGNATURE_HEADER])

        with pytest.raises(WebhookVerificationError, match="signature"):
            webhooks.verify(
                vector["body"], {**headers, webhooks.SIGNATURE_HEADER: forged}, vector["secret"], allow_v1=True
            )

    def test_rejects_a_bare_v1_digest_without_the_version_prefix_when_v2_is_absent(
        self, vector: dict[str, Any]
    ) -> None:
        headers = without_v2(vector["headers"])
        bare = headers[webhooks.SIGNATURE_HEADER].removeprefix("v1=")

        with pytest.raises(WebhookVerificationError, match="signature"):
            webhooks.verify(
                vector["body"], {**headers, webhooks.SIGNATURE_HEADER: bare}, vector["secret"], allow_v1=True
            )

    def test_accepts_a_v1_signature_listed_alongside_other_versions_when_v2_is_absent(
        self, vector: dict[str, Any]
    ) -> None:
        headers = without_v2(vector["headers"])
        signatures = f"v2=deadbeef, {headers[webhooks.SIGNATURE_HEADER]}"

        result = webhooks.verify(
            vector["body"], {**headers, webhooks.SIGNATURE_HEADER: signatures}, vector["secret"], allow_v1=True
        )

        assert result.type == "message.received"


class TestV2Signature:
    """``izap-webhook-signature-v2`` is checked by default whenever the delivery carries it."""

    def test_v2_present_and_valid_passes(self, vector: dict[str, Any]) -> None:
        event = webhooks.verify(vector["body"], vector["headers"], vector["secret"])

        assert event.id == vector["headers"][webhooks.ID_HEADER]

    def test_v2_present_and_tampered_id_fails(self, vector: dict[str, Any]) -> None:
        headers = {**vector["headers"], webhooks.ID_HEADER: vector["headers"][webhooks.ID_HEADER][::-1]}

        with pytest.raises(WebhookVerificationError, match="signature"):
            webhooks.verify(vector["body"], headers, vector["secret"])

    def test_v2_present_and_tampered_timestamp_fails(self, vector: dict[str, Any]) -> None:
        headers = {**vector["headers"], webhooks.TIMESTAMP_HEADER: str(timestamp_of(vector) + 1)}

        with pytest.raises(WebhookVerificationError, match="signature"):
            webhooks.verify(vector["body"], headers, vector["secret"])

    def test_v2_present_and_tampered_body_fails(self, vector: dict[str, Any]) -> None:
        body = vector["body"].replace("What are your hours?", "What are your prices?")

        with pytest.raises(WebhookVerificationError, match="signature"):
            webhooks.verify(body, vector["headers"], vector["secret"])

    def test_v2_present_and_forged_fails_even_though_v1_still_matches(self, vector: dict[str, Any]) -> None:
        """v2 must decide on its own, never silently falling back to a still-valid v1."""
        forged = flipped(vector["headers"][webhooks.SIGNATURE_HEADER_V2])
        headers = {**vector["headers"], webhooks.SIGNATURE_HEADER_V2: forged}
        assert headers[webhooks.SIGNATURE_HEADER] == vector["headers"][webhooks.SIGNATURE_HEADER]  # v1 untouched

        with pytest.raises(WebhookVerificationError, match="signature"):
            webhooks.verify(vector["body"], headers, vector["secret"])

    @pytest.mark.parametrize("blank", ["", "   "])
    def test_v2_present_but_blank_fails_even_with_allow_v1(self, vector: dict[str, Any], blank: str) -> None:
        """A replay that blanks v2 instead of removing it must not downgrade to v1."""
        headers = {**vector["headers"], webhooks.SIGNATURE_HEADER_V2: blank}

        with pytest.raises(WebhookVerificationError, match="signature"):
            webhooks.verify(vector["body"], headers, vector["secret"], allow_v1=True)

    def test_v2_absent_is_rejected_by_default(self, vector: dict[str, Any]) -> None:
        headers = without_v2(vector["headers"])

        with pytest.raises(WebhookVerificationError, match=webhooks.SIGNATURE_HEADER_V2):
            webhooks.verify(vector["body"], headers, vector["secret"])

    def test_v2_absent_accepts_v1_when_allow_v1_is_set(self, vector: dict[str, Any]) -> None:
        headers = without_v2(vector["headers"])

        event = webhooks.verify(vector["body"], headers, vector["secret"], allow_v1=True)

        assert event.id == vector["headers"][webhooks.ID_HEADER]

    def test_signs_v2_like_the_backend(self, vector: dict[str, Any]) -> None:
        signature = webhooks.sign_v2(
            vector["body"].encode(),
            vector["secret"],
            vector["headers"][webhooks.ID_HEADER],
            timestamp_of(vector),
        )

        assert signature == vector["headers"][webhooks.SIGNATURE_HEADER_V2]


class TestTimestamp:
    def test_accepts_a_delivery_at_the_edge_of_the_window(self, vector: dict[str, Any], now: Any) -> None:
        now(timestamp_of(vector) + webhooks.DEFAULT_TOLERANCE)

        assert webhooks.verify(vector["body"], vector["headers"], vector["secret"]).id

    def test_rejects_a_stale_delivery(self, vector: dict[str, Any], now: Any) -> None:
        now(timestamp_of(vector) + webhooks.DEFAULT_TOLERANCE + 1)

        with pytest.raises(WebhookVerificationError, match="timestamp"):
            webhooks.verify(vector["body"], vector["headers"], vector["secret"])

    def test_rejects_a_delivery_from_the_future(self, vector: dict[str, Any], now: Any) -> None:
        now(timestamp_of(vector) - webhooks.DEFAULT_TOLERANCE - 1)

        with pytest.raises(WebhookVerificationError, match="timestamp"):
            webhooks.verify(vector["body"], vector["headers"], vector["secret"])

    def test_honours_a_custom_tolerance(self, vector: dict[str, Any], now: Any) -> None:
        now(timestamp_of(vector) + 60)

        with pytest.raises(WebhookVerificationError, match="timestamp"):
            webhooks.verify(vector["body"], vector["headers"], vector["secret"], tolerance=30)
        assert webhooks.verify(vector["body"], vector["headers"], vector["secret"], tolerance=60).id

    @pytest.mark.parametrize(
        "timestamp", ["", "12a", " 1789430400", "-1789430400", "1789430400.0", "١٢٣", "9" * 13, "9" * 5000]
    )
    def test_rejects_a_malformed_timestamp(self, vector: dict[str, Any], timestamp: str) -> None:
        headers = {**vector["headers"], webhooks.TIMESTAMP_HEADER: timestamp}

        with pytest.raises(WebhookVerificationError, match=webhooks.TIMESTAMP_HEADER):
            webhooks.verify(vector["body"], headers, vector["secret"])


class TestMalformedDeliveries:
    @pytest.mark.parametrize("header", [webhooks.TIMESTAMP_HEADER, webhooks.ID_HEADER])
    def test_rejects_a_missing_header(self, vector: dict[str, Any], header: str) -> None:
        headers = {name: value for name, value in vector["headers"].items() if name != header}

        with pytest.raises(WebhookVerificationError, match=f"missing {header}"):
            webhooks.verify(vector["body"], headers, vector["secret"])

    def test_allow_v1_still_requires_the_delivery_id(self, vector: dict[str, Any]) -> None:
        headers = without_v2({name: value for name, value in vector["headers"].items() if name != webhooks.ID_HEADER})

        with pytest.raises(WebhookVerificationError, match=f"missing {webhooks.ID_HEADER}"):
            webhooks.verify(vector["body"], headers, vector["secret"], allow_v1=True)

    def test_rejects_when_both_signature_headers_are_missing(self, vector: dict[str, Any]) -> None:
        headers = {
            name: value
            for name, value in vector["headers"].items()
            if name not in (webhooks.SIGNATURE_HEADER, webhooks.SIGNATURE_HEADER_V2)
        }

        with pytest.raises(WebhookVerificationError, match=f"missing {webhooks.SIGNATURE_HEADER_V2}"):
            webhooks.verify(vector["body"], headers, vector["secret"])

    def test_v1_header_is_optional_when_v2_is_present(self, vector: dict[str, Any]) -> None:
        headers = {name: value for name, value in vector["headers"].items() if name != webhooks.SIGNATURE_HEADER}

        assert webhooks.verify(vector["body"], headers, vector["secret"]).id

    @pytest.mark.parametrize("body", ["not json", "[1, 2, 3]"])
    def test_rejects_a_signed_body_that_is_not_a_json_object(self, vector: dict[str, Any], body: str) -> None:
        headers = without_v2(vector["headers"])
        timestamp = headers[webhooks.TIMESTAMP_HEADER]
        headers = {**headers, webhooks.SIGNATURE_HEADER: webhooks.sign(body, vector["secret"], timestamp)}

        with pytest.raises(WebhookVerificationError, match="JSON"):
            webhooks.verify(body, headers, vector["secret"], allow_v1=True)

    def test_falls_back_to_the_event_header_when_the_body_has_no_event(self, vector: dict[str, Any]) -> None:
        body = json.dumps({"business_id": "b"})
        headers = without_v2(vector["headers"])
        timestamp = headers[webhooks.TIMESTAMP_HEADER]
        headers = {**headers, webhooks.SIGNATURE_HEADER: webhooks.sign(body, vector["secret"], timestamp)}

        assert webhooks.verify(body, headers, vector["secret"], allow_v1=True).type == "message.received"

    def test_verification_errors_are_value_errors_and_sdk_errors(self) -> None:
        assert issubclass(WebhookVerificationError, ValueError)
        assert issubclass(WebhookVerificationError, IzapError)

    @pytest.mark.parametrize(("secret", "tolerance"), [("", 300), ("izap_whsec_x", -1)])
    def test_rejects_bad_arguments(self, vector: dict[str, Any], secret: str, tolerance: int) -> None:
        with pytest.raises(ValueError):
            webhooks.verify(vector["body"], vector["headers"], secret, tolerance=tolerance)
