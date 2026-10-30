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
    ("assessments", "aggregate", (), {"from_": FROM, "to": TO, "bucket": "day", "group_by": ["decision", "reason"],
                                      "metrics": ["count", "late_flips"], "flow": "account_creation", "revision": "first",
                                      "time_zone": "Europe/London"},
     "aggregate", "POST", "/v1/assessments/aggregate", 200),
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
    ("accounts", "list_linked", (ACCOUNT,), {"limit": 1, "cursor": "next_fixture"},
     "linked", "GET", f"/v1/accounts/{ACCOUNT}/linked_accounts", 200),
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
    if name == "aggregate":
        assert json.loads(request.content) == {"from": FROM, "to": TO, "bucket": "day", "group_by": ["decision", "reason"],
                                               "metrics": ["count", "late_flips"], "limit": 20, "flow": "account_creation",
                                               "revision": "first", "time_zone": "Europe/London"}
        assert result.buckets[0].groups[0].reason == "aged_identity" and result.buckets[0].groups[0].impact == "medium"
        assert result.buckets[0].late_flips[0].to == "review"
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


@pytest.mark.parametrize("asynchronous", [False, True])
def test_identifier_searches_preserve_typed_inputs_and_match_evidence(asynchronous):
    from noresponse import IdentifierSearch, IdentifierMatch, AccountDirectoryPage

    identifier = IdentifierSearch(kind="username", value="janedoe", match="canonical", namespace="customer")
    matched = {"kind": "username", "value": "JaneDoe", "match_basis": "canonical", "namespace": "customer", "provenance": "submitted", "assessment_id": ASSESSMENT}
    account_page = {"schema_version": "1", "items": [{"account_id": ACCOUNT, "latest": EXAMPLES["revision"], "assessments": 2, "matched_identifier": matched}], "total": 1, "total_capped": False}
    assessment_page = {"schema_version": "1", "retention_days": 365, "items": [{**EXAMPLES["revision"], "matched_identifier": matched}], "total": 1, "total_capped": False}
    client, seen = make([answer(account_page, 200), answer(assessment_page, 200)])

    async def run():
        async with client:
            return (await client.accounts.search_async(identifier=identifier, limit=1),
                    await client.assessments.search_async(from_=FROM, to=TO, identifier=identifier, limit=1))

    if asynchronous:
        account_response, assessments = asyncio.run(run())
    else:
        with client:
            account_response = client.accounts.search(identifier=identifier, limit=1)
            assessments = client.assessments.search(from_=FROM, to=TO, identifier=identifier, limit=1)
    # Account search was already shipped as the generated operation envelope.
    # Keep .result and headers available to existing sync/async callers.
    assert account_response.headers["x-request-id"] == ["a" * 32]
    accounts = account_response.result
    assert isinstance(accounts, AccountDirectoryPage)
    for request, page in zip(seen, (accounts, assessments)):
        assert json.loads(request.content)["identifier"] == {"kind": "username", "value": "janedoe", "match": "canonical", "namespace": "customer"}
        match = page.items[0].matched_identifier
        assert isinstance(match, IdentifierMatch)
        assert match.value == "JaneDoe" and match.match_basis == "canonical"
        assert match.provenance == "submitted" and match.namespace == "customer"
        assert match.assessment_id == ASSESSMENT
    assert assessments.meta.request_id == "a" * 32
    assert accounts.items[0].current is None
    assert [request.url.path for request in seen] == ["/v1/accounts/search", "/v1/assessments/search"]


@pytest.mark.parametrize("asynchronous", [False, True])
def test_combined_identifier_searches_preserve_typed_scope_and_witnesses(asynchronous):
    from noresponse import IdentifierExpression, IdentifierTermMatch

    expression = {"and": [
        {"term": {"kind": "phone", "value": "+14155552671", "match": "canonical"}},
        {"or": [
            {"term": {"kind": "email", "value": "other@example.com", "match": "exact"}},
            {"term": {"kind": "username", "value": "janedoe", "match": "canonical", "namespace": "customer"}},
        ]},
    ]}
    matched = [
        {"kind": "phone", "value": "+14155552671", "match_basis": "canonical", "provenance": "submitted", "assessment_id": ASSESSMENT, "term_index": 0},
        {"kind": "username", "value": "JaneDoe", "match_basis": "canonical", "namespace": "customer", "provenance": "submitted", "assessment_id": ASSESSMENT, "term_index": 2},
    ]
    account_query = IdentifierExpression.model_validate({"scope": "account", "expression": expression})
    assessment_query = IdentifierExpression.model_validate({"scope": "assessment", "expression": expression})
    account_page = {"schema_version": "1", "items": [{"account_id": ACCOUNT, "latest": EXAMPLES["revision"], "assessments": 2, "matched_identifiers": matched}], "total": 1, "total_capped": False}
    assessment_page = {"schema_version": "1", "retention_days": 365, "items": [{**EXAMPLES["revision"], "matched_identifiers": matched}], "total": 1, "total_capped": False}
    client, seen = make([answer(account_page, 200), answer(assessment_page, 200)])

    async def run():
        async with client:
            return (await client.accounts.search_async(identifier_expression=account_query),
                    await client.assessments.search_async(from_=FROM, to=TO, identifier_expression=assessment_query))

    if asynchronous:
        account_response, assessments = asyncio.run(run())
    else:
        with client:
            account_response = client.accounts.search(identifier_expression=account_query)
            assessments = client.assessments.search(from_=FROM, to=TO, identifier_expression=assessment_query)
    assert account_response.headers["x-request-id"] == ["a" * 32]
    for index, page in enumerate((account_response.result, assessments)):
        assert json.loads(seen[index].content)["identifier_expression"] == {"scope": "assessment" if index else "account", "expression": expression}
        assert page.items[0].matched_identifier is None
        actual = page.items[0].matched_identifiers
        assert all(isinstance(value, IdentifierTermMatch) for value in actual)
        assert [(value.term_index, value.kind, value.value, value.assessment_id) for value in actual] == [
            (value["term_index"], value["kind"], value["value"], value["assessment_id"]) for value in matched
        ]
        assert actual[1].namespace == "customer"
    assert assessments.meta.request_id == "a" * 32


@pytest.mark.parametrize("asynchronous", [False, True])
def test_linked_accounts_keep_both_submitted_witnesses(asynchronous):
    from noresponse import LinkedAccountPage, SharedIdentifier

    client, seen = make([answer(EXAMPLES["linked"], 200)])

    async def run():
        async with client:
            return await client.accounts.list_linked_async(ACCOUNT, limit=1, cursor="next_fixture")

    if asynchronous:
        page = asyncio.run(run())
    else:
        with client:
            page = client.accounts.list_linked(ACCOUNT, limit=1, cursor="next_fixture")
    assert seen[0].url.params["limit"] == "1" and seen[0].url.params["cursor"] == "next_fixture"
    assert isinstance(page, LinkedAccountPage) and page.meta.request_id == "a" * 32
    want = EXAMPLES["linked"]["items"][0]
    shared = page.items[0].shared_identifiers[0]
    assert isinstance(shared, SharedIdentifier)
    assert page.items[0].account_id == want["account_id"]
    expected = want["shared_identifiers"][0]
    assert (shared.kind, shared.match_basis, shared.account.value, shared.linked_account.value, shared.linked_account.assessment_id) == (
        expected["kind"], expected["match_basis"], expected["account"]["value"], expected["linked_account"]["value"], expected["linked_account"]["assessment_id"])
    assert page.next_cursor == "next_fixture" and page.total_capped is False
