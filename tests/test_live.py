"""Consumer smoke test of the client against a live API.

Skipped unless NORESPONSE_LIVE_URL and NORESPONSE_LIVE_API_KEY name an API
and a key with the assess and history scopes (a test key keeps it off real
sources). It assesses a synthetic account, replays the request, reads it
back, waits for it to settle, lists its history and checks the typed 404.
NORESPONSE_LIVE_WEBHOOK_VECTORS names deliveries the same API signed, in the
shape of webhook-signature-vector.json, for the verifier. Each step writes
its name to NORESPONSE_LIVE_REPORT, and "done" at the end, so a failure
names the operation (integrations/regression/suites/sdks.sh).
"""
import json
import os
import uuid
from pathlib import Path

import pytest

from noresponse import NoResponse, NotFoundError, WebhookVerificationError, construct_event, wait

URL = os.environ.get("NORESPONSE_LIVE_URL")
KEY = os.environ.get("NORESPONSE_LIVE_API_KEY")
VECTORS = os.environ.get("NORESPONSE_LIVE_WEBHOOK_VECTORS")
REPORT = os.environ.get("NORESPONSE_LIVE_REPORT")
pytestmark = pytest.mark.skipif(not (URL and KEY), reason="set NORESPONSE_LIVE_URL and NORESPONSE_LIVE_API_KEY to run against a live API")


def step(name: str) -> None:
    if REPORT:
        Path(REPORT).write_text(name)


def test_a_consumer_assesses_waits_for_and_lists_an_account():
    client = NoResponse(api_key=KEY, server_url=URL, timeout_ms=30_000)
    account_id = "sdk-live-python-" + os.environ.get("NORESPONSE_LIVE_RUN", uuid.uuid4().hex[:8])
    idempotency_key = "sdk-live-" + uuid.uuid4().hex
    request = {"account_id": account_id, "flow": "account_creation", "identifiers": {"email": "sdk-live@example.com"}}

    step("create")
    created = client.assessments.create(idempotency_key=idempotency_key, **request)
    assert created.id.startswith("asm_")
    assert created.detail.account_id == account_id

    step("replay")
    assert client.assessments.create(idempotency_key=idempotency_key, **request).id == created.id

    step("get")
    assert client.assessments.get(created.id).id == created.id

    step("wait")
    settled = wait(client.assessments, created.id, timeout=60.0)
    assert settled.status in {"complete", "partial"}
    assert settled.account is not None and settled.account.risk.decision

    step("query")
    history = client.assessments.query(account_id=account_id, limit=5)
    assert {item.account_id for item in history.items} == {account_id}
    assert created.id in {item.assessment_id for item in history.items}

    step("list_account_assessments")
    page = client.accounts.list_assessments(account_id, limit=5)
    assert created.id in {item.assessment_id for item in page.items}

    step("get_account")
    account = client.accounts.get(account_id)
    assert account.id == account_id
    assert account.risk.decision == settled.account.risk.decision

    step("not_found")
    with pytest.raises(NotFoundError) as missing:
        client.assessments.get("asm_" + "0" * 26)
    assert missing.value.status == 404 and missing.value.code and missing.value.request_id

    for vector in json.loads(Path(VECTORS).read_text()) if VECTORS else []:
        step("verify_webhook " + vector["type"])
        secrets = {vector["key_id"]: vector["secret_utf8"]}
        now = int(vector["timestamp"])
        assert construct_event(vector["payload"].encode(), vector["headers"], secrets, now=now).type == vector["type"]
        with pytest.raises(WebhookVerificationError) as refused:
            construct_event((vector["payload"] + " ").encode(), vector["headers"], secrets, now=now)
        assert refused.value.code == "invalid_signature"
    step("done")
