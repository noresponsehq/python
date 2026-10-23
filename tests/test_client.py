import asyncio
import json
import re
from pathlib import Path

import httpx
import pytest

from noresponse import (
    Account,
    AccountDeletion,
    PermissionDeniedError,
    APIConnectionError,
    APIStatusError,
    APITimeoutError,
    Assessment,
    AssessmentPage,
    Integration,
    IntegrationList,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    NoResponse,
    NoResponseError,
    NotFoundError,
    RateLimitError,
    ResponseValidationError,
)

FIXTURES = Path(__file__).parent / "fixtures"
UUID = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$")
KEY = "nrk_0TESTKEY00000000000000000_" + "s" * 43
NO_RETRIES = None


def fixture(name):
    return json.loads((FIXTURES / name).read_text())


PENDING = fixture("valid/assessment-pending.json")
COMPLETE = fixture("valid/assessment-complete.json")
LIST = fixture("valid/assessment-list.json")
OUTCOME = fixture("valid/assessment-outcome.json")
ROTATION = fixture("valid/key-rotation.json")
INTEGRATION = fixture("valid/integration-auth0.json")
INTEGRATION_ROTATED = fixture("valid/integration-auth0-rotated.json")
INTEGRATIONS = fixture("valid/integration-list.json")
ACCOUNT = fixture("valid/account.json")
ACCOUNT_BLOCK = fixture("valid/account-block.json")
ACCOUNT_DELETION = fixture("valid/account-deletion.json")
REQUEST = {"account_id": "usr_8f2k1", "identifiers": {"email": "jordan.lee@example.com", "name": "Jordan Lee"}}


def answer(body, status=200, headers=None, problem=False):
    return httpx.Response(
        status,
        content=json.dumps(body).encode(),
        headers={
            "content-type": "application/problem+json" if problem else "application/json",
            "x-request-id": "a" * 32,
            **(headers or {}),
        },
    )


def problem(status, code, headers=None, **extra):
    body = {
        "type": f"https://docs.noresponse.org/problems/{code}",
        "title": "Problem title",
        "status": status,
        "detail": f"detail for {code}",
        "code": code,
        "request_id": "b" * 32,
        **extra,
    }
    return answer(body, status, headers, problem=True)


def make(responses, **options):
    """A client whose transport answers from a list (the last answer repeats) or a function."""
    seen = []

    def handler(request):
        seen.append(request)
        if callable(responses):
            return responses(request, len(seen))
        item = responses[min(len(seen), len(responses)) - 1]
        if isinstance(item, Exception):
            raise item
        return item

    transport = httpx.MockTransport(handler)
    sdk = NoResponse(
        KEY,
        server_url="https://api.example.test",
        client=httpx.Client(transport=transport),
        async_client=httpx.AsyncClient(transport=transport),
        **options,
    )
    return sdk, seen


def test_construction_reads_the_environment_and_defaults_the_server(monkeypatch):
    monkeypatch.setenv("NORESPONSE_API_KEY", KEY)
    monkeypatch.delenv("NORESPONSE_BASE_URL", raising=False)
    sdk = NoResponse()
    assert sdk.sdk_configuration.get_server_details()[0] == "https://api.noresponse.org"
    monkeypatch.setenv("NORESPONSE_BASE_URL", "https://api-example.invalid/")
    assert NoResponse().sdk_configuration.get_server_details()[0] == "https://api-example.invalid"


def test_construction_refuses_what_cannot_work(monkeypatch):
    monkeypatch.delenv("NORESPONSE_API_KEY", raising=False)
    with pytest.raises(ValueError, match="NORESPONSE_API_KEY"):
        NoResponse()
    with pytest.raises(ValueError, match="line break"):
        NoResponse("k\r\nX-Injected: 1")
    with pytest.raises(ValueError, match="HTTPS"):
        NoResponse(KEY, server_url="http://api.noresponse.org")
    NoResponse(KEY, server_url="http://localhost:8080")
    for bad in ("https://example.com/api?tenant=demo", "https://example.com/api#fragment", "https://example.com/api?"):
        with pytest.raises(ValueError, match="query or fragment"):
            NoResponse(KEY, server_url=bad)
    for bad in (0, -5, 1.5, True):
        with pytest.raises(ValueError, match="timeout_ms"):
            NoResponse(KEY, timeout_ms=bad)


def test_the_key_never_appears_when_the_client_is_printed():
    sdk, _ = make([answer(COMPLETE)])
    assert KEY not in repr(sdk) and KEY not in str(sdk)


def test_create_sends_the_contract_request_and_returns_the_assessment_with_meta():
    sdk, seen = make([answer(PENDING, 202, {"Retry-After": "2", "Location": "/v1/assessments/" + PENDING["assessment_id"]})])
    assessment = sdk.assessments.create(**REQUEST, policy_context={"flow": "signup", "region": "AU"})
    request = seen[0]
    assert request.method == "POST" and request.url.path == "/v1/assessments"
    assert request.headers["authorization"] == "Bearer " + KEY
    assert UUID.match(request.headers["idempotency-key"])
    assert json.loads(request.content) == {
        "account_id": "usr_8f2k1",
        "identifiers": {"email": "jordan.lee@example.com", "name": "Jordan Lee"},
        "policy_context": {"flow": "signup", "region": "AU"},
    }
    assert isinstance(assessment, Assessment)
    assert assessment.status == "pending" and assessment.assessment_id == PENDING["assessment_id"]
    assert assessment.recommendation is None
    assert assessment.meta.request_id == "a" * 32
    assert assessment.meta.retry_after == 2
    assert assessment.meta.location == "/v1/assessments/" + PENDING["assessment_id"]
    assert assessment.meta.idempotent_replayed is False
    # meta is not part of the body.
    assert "meta" not in assessment.model_dump()
    assert "meta" not in repr(assessment)


def test_create_with_an_apps_own_login_leaves_auth_context_out_of_the_body():
    sdk, seen = make([answer(COMPLETE)])
    sdk.assessments.create(**REQUEST, auth_context=None)
    assert json.loads(seen[0].content) == {
        "account_id": "usr_8f2k1",
        "identifiers": {"email": "jordan.lee@example.com", "name": "Jordan Lee"},
    }


def test_idempotency_key_is_generated_once_and_sent_on_every_retry():
    sdk, seen = make([problem(503, "unavailable"), answer(COMPLETE, headers={"Idempotent-Replayed": "true"})])
    assessment = sdk.assessments.create(**REQUEST)
    assert len(seen) == 2
    assert seen[0].headers["idempotency-key"] == seen[1].headers["idempotency-key"]
    assert UUID.match(seen[0].headers["idempotency-key"])
    assert assessment.meta.idempotent_replayed is True
    sdk.assessments.create(**REQUEST, idempotency_key="signup-usr_8f2k1-0001")
    assert seen[2].headers["idempotency-key"] == "signup-usr_8f2k1-0001"
    other = sdk.assessments.create(**REQUEST)
    assert other is not assessment and seen[3].headers["idempotency-key"] != seen[0].headers["idempotency-key"]


def test_get_sends_response_mode_and_wait_polls_until_settled(monkeypatch):
    sdk, seen = make([answer(PENDING, headers={"Retry-After": "1"}), answer(COMPLETE)])
    slept = []
    import noresponse._wait as wait_module

    monkeypatch.setattr(wait_module.time, "sleep", lambda s: slept.append(s))
    settled = sdk.assessments.wait(PENDING["assessment_id"], timeout=30, response_mode="detailed")
    assert settled.status == "complete"
    assert slept == [1.0]
    assert all(r.url.path == "/v1/assessments/" + PENDING["assessment_id"] for r in seen)
    assert all(r.url.params["response_mode"] == "detailed" for r in seen)


def test_errors_carry_the_same_fields_whatever_the_status():
    cases = [
        (400, "invalid_request", BadRequestError, {"invalid_params": [{"field": "identifiers", "reason": "required"}]}),
        (401, "unauthenticated", AuthenticationError, {}),
        (404, "not_found", NotFoundError, {}),
        (409, "idempotency_key_reused", ConflictError, {}),
    ]
    for status, code, klass, extra in cases:
        sdk, _ = make([problem(status, code, **extra)], retry_config=NO_RETRIES)
        with pytest.raises(klass) as caught:
            sdk.assessments.get("asm_01JA2Z8K6Q4V7W9XBCDEFGHJKM")
        error = caught.value
        assert isinstance(error, NoResponseError)
        assert (error.status, error.code, error.request_id) == (status, code, "b" * 32)
        assert error.title == "Problem title" and error.detail == f"detail for {code}"
        assert error.type == f"https://docs.noresponse.org/problems/{code}"
        assert error.retry_after is None
        assert str(error) == f"HTTP {status} {code}: Problem title. detail for {code} (request {'b' * 32})"
        assert error.invalid_params == extra.get("invalid_params")


def test_rate_limit_and_unclassified_failures():
    sdk, _ = make([problem(429, "rate_limited", {"Retry-After": "7"})], retry_config=NO_RETRIES)
    with pytest.raises(RateLimitError) as caught:
        sdk.assessments.create(**REQUEST)
    assert caught.value.retry_after == 7 and caught.value.code == "rate_limited"
    # A 5xx the contract does not describe, with a body that is not a problem document.
    sdk, _ = make(
        [httpx.Response(502, content=b"<html>bad gateway</html>", headers={"content-type": "text/html", "x-request-id": "c" * 32})],
        retry_config=NO_RETRIES,
    )
    with pytest.raises(APIStatusError) as caught:
        sdk.assessments.get("asm_01JA2Z8K6Q4V7W9XBCDEFGHJKM")
    error = caught.value
    assert isinstance(error, NoResponseError)
    assert error.status == 502 and error.code is None and error.type is None and error.title is None
    assert error.request_id == "c" * 32
    assert "bad gateway" in str(error)


def test_a_body_that_does_not_match_the_contract_is_invalid_response():
    sdk, _ = make([answer({"assessment_id": 5})], retry_config=NO_RETRIES)
    with pytest.raises(ResponseValidationError) as caught:
        sdk.assessments.get("asm_01JA2Z8K6Q4V7W9XBCDEFGHJKM")
    assert caught.value.code == "invalid_response" and isinstance(caught.value, NoResponseError)


def test_connection_failures_and_timeouts_have_their_own_classes():
    sdk, seen = make([httpx.ConnectError("refused")], retry_config=NO_RETRIES)
    with pytest.raises(APIConnectionError) as caught:
        sdk.assessments.create(**REQUEST)
    assert not isinstance(caught.value, APITimeoutError)
    assert isinstance(caught.value.cause, httpx.ConnectError)
    sdk, _ = make([httpx.ReadTimeout("slow")], retry_config=NO_RETRIES)
    with pytest.raises(APITimeoutError) as caught:
        sdk.assessments.get("asm_01JA2Z8K6Q4V7W9XBCDEFGHJKM")
    assert isinstance(caught.value, APIConnectionError) and isinstance(caught.value, TimeoutError)
    assert not isinstance(caught.value, NoResponseError)


def test_query_pages_iterate_across_every_page():
    first = {**LIST, "next_cursor": "cursor-2"}
    second = {**LIST, "items": LIST["items"][:1]}
    second.pop("next_cursor", None)

    def handler(request, number):
        body = json.loads(request.content)
        assert body["account_id"] == "acct_7f3a9c" and body["limit"] == 1
        return answer(second if body.get("cursor") == "cursor-2" else first)

    sdk, seen = make(handler)
    page = sdk.assessments.query(account_id="acct_7f3a9c", limit=1)
    assert isinstance(page, AssessmentPage)
    assert page.has_more and page.next_cursor == "cursor-2"
    assert len(page.items) == len(LIST["items"]) and isinstance(page.items[0], Assessment)
    ids = [a.assessment_id for a in page]
    assert ids == [a["assessment_id"] for a in LIST["items"]] + [LIST["items"][0]["assessment_id"]]
    assert len(seen) == 2
    last = page.next_page()
    assert last is not None and not last.has_more and last.next_page() is None


def test_accounts_get_reads_the_current_risk():
    sdk, seen = make([answer(ACCOUNT), answer(ACCOUNT_BLOCK), problem(404, "not_found")], retry_config=NO_RETRIES)
    account = sdk.accounts.get("acct_7f3a9c")
    assert isinstance(account, Account)
    assert (seen[0].method, seen[0].url.path, seen[0].url.query) == ("GET", "/v1/accounts/acct_7f3a9c", b"")
    assert account.id == ACCOUNT["id"] and account.assessment_id == ACCOUNT["assessment_id"]
    assert account.risk.score == ACCOUNT["risk"]["score"] and account.risk.decision == "step_up"
    assert [reason.code for reason in account.risk.reasons] == [r["code"] for r in ACCOUNT["risk"]["reasons"]]
    flows = account.decisions_by_flow
    assert (flows.signup, flows.login, flows.purchase) == ("step_up", "step_up", "step_up")
    assert account.meta.request_id == "a" * 32
    blocked = sdk.accounts.get("tenant:usr|42")
    assert blocked.risk.decision == "block"
    assert seen[1].url.path == "/v1/accounts/tenant:usr|42"  # one path segment, decoded as sent
    with pytest.raises(NotFoundError) as caught:
        sdk.accounts.get("acct_missing")
    assert caught.value.code == "not_found"


def test_accounts_delete_erases_and_a_repeat_answers_zero():
    repeat = {**ACCOUNT_DELETION, "assessments_deleted": 0}
    sdk, seen = make([answer(ACCOUNT_DELETION), answer(repeat), problem(403, "tenant_forbidden")], retry_config=NO_RETRIES)
    deletion = sdk.accounts.delete("acct_7f3a9c")
    assert isinstance(deletion, AccountDeletion)
    assert (seen[0].method, seen[0].url.path, seen[0].content) == ("DELETE", "/v1/accounts/acct_7f3a9c", b"")
    assert deletion.id == "acct_7f3a9c" and deletion.deleted is True and deletion.assessments_deleted == 3
    assert deletion.meta.request_id == "a" * 32
    assert sdk.accounts.delete("acct_7f3a9c").assessments_deleted == 0
    with pytest.raises(PermissionDeniedError) as caught:
        sdk.accounts.delete("acct_7f3a9c")
    assert caught.value.code == "tenant_forbidden"

    async def scenario():
        sdk, seen = make([answer(ACCOUNT_DELETION)])
        async with sdk:
            erased = await sdk.accounts.delete_async("acct_7f3a9c")
        assert erased.assessments_deleted == 3 and seen[0].method == "DELETE"

    asyncio.run(scenario())


def test_accounts_list_assessments_sends_query_parameters_and_pages():
    first = {**LIST, "next_cursor": "cursor-2"}
    second = {**LIST, "items": LIST["items"][:1]}
    second.pop("next_cursor", None)

    def handler(request, number):
        assert request.method == "GET" and request.url.path == "/v1/accounts/acct_7f3a9c/assessments"
        assert request.content == b""
        params = dict(request.url.params)
        assert params["limit"] == "1" and params["response_mode"] == "detailed"
        return answer(second if params.get("cursor") == "cursor-2" else first)

    sdk, seen = make(handler)
    page = sdk.accounts.list_assessments("acct_7f3a9c", limit=1, response_mode="detailed")
    assert isinstance(page, AssessmentPage)
    assert page.has_more and page.next_cursor == "cursor-2" and page.meta.request_id == "a" * 32
    ids = [a.assessment_id for a in page]
    assert ids == [a["assessment_id"] for a in LIST["items"]] + [LIST["items"][0]["assessment_id"]]
    assert len(seen) == 2 and "cursor" not in dict(seen[0].url.params)
    assert dict(seen[1].url.params)["cursor"] == "cursor-2"

    async def scenario():
        sdk, seen = make(handler)
        async with sdk:
            page = await sdk.accounts.list_assessments_async("acct_7f3a9c", limit=1, response_mode="detailed")
            everything = [item.assessment_id async for item in page]
            assert len(everything) == len(LIST["items"]) + 1
        sdk, _ = make([answer(ACCOUNT)])
        async with sdk:
            account = await sdk.accounts.get_async("acct_7f3a9c")
            assert account.risk.decision == ACCOUNT["risk"]["decision"]

    asyncio.run(scenario())


def test_async_methods_mirror_the_sync_ones():
    async def scenario():
        first = {**LIST, "next_cursor": "cursor-2"}
        second = {**LIST, "items": LIST["items"][:1]}
        second.pop("next_cursor", None)

        def handler(request, number):
            if request.url.path == "/v1/assessments/query":
                return answer(second if json.loads(request.content).get("cursor") == "cursor-2" else first)
            if request.method == "POST" and request.url.path == "/v1/assessments":
                return answer(COMPLETE)
            return answer(COMPLETE)

        sdk, seen = make(handler)
        async with sdk:
            created = await sdk.assessments.create_async(**REQUEST)
            assert created.status == "complete" and UUID.match(seen[0].headers["idempotency-key"])
            got = await sdk.assessments.get_async(created.assessment_id)
            assert got.assessment_id == created.assessment_id
            waited = await sdk.assessments.wait_async(created.assessment_id)
            assert waited.status == "complete"
            page = await sdk.assessments.query_async(account_id="acct_7f3a9c", limit=1)
            everything = [item.assessment_id async for item in page]
            assert len(everything) == len(LIST["items"]) + 1

    asyncio.run(scenario())


def test_record_outcome_and_key_rotation():
    sdk, seen = make([answer(OUTCOME, 202), answer(ROTATION, 201)])
    receipt = sdk.assessments.record_outcome(OUTCOME["assessment_id"], outcome="chargeback", external_ref="case-42")
    assert receipt.outcome == OUTCOME["outcome"] and receipt.meta.request_id == "a" * 32
    assert seen[0].url.path == f"/v1/assessments/{OUTCOME['assessment_id']}/outcomes"
    assert UUID.match(seen[0].headers["idempotency-key"])
    assert json.loads(seen[0].content) == {"outcome": "chargeback", "external_ref": "case-42"}
    rotation = sdk.keys.rotate(overlap_seconds=3600)
    assert rotation.key == ROTATION["key"] and rotation.previous_key_expires_at == ROTATION["previous_key_expires_at"]
    assert json.loads(seen[1].content) == {"overlap_seconds": 3600}


def test_webhook_endpoints_register_list_rotate_test_and_delete_without_retrying_writes():
    created = fixture("valid/webhook-endpoint-created.json")
    listed = fixture("valid/webhook-endpoint-list.json")
    rotated = fixture("valid/webhook-key-rotation.json")
    sent = fixture("valid/webhook-test-assessment-updated.json")
    deleted = httpx.Response(204, headers={"x-request-id": "b" * 32, "cache-control": "no-store"})
    sdk, seen = make([answer(created, 201), answer(listed), answer(rotated, 201), answer(sent, 202), deleted, answer({}, 503, problem=True)])
    endpoint_id = created["endpoint"]["endpoint_id"]
    endpoint = sdk.webhook_endpoints.create(url="https://hooks.example.com/noresponse")
    assert endpoint.signing_secret.secret == created["signing_secret"]["secret"] and endpoint.endpoint.state == "unverified"
    assert len(sdk.webhook_endpoints.list().items[0].signing_keys) == 2
    assert sdk.webhook_endpoints.rotate_signing_key(endpoint_id).previous_key_id == rotated["previous_key_id"]
    assert sdk.webhook_endpoints.send_test_event(endpoint_id, event="assessment.updated").delivery_id == sent["delivery_id"]
    assert sdk.webhook_endpoints.delete(endpoint_id) is None
    with pytest.raises(Exception):
        sdk.webhook_endpoints.send_test_event(endpoint_id, event="endpoint.verification")
    assert [(r.method, r.url.path) for r in seen] == [
        ("POST", "/v1/webhooks"),
        ("GET", "/v1/webhooks"),
        ("POST", f"/v1/webhooks/{endpoint_id}/rotate"),
        ("POST", f"/v1/webhooks/{endpoint_id}/test"),
        ("DELETE", f"/v1/webhooks/{endpoint_id}"),
        ("POST", f"/v1/webhooks/{endpoint_id}/test"),
    ]
    assert json.loads(seen[0].content) == {"url": "https://hooks.example.com/noresponse"}
    assert json.loads(seen[2].content) == {}
    assert json.loads(seen[3].content) == {"event": "assessment.updated"}


def test_webhook_endpoints_list_deliveries_and_replay_one_without_retrying():
    page = fixture("valid/webhook-delivery-list.json")
    replayed = fixture("valid/webhook-replay.json")
    endpoint_id, event_id = page["endpoint_id"], page["items"][0]["event_id"]
    sdk, seen = make([answer(page), answer(replayed, 202), answer({}, 503, problem=True)])
    listed = sdk.webhook_endpoints.list_deliveries(endpoint_id, limit=3, cursor="abc")
    assert [item.status for item in listed.items] == ["delivered", "failed", "failed"]
    assert listed.items[1].response_code == 500 and listed.items[2].response_code is None
    assert listed.next_cursor == page["next_cursor"]
    assert sdk.webhook_endpoints.replay_delivery(endpoint_id, event_id).event_id == event_id
    with pytest.raises(Exception):
        sdk.webhook_endpoints.replay_delivery(endpoint_id, event_id)
    assert [(r.method, r.url.path, dict(r.url.params)) for r in seen] == [
        ("GET", f"/v1/webhooks/{endpoint_id}/deliveries", {"limit": "3", "cursor": "abc"}),
        ("POST", f"/v1/webhooks/{endpoint_id}/deliveries/{event_id}/replay", {}),
        ("POST", f"/v1/webhooks/{endpoint_id}/deliveries/{event_id}/replay", {}),
    ]
    assert json.loads(seen[1].content) == {}


def test_integrations_create_list_rotate_and_delete():
    integration_id = INTEGRATION["integration_id"]
    deleted = httpx.Response(204, headers={"x-request-id": "c" * 32})
    sdk, seen = make([answer(INTEGRATION, 201), answer(INTEGRATIONS), answer(INTEGRATION_ROTATED), deleted])
    created = sdk.integrations.create(platform="auth0", hook_points=["post_login"])
    assert isinstance(created, Integration)
    assert created.integration_id == integration_id and created.secret == INTEGRATION["secret"]
    assert created.meta.request_id == "a" * 32
    assert (seen[0].method, seen[0].url.path) == ("POST", "/v1/integrations")
    assert json.loads(seen[0].content) == {"platform": "auth0", "hook_points": ["post_login"]}
    assert "idempotency-key" not in seen[0].headers
    listed = sdk.integrations.list()
    assert isinstance(listed, IntegrationList)
    assert [item.integration_id for item in listed.items] == [item["integration_id"] for item in INTEGRATIONS["items"]]
    assert all(item.secret is None for item in listed.items)
    assert (seen[1].method, seen[1].url.path) == ("GET", "/v1/integrations")
    rotated = sdk.integrations.rotate(integration_id)
    assert rotated.secret == INTEGRATION_ROTATED["secret"]
    assert rotated.previous_secret_expires_at == INTEGRATION_ROTATED["previous_secret_expires_at"]
    assert (seen[2].method, seen[2].url.path) == ("POST", f"/v1/integrations/{integration_id}/rotate")
    assert json.loads(seen[2].content) == {}
    meta = sdk.integrations.delete(integration_id)
    assert meta.request_id == "c" * 32
    assert (seen[3].method, seen[3].url.path) == ("DELETE", f"/v1/integrations/{integration_id}")


def test_integrations_create_and_rotate_are_never_retried():
    sdk, seen = make([problem(503, "unavailable", headers={"retry-after": "1"})])
    with pytest.raises(APIStatusError):
        sdk.integrations.create(platform="workos", signing_secret="wos_action_secret_k3Yx8pQ2mN7vR4tW")
    assert len(seen) == 1
    assert json.loads(seen[0].content)["signing_secret"] == "wos_action_secret_k3Yx8pQ2mN7vR4tW"
    with pytest.raises(APIStatusError):
        sdk.integrations.rotate(INTEGRATION["integration_id"], signing_secret="wos_action_secret_Z9cD1eF5gH0jL4sP")
    assert len(seen) == 2

    async def scenario():
        sdk, seen = make([answer(INTEGRATION, 201), answer(INTEGRATIONS)])
        async with sdk:
            created = await sdk.integrations.create_async(platform="auth0")
            assert created.integration_id == INTEGRATION["integration_id"]
            listed = await sdk.integrations.list_async()
            assert len(listed.items) == len(INTEGRATIONS["items"])
        assert [r.method for r in seen] == ["POST", "GET"]

    asyncio.run(scenario())


def test_raw_responses_are_still_available():
    sdk, _ = make([answer(COMPLETE)])
    raw = sdk.assessments.with_raw_response.get("asm_01JA2Z8K6Q4V7W9XBCDEFGHJKM")
    assert raw.http_response.status_code == 200


def test_webhook_namespace_is_on_the_client():
    from noresponse import Webhook, construct_event

    assert NoResponse.webhooks is Webhook and Webhook.construct_event is construct_event


def test_debug_logging_leaves_out_the_key_and_the_bodies(monkeypatch):
    lines = []

    class Sink:
        def debug(self, msg, *args, **kwargs):
            lines.append(msg % args if args else msg)

    sdk, _ = make([answer(COMPLETE)], debug_logger=Sink())
    sdk.assessments.create(**REQUEST)
    text = "\n".join(lines)
    assert "Request: POST https://api.example.test/v1/assessments" in text
    assert "Response: 200 https://api.example.test/v1/assessments (request " + "a" * 32 + ")" in text
    assert KEY not in text and "jordan.lee@example.com" not in text and "Bearer" not in text
    monkeypatch.delenv("NORESPONSE_LOG", raising=False)
    monkeypatch.delenv("NORESPONSE_DEBUG", raising=False)
    quiet, _ = make([answer(COMPLETE)])
    quiet.assessments.create(**REQUEST)


def test_wait_is_callable_from_the_package_root(monkeypatch):
    import noresponse

    assert callable(noresponse.wait) and callable(noresponse.wait_async)
    import noresponse._wait as wait_module

    monkeypatch.setattr(wait_module.time, "sleep", lambda s: None)
    sdk, _ = make([answer(PENDING, headers={"Retry-After": "1"}), answer(COMPLETE)])
    assert noresponse.wait(sdk, PENDING["assessment_id"]).status == "complete"
