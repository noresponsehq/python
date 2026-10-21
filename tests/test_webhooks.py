import hashlib
import hmac
import json
from pathlib import Path

import pytest

from noresponse.models.shared.assessment import Assessment
from noresponse.webhooks import (
    AssessmentExpired,
    EndpointVerification,
    WebhookVerificationError,
    construct_event,
    verification_response,
)

FIXTURES = Path(__file__).parent / "fixtures"
VECTOR = json.loads((FIXTURES / "webhook-signature-vector.json").read_text())
PAYLOAD = VECTOR["payload"].encode()
SECRETS = {VECTOR["key_id"]: VECTOR["secret_utf8"]}
HEADERS = VECTOR["headers"]
NOW = int(VECTOR["timestamp"])


def fixture(name):
    return json.loads((FIXTURES / name).read_text())


def signed(body, secret, event_id, key_id="whk_sdktest01", timestamp="1791968402"):
    raw = json.dumps(body).encode()
    digest = hmac.new(secret.encode(), timestamp.encode() + b"." + raw, hashlib.sha256).hexdigest()
    headers = [
        ("NR-Webhook-Id", event_id),
        ("NR-Webhook-Timestamp", timestamp),
        ("NR-Webhook-Key-Id", key_id),
        ("NR-Webhook-Signature", "v1=" + digest),
    ]
    return raw, headers


def refused(code, *args, **kwargs):
    with pytest.raises(WebhookVerificationError) as caught:
        construct_event(*args, **kwargs)
    assert caught.value.code == code, str(caught.value)


def test_shared_vector_yields_typed_assessment():
    event = construct_event(PAYLOAD, HEADERS, SECRETS, now=NOW)
    assert event.type == "assessment.updated"
    assert event.id == HEADERS["NR-Webhook-Id"]
    assert event.created_at == "2026-10-14T09:00:02.000Z"
    assert isinstance(event.data, Assessment)
    assert event.data.assessment_id == "asm_01JA2Z8K6Q4V7W9XBCDEFGHJKM"
    assert event.data.assessment_version == 2
    assert event.data.risk is not None and event.data.risk.recommendation == "step_up"
    assert not event.expired
    # A str body and lower-case header names verify the same delivery.
    lower = {k.lower(): v for k, v in HEADERS.items()}
    assert construct_event(VECTOR["payload"], lower, SECRETS, now=NOW).id == event.id


def test_refusals():
    refused("invalid_signature", PAYLOAD + b" ", HEADERS, SECRETS, now=NOW)
    refused("invalid_timestamp", PAYLOAD, HEADERS, SECRETS, now=NOW + 301)
    refused("invalid_timestamp", PAYLOAD, HEADERS, SECRETS, now=NOW - 301)
    assert construct_event(PAYLOAD, HEADERS, SECRETS, now=NOW + 301, tolerance_seconds=600).id == HEADERS["NR-Webhook-Id"]
    refused("duplicate_header", PAYLOAD, [*HEADERS.items(), ("nr-webhook-id", "duplicate")], SECRETS, now=NOW)
    refused("duplicate_header", PAYLOAD, [*HEADERS.items(), ("nr-webhook-ID", HEADERS["NR-Webhook-Id"])], SECRETS, now=NOW)
    refused("duplicate_header", PAYLOAD, {**HEADERS, "NR-Webhook-Id": [HEADERS["NR-Webhook-Id"]] * 2}, SECRETS, now=NOW)
    missing = {k: v for k, v in HEADERS.items() if k != "NR-Webhook-Signature"}
    refused("missing_header", PAYLOAD, missing, SECRETS, now=NOW)
    refused("unknown_key", PAYLOAD, HEADERS, {"whk_other0001": VECTOR["secret_utf8"]}, now=NOW)
    refused("invalid_signature", PAYLOAD, HEADERS, {VECTOR["key_id"]: "other-secret"}, now=NOW)
    refused("invalid_signature", PAYLOAD, {**HEADERS, "NR-Webhook-Signature": "v2=abc"}, SECRETS, now=NOW)


def test_httpx_headers_keep_repeats_apart():
    httpx = pytest.importorskip("httpx")
    headers = httpx.Headers([*HEADERS.items(), ("NR-Webhook-Signature", HEADERS["NR-Webhook-Signature"])])
    refused("duplicate_header", PAYLOAD, headers, SECRETS, now=NOW)
    assert construct_event(PAYLOAD, httpx.Headers(HEADERS), SECRETS, now=NOW).id == HEADERS["NR-Webhook-Id"]


def test_rotation_and_event_id():
    complete = fixture("valid/assessment-complete.json")
    event = {"id": "evt_01JA2ZB4N5P6Q7R8S9T0VWXYZ2", "type": "assessment.updated", "created_at": "2026-10-18T11:00:04Z", "data": complete}
    both = {"whk_sdktest01": "old-secret", "whk_sdktest02": "new-secret"}
    raw, headers = signed(event, "new-secret", event["id"], "whk_sdktest02")
    verified = construct_event(raw, headers, both, now=NOW)
    assert isinstance(verified.data, Assessment)
    assert verified.data.assessment_id == complete["assessment_id"]
    raw, headers = signed(event, "new-secret", "evt_01JA2ZB4N5P6Q7R8S9T0VWXYZ9", "whk_sdktest02")
    refused("invalid_payload", raw, headers, both, now=NOW)
    pointer = {**event, "data": {"assessment_id": complete["assessment_id"], "assessment_url": "/v1/assessments/x"}}
    raw, headers = signed(pointer, "new-secret", event["id"], "whk_sdktest02")
    refused("invalid_payload", raw, headers, both, now=NOW)


def test_expired_and_verification_events():
    expired = fixture("valid/webhook-assessment-expired.json")
    raw, headers = signed(expired, "secret", expired["id"])
    event = construct_event(raw, headers, {"whk_sdktest01": "secret"}, now=NOW)
    assert event.expired
    assert event.data == AssessmentExpired(expired["data"]["assessment_id"], expired["data"]["account_id"], 2)
    with pytest.raises(WebhookVerificationError):
        verification_response(event)

    ping = fixture("valid/webhook-endpoint-verification.json")
    raw, headers = signed(ping, "secret", ping["id"])
    event = construct_event(raw, headers, {"whk_sdktest01": "secret"}, now=NOW)
    assert event.type == "endpoint.verification"
    assert event.data == EndpointVerification(ping["data"]["endpoint_id"], ping["data"]["challenge"])
    assert verification_response(event) == {"challenge": ping["data"]["challenge"]}


def test_unknown_fields_are_accepted():
    # The API adds fields without a new version, so keys this SDK does not
    # know must not stop a signed event from verifying.
    for name in (
        "invalid/webhook-tenant-id.json",
        "invalid/webhook-identifier-leak.json",
        "invalid/webhook-expired-with-assessment-url.json",
    ):
        body = fixture(name)
        raw, headers = signed(body, "secret", body["id"])
        assert construct_event(raw, headers, {"whk_sdktest01": "secret"}, now=NOW).id == body["id"]


def test_contract_invalid_fixtures_and_malformed_identifiers_are_refused():
    for name in (
        "invalid/webhook-update-names-source.json",
        "invalid/webhook-unknown-event-type.json",
        "invalid/webhook-update-pointer-only.json",
        "invalid/webhook-update-with-expired-status.json",
        "invalid/webhook-verification-without-challenge.json",
    ):
        body = fixture(name)
        raw, headers = signed(body, "secret", body["id"])
        refused("invalid_payload", raw, headers, {"whk_sdktest01": "secret"}, now=NOW)

    valid = fixture("valid/webhook-endpoint-verification.json")
    for mutate in (
        lambda body: body.update(id="evt_bad"),
        lambda body: body["data"].update(endpoint_id="whe_bad"),
        lambda body: body.update(created_at="tomorrow"),
        lambda body: body.update(created_at="2026-10-14"),
    ):
        body = json.loads(json.dumps(valid))
        mutate(body)
        raw, headers = signed(body, "secret", body["id"])
        refused("invalid_payload", raw, headers, {"whk_sdktest01": "secret"}, now=NOW)
