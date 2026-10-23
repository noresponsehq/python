"""Late-result handlers. Hand-written; not generated.

An assessment can be revised after the signup was allowed: a slow source
settles and the recommendation rises. NoResponse sends the new version as a
signed assessment.updated webhook. handle_late_result verifies that delivery
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
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any, Callable, Mapping, Optional, Tuple, Union
from urllib.parse import quote, urlencode

from .webhooks import DEFAULT_TOLERANCE_SECONDS, Headers, WebhookEvent, construct_event

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
    "workos_actions",
]

# What to do to the user. "ban" also ends every session.
LateResultAction = str
NONE = "none"
REVOKE_SESSIONS = "revoke_sessions"
BAN = "ban"
_ACTIONS = (NONE, REVOKE_SESSIONS, BAN)

# The action for each recommendation. A recommendation you leave out does nothing.
LatePolicy = Mapping[str, str]

# Revoke sessions on review; do nothing on allow or step_up. Banning is opt-in.
DEFAULT_LATE_RESULT_POLICY: LatePolicy = {"allow": NONE, "step_up": NONE, "review": REVOKE_SESSIONS}

# transport(method, url, headers, body) -> (status, response body bytes).
# The default uses urllib. Pass your own for a proxy or for tests.
Transport = Callable[[str, str, Mapping[str, str], Optional[bytes]], Tuple[int, bytes]]


class ProviderActionError(Exception):
    """The provider's admin API refused a call. Answer the webhook with a 5xx so NoResponse retries it.

    A 404 is never raised: the user or session is already gone, so the action is done.
    """

    def __init__(self, provider: str, status: int, message: str) -> None:
        super().__init__(message)
        self.provider = provider
        self.status = status


class LateResultProvider:
    """The two admin actions, for one auth provider. Build one with clerk_actions, workos_actions or auth0_actions."""

    name: str

    def revoke_sessions(self, user_id: str) -> None:
        """End every active session of the user."""
        raise NotImplementedError

    def ban(self, user_id: str) -> None:
        """Stop the user signing in again and end their sessions."""
        raise NotImplementedError


@dataclass(frozen=True)
class LateResult:
    # The verified event. Answer an endpoint.verification with verification_response(event).
    event: WebhookEvent
    # The action taken. "none" when the policy, the event or the user id called for nothing.
    action: str
    # The provider user id acted on, when an action was taken.
    user_id: Optional[str] = None


def _text(value: Any) -> Optional[str]:
    value = getattr(value, "value", value)
    return value if isinstance(value, str) else None


def late_result_action(event: WebhookEvent, policy: Optional[LatePolicy] = None) -> str:
    """The action your policy names for a verified event.

    Only a served assessment with a recommendation can act; a test event from
    webhook_endpoints.send_test_event never does.
    """
    chosen = DEFAULT_LATE_RESULT_POLICY if policy is None else policy
    data = event.data
    if event.type != "assessment.updated" or event.expired or event.test:
        return NONE
    recommendation = _text(getattr(data, "recommendation", None))
    if recommendation is None:
        recommendation = _text(getattr(getattr(data, "risk", None), "recommendation", None))
    if recommendation not in ("allow", "step_up", "review"):
        return NONE
    action = chosen.get(recommendation)
    if action is None:
        return NONE
    if action not in _ACTIONS:
        raise TypeError(f"unknown late result action {action!r}")
    return action


def handle_late_result(
    payload: Union[bytes, str],
    headers: Headers,
    secrets: Mapping[str, Union[str, bytes]],
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
    assessment's account_id to the provider user id (default: the account_id
    itself); return None to take no action, or raise to fail the delivery so it
    is retried. A test event acts on nothing. Revoke and ban are safe to repeat,
    but deduplicate on result.event.id and ignore versions older than one you
    have acted on.
    """
    event = construct_event(payload, headers, secrets, tolerance_seconds=tolerance_seconds, now=now)
    action = late_result_action(event, policy)
    if action == NONE:
        return LateResult(event, NONE)
    account_id = event.data.account_id  # type: ignore[union-attr]
    user_id = resolve_user_id(account_id, event) if resolve_user_id else account_id
    if not user_id:
        return LateResult(event, NONE)
    if action == BAN:
        provider.ban(user_id)
    else:
        provider.revoke_sessions(user_id)
    return LateResult(event, action, user_id)


def _urllib_transport(method: str, url: str, headers: Mapping[str, str], body: Optional[bytes]) -> Tuple[int, bytes]:
    request = urllib.request.Request(url, data=body, method=method, headers=dict(headers))
    try:
        with urllib.request.urlopen(request, timeout=30) as response:  # noqa: S310 - caller-supplied https base
            return response.status, response.read()
    except urllib.error.HTTPError as error:
        try:
            return error.code, error.read()
        finally:
            error.close()


class _Caller:
    def __init__(self, name: str, base_url: str, authorization: str, transport: Optional[Transport]) -> None:
        self.name = name
        self.base = base_url.rstrip("/")
        self.authorization = authorization
        self.transport = transport or _urllib_transport

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
        status, text = self.transport(method, url, headers, data)
        # Every call names a user or a session. A 404 means it is already gone,
        # so revoke and ban count it as done and a repeated delivery does not fail.
        if status == 404:
            return None
        if not 200 <= status < 300:
            raise ProviderActionError(self.name, status, f"{self.name} {method} {path} answered {status}")
        if not text:
            return None
        try:
            return json.loads(text)
        except ValueError:
            return None


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


class _Auth0(LateResultProvider):
    name = "auth0"

    def __init__(self, call: _Caller) -> None:
        self._call = call

    def revoke_sessions(self, user_id: str) -> None:
        user = _segment(user_id)
        self._call("DELETE", f"/users/{user}/sessions")
        self._call("DELETE", f"/users/{user}/refresh-tokens")

    def ban(self, user_id: str) -> None:
        self._call("PATCH", f"/users/{_segment(user_id)}", body={"blocked": True})
        self.revoke_sessions(user_id)


def auth0_actions(
    token: str,
    *,
    domain: Optional[str] = None,
    base_url: Optional[str] = None,
    transport: Optional[Transport] = None,
) -> LateResultProvider:
    """Auth0 Management API.

    token needs update:users, delete:sessions and delete:refresh_tokens. domain
    (such as example.eu.auth0.com) gives https://{domain}/api/v2; base_url
    replaces it. revoke_sessions deletes every session (DELETE /users/{id}/sessions)
    and refresh token (DELETE /users/{id}/refresh-tokens). ban first sets
    blocked: true (PATCH /users/{id}), then does the same.
    """
    if not token:
        raise ValueError("auth0_actions needs token")
    base = base_url or (f"https://{domain}/api/v2" if domain else None)
    if not base:
        raise ValueError("auth0_actions needs domain or base_url")
    return _Auth0(_Caller("auth0", base, f"Bearer {token}", transport))
