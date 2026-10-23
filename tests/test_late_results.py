import hashlib
import hmac
import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from types import SimpleNamespace
from urllib.parse import parse_qsl, urlsplit

import pytest

from noresponse import (
    DEFAULT_LATE_RESULT_POLICY,
    ProviderActionError,
    WebhookVerificationError,
    auth0_actions,
    clerk_actions,
    handle_late_result,
    late_result_action,
    log_only_actions,
    workos_actions,
)
from noresponse.webhooks import AccountDeleted, AssessmentExpired, EndpointVerification, WebhookEvent

FIXTURES = Path(__file__).parent / "fixtures"
SECRET = "late-result-secret"
KEY = "whk_sdktest01"
NOW = 1791968402
SECRETS = {KEY: SECRET}


def fixture(name):
    return json.loads((FIXTURES / name).read_text())


VIEW = fixture("valid/assessment-view-complete.json")


def decided(decision):
    return {**VIEW, "account": {**VIEW["account"], "risk": {**VIEW["account"]["risk"], "decision": decision}}}


REVIEW = decided("review")
STEP_UP = decided("step_up")
PENDING = fixture("valid/assessment-view-pending.json")
KNOWN_PENDING = fixture("valid/assessment-view-pending-known-account.json")
EXPIRED = fixture("valid/webhook-assessment-expired.json")


def delivery(data, account_id=None, **extra):
    body = {
        "id": "evt_01JA2ZB4N5P6Q7R8S9T0VWXYZ2",
        "type": "assessment.updated",
        "created_at": "2026-10-18T11:00:04Z",
        **extra,
        "data": {**data, "detail": {**data["detail"], "account_id": account_id}} if account_id else data,
    }
    raw = json.dumps(body).encode("utf-8")
    stamp = str(NOW)
    digest = hmac.new(SECRET.encode(), stamp.encode() + b"." + raw, hashlib.sha256).hexdigest()
    headers = {
        "NR-Webhook-Id": body["id"],
        "NR-Webhook-Timestamp": stamp,
        "NR-Webhook-Key-Id": KEY,
        "NR-Webhook-Signature": "v1=" + digest,
    }
    return raw, headers


class Call:
    def __init__(self, method, path, query, auth, body):
        self.method, self.path, self.query, self.auth, self.body = method, path, query, auth, body


class MockProvider:
    """A local HTTP server standing in for a provider's admin API. It records each request and answers from route."""

    def __init__(self, route):
        self.calls = []
        outer = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def handle_any(self):
                length = int(self.headers.get("Content-Length") or 0)
                text = self.rfile.read(length).decode() if length else ""
                url = urlsplit(self.path)
                call = Call(
                    self.command,
                    url.path,
                    dict(parse_qsl(url.query)),
                    self.headers.get("Authorization"),
                    json.loads(text) if text else None,
                )
                call.accept = self.headers.get("Accept")
                call.content_type = self.headers.get("Content-Type")
                outer.calls.append(call)
                status, body = route(call) or (404, {"error": "not found"})
                payload = b"" if body is None else json.dumps(body).encode()
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)

            do_GET = do_POST = do_PUT = do_PATCH = do_DELETE = handle_any

        self.server = HTTPServer(("127.0.0.1", 0), Handler)
        self.url = f"http://127.0.0.1:{self.server.server_address[1]}"
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def close(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()


@pytest.fixture
def mock_provider():
    made = []

    def make(route):
        m = MockProvider(route)
        made.append(m)
        return m

    yield make
    for m in made:
        m.close()


def test_the_default_policy_revokes_on_review_and_block_and_does_nothing_on_allow_step_up_pending_or_expiry():
    def ev(data):
        return WebhookEvent("evt_x", "assessment.updated", "2026-10-18T11:00:04Z", data)

    class Data:
        def __init__(self, status, decision=None):
            self.status = status
            self.account = SimpleNamespace(risk=SimpleNamespace(decision=decision)) if decision else None

    assert late_result_action(ev(Data("complete", "review"))) == "revoke_sessions"
    assert late_result_action(ev(Data("complete", "block"))) == "revoke_sessions"
    assert late_result_action(ev(Data("complete", "step_up"))) == "none"
    assert late_result_action(ev(Data("partial", "allow"))) == "none"
    assert late_result_action(ev(Data("pending"))) == "none"
    assert late_result_action(ev(Data("pending", "review"))) == "none"
    assert late_result_action(ev(AssessmentExpired("asm_x", "acct", 1))) == "none"
    assert late_result_action(WebhookEvent("evt_x", "endpoint.verification", "x", EndpointVerification("whe_x", "c"))) == "none"
    assert late_result_action(WebhookEvent("evt_x", "account.deleted", "x", AccountDeleted("acct_1", 1, "x"))) == "none"
    assert late_result_action(ev(Data("complete", "step_up")), {"step_up": "ban"}) == "ban"
    assert late_result_action(ev(Data("complete", "block")), {"block": "ban"}) == "ban"
    assert late_result_action(ev(Data("complete", "review")), {"step_up": "ban"}) == "none"
    with pytest.raises(TypeError):
        late_result_action(ev(Data("complete", "review")), {"review": "delete"})
    assert dict(DEFAULT_LATE_RESULT_POLICY) == {"allow": "none", "step_up": "none", "review": "revoke_sessions", "block": "revoke_sessions"}


def test_clerk_review_revokes_each_active_session_and_a_ban_policy_bans_the_user(mock_provider):
    def route(c):
        if c.method == "GET" and c.path == "/v1/sessions":
            return 200, ([{"id": "sess_1", "status": "active"}, {"id": "sess_2", "status": "active"}] if c.query.get("offset") == "0" else [])
        if c.method == "POST" and c.path in ("/v1/sessions/sess_1/revoke", "/v1/sessions/sess_2/revoke"):
            return 200, {"id": c.path.split("/")[3], "status": "revoked"}
        if c.method == "POST" and c.path == "/v1/users/user_2EXAMPLE/ban":
            return 200, {"id": "user_2EXAMPLE", "banned": True}

    mock = mock_provider(route)
    clerk = clerk_actions("sk_test_mock", base_url=mock.url + "/v1")
    raw, headers = delivery(REVIEW, "user_2EXAMPLE")
    result = handle_late_result(raw, headers, SECRETS, clerk, now=NOW)
    assert result.action == "revoke_sessions"
    assert result.user_id == "user_2EXAMPLE"
    assert result.event.data.id == REVIEW["id"]
    assert [f"{c.method} {c.path}" for c in mock.calls] == [
        "GET /v1/sessions",
        "POST /v1/sessions/sess_1/revoke",
        "POST /v1/sessions/sess_2/revoke",
    ]
    assert mock.calls[0].query == {"user_id": "user_2EXAMPLE", "status": "active", "limit": "100", "offset": "0"}
    assert all(c.auth == "Bearer sk_test_mock" and c.accept == "application/json" for c in mock.calls)

    mock.calls.clear()
    banned = handle_late_result(raw, headers, SECRETS, clerk, now=NOW, policy={"review": "ban"})
    assert banned.action == "ban"
    assert [f"{c.method} {c.path}" for c in mock.calls] == ["POST /v1/users/user_2EXAMPLE/ban"]


def test_clerk_pages_a_full_first_page_and_reads_a_data_envelope(mock_provider):
    def route(c):
        if c.method == "GET":
            if c.query["offset"] == "0":
                return 200, {"data": [{"id": f"sess_{i}", "status": "active"} for i in range(100)]}
            return 200, {"data": [{"id": "sess_last", "status": "active"}, {"id": "sess_old", "status": "revoked"}]}
        return 200, {}

    mock = mock_provider(route)
    clerk_actions("sk_test_mock", base_url=mock.url).revoke_sessions("user_1")
    gets = [c for c in mock.calls if c.method == "GET"]
    assert [g.query["offset"] for g in gets] == ["0", "100"]
    posts = [c.path for c in mock.calls if c.method == "POST"]
    assert len(posts) == 101 and posts[-1] == "/sessions/sess_last/revoke"


def test_workos_revoke_pages_through_the_sessions_and_ban_revokes_then_deletes_the_user(mock_provider):
    def route(c):
        if c.method == "GET" and c.path == "/user_management/users/user_01WORKOS/sessions":
            if "after" not in c.query:
                return 200, {
                    "object": "list",
                    "data": [{"id": "session_A", "status": "active"}, {"id": "session_X", "status": "revoked"}],
                    "list_metadata": {"before": None, "after": "session_X"},
                }
            return 200, {"object": "list", "data": [{"id": "session_B", "status": "active"}], "list_metadata": {"before": "session_B", "after": None}}
        if c.method == "POST" and c.path == "/user_management/sessions/revoke":
            return 200, {"id": c.body["session_id"], "status": "revoked"}
        if c.method == "DELETE" and c.path == "/user_management/users/user_01WORKOS":
            return 202, None

    mock = mock_provider(route)
    workos = workos_actions("sk_test_workos", base_url=mock.url)
    raw, headers = delivery(STEP_UP, "acct_7f3a9c")
    result = handle_late_result(
        raw,
        headers,
        SECRETS,
        workos,
        now=NOW,
        policy={"step_up": "ban"},
        resolve_user_id=lambda account_id, event: "user_01WORKOS" if account_id == "acct_7f3a9c" else None,
    )
    assert result.action == "ban"
    assert result.user_id == "user_01WORKOS"
    assert [
        f"{c.method} {c.path} {json.dumps(c.body if c.body is not None else c.query, separators=(',', ':'))}" for c in mock.calls
    ] == [
        'GET /user_management/users/user_01WORKOS/sessions {"limit":"100"}',
        'GET /user_management/users/user_01WORKOS/sessions {"limit":"100","after":"session_X"}',
        'POST /user_management/sessions/revoke {"session_id":"session_A"}',
        'POST /user_management/sessions/revoke {"session_id":"session_B"}',
        "DELETE /user_management/users/user_01WORKOS {}",
    ]
    assert all(c.auth == "Bearer sk_test_workos" for c in mock.calls)
    assert [c.content_type for c in mock.calls if c.method == "POST"] == ["application/json"] * 2


def test_workos_ban_treats_a_missing_user_as_done(mock_provider):
    mock = mock_provider(lambda c: (200, {"data": [], "list_metadata": {"after": None}}) if c.method == "GET" else None)
    workos_actions("sk_test_workos", base_url=mock.url).ban("user_gone")
    assert [f"{c.method} {c.path}" for c in mock.calls] == ["GET /user_management/users/user_gone/sessions", "DELETE /user_management/users/user_gone"]


def test_auth0_review_deletes_sessions_and_refresh_tokens_ban_blocks_first_the_pipe_is_escaped(mock_provider):
    user_id = "auth0|64abc0de1234567890abcdef"
    escaped = "auth0%7C64abc0de1234567890abcdef"

    def route(c):
        if c.path == f"/api/v2/users/{escaped}/sessions" and c.method == "DELETE":
            return 202, None
        if c.path == f"/api/v2/users/{escaped}/refresh-tokens" and c.method == "DELETE":
            return 202, None
        if c.path == f"/api/v2/users/{escaped}" and c.method == "PATCH":
            return 200, {"user_id": user_id, "blocked": c.body["blocked"]}

    mock = mock_provider(route)
    auth0 = auth0_actions("mgmt_token", base_url=mock.url + "/api/v2")
    raw, headers = delivery(REVIEW, user_id)
    result = handle_late_result(raw, headers, SECRETS, auth0, now=NOW)
    assert result.action == "revoke_sessions"
    assert [f"{c.method} {c.path}" for c in mock.calls] == [f"DELETE /api/v2/users/{escaped}/sessions", f"DELETE /api/v2/users/{escaped}/refresh-tokens"]

    mock.calls.clear()
    handle_late_result(raw, headers, SECRETS, auth0, now=NOW, policy={"review": "ban"})
    assert [f"{c.method} {c.path} {json.dumps(c.body, separators=(',', ':'))}" for c in mock.calls] == [
        f'PATCH /api/v2/users/{escaped} {{"blocked":true}}',
        f"DELETE /api/v2/users/{escaped}/sessions null",
        f"DELETE /api/v2/users/{escaped}/refresh-tokens null",
    ]
    assert all(c.auth == "Bearer mgmt_token" for c in mock.calls)


FEATURE_NOT_ENABLED = (403, {"statusCode": 403, "error": "Forbidden", "message": "This feature is not enabled for this tenant.", "errorCode": "feature_not_enabled"})


class Auth0WithoutSessionsApi:
    """An Auth0 tenant on a plan without the sessions API, as a Free tenant answers.

    Both bulk endpoints refuse with 403 feature_not_enabled, while
    /device-credentials and PATCH /users/{id} work. It keeps the refresh tokens
    and the blocked flag, so a repeated delivery sees what the first left.
    """

    def __init__(self, escaped, refresh_tokens_api=False):
        self.escaped = escaped
        self.refresh_tokens_api = refresh_tokens_api
        self.blocked = False
        self.credentials = [("dcr_a", "refresh_token"), ("dcr_b", "refresh_token"), ("dcr_r", "rotating_refresh_token")]

    def __call__(self, c):
        user = f"/api/v2/users/{self.escaped}"
        if c.method == "DELETE" and c.path == user + "/sessions":
            return FEATURE_NOT_ENABLED
        if c.method == "DELETE" and c.path == user + "/refresh-tokens":
            if not self.refresh_tokens_api:
                return FEATURE_NOT_ENABLED
            self.credentials = []
            return 202, None
        if c.method == "PATCH" and c.path == user:
            self.blocked = c.body.get("blocked") is True
            return 200, {"blocked": self.blocked}
        if c.method == "GET" and c.path == "/api/v2/device-credentials":
            return 200, [{"id": i, "type": t, "user_id": c.query["user_id"]} for i, t in self.credentials if t == c.query["type"]]
        if c.method == "DELETE" and c.path.startswith("/api/v2/device-credentials/"):
            credential = c.path.rsplit("/", 1)[1]
            if credential not in [i for i, _ in self.credentials]:
                return 404, {"errorCode": "inexistent_device_credential"}
            self.credentials = [(i, t) for i, t in self.credentials if i != credential]
            return 204, None
        return None


def test_auth0_without_the_sessions_api_blocks_deletes_device_credentials_and_reports_ban(mock_provider):
    user_id = "auth0|64abc0de1234567890abcdef"
    escaped = "auth0%7C64abc0de1234567890abcdef"
    tenant = Auth0WithoutSessionsApi(escaped)
    mock = mock_provider(tenant)
    auth0 = auth0_actions("mgmt_token", base_url=mock.url + "/api/v2")
    raw, headers = delivery(REVIEW, user_id)

    result = handle_late_result(raw, headers, SECRETS, auth0, now=NOW)
    assert result.action == "ban" and result.user_id == user_id
    assert tenant.blocked and tenant.credentials == []
    assert [f"{c.method} {c.path} {c.query.get('type', '')}".rstrip() for c in mock.calls] == [
        f"DELETE /api/v2/users/{escaped}/sessions",
        f"PATCH /api/v2/users/{escaped}",
        f"DELETE /api/v2/users/{escaped}/refresh-tokens",
        "GET /api/v2/device-credentials refresh_token",
        "GET /api/v2/device-credentials rotating_refresh_token",
        "DELETE /api/v2/device-credentials/dcr_a",
        "DELETE /api/v2/device-credentials/dcr_b",
        "DELETE /api/v2/device-credentials/dcr_r",
    ]
    assert all(c.query["user_id"] == user_id for c in mock.calls if c.method == "GET")

    # The same delivery again: still blocked, nothing left to delete, same report.
    mock.calls.clear()
    assert handle_late_result(raw, headers, SECRETS, auth0, now=NOW).action == "ban"
    assert tenant.blocked
    assert not [c for c in mock.calls if c.method == "DELETE" and c.path.startswith("/api/v2/device-credentials/")]

    # ban blocks first, and the plan refusing the sessions endpoint is no failure.
    tenant.blocked = False
    tenant.credentials.append(("dcr_c", "refresh_token"))
    mock.calls.clear()
    assert handle_late_result(raw, headers, SECRETS, auth0, now=NOW, policy={"review": "ban"}).action == "ban"
    assert mock.calls[0].method == "PATCH"
    assert tenant.blocked and tenant.credentials == []

    # Called directly, revoke_sessions takes the same fallback.
    tenant.blocked = False
    auth0.revoke_sessions(user_id)
    assert tenant.blocked


def test_auth0_with_refresh_tokens_but_no_sessions_api_still_blocks_and_a_scope_refusal_never_falls_back(mock_provider):
    tenant = Auth0WithoutSessionsApi("auth0%7Cabc", refresh_tokens_api=True)
    mock = mock_provider(tenant)
    raw, headers = delivery(REVIEW, "auth0|abc")
    assert handle_late_result(raw, headers, SECRETS, auth0_actions("mgmt_token", base_url=mock.url + "/api/v2"), now=NOW).action == "ban"
    assert tenant.blocked
    assert not [c for c in mock.calls if c.path == "/api/v2/device-credentials"]

    scope = (403, {"statusCode": 403, "error": "Forbidden", "message": "Insufficient scope, expected any of: delete:sessions", "errorCode": "insufficient_scope"})
    scoped = mock_provider(lambda c: scope if c.method == "DELETE" else (200, {}))
    with pytest.raises(ProviderActionError) as refused:
        handle_late_result(raw, headers, SECRETS, auth0_actions("mgmt_token", base_url=scoped.url + "/api/v2"), now=NOW)
    assert refused.value.status == 403 and refused.value.code == "insufficient_scope"
    assert [c.method for c in scoped.calls] == ["DELETE"]


def test_a_provider_without_act_reports_the_action_asked_for():
    done = []

    class Custom:
        name = "custom"

        def revoke_sessions(self, user_id):
            done.append(f"revoke {user_id}")

        def ban(self, user_id):
            done.append(f"ban {user_id}")

    raw, headers = delivery(REVIEW, "u_1")
    assert handle_late_result(raw, headers, SECRETS, Custom(), now=NOW).action == "revoke_sessions"
    assert handle_late_result(raw, headers, SECRETS, Custom(), now=NOW, policy={"review": "ban"}).action == "ban"
    assert done == ["revoke u_1", "ban u_1"]


def test_an_unverified_quiet_or_unmapped_event_makes_no_provider_call_and_a_provider_refusal_raises(mock_provider):
    mock = mock_provider(lambda c: (403, {"error": "insufficient_scope", "secret": "leak"}) if c.method == "DELETE" else None)
    auth0 = auth0_actions("mgmt_token", base_url=mock.url + "/api/v2")
    raw, headers = delivery(REVIEW, "auth0|abc")
    with pytest.raises(WebhookVerificationError) as bad:
        handle_late_result(raw, headers, {KEY: "wrong"}, auth0, now=NOW)
    assert bad.value.code == "invalid_signature"
    with pytest.raises(WebhookVerificationError):
        handle_late_result(raw + b" ", headers, SECRETS, auth0, now=NOW)
    with pytest.raises(WebhookVerificationError) as stale:
        handle_late_result(raw, headers, SECRETS, auth0, now=NOW + 301)
    assert stale.value.code == "invalid_timestamp"
    for data in (STEP_UP, PENDING, {**KNOWN_PENDING, "account": REVIEW["account"]}, EXPIRED["data"]):
        d_raw, d_headers = delivery(data)
        assert handle_late_result(d_raw, d_headers, SECRETS, auth0, now=NOW).action == "none"
    assert handle_late_result(raw, headers, SECRETS, auth0, now=NOW, resolve_user_id=lambda a, e: None).action == "none"
    assert len(mock.calls) == 0
    with pytest.raises(ProviderActionError) as refused:
        handle_late_result(raw, headers, SECRETS, auth0, now=NOW)
    assert refused.value.status == 403 and refused.value.provider == "auth0"
    assert "leak" not in str(refused.value) and "mgmt_token" not in str(refused.value)
    assert len(mock.calls) == 1


def test_arguments_and_an_injected_transport():
    with pytest.raises(ValueError):
        clerk_actions("")
    with pytest.raises(ValueError):
        auth0_actions("t")
    seen = []

    def transport(method, url, headers, body):
        seen.append((method, url, dict(headers), body))
        return 200, b""

    clerk = clerk_actions("sk", base_url="https://example.invalid/v1/", transport=transport)
    with pytest.raises(ValueError):
        clerk.ban("")
    clerk.ban("user|1")
    assert seen == [("POST", "https://example.invalid/v1/users/user%7C1/ban", {"Authorization": "Bearer sk", "Accept": "application/json"}, None)]


def test_a_webhook_test_event_acts_on_nothing_whatever_the_policy_and_user_id(mock_provider):
    mock = mock_provider(lambda c: (200, {}))
    workos = workos_actions("sk_test_workos", base_url=mock.url)
    raw, headers = delivery(STEP_UP, "acct_7f3a9c", test=True)
    resolved = []

    def resolve(account_id, event):
        resolved.append(account_id)
        return "user_01WORKOS"

    result = handle_late_result(
        raw, headers, SECRETS, workos, now=NOW, policy={"allow": "ban", "step_up": "ban", "review": "ban"}, resolve_user_id=resolve
    )
    assert result.event.test is True
    assert result.action == "none" and result.user_id is None
    assert resolved == [] and mock.calls == []
    assert late_result_action(result.event, {"step_up": "ban"}) == "none"


def test_a_repeated_delivery_is_safe_a_provider_404_for_a_gone_user_or_session_counts_as_done(mock_provider):
    # Every user and session is already gone, as after a first WorkOS ban deleted the user.
    mock = mock_provider(lambda c: (404, {"error": "not_found"}))
    raw, headers = delivery(REVIEW, "user_gone")
    providers = [
        workos_actions("sk_test_workos", base_url=mock.url),
        clerk_actions("sk_test_mock", base_url=mock.url + "/v1"),
        auth0_actions("mgmt_token", base_url=mock.url + "/api/v2"),
    ]
    for provider in providers:
        for review in ("ban", "revoke_sessions"):
            for _ in range(2):
                assert handle_late_result(raw, headers, SECRETS, provider, now=NOW, policy={"review": review}).action == review
    assert mock.calls


def test_a_clerk_session_gone_between_list_and_revoke_is_done_and_other_refusals_still_raise(mock_provider):
    def route(c):
        if c.method == "GET" and c.path == "/v1/sessions":
            return 200, [{"id": "sess_1", "status": "active"}]
        if c.method == "POST" and c.path == "/v1/sessions/sess_1/revoke":
            return 404, {"errors": [{"code": "resource_not_found"}]}
        if c.method == "POST" and c.path == "/v1/users/user_2EXAMPLE/ban":
            return 500, {"error": "boom"}
        return None

    mock = mock_provider(route)
    clerk = clerk_actions("sk_test_mock", base_url=mock.url + "/v1")
    raw, headers = delivery(REVIEW, "user_2EXAMPLE")
    assert handle_late_result(raw, headers, SECRETS, clerk, now=NOW).action == "revoke_sessions"
    with pytest.raises(ProviderActionError) as refused:
        handle_late_result(raw, headers, SECRETS, clerk, now=NOW, policy={"review": "ban"})
    assert refused.value.status == 500


def test_the_log_only_provider_logs_what_it_would_revoke_or_ban_and_calls_nothing(monkeypatch, caplog):
    def refuse(*args, **kwargs):
        raise AssertionError("the log-only provider must not call out")

    monkeypatch.setattr("urllib.request.urlopen", refuse)
    lines = []
    log_only = log_only_actions(lines.append)
    assert log_only.name == "log_only"
    raw, headers = delivery(REVIEW, "usr_8f2k1")
    revoked = handle_late_result(raw, headers, SECRETS, log_only, now=NOW)
    assert (revoked.action, revoked.user_id) == ("revoke_sessions", "usr_8f2k1")
    banned = handle_late_result(raw, headers, SECRETS, log_only, now=NOW, policy={"review": "ban"})
    assert banned.action == "ban"
    assert lines == [
        "NoResponse late result (log only): would revoke every session of user usr_8f2k1",
        "NoResponse late result (log only): would ban user usr_8f2k1 and end their sessions",
    ]
    raw, headers = delivery(REVIEW, "usr_8f2k1", test=True)
    assert handle_late_result(raw, headers, SECRETS, log_only, now=NOW).action == "none"
    assert len(lines) == 2
    with pytest.raises(ValueError):
        log_only.ban("")

    with caplog.at_level("WARNING", logger="noresponse.late_results"):
        log_only_actions().revoke_sessions("usr_8f2k1")
    assert [(r.name, r.levelname, r.getMessage()) for r in caplog.records] == [
        ("noresponse.late_results", "WARNING", "NoResponse late result (log only): would revoke every session of user usr_8f2k1"),
    ]
