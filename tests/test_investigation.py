"""Public sync and asyncio clients exercise the actual generated HTTP operations."""
import asyncio
import copy
import json

import httpx
import pytest

from noresponse import APITimeoutError, ConflictError, Requests
from test_client import answer, fixture, make, problem, UUID

EXAMPLES = fixture("investigation-responses.json")
ACCOUNT = EXAMPLES["outcome"]["account_id"]
ASSESSMENT = EXAMPLES["revision"]["id"]
CREDENTIAL = EXAMPLES["credential"]["id"]
FROM, TO = "2026-10-01T00:00:00Z", "2026-10-02T00:00:00Z"
IDEMPOTENCY = "investigation-feedback-fixture"
CASES = [
    ("assessments", "search", (), {"from_": FROM, "to": TO, "decision": "block", "limit": 1, "cursor": "next_fixture"},
     "search", "POST", "/v1/assessments/search", 200),
    ("assessments", "retrieve_version", (ASSESSMENT, 1), {"response_mode": "standard"},
     "revision", "GET", f"/v1/assessments/{ASSESSMENT}/versions/1", 200),
    ("assessments", "bind_account", (ASSESSMENT,), {"account_id": ACCOUNT},
     "binding", "POST", f"/v1/assessments/{ASSESSMENT}/bind", 201),
    ("accounts", "record_outcome", (ACCOUNT,), {"outcome": "confirmed_abuse", "idempotency_key": IDEMPOTENCY},
     "outcome", "POST", f"/v1/accounts/{ACCOUNT}/outcomes", 202),
    ("accounts", "list_outcomes", (ACCOUNT,), {"limit": 1, "cursor": "next_fixture"},
     "outcomes", "GET", f"/v1/accounts/{ACCOUNT}/outcomes", 200),
    ("accounts", "retrieve_decision", (ACCOUNT, 1), {},
     "decision", "GET", f"/v1/accounts/{ACCOUNT}/decisions/1", 200),
    ("accounts", "associate_credential", (ACCOUNT,), {"sha256": "f" * 64},
     "credential", "POST", f"/v1/accounts/{ACCOUNT}/credentials", 201),
    ("accounts", "list_credentials", (ACCOUNT,), {"limit": 1, "cursor": "next_fixture"},
     "credentials", "GET", f"/v1/accounts/{ACCOUNT}/credentials", 200),
    ("accounts", "retire_credential", (ACCOUNT, CREDENTIAL), {},
     "retired", "DELETE", f"/v1/accounts/{ACCOUNT}/credentials/{CREDENTIAL}", 200),
    ("accounts", "export", (ACCOUNT,), {"response_mode": "standard"},
     "export", "GET", f"/v1/accounts/{ACCOUNT}/export", 200),
    ("requests", "list", (), {"from_": FROM, "to": TO, "request_id": "a" * 32, "status": 200,
                               "limit": 1, "cursor": "next_fixture"},
     "requests", "GET", "/v1/requests", 200),
]


def verify(result, seen, name, method, path):
    assert len(seen) == 1
    request = seen[0]
    assert request.method == method
    assert request.url.path == path
    assert result.meta.request_id == "a" * 32
    assert not hasattr(result, "result"), "public methods must return the model, not a response envelope"
    assert "meta" not in result.model_dump()
    if name == "search":
        assert json.loads(request.content) == {"from": FROM, "to": TO, "decision": "block", "limit": 1, "cursor": "next_fixture"}
        assert result.items[0].detail.assessment_version == EXAMPLES["revision"]["detail"]["assessment_version"]
    if name == "outcome":
        assert request.headers["idempotency-key"] == IDEMPOTENCY
        assert json.loads(request.content) == {"outcome": "confirmed_abuse"}
        assert result.risk_version == 2
    if name == "binding":
        assert json.loads(request.content) == {"account_id": ACCOUNT}
    if name == "credential":
        assert json.loads(request.content) == {"sha256": "f" * 64}
        assert not hasattr(result, "sha256")
    if name == "retired":
        assert result.retired_by.key_id == "fixture-key"
    if name == "export":
        assert result.complete
        assert result.decisions[0].account.risk_version == 1
    if name == "requests":
        assert request.url.params["from"] == FROM
        assert request.url.params["to"] == TO
        assert request.url.params["request_id"] == "a" * 32
        assert request.url.params["status"] == "200"
        assert result.items[0].decision.account.risk_version == 1
    if name in ("outcomes", "credentials", "requests"):
        assert request.url.params["cursor"] == "next_fixture"
        assert result.next_cursor == "next_fixture"


@pytest.mark.parametrize("group,operation,args,kwargs,name,method,path,status", CASES)
def test_sync_investigation_surface(group, operation, args, kwargs, name, method, path, status):
    sdk, seen = make([answer(EXAMPLES[name], status)])
    assert isinstance(sdk.requests, Requests)
    with sdk:
        result = getattr(getattr(sdk, group), operation)(*args, **kwargs)
    verify(result, seen, name, method, path)


@pytest.mark.parametrize("group,operation,args,kwargs,name,method,path,status", CASES)
def test_async_investigation_surface(group, operation, args, kwargs, name, method, path, status):
    sdk, seen = make([answer(EXAMPLES[name], status)])

    async def run():
        async with sdk:
            return await getattr(getattr(sdk, group), operation + "_async")(*args, **kwargs)

    verify(asyncio.run(run()), seen, name, method, path)


def test_feedback_generates_a_key_once_and_preserves_an_explicit_correction():
    correction = copy.deepcopy(EXAMPLES["outcome"])
    correction.update(outcome="false_positive", supersedes=EXAMPLES["outcome"]["id"])
    sdk, seen = make([answer(EXAMPLES["outcome"], 202), answer(correction, 202)])
    with sdk:
        sdk.accounts.record_outcome(ACCOUNT, outcome="confirmed_abuse")
        result = sdk.accounts.record_outcome(ACCOUNT, outcome="false_positive", supersedes=correction["supersedes"],
                                             idempotency_key=IDEMPOTENCY)
    assert UUID.fullmatch(seen[0].headers["idempotency-key"])
    assert seen[1].headers["idempotency-key"] == IDEMPOTENCY
    assert json.loads(seen[1].content) == {"outcome": "false_positive", "supersedes": correction["supersedes"]}
    assert result.supersedes == correction["supersedes"]


def test_stale_correction_remains_a_typed_conflict():
    sdk, _ = make([problem(409, "outcome_conflict")])
    with sdk, pytest.raises(ConflictError) as error:
        sdk.accounts.record_outcome(ACCOUNT, outcome="false_positive", supersedes=EXAMPLES["outcome"]["id"])
    assert error.value.code == "outcome_conflict"


def test_new_sync_methods_keep_public_timeout_translation():
    sdk, _ = make([httpx.ReadTimeout("fixture timeout")], retry_config=None)
    with sdk, pytest.raises(APITimeoutError):
        sdk.requests.list(from_=FROM, to=TO)


def test_new_async_methods_keep_public_timeout_translation():
    sdk, _ = make([httpx.ReadTimeout("fixture timeout")], retry_config=None)

    async def run():
        async with sdk:
            with pytest.raises(APITimeoutError):
                await sdk.requests.list_async(from_=FROM, to=TO)

    asyncio.run(run())
