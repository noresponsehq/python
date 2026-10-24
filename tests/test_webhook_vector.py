"""The contract's signature vector through the generated webhook verifier."""

import hashlib
import hmac
import json
from pathlib import Path

import pytest

from noresponse import WebhookVerificationError, construct_event
from noresponse.models.shared import (
    AccountDeletedEvent,
    AccountRiskChangedEvent,
    AssessmentUpdatedEvent,
    EndpointVerificationEvent,
    WebhookEndpointDisabledEvent,
    WorkspaceDeletedEvent,
)

FIXTURES = Path(__file__).parent / "fixtures"
VECTOR = json.loads((FIXTURES / "webhook-signature-vector.json").read_text())
SECRETS = {VECTOR["key_id"]: VECTOR["secret_utf8"]}
NOW = int(VECTOR["timestamp"])
EVENT_MODELS = {
    "assessment.updated": AssessmentUpdatedEvent,
    "endpoint.verification": EndpointVerificationEvent,
    "account.deleted": AccountDeletedEvent,
    "workspace.deleted": WorkspaceDeletedEvent,
    "webhook_endpoint.disabled": WebhookEndpointDisabledEvent,
    "account.risk_changed": AccountRiskChangedEvent,
}


def test_the_vector_verifies_into_a_typed_assessment_event():
    event = construct_event(VECTOR["payload"].encode(), VECTOR["headers"], SECRETS, now=NOW)
    assert event.type == "assessment.updated"
    assert event.data.id == "asm_01JA2Z8K6Q4V7W9XBCDEFGHJKM"
    assert event.data.detail.assessment_version == 2


@pytest.mark.parametrize(
    "payload, headers, secrets, now, code",
    [
        (VECTOR["payload"] + " ", VECTOR["headers"], SECRETS, NOW, "invalid_signature"),
        (VECTOR["payload"], VECTOR["headers"], SECRETS, NOW + 301, "invalid_timestamp"),
        (VECTOR["payload"], VECTOR["headers"], {"whk_other0001": VECTOR["secret_utf8"]}, NOW, "unknown_key"),
        (VECTOR["payload"], {**VECTOR["headers"], "nr-webhook-signature": VECTOR["headers"]["NR-Webhook-Signature"]}, SECRETS, NOW, "duplicate_header"),
        (VECTOR["payload"], {k: v for k, v in VECTOR["headers"].items() if k != "NR-Webhook-Id"}, SECRETS, NOW, "missing_header"),
    ],
)
def test_a_tampered_stale_unknown_or_repeated_delivery_is_refused(payload, headers, secrets, now, code):
    with pytest.raises(WebhookVerificationError) as refused:
        construct_event(payload, headers, secrets, now=now)
    assert refused.value.code == code


@pytest.mark.parametrize("name", sorted(p.name for p in (FIXTURES / "valid").glob("webhook-*.json") if json.loads(p.read_text()).get("type")))
def test_every_contract_event_fixture_parses_into_its_typed_event(name):
    body = json.loads((FIXTURES / "valid" / name).read_text())
    raw = json.dumps(body, separators=(",", ":")).encode()
    signature = "v1=" + hmac.new(b"fixture-secret", f"{NOW}.".encode() + raw, hashlib.sha256).hexdigest()
    headers = {"NR-Webhook-Id": body["id"], "NR-Webhook-Timestamp": str(NOW), "NR-Webhook-Key-Id": "whk_fixture0001", "NR-Webhook-Signature": signature}
    event = construct_event(raw, headers, {"whk_fixture0001": "fixture-secret"}, now=NOW)
    assert event.type == body["type"]
    assert isinstance(event, EVENT_MODELS[body["type"]])
    assert event.model_dump(mode="json", by_alias=True) == body
