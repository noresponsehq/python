"""Late-result handlers. Hand-written; not generated.

An assessment can be revised after the account creation was allowed: a slow source
settles and the account's decision rises. NoResponse sends the new version as
a signed assessment.updated webhook. handle_late_result verifies that delivery
with construct_event, picks an action from your policy, and acts through the
auth provider's admin API: revoke the user's sessions or ban the user.

The handler verifies the delivery itself, so it never acts on an unverified
event, and it never acts on a test event from webhook_endpoints.send_test_event.
The provider calls are thin: you pass the credentials, and each action is the
provider's documented admin endpoint. A provider 404 for a user or session
that is already gone counts as done, so a repeated delivery is safe.
"""

from __future__ import annotations

import json
import logging
import math
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any, Callable, Mapping, Optional, Tuple, Union
from urllib.parse import quote, urlencode

from .models.shared import WebhookEvent
from .webhook_verification import DEFAULT_TOLERANCE_SECONDS, Headers, construct_event

__all__ = [
    "DEFAULT_LATE_RESULT_POLICY",
    "LateResult",
    "LateResultAction",
    "LateResultProvider",
    "ProviderActionError",
    "Transport",
    "auth0_actions",
    "clerk_actions",
    "handle_late_result",
    "late_result_action",
    "log_only_actions",
    "workos_actions",
]

# What to do to the user. "ban" also ends every session.
LateResultAction = str
NONE = "none"
REVOKE_SESSIONS = "revoke_sessions"
BAN = "ban"
_ACTIONS = (NONE, REVOKE_SESSIONS, BAN)

# The action for each account decision (account.risk.decision). A decision you leave out does nothing.
LatePolicy = Mapping[str, str]

# Revoke sessions on review and block; do nothing on allow or step_up. Banning is opt-in.
DEFAULT_LATE_RESULT_POLICY: LatePolicy = {"allow": NONE, "step_up": NONE, "review": REVOKE_SESSIONS, "block": REVOKE_SESSIONS}

# transport(method, url, headers, body) -> (status, response body bytes), or
# (status, body, response headers) so a 429's Retry-After and
# X-RateLimit-Reset are honoured. The default uses urllib and returns the
# headers. Pass your own for a proxy or for tests.
Transport = Callable[
    [str, str, Mapping[str, str], Optional[bytes]],
    Union[Tuple[int, bytes], Tuple[int, bytes, Mapping[str, str]]],
]


class ProviderActionError(Exception):
    """The provider's admin API refused a call. Answer the webhook with a 5xx so NoResponse retries it.

    A 404 is never raised: the user or session is already gone, so the action is done.
    """

    def __init__(self, provider: str, status: int, message: str, code: Optional[str] = None) -> None:
        super().__init__(message)
        self.provider = provider
        self.status = status
        # The provider's error code from the response body, such as Auth0's
        # errorCode "insufficient_scope", when it sent one.
        self.code = code


class LateResultProvider:
    """The two admin actions, for one auth provider. Build one with clerk_actions, workos_actions or auth0_actions."""

    name: str

    def revoke_sessions(self, user_id: str) -> None:
        """End every active session of the user."""
        raise NotImplementedError

    def ban(self, user_id: str) -> None:
        """Stop the user signing in again and end their sessions."""
        raise NotImplementedError

    def act(self, action: str, user_id: str) -> str:
        """Take action ("revoke_sessions" or "ban") and return the action that ran.

        The default calls ban or revoke_sessions and returns action. A provider
        that has to do more than it was asked overrides it: auth0_actions
        returns "ban" when the tenant's plan has no sessions API and it blocked
        the user to end their sessions.
        """
        if action == BAN:
            self.ban(user_id)
        else:
            self.revoke_sessions(user_id)
        return action


@dataclass(frozen=True)
class LateResult:
    # The verified event. Answer an endpoint.verification with a WebhookVerificationResponse echoing its challenge.
    event: WebhookEvent
    # The action that ran. "none" when the policy, the event or the user id
    # called for nothing. It can be stronger than the policy's action when the
    # provider had to fall back: auth0_actions reports "ban" when it blocked
    # the user because the tenant's plan cannot end sessions.
    action: str
    # The provider user id acted on, when an action was taken.
    user_id: Optional[str] = None


def _text(value: Any) -> Optional[str]:
    value = getattr(value, "value", value)
    return value if isinstance(value, str) else None


def late_result_action(event: WebhookEvent, policy: Optional[LatePolicy] = None) -> str:
    """The action your policy names for a verified event's account.risk.decision.

    Only a complete or partial assessment whose account has a decision can act;
    a pending one and a test event from webhook_endpoints.send_test_event never do.
    """
    chosen = DEFAULT_LATE_RESULT_POLICY if policy is None else policy
    data = event.data
    if event.type not in ("assessment.updated", "account.risk_changed") or (event.type == "assessment.updated" and event.test is True):
        return NONE
    # A pending answer carries an earlier assessment's decision; acting on it would repeat that action.
    if _text(getattr(data, "status", None)) == "pending":
        return NONE
    account = getattr(data, "account", None)
    if event.type == "account.risk_changed":
        # The event is sent when any flow's decision changes; sessions are about the login
        # decision, so an unchanged login decision acts on nothing.
        decision = _text(getattr(getattr(account, "decisions_by_flow", None), "login", None))
        previous = _text(getattr(getattr(data, "previous_decisions_by_flow", None), "login", None))
        if previous == decision:
            return NONE
    else:
        decision = _text(getattr(getattr(account, "risk", None), "decision", None))
    if decision not in ("allow", "step_up", "review", "block"):
        return NONE
    action = chosen.get(decision)
    if action is None:
        return NONE
    if action not in _ACTIONS:
        raise TypeError(f"unknown late result action {action!r}")
    return action


def handle_late_result(
    payload: Union[bytes, str],
    headers: Headers,
    secrets: Mapping[str, str],
    provider: LateResultProvider,
    *,
    policy: Optional[LatePolicy] = None,
    resolve_user_id: Optional[Callable[[str, WebhookEvent], Optional[str]]] = None,
    tolerance_seconds: int = DEFAULT_TOLERANCE_SECONDS,
    now: Optional[float] = None,
) -> LateResult:
    """Verify a webhook delivery and apply your policy to it.

    payload, headers, secrets, tolerance_seconds and now are exactly what
    construct_event takes; a delivery that fails verification raises
    WebhookVerificationError before any provider call. resolve_user_id maps the
    assessment's detail.account_id to the provider user id (default: the account_id
    itself); return None to take no action, or raise to fail the delivery so it
    is retried. A test event acts on nothing. Revoke and ban are safe to repeat,
    but deduplicate on result.event.id and ignore versions older than one you
    have acted on.
    """
    event = construct_event(payload, headers, secrets, tolerance_seconds=tolerance_seconds, now=now)
    action = late_result_action(event, policy)
    if action == NONE:
        return LateResult(event, NONE)
    account_id = event.data.account.id if event.type == "account.risk_changed" else event.data.detail.account_id  # type: ignore[union-attr]
    user_id = resolve_user_id(account_id, event) if resolve_user_id else account_id
    if not user_id:
        return LateResult(event, NONE)
    act = getattr(provider, "act", None)
    if callable(act):
        ran = act(action, user_id)
    elif action == BAN:
        provider.ban(user_id)
        ran = action
    else:
        provider.revoke_sessions(user_id)
        ran = action
    return LateResult(event, ran if ran in _ACTIONS else action, user_id)


def _urllib_transport(method: str, url: str, headers: Mapping[str, str], body: Optional[bytes]) -> Tuple[int, bytes, Mapping[str, str]]:
    request = urllib.request.Request(url, data=body, method=method, headers=dict(headers))
    try:
        with urllib.request.urlopen(request, timeout=30) as response:  # noqa: S310 - caller-supplied https base
            return response.status, response.read(), dict(response.headers.items())
    except urllib.error.HTTPError as error:
        try:
            return error.code, error.read(), dict(error.headers.items()) if error.headers else {}
        finally:
            error.close()


# Rate limits. Auth0 answers 429 when the Management API rate limit is hit,
# and a 429 means it did not act, so the call is safe to send again, a DELETE
# included. One revoke or ban waits at most _RATE_LIMIT_BUDGET seconds in all,
# and each call retries at most _RATE_LIMIT_RETRIES times: it waits
# Retry-After seconds, else until X-RateLimit-Reset (Unix seconds), else
# 0.25, 0.5, 1 and 2 s. A wait that would pass the budget is not started: the
# 429 raises at once as ProviderActionError, the webhook answers 5xx and
# NoResponse delivers it again later. The budget keeps the handler inside the
# 5 s a delivery has to be answered.
_RATE_LIMIT_RETRIES = 4
_RATE_LIMIT_BUDGET = 3.0
_RATE_LIMIT_BACKOFF = 0.25


def _header(headers: Mapping[str, str], name: str) -> Optional[str]:
    for key, value in headers.items():
        if key.lower() == name:
            return str(value).strip()
    return None


def _number(text: Optional[str]) -> Optional[float]:
    try:
        value = float(text) if text else None
    except ValueError:
        return None
    return value if value is not None and math.isfinite(value) else None


def _rate_limit_wait(headers: Mapping[str, str], retry: int) -> float:
    """How long a 429 asks to wait, in seconds."""
    after = _number(_header(headers, "retry-after"))
    if after is not None and after >= 0:
        return after
    reset = _number(_header(headers, "x-ratelimit-reset"))
    if reset is not None:
        return max(0.0, reset - time.time())
    return _RATE_LIMIT_BACKOFF * 2**retry


class _Caller:
    def __init__(
        self,
        name: str,
        base_url: str,
        authorization: str,
        transport: Optional[Transport],
        retry_rate_limits: bool = False,
    ) -> None:
        self.name = name
        self.base = base_url.rstrip("/")
        self.authorization = authorization
        self.transport = transport or _urllib_transport
        self.retry_rate_limits = retry_rate_limits
        self.waited = 0.0

    def fresh(self) -> "_Caller":
        """A caller with the same settings and its own rate-limit budget, for one action."""
        return _Caller(self.name, self.base, self.authorization, self.transport, self.retry_rate_limits)

    def __call__(
        self,
        method: str,
        path: str,
        query: Optional[Mapping[str, str]] = None,
        body: Optional[Any] = None,
    ) -> Any:
        url = self.base + path + ("?" + urlencode(query) if query else "")
        headers = {"Authorization": self.authorization, "Accept": "application/json"}
        data: Optional[bytes] = None
        if body is not None:
            headers["Content-Type"] = "application/json"
            data = json.dumps(body, separators=(",", ":")).encode("utf-8")
        retry = 0
        while True:
            answer = self.transport(method, url, headers, data)
            status, text = answer[0], answer[1]
            if status == 429 and self.retry_rate_limits and retry < _RATE_LIMIT_RETRIES:
                wait = _rate_limit_wait(answer[2] if len(answer) > 2 else {}, retry)  # type: ignore[misc]
                if self.waited + wait <= _RATE_LIMIT_BUDGET:
                    self.waited += wait
                    time.sleep(wait)
                    retry += 1
                    continue
            break
        # Every call names a user or a session. A 404 means it is already gone,
        # so revoke and ban count it as done and a repeated delivery does not fail.
        if status == 404:
            return None
        if not 200 <= status < 300:
            raise ProviderActionError(self.name, status, f"{self.name} {method} {path} answered {status}", _error_code(text))
        if not text:
            return None
        try:
            return json.loads(text)
        except ValueError:
            return None


def _error_code(text: bytes) -> Optional[str]:
    """The error code in a provider's error body: Auth0's errorCode, or a top-level code."""
    try:
        body = json.loads(text) if text else None
    except ValueError:
        return None
    if not isinstance(body, dict):
        return None
    code = body.get("errorCode", body.get("code"))
    return code if isinstance(code, str) and code else None


def _segment(user_id: Any) -> str:
    if not isinstance(user_id, str) or user_id == "":
        raise ValueError("user id must be a non-empty string")
    return quote(user_id, safe="")


def _sessions(body: Any) -> list:
    if isinstance(body, list):
        return body
    data = body.get("data") if isinstance(body, dict) else None
    return data if isinstance(data, list) else []


def _active_ids(page: list) -> list:
    return [s["id"] for s in page if isinstance(s, dict) and s.get("status") == "active" and isinstance(s.get("id"), str) and s["id"]]


class _Clerk(LateResultProvider):
    name = "clerk"
    _PAGE = 100

    def __init__(self, call: _Caller) -> None:
        self._call = call

    def revoke_sessions(self, user_id: str) -> None:
        _segment(user_id)
        active: list = []
        for offset in range(0, self._PAGE * 1000, self._PAGE):
            page = _sessions(
                self._call(
                    "GET",
                    "/sessions",
                    {"user_id": user_id, "status": "active", "limit": str(self._PAGE), "offset": str(offset)},
                )
            )
            active += _active_ids(page)
            if len(page) < self._PAGE:
                break
        for session_id in active:
            self._call("POST", f"/sessions/{quote(session_id, safe='')}/revoke")

    def ban(self, user_id: str) -> None:
        self._call("POST", f"/users/{_segment(user_id)}/ban")


def clerk_actions(secret_key: str, *, base_url: str = "https://api.clerk.com/v1", transport: Optional[Transport] = None) -> LateResultProvider:
    """Clerk Backend API (secret_key is sk_...).

    revoke_sessions lists the user's active sessions (GET /sessions?user_id&status=active)
    and revokes each (POST /sessions/{id}/revoke). ban is POST /users/{id}/ban,
    which revokes every session and blocks sign-in.
    """
    if not secret_key:
        raise ValueError("clerk_actions needs secret_key")
    return _Clerk(_Caller("clerk", base_url, f"Bearer {secret_key}", transport))


class _WorkOS(LateResultProvider):
    name = "workos"

    def __init__(self, call: _Caller) -> None:
        self._call = call

    def revoke_sessions(self, user_id: str) -> None:
        user = _segment(user_id)
        active: list = []
        after: Optional[str] = None
        for _ in range(1000):
            query = {"limit": "100"}
            if after:
                query["after"] = after
            body = self._call("GET", f"/user_management/users/{user}/sessions", query)
            active += _active_ids(_sessions(body))
            metadata = body.get("list_metadata") if isinstance(body, dict) else None
            following = metadata.get("after") if isinstance(metadata, dict) else None
            if not isinstance(following, str) or following == "":
                break
            after = following
        for session_id in active:
            self._call("POST", "/user_management/sessions/revoke", body={"session_id": session_id})

    def ban(self, user_id: str) -> None:
        self.revoke_sessions(user_id)
        self._call("DELETE", f"/user_management/users/{_segment(user_id)}")


def workos_actions(api_key: str, *, base_url: str = "https://api.workos.com", transport: Optional[Transport] = None) -> LateResultProvider:
    """WorkOS User Management (api_key is sk_...).

    revoke_sessions pages through GET /user_management/users/{id}/sessions and
    revokes each active one with POST /user_management/sessions/revoke. WorkOS
    has no block or ban, so ban revokes the sessions and then deletes the user
    (DELETE /user_management/users/{id}); deletion is permanent.
    """
    if not api_key:
        raise ValueError("workos_actions needs api_key")
    return _WorkOS(_Caller("workos", base_url, f"Bearer {api_key}", transport))


def _not_on_plan(error: ProviderActionError) -> bool:
    """Auth0 answers 403 feature_not_enabled when the tenant's plan does not include an endpoint."""
    return error.status == 403 and error.code == "feature_not_enabled"


class _Auth0(LateResultProvider):
    name = "auth0"
    _PAGE = 100

    def __init__(self, call: _Caller) -> None:
        self._caller = call

    @staticmethod
    def _block(call: _Caller, user: str) -> None:
        call("PATCH", f"/users/{user}", body={"blocked": True})

    @staticmethod
    def _delete_sessions(call: _Caller, user: str) -> bool:
        """End every session; False when the plan has no sessions API."""
        try:
            call("DELETE", f"/users/{user}/sessions")
        except ProviderActionError as error:
            if _not_on_plan(error):
                return False
            raise
        return True

    def _delete_refresh_tokens(self, call: _Caller, user_id: str, user: str) -> None:
        try:
            call("DELETE", f"/users/{user}/refresh-tokens")
            return
        except ProviderActionError as error:
            if not _not_on_plan(error):
                raise
        # Collect every id before deleting any, so the pages do not shift underneath.
        ids: list = []
        for kind in ("refresh_token", "rotating_refresh_token"):
            for page in range(10):
                body = call(
                    "GET",
                    "/device-credentials",
                    {"user_id": user_id, "type": kind, "page": str(page), "per_page": str(self._PAGE)},
                )
                listed = body if isinstance(body, list) else []
                ids += [c["id"] for c in listed if isinstance(c, dict) and isinstance(c.get("id"), str) and c["id"]]
                if len(listed) < self._PAGE:
                    break
        for credential_id in ids:
            call("DELETE", f"/device-credentials/{quote(credential_id, safe='')}")

    def _revoke(self, user_id: str) -> str:
        user = _segment(user_id)
        call = self._caller.fresh()
        ended = self._delete_sessions(call, user)
        # Without the sessions API a login session survives; blocking is the only way to end it.
        if not ended:
            self._block(call, user)
        self._delete_refresh_tokens(call, user_id, user)
        return REVOKE_SESSIONS if ended else BAN

    def revoke_sessions(self, user_id: str) -> None:
        self._revoke(user_id)

    def ban(self, user_id: str) -> None:
        user = _segment(user_id)
        call = self._caller.fresh()
        self._block(call, user)
        # The block already ends a session the plan cannot delete.
        self._delete_sessions(call, user)
        self._delete_refresh_tokens(call, user_id, user)

    def act(self, action: str, user_id: str) -> str:
        if action == BAN:
            self.ban(user_id)
            return BAN
        return self._revoke(user_id)


def auth0_actions(
    token: str,
    *,
    domain: Optional[str] = None,
    base_url: Optional[str] = None,
    transport: Optional[Transport] = None,
) -> LateResultProvider:
    """Auth0 Management API.

    token needs update:users, delete:sessions, delete:refresh_tokens,
    read:device_credentials and delete:device_credentials. domain (such as
    example.eu.auth0.com) gives https://{domain}/api/v2; base_url replaces it.
    revoke_sessions deletes every session (DELETE /users/{id}/sessions) and
    refresh token (DELETE /users/{id}/refresh-tokens). ban first sets
    blocked: true (PATCH /users/{id}), then does the same.

    Auth0 offers the sessions and refresh-token endpoints on Enterprise plans
    only; on other plans they answer 403 feature_not_enabled. Then refresh
    tokens are deleted one by one through /device-credentials (types
    refresh_token and rotating_refresh_token), which every plan has. A login
    session cannot be ended, so revoke_sessions blocks the user before deleting
    the refresh tokens, and act reports "ban". Unblock the user in the
    dashboard to undo it. Any other refusal, such as 403 insufficient_scope,
    raises.

    A 429 from the Management API is waited out and retried: Retry-After,
    else X-RateLimit-Reset, else 0.25 s doubling, at most 4 retries a call and
    3 s of waiting a revoke or ban. Past that the 429 raises as
    ProviderActionError. A custom transport passes the response headers as a
    third tuple element; without them the backoff applies.
    """
    if not token:
        raise ValueError("auth0_actions needs token")
    base = base_url or (f"https://{domain}/api/v2" if domain else None)
    if not base:
        raise ValueError("auth0_actions needs domain or base_url")
    return _Auth0(_Caller("auth0", base, f"Bearer {token}", transport, retry_rate_limits=True))


class _LogOnly(LateResultProvider):
    name = "log_only"

    def __init__(self, log: Callable[[str], None]) -> None:
        self._log = log

    def revoke_sessions(self, user_id: str) -> None:
        _segment(user_id)
        self._log(f"NoResponse late result (log only): would revoke every session of user {user_id}")

    def ban(self, user_id: str) -> None:
        _segment(user_id)
        self._log(f"NoResponse late result (log only): would ban user {user_id} and end their sessions")


def log_only_actions(log: Optional[Callable[[str], None]] = None) -> LateResultProvider:
    """A provider for an app with its own login, or for trying the handler first.

    revoke_sessions and ban each log one line saying what they would do and
    call nothing: no request leaves your process. log receives that line; by
    default it goes to the "noresponse.late_results" logger at WARNING, so it
    shows without any logging setup. Replace it with your own
    LateResultProvider once you know what revoking and banning mean in your app.
    """
    if log is None:
        log = logging.getLogger("noresponse.late_results").warning
    return _LogOnly(log)
