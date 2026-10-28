"""The NoResponse client. Hand-written; not generated.

A thin layer over the generated operations that makes the common path short:

* the API key and server URL come from NORESPONSE_API_KEY and NORESPONSE_BASE_URL;
* create and record_outcome generate an idempotency_key when you leave it out,
  and every retry of that call sends the same one;
* methods return the model itself (an Assessment, not a response envelope), with
  the response headers on its meta attribute;
* connection failures and timeouts raise APIConnectionError and APITimeoutError;
* query and accounts.list_assessments return an AssessmentPage you can iterate
  across pages, and accounts.list_changed returns the AccountList page;
* key_usage.buffer() batches key usage and sends it from a background thread.

Each method has an async twin with the suffix _async.
"""

from __future__ import annotations

import functools
import logging
import os
import uuid
from typing import Any, Awaitable, Callable, Dict, Iterable, Mapping, Optional, TypeVar, Union, cast
from urllib.parse import urlsplit

import httpx
from typing_extensions import ParamSpec

from . import models
from .accounts import Accounts as _Accounts
from .requests import Requests as _Requests
from .assessments import Assessments as _Assessments
from .errors import APIConnectionError, APITimeoutError
from .httpclient import AsyncHttpClient, HttpClient
from .integrations import Integrations as _Integrations
from .keys import Keys as _Keys
from .settings import Settings as _Settings
from .keyusage import KeyUsage as _KeyUsage
from .key_usage import KeyUsageBuffer
from .webhookendpoints import WebhookEndpoints as _WebhookEndpoints
from .responses import (
    AssessmentSearchPage,
    as_assessment_search_page,
    AssessmentRevision,
    as_assessment_revision,
    AccountBinding,
    as_account_binding,
    AccountOutcome,
    as_account_outcome,
    AccountOutcomePage,
    as_account_outcome_page,
    AccountDecisionSnapshot,
    as_account_decision_snapshot,
    CredentialAssociation,
    as_credential_association,
    CredentialPage,
    as_credential_page,
    AccountExport,
    as_account_export,
    RequestDiagnosticPage,
    as_request_diagnostic_page,
    Account,
    AccountDeletion,
    AccountList,
    AssessmentDeletion,
    Assessment,
    AssessmentOutcome,
    AssessmentPage,
    Enforcement,
    Integration,
    IntegrationList,
    Key,
    KeyList,
    KeyRotation,
    KeyUsageBatch,
    ResponseMeta,
    Settings as SettingsModel,
    as_account,
    as_account_deletion,
    as_account_list,
    as_enforcement,
    as_assessment_deletion,
    as_assessment,
    as_integration,
    as_integration_list,
    as_key,
    as_key_list,
    as_settings,
    as_key_usage_batch,
    as_outcome,
    as_rotation,
)
from .sdk import NoResponse as _NoResponse
from .types import UNSET, OptionalNullable
from .utils import RetryConfig
from .utils.logger import Logger, NoOpLogger
from ._wait import DEFAULT_WAIT_SECONDS, wait, wait_async
from . import webhook_verification

__all__ = ["DEFAULT_BASE_URL", "DEFAULT_TIMEOUT_MS", "Accounts", "Assessments", "Integrations", "KeyUsage", "Keys", "NoResponse", "Requests", "Settings"]

DEFAULT_BASE_URL = "https://api.noresponse.org"
DEFAULT_TIMEOUT_MS = 10_000

P = ParamSpec("P")
R = TypeVar("R")

Identifiers = Union[
    models.shared.AssessmentRequestIdentifiers,
    models.shared.AssessmentRequestIdentifiersTypedDict,
    Mapping[str, str],
]
"""email, username, phone, name and ip, as a dict or the model. At least one of email, username or phone is required."""
PolicyContext = Union[models.shared.AssessmentRequestPolicyContext, models.shared.AssessmentRequestPolicyContextTypedDict]
ClientContext = Union[models.shared.AssessmentRequestClientContext, models.shared.AssessmentRequestClientContextTypedDict]
AuthContext = Union[models.shared.AuthContext, models.shared.AuthContextTypedDict]
IssuedCredential = Union[
    models.shared.AssessmentRequestIssuedCredential, models.shared.AssessmentRequestIssuedCredentialTypedDict
]


def _translated(error: httpx.HTTPError) -> Optional[APIConnectionError]:
    if isinstance(error, httpx.TimeoutException):
        return APITimeoutError(f"Request timed out: {error}", cause=error)
    if isinstance(error, httpx.TransportError):
        return APIConnectionError(f"Connection error: {error}", cause=error)
    return None


def _sync(function: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(function)
    def call(*args: P.args, **kwargs: P.kwargs) -> R:
        try:
            return function(*args, **kwargs)
        except httpx.HTTPError as error:
            translated = _translated(error)
            if translated is None:
                raise
            raise translated from error

    return call


def _async(function: Callable[P, Awaitable[R]]) -> Callable[P, Awaitable[R]]:
    @functools.wraps(function)
    async def call(*args: P.args, **kwargs: P.kwargs) -> R:
        try:
            return await function(*args, **kwargs)
        except httpx.HTTPError as error:
            translated = _translated(error)
            if translated is None:
                raise
            raise translated from error

    return call


def _key(idempotency_key: Optional[str]) -> str:
    return idempotency_key if idempotency_key else str(uuid.uuid4())


class Assessments(_Assessments):
    """Assessments of account creation, login and purchase."""

    # create ---------------------------------------------------------------

    def search(  # type: ignore[override]
        self,
        *,
        from_: str,
        to: str,
        account_id: Optional[str] = None,
        flow: Optional[models.shared.Flow] = None,
        status: Optional[models.shared.Status] = None,
        recommendation: Optional[models.shared.Recommendation] = None,
        decision: Optional[models.shared.AssessmentSearchRequestDecision] = None,
        limit: Optional[int] = 20,
        cursor: Optional[str] = None,
        response_mode: Optional[models.shared.ResponseMode] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AssessmentSearchPage:
        """Return the AssessmentSearchPage directly, with headers on meta."""
        response = _sync(super().search)(
            from_=from_,
            to=to,
            account_id=account_id,
            flow=flow,
            status=status,
            recommendation=recommendation,
            decision=decision,
            limit=limit,
            cursor=cursor,
            response_mode=response_mode,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_assessment_search_page)

    async def search_async(  # type: ignore[override]
        self,
        *,
        from_: str,
        to: str,
        account_id: Optional[str] = None,
        flow: Optional[models.shared.Flow] = None,
        status: Optional[models.shared.Status] = None,
        recommendation: Optional[models.shared.Recommendation] = None,
        decision: Optional[models.shared.AssessmentSearchRequestDecision] = None,
        limit: Optional[int] = 20,
        cursor: Optional[str] = None,
        response_mode: Optional[models.shared.ResponseMode] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AssessmentSearchPage:
        """Return the AssessmentSearchPage directly, with headers on meta."""
        response = await _async(super().search_async)(
            from_=from_,
            to=to,
            account_id=account_id,
            flow=flow,
            status=status,
            recommendation=recommendation,
            decision=decision,
            limit=limit,
            cursor=cursor,
            response_mode=response_mode,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_assessment_search_page)

    def retrieve_version(  # type: ignore[override]
        self,
        assessment_id: str,
        version: int,
        *,
        response_mode: Optional[models.shared.ResponseMode] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AssessmentRevision:
        """Return the AssessmentRevision directly, with headers on meta."""
        response = _sync(super().retrieve_version)(
            assessment_id,
            version,
            response_mode=response_mode,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_assessment_revision)

    async def retrieve_version_async(  # type: ignore[override]
        self,
        assessment_id: str,
        version: int,
        *,
        response_mode: Optional[models.shared.ResponseMode] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AssessmentRevision:
        """Return the AssessmentRevision directly, with headers on meta."""
        response = await _async(super().retrieve_version_async)(
            assessment_id,
            version,
            response_mode=response_mode,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_assessment_revision)

    def bind_account(  # type: ignore[override]
        self,
        assessment_id: str,
        *,
        account_id: str,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AccountBinding:
        """Return the AccountBinding directly, with headers on meta."""
        response = _sync(super().bind_account)(
            assessment_id,
            account_id=account_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_account_binding)

    async def bind_account_async(  # type: ignore[override]
        self,
        assessment_id: str,
        *,
        account_id: str,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AccountBinding:
        """Return the AccountBinding directly, with headers on meta."""
        response = await _async(super().bind_account_async)(
            assessment_id,
            account_id=account_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_account_binding)

    def create(  # type: ignore[override]
        self,
        *,
        account_id: str,
        flow: models.shared.Flow,
        identifiers: Identifiers,
        depth: Optional[models.shared.Depth] = None,
        idempotency_key: Optional[str] = None,
        policy_context: Optional[PolicyContext] = None,
        request_id: Optional[str] = None,
        deadline_ms: Optional[int] = None,
        response_mode: Optional[models.shared.ResponseMode] = None,
        client_context: Optional[ClientContext] = None,
        auth_context: Optional[AuthContext] = None,
        issued_credential: Optional[IssuedCredential] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Assessment:
        """Assess an account creation, login or purchase for abuse.

        flow is "account_creation", "login" or "purchase"; depth is "quick" or "full"
        (default full for account_creation and purchase, quick for login). The result is
        the assessment whether the API answered 200 (complete or partial) or
        202 (pending). Act on account.risk.decision; account is None while the
        account's first assessment is pending, so apply your own fallback, then
        wait() or take the webhook. idempotency_key is generated when omitted and is sent
        again on every retry of this call; pass your own, derived from your
        account creation attempt, so that a retry from your side replays the same
        assessment instead of starting new work. issued_credential is
        {"sha256": hash_issued_credential(key)} when your gate issued a key.
        """
        response = _sync(super().create)(
            idempotency_key=_key(idempotency_key),
            account_id=account_id,
            identifiers=cast(Any, identifiers),
            flow=flow,
            depth=depth,
            policy_context=policy_context,
            request_id=request_id,
            deadline_ms=deadline_ms,
            response_mode=response_mode,
            client_context=client_context,
            auth_context=auth_context,
            issued_credential=issued_credential,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _assessment(response)

    async def create_async(  # type: ignore[override]
        self,
        *,
        account_id: str,
        flow: models.shared.Flow,
        identifiers: Identifiers,
        depth: Optional[models.shared.Depth] = None,
        idempotency_key: Optional[str] = None,
        policy_context: Optional[PolicyContext] = None,
        request_id: Optional[str] = None,
        deadline_ms: Optional[int] = None,
        response_mode: Optional[models.shared.ResponseMode] = None,
        client_context: Optional[ClientContext] = None,
        auth_context: Optional[AuthContext] = None,
        issued_credential: Optional[IssuedCredential] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Assessment:
        """The asyncio form of create."""
        response = await _async(super().create_async)(
            idempotency_key=_key(idempotency_key),
            account_id=account_id,
            identifiers=cast(Any, identifiers),
            flow=flow,
            depth=depth,
            policy_context=policy_context,
            request_id=request_id,
            deadline_ms=deadline_ms,
            response_mode=response_mode,
            client_context=client_context,
            auth_context=auth_context,
            issued_credential=issued_credential,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _assessment(response)

    # get and wait ---------------------------------------------------------

    def get(  # type: ignore[override]
        self,
        assessment_id: str,
        *,
        response_mode: Optional[models.shared.ResponseMode] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Assessment:
        """Fetch the latest version of one assessment."""
        response = _sync(super().get)(
            assessment_id,
            response_mode=response_mode,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _assessment(response)

    async def get_async(  # type: ignore[override]
        self,
        assessment_id: str,
        *,
        response_mode: Optional[models.shared.ResponseMode] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Assessment:
        """The asyncio form of get."""
        response = await _async(super().get_async)(
            assessment_id,
            response_mode=response_mode,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _assessment(response)

    def wait(
        self,
        assessment_id: str,
        *,
        timeout: float = DEFAULT_WAIT_SECONDS,
        response_mode: Optional[models.shared.ResponseMode] = None,
    ) -> Assessment:
        """Poll get() until the assessment's status is "complete".

        Sleeps for the Retry-After the API sends between polls, at least one
        second. After timeout seconds it returns the latest answer if that is
        partial (its status stays "partial"), and raises APITimeoutError (a
        WaitTimeoutError, whose last attribute is the final pending
        assessment) if the assessment is still pending.
        """
        return wait(self, assessment_id, timeout=timeout, response_mode=response_mode)

    async def wait_async(
        self,
        assessment_id: str,
        *,
        timeout: float = DEFAULT_WAIT_SECONDS,
        response_mode: Optional[models.shared.ResponseMode] = None,
    ) -> Assessment:
        """The asyncio form of wait."""
        return await wait_async(self, assessment_id, timeout=timeout, response_mode=response_mode)

    # query ----------------------------------------------------------------

    def query(  # type: ignore[override]
        self,
        *,
        account_id: str,
        limit: Optional[int] = 20,
        cursor: Optional[str] = None,
        response_mode: Optional[models.shared.ResponseMode] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AssessmentPage:
        """One page of an account's unexpired assessments, newest first.

        Iterate the page to walk every item across every page.
        """
        response = _sync(super().query)(
            account_id=account_id,
            limit=limit,
            cursor=cursor,
            response_mode=response_mode,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        if not isinstance(response, models.operations.QueryAccountAssessmentsResponse):
            return response  # type: ignore[return-value]

        def fetch(next_cursor: str) -> AssessmentPage:
            return self.query(
                account_id=account_id,
                limit=limit,
                cursor=next_cursor,
                response_mode=response_mode,
                retries=retries,
                server_url=server_url,
                timeout_ms=timeout_ms,
                http_headers=http_headers,
            )

        return _page(response, fetch)

    async def query_async(  # type: ignore[override]
        self,
        *,
        account_id: str,
        limit: Optional[int] = 20,
        cursor: Optional[str] = None,
        response_mode: Optional[models.shared.ResponseMode] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AssessmentPage:
        """The asyncio form of query. Walk every page with ``async for``."""
        response = await _async(super().query_async)(
            account_id=account_id,
            limit=limit,
            cursor=cursor,
            response_mode=response_mode,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        if not isinstance(response, models.operations.QueryAccountAssessmentsResponse):
            return response  # type: ignore[return-value]

        def fetch(next_cursor: str) -> Awaitable[AssessmentPage]:
            return self.query_async(
                account_id=account_id,
                limit=limit,
                cursor=next_cursor,
                response_mode=response_mode,
                retries=retries,
                server_url=server_url,
                timeout_ms=timeout_ms,
                http_headers=http_headers,
            )

        return _page(response, fetch)

    # record_outcome -------------------------------------------------------

    def record_outcome(  # type: ignore[override]
        self,
        assessment_id: str,
        *,
        outcome: models.shared.Outcome,
        idempotency_key: Optional[str] = None,
        observed_at: Optional[str] = None,
        external_ref: Optional[str] = None,
        notes: Optional[str] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AssessmentOutcome:
        """Report what you later learned about an assessed account.

        idempotency_key is generated when omitted; derive your own from the case
        so that a retry from your side records the outcome once.
        """
        response = _sync(super().record_outcome)(
            assessment_id,
            idempotency_key=_key(idempotency_key),
            outcome=outcome,
            observed_at=observed_at,
            external_ref=external_ref,
            notes=notes,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _outcome(response)

    async def record_outcome_async(  # type: ignore[override]
        self,
        assessment_id: str,
        *,
        outcome: models.shared.Outcome,
        idempotency_key: Optional[str] = None,
        observed_at: Optional[str] = None,
        external_ref: Optional[str] = None,
        notes: Optional[str] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AssessmentOutcome:
        """The asyncio form of record_outcome."""
        response = await _async(super().record_outcome_async)(
            assessment_id,
            idempotency_key=_key(idempotency_key),
            outcome=outcome,
            observed_at=observed_at,
            external_ref=external_ref,
            notes=notes,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _outcome(response)

    # delete ---------------------------------------------------------------

    def delete(  # type: ignore[override]
        self,
        assessment_id: str,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AssessmentDeletion:
        """Delete one assessment and score its account again from what remains.

        Needs the history scope. account.current_assessment_id names the
        assessment the account's risk now comes from, and is None when none is
        left. An unknown or already deleted assessment raises NotFoundError.
        """
        response = _sync(super().delete)(
            assessment_id, retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return _assessment_deletion(response)

    async def delete_async(  # type: ignore[override]
        self,
        assessment_id: str,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AssessmentDeletion:
        """The asyncio form of delete."""
        response = await _async(super().delete_async)(
            assessment_id, retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return _assessment_deletion(response)


def _assessment_deletion(response: Any) -> AssessmentDeletion:
    if not isinstance(response, models.operations.DeleteAssessmentResponse):
        return response  # type: ignore[no-any-return]
    return as_assessment_deletion(response.result, ResponseMeta.from_headers(response.headers))


def _assessment(response: Any) -> Assessment:
    # A raw-response wrapper (with_raw_response) hands back its own object untouched.
    if not isinstance(response, (models.operations.CreateAssessmentResponse, models.operations.GetAssessmentResponse)):
        return response  # type: ignore[no-any-return]
    return as_assessment(response.result, ResponseMeta.from_headers(response.headers))


def _outcome(response: Any) -> AssessmentOutcome:
    if not isinstance(response, models.operations.RecordAssessmentOutcomeResponse):
        return response  # type: ignore[no-any-return]
    return as_outcome(response.result, ResponseMeta.from_headers(response.headers))


def _page(
    response: Union[models.operations.QueryAccountAssessmentsResponse, models.operations.ListAccountAssessmentsResponse],
    fetch: Callable[[str], Any],
) -> AssessmentPage:
    body = response.result
    return AssessmentPage(
        account_id=body.account_id,
        items=list(body.items),
        next_cursor=body.next_cursor or None,
        retention_days=body.retention_days,
        meta=ResponseMeta.from_headers(response.headers),
        fetch=fetch,
    )


class Accounts(_Accounts):
    """Your accounts.

    An account is the account_id you send with your assessments. It holds one
    current risk, the risk of its latest assessment with a decision, and its
    assessments are its history. Reads need history; reports and credential
    associations need assess; retiring an association needs delete.
    """

    def record_outcome(  # type: ignore[override]
        self,
        account_id: str,
        *,
        outcome: models.shared.Outcome,
        idempotency_key: Optional[str] = None,
        observed_at: Optional[str] = None,
        external_ref: Optional[str] = None,
        supersedes: Optional[str] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AccountOutcome:
        """Return the AccountOutcome directly, with headers on meta."""
        response = _sync(super().record_outcome)(
            account_id,
            outcome=outcome,
            idempotency_key=_key(idempotency_key),
            observed_at=observed_at,
            external_ref=external_ref,
            supersedes=supersedes,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_account_outcome)

    async def record_outcome_async(  # type: ignore[override]
        self,
        account_id: str,
        *,
        outcome: models.shared.Outcome,
        idempotency_key: Optional[str] = None,
        observed_at: Optional[str] = None,
        external_ref: Optional[str] = None,
        supersedes: Optional[str] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AccountOutcome:
        """Return the AccountOutcome directly, with headers on meta."""
        response = await _async(super().record_outcome_async)(
            account_id,
            outcome=outcome,
            idempotency_key=_key(idempotency_key),
            observed_at=observed_at,
            external_ref=external_ref,
            supersedes=supersedes,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_account_outcome)

    def list_outcomes(  # type: ignore[override]
        self,
        account_id: str,
        *,
        limit: Optional[int] = 20,
        cursor: Optional[str] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AccountOutcomePage:
        """Return the AccountOutcomePage directly, with headers on meta."""
        response = _sync(super().list_outcomes)(
            account_id,
            limit=limit,
            cursor=cursor,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_account_outcome_page)

    async def list_outcomes_async(  # type: ignore[override]
        self,
        account_id: str,
        *,
        limit: Optional[int] = 20,
        cursor: Optional[str] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AccountOutcomePage:
        """Return the AccountOutcomePage directly, with headers on meta."""
        response = await _async(super().list_outcomes_async)(
            account_id,
            limit=limit,
            cursor=cursor,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_account_outcome_page)

    def retrieve_decision(  # type: ignore[override]
        self,
        account_id: str,
        risk_version: int,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AccountDecisionSnapshot:
        """Return the AccountDecisionSnapshot directly, with headers on meta."""
        response = _sync(super().retrieve_decision)(
            account_id,
            risk_version,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_account_decision_snapshot)

    async def retrieve_decision_async(  # type: ignore[override]
        self,
        account_id: str,
        risk_version: int,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AccountDecisionSnapshot:
        """Return the AccountDecisionSnapshot directly, with headers on meta."""
        response = await _async(super().retrieve_decision_async)(
            account_id,
            risk_version,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_account_decision_snapshot)

    def associate_credential(  # type: ignore[override]
        self,
        account_id: str,
        *,
        sha256: str,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> CredentialAssociation:
        """Return the CredentialAssociation directly, with headers on meta."""
        response = _sync(super().associate_credential)(
            account_id,
            sha256=sha256,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_credential_association)

    async def associate_credential_async(  # type: ignore[override]
        self,
        account_id: str,
        *,
        sha256: str,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> CredentialAssociation:
        """Return the CredentialAssociation directly, with headers on meta."""
        response = await _async(super().associate_credential_async)(
            account_id,
            sha256=sha256,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_credential_association)

    def list_credentials(  # type: ignore[override]
        self,
        account_id: str,
        *,
        limit: Optional[int] = 20,
        cursor: Optional[str] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> CredentialPage:
        """Return the CredentialPage directly, with headers on meta."""
        response = _sync(super().list_credentials)(
            account_id,
            limit=limit,
            cursor=cursor,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_credential_page)

    async def list_credentials_async(  # type: ignore[override]
        self,
        account_id: str,
        *,
        limit: Optional[int] = 20,
        cursor: Optional[str] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> CredentialPage:
        """Return the CredentialPage directly, with headers on meta."""
        response = await _async(super().list_credentials_async)(
            account_id,
            limit=limit,
            cursor=cursor,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_credential_page)

    def retire_credential(  # type: ignore[override]
        self,
        account_id: str,
        credential_id: str,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> CredentialAssociation:
        """Return the CredentialAssociation directly, with headers on meta."""
        response = _sync(super().retire_credential)(
            account_id,
            credential_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_credential_association)

    async def retire_credential_async(  # type: ignore[override]
        self,
        account_id: str,
        credential_id: str,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> CredentialAssociation:
        """Return the CredentialAssociation directly, with headers on meta."""
        response = await _async(super().retire_credential_async)(
            account_id,
            credential_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_credential_association)

    def export(  # type: ignore[override]
        self,
        account_id: str,
        *,
        response_mode: Optional[models.shared.ResponseMode] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AccountExport:
        """Return the AccountExport directly, with headers on meta."""
        response = _sync(super().export)(
            account_id,
            response_mode=response_mode,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_account_export)

    async def export_async(  # type: ignore[override]
        self,
        account_id: str,
        *,
        response_mode: Optional[models.shared.ResponseMode] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AccountExport:
        """Return the AccountExport directly, with headers on meta."""
        response = await _async(super().export_async)(
            account_id,
            response_mode=response_mode,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_account_export)

    def get(  # type: ignore[override]
        self,
        account_id: str,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Account:
        """The account's current risk, with a decision for each flow.

        An account with no unexpired assessment that has a decision raises
        NotFoundError.
        """
        response = _sync(super().get)(
            account_id, retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return _account(response)

    async def get_async(  # type: ignore[override]
        self,
        account_id: str,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Account:
        """The asyncio form of get."""
        response = await _async(super().get_async)(
            account_id, retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return _account(response)

    def delete(  # type: ignore[override]
        self,
        account_id: str,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AccountDeletion:
        """Erase the account in your key's environment: every assessment of it.

        Idempotent: a repeat answers assessments_deleted 0. An account.deleted
        webhook follows when something was deleted.
        """
        response = _sync(super().delete)(
            account_id, retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return _account_deletion(response)

    async def delete_async(  # type: ignore[override]
        self,
        account_id: str,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AccountDeletion:
        """The asyncio form of delete."""
        response = await _async(super().delete_async)(
            account_id, retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return _account_deletion(response)

    def list_assessments(  # type: ignore[override]
        self,
        account_id: str,
        *,
        limit: Optional[int] = 20,
        cursor: Optional[str] = None,
        response_mode: Optional[models.shared.ResponseMode] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AssessmentPage:
        """One page of the account's unexpired assessments, newest first.

        The same pages as assessments.query, with the account_id in the URL.
        Iterate the page to walk every item across every page.
        """
        response = _sync(super().list_assessments)(
            account_id,
            limit=limit,
            cursor=cursor,
            response_mode=response_mode,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        if not isinstance(response, models.operations.ListAccountAssessmentsResponse):
            return response  # type: ignore[return-value]

        def fetch(next_cursor: str) -> AssessmentPage:
            return self.list_assessments(
                account_id,
                limit=limit,
                cursor=next_cursor,
                response_mode=response_mode,
                retries=retries,
                server_url=server_url,
                timeout_ms=timeout_ms,
                http_headers=http_headers,
            )

        return _page(response, fetch)

    async def list_assessments_async(  # type: ignore[override]
        self,
        account_id: str,
        *,
        limit: Optional[int] = 20,
        cursor: Optional[str] = None,
        response_mode: Optional[models.shared.ResponseMode] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AssessmentPage:
        """The asyncio form of list_assessments. Walk every page with ``async for``."""
        response = await _async(super().list_assessments_async)(
            account_id,
            limit=limit,
            cursor=cursor,
            response_mode=response_mode,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        if not isinstance(response, models.operations.ListAccountAssessmentsResponse):
            return response  # type: ignore[return-value]

        def fetch(next_cursor: str) -> Awaitable[AssessmentPage]:
            return self.list_assessments_async(
                account_id,
                limit=limit,
                cursor=next_cursor,
                response_mode=response_mode,
                retries=retries,
                server_url=server_url,
                timeout_ms=timeout_ms,
                http_headers=http_headers,
            )

        return _page(response, fetch)

    def list_changed(  # type: ignore[override]
        self,
        *,
        changed_since: Optional[str] = None,
        limit: Optional[int] = 50,
        unenforced: Optional[bool] = False,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AccountList:
        """The accounts whose risk changed, oldest change first.

        Pass next_cursor back as changed_since to read the changes after this
        page. With unenforced=True, only the accounts that still need action.
        """
        response = _sync(super().list_changed)(
            changed_since=changed_since, limit=limit, unenforced=unenforced,
            retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers,
        )
        return _account_list(response)

    async def list_changed_async(  # type: ignore[override]
        self,
        *,
        changed_since: Optional[str] = None,
        limit: Optional[int] = 50,
        unenforced: Optional[bool] = False,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> AccountList:
        """The asyncio form of list_changed."""
        response = await _async(super().list_changed_async)(
            changed_since=changed_since, limit=limit, unenforced=unenforced,
            retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers,
        )
        return _account_list(response)

    def record_enforcement(  # type: ignore[override]
        self,
        account_id: str,
        *,
        risk_version: int,
        flow: models.shared.Flow,
        action: models.shared.EnforcementAction,
        state_before: models.shared.EnforcementState,
        status: models.shared.EnforcementStatus,
        provider: models.shared.EnforcementProvider,
        error_code: Optional[str] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Enforcement:
        """Record what you did to the account in your auth provider at one risk_version.

        A repeat of the same record returns the stored record, so a retry is safe.
        """
        response = _sync(super().record_enforcement)(
            account_id, risk_version=risk_version, flow=flow, action=action, state_before=state_before,
            status=status, provider=provider, error_code=error_code,
            retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers,
        )
        return _enforcement(response)

    async def record_enforcement_async(  # type: ignore[override]
        self,
        account_id: str,
        *,
        risk_version: int,
        flow: models.shared.Flow,
        action: models.shared.EnforcementAction,
        state_before: models.shared.EnforcementState,
        status: models.shared.EnforcementStatus,
        provider: models.shared.EnforcementProvider,
        error_code: Optional[str] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Enforcement:
        """The asyncio form of record_enforcement."""
        response = await _async(super().record_enforcement_async)(
            account_id, risk_version=risk_version, flow=flow, action=action, state_before=state_before,
            status=status, provider=provider, error_code=error_code,
            retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers,
        )
        return _enforcement(response)


def _account_list(response: Any) -> AccountList:
    if not isinstance(response, models.operations.ListAccountsResponse):
        return response  # type: ignore[no-any-return]
    return as_account_list(response.result, ResponseMeta.from_headers(response.headers))


def _enforcement(response: Any) -> Enforcement:
    if not isinstance(response, models.operations.RecordEnforcementResponse):
        return response  # type: ignore[no-any-return]
    return as_enforcement(response.result, ResponseMeta.from_headers(response.headers))


def _account(response: Any) -> Account:
    if not isinstance(response, models.operations.GetAccountResponse):
        return response  # type: ignore[no-any-return]
    return as_account(response.result, ResponseMeta.from_headers(response.headers))


def _account_deletion(response: Any) -> AccountDeletion:
    if not isinstance(response, models.operations.DeleteAccountResponse):
        return response  # type: ignore[no-any-return]
    return as_account_deletion(response.result, ResponseMeta.from_headers(response.headers))


class Keys(_Keys):
    """Your own API keys."""

    def rotate(  # type: ignore[override]
        self,
        *,
        overlap_seconds: Optional[int] = None,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> KeyRotation:
        """Mint a replacement for the key that signs the request.

        The old key keeps working for overlap_seconds (default 24 hours, from 60
        seconds to 7 days). Rotation is not idempotent: a retry after a lost
        answer mints another key.
        """
        response = _sync(super().rotate)(
            overlap_seconds=overlap_seconds,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _rotation(response)

    async def rotate_async(  # type: ignore[override]
        self,
        *,
        overlap_seconds: Optional[int] = None,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> KeyRotation:
        """The asyncio form of rotate."""
        response = await _async(super().rotate_async)(
            overlap_seconds=overlap_seconds,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _rotation(response)

    # With the management scope: the keys of the signing key's environment.

    def create(  # type: ignore[override]
        self,
        workspace_id: str,
        *,
        environment: Union[models.shared.KeyEnvironment, str],
        scopes: Iterable[Union[models.shared.KeyRequestScope, str]],
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Key:
        """Create a key in the signing key's environment, with scopes the signing key holds.

        Needs the management scope. The secret is in key, shown once. Not
        idempotent, so never retried: a retry after a lost answer creates a
        second key.
        """
        response = _sync(super().create)(
            workspace_id, environment=cast(Any, environment), scopes=cast(Any, list(scopes)),
            server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers,
        )
        return _answer(response, as_key)

    async def create_async(  # type: ignore[override]
        self,
        workspace_id: str,
        *,
        environment: Union[models.shared.KeyEnvironment, str],
        scopes: Iterable[Union[models.shared.KeyRequestScope, str]],
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Key:
        """The asyncio form of create."""
        response = await _async(super().create_async)(
            workspace_id, environment=cast(Any, environment), scopes=cast(Any, list(scopes)),
            server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers,
        )
        return _answer(response, as_key)

    def list(  # type: ignore[override]
        self,
        workspace_id: str,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> KeyList:
        """The keys of the signing key's environment, newest first, without secrets. Needs the management scope."""
        response = _sync(super().list)(
            workspace_id, retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return _answer(response, as_key_list)

    async def list_async(  # type: ignore[override]
        self,
        workspace_id: str,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> KeyList:
        """The asyncio form of list."""
        response = await _async(super().list_async)(
            workspace_id, retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return _answer(response, as_key_list)

    def revoke(  # type: ignore[override]
        self,
        workspace_id: str,
        key_id: str,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Key:
        """Revoke a key of the signing key's environment at once. A key cannot revoke itself. Needs the management scope."""
        response = _sync(super().revoke)(
            workspace_id, key_id, retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return _answer(response, as_key)

    async def revoke_async(  # type: ignore[override]
        self,
        workspace_id: str,
        key_id: str,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Key:
        """The asyncio form of revoke."""
        response = await _async(super().revoke_async)(
            workspace_id, key_id, retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return _answer(response, as_key)


class Settings(_Settings):
    """The settings of the signing key's environment. Every method needs the management scope."""

    def get(  # type: ignore[override]
        self,
        workspace_id: str,
        environment: Union[models.shared.KeyEnvironment, str],
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> SettingsModel:
        """Read the environment's settings; the other environment answers 404."""
        response = _sync(super().get)(
            workspace_id, cast(Any, environment), retries=retries, server_url=server_url, timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_settings)

    async def get_async(  # type: ignore[override]
        self,
        workspace_id: str,
        environment: Union[models.shared.KeyEnvironment, str],
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> SettingsModel:
        """The asyncio form of get."""
        response = await _async(super().get_async)(
            workspace_id, cast(Any, environment), retries=retries, server_url=server_url, timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_settings)

    def update(  # type: ignore[override]
        self,
        workspace_id: str,
        environment: Union[models.shared.KeyEnvironment, str],
        *,
        retention_days: Optional[int] = None,
        refused_sources: Optional[Iterable[Union[models.shared.SourceID, str]]] = None,
        flows: Optional[Union[models.shared.SettingsRequestFlows, models.shared.SettingsRequestFlowsTypedDict]] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> SettingsModel:
        """Change only what you name, in one transaction."""
        response = _sync(super().update)(
            workspace_id, cast(Any, environment), retention_days=retention_days,
            refused_sources=cast(Any, None if refused_sources is None else list(refused_sources)), flows=flows,
            retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers,
        )
        return _answer(response, as_settings)

    async def update_async(  # type: ignore[override]
        self,
        workspace_id: str,
        environment: Union[models.shared.KeyEnvironment, str],
        *,
        retention_days: Optional[int] = None,
        refused_sources: Optional[Iterable[Union[models.shared.SourceID, str]]] = None,
        flows: Optional[Union[models.shared.SettingsRequestFlows, models.shared.SettingsRequestFlowsTypedDict]] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> SettingsModel:
        """The asyncio form of update."""
        response = await _async(super().update_async)(
            workspace_id, cast(Any, environment), retention_days=retention_days,
            refused_sources=cast(Any, None if refused_sources is None else list(refused_sources)), flows=flows,
            retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers,
        )
        return _answer(response, as_settings)


KeyUsageEvents = Union[
    Iterable[models.shared.KeyUsageEvent],
    Iterable[models.shared.KeyUsageEventTypedDict],
]
"""1 to 500 events, as dicts or models: key_sha256, ip, occurred_at and optionally user_agent, model, input_tokens,
output_tokens and sample_rate."""


class KeyUsage(_KeyUsage):
    """Usage of the API keys your platform issued to your accounts. Needs the assess scope.

    Most callers use ``buffer()``, which batches facts and sends them from a
    background thread; ``record`` sends one batch now.
    """

    def record(  # type: ignore[override]
        self,
        *,
        events: KeyUsageEvents,
        idempotency_key: Optional[str] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> KeyUsageBatch:
        """Send one batch of 1 to 500 events (at most 256 KiB).

        idempotency_key is generated when omitted and sent on every retry of this
        call, so a retried batch is counted once.
        """
        response = _sync(super().record)(
            idempotency_key=_key(idempotency_key),
            events=events,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _key_usage_batch(response)

    async def record_async(  # type: ignore[override]
        self,
        *,
        events: KeyUsageEvents,
        idempotency_key: Optional[str] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> KeyUsageBatch:
        """The asyncio form of record."""
        response = await _async(super().record_async)(
            idempotency_key=_key(idempotency_key),
            events=events,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _key_usage_batch(response)

    def buffer(self, **options: Any) -> KeyUsageBuffer:
        """A buffer that sends recorded facts from a background thread. Keep one per process.

        Options: batch_size (default 100, at most 500), flush_interval (seconds,
        default 5), max_queue (default 10 000; the oldest fact is dropped when
        full), sample_rate, on_error and flush_at_exit (default True).
        """
        return KeyUsageBuffer(self, **options)


def _key_usage_batch(response: Any) -> KeyUsageBatch:
    if not isinstance(response, models.operations.RecordKeyUsageResponse):
        return response  # type: ignore[no-any-return]
    return as_key_usage_batch(response.result, ResponseMeta.from_headers(response.headers))


def _rotation(response: Any) -> KeyRotation:
    if not isinstance(response, models.operations.RotateAPIKeyResponse):
        return response  # type: ignore[no-any-return]
    return as_rotation(response.result, ResponseMeta.from_headers(response.headers))


class WebhookEndpoints(_WebhookEndpoints):
    """Your webhook endpoints.

    create and rotate_signing_key return a signing secret shown only in that
    answer. None of create, rotate_signing_key, send_test_event and
    replay_delivery is retried: a retry would register, issue or send again.
    """

    def create(  # type: ignore[override]
        self,
        *,
        url: str,
        response_mode: Optional[models.shared.ResponseMode] = None,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.shared.WebhookEndpointCreated:
        """Register an endpoint. It starts unverified: send endpoint.verification with send_test_event."""
        response = _sync(super().create)(
            url=url, response_mode=response_mode, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return response.result

    async def create_async(  # type: ignore[override]
        self,
        *,
        url: str,
        response_mode: Optional[models.shared.ResponseMode] = None,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.shared.WebhookEndpointCreated:
        """The asyncio form of create."""
        response = await _async(super().create_async)(
            url=url, response_mode=response_mode, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return response.result

    def list(  # type: ignore[override]
        self,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.shared.WebhookEndpointList:
        """Every endpoint you hold, in every state, with its signing key ids."""
        return _sync(super().list)(retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers).result

    async def list_async(  # type: ignore[override]
        self,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.shared.WebhookEndpointList:
        """The asyncio form of list."""
        response = await _async(super().list_async)(retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers)
        return response.result

    def delete(  # type: ignore[override]
        self,
        endpoint_id: str,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> None:
        """Delete an endpoint and its keys; deliveries still queued for it are dropped."""
        _sync(super().delete)(endpoint_id, retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers)

    async def delete_async(  # type: ignore[override]
        self,
        endpoint_id: str,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> None:
        """The asyncio form of delete."""
        await _async(super().delete_async)(endpoint_id, retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers)

    def rotate_signing_key(  # type: ignore[override]  # pylint: disable=arguments-differ
        self,
        endpoint_id: str,
        *,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.shared.WebhookKeyRotation:
        """Issue a new signing key. The previous one keeps verifying for 7 days."""
        response = _sync(super().rotate_signing_key)(
            endpoint_id, body={}, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return response.result

    async def rotate_signing_key_async(  # type: ignore[override]  # pylint: disable=arguments-differ
        self,
        endpoint_id: str,
        *,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.shared.WebhookKeyRotation:
        """The asyncio form of rotate_signing_key."""
        response = await _async(super().rotate_signing_key_async)(
            endpoint_id, body={}, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return response.result

    def send_test_event(  # type: ignore[override]
        self,
        endpoint_id: str,
        *,
        event: models.shared.WebhookTestRequestEvent,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.shared.WebhookTest:
        """Send endpoint.verification now, or queue an assessment.updated test event with test true."""
        response = _sync(super().send_test_event)(
            endpoint_id, event=event, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return response.result

    async def send_test_event_async(  # type: ignore[override]
        self,
        endpoint_id: str,
        *,
        event: models.shared.WebhookTestRequestEvent,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.shared.WebhookTest:
        """The asyncio form of send_test_event."""
        response = await _async(super().send_test_event_async)(
            endpoint_id, event=event, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return response.result

    def list_deliveries(  # type: ignore[override]
        self,
        endpoint_id: str,
        *,
        limit: Optional[int] = 20,
        cursor: Optional[str] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.shared.WebhookDeliveryList:
        """One page of the endpoint's delivery attempts, newest first.

        Pass the page's next_cursor back as cursor for the next page; it is
        None on the last one. Attempts are kept for 30 days, or your retention
        when that is shorter.
        """
        response = _sync(super().list_deliveries)(
            endpoint_id, limit=limit, cursor=cursor, retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        if not isinstance(response, models.operations.ListWebhookDeliveriesResponse):
            return response  # type: ignore[return-value]
        return response.result

    async def list_deliveries_async(  # type: ignore[override]
        self,
        endpoint_id: str,
        *,
        limit: Optional[int] = 20,
        cursor: Optional[str] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.shared.WebhookDeliveryList:
        """The asyncio form of list_deliveries."""
        response = await _async(super().list_deliveries_async)(
            endpoint_id, limit=limit, cursor=cursor, retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        if not isinstance(response, models.operations.ListWebhookDeliveriesResponse):
            return response  # type: ignore[return-value]
        return response.result

    def replay_delivery(  # type: ignore[override]  # pylint: disable=arguments-differ
        self,
        endpoint_id: str,
        event_id: str,
        *,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.shared.WebhookReplay:
        """Send one logged event again: the same id and body, a fresh timestamp and signature."""
        response = _sync(super().replay_delivery)(
            endpoint_id, event_id, body={}, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return response.result

    async def replay_delivery_async(  # type: ignore[override]  # pylint: disable=arguments-differ
        self,
        endpoint_id: str,
        event_id: str,
        *,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.shared.WebhookReplay:
        """The asyncio form of replay_delivery."""
        response = await _async(super().replay_delivery_async)(
            endpoint_id, event_id, body={}, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return response.result


HookPoints = Iterable[Union[models.shared.IntegrationHookPoint, str]]
"""pre_registration, post_login or both (the default)."""


class Integrations(_Integrations):
    """Hosted provider integrations: a WorkOS or Auth0 Action that NoResponse answers.

    Every method needs a key with the integrations scope. create and rotate are
    not idempotent and are never retried: a retry after a lost answer registers
    or rotates again.
    """

    def create(  # type: ignore[override]
        self,
        *,
        platform: Union[models.shared.IntegrationPlatform, str],
        hook_points: Optional[HookPoints] = None,
        signing_secret: Optional[str] = None,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Integration:
        """Register a WorkOS or Auth0 integration and return its endpoint url.

        For WorkOS, pass the Actions signing_secret from the WorkOS dashboard. For
        Auth0, the answer's secret is the Action's shared secret, shown once.
        """
        response = _sync(super().create)(
            platform=cast(Any, platform),
            hook_points=cast(Any, hook_points),
            signing_secret=signing_secret,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _integration(response)

    async def create_async(  # type: ignore[override]
        self,
        *,
        platform: Union[models.shared.IntegrationPlatform, str],
        hook_points: Optional[HookPoints] = None,
        signing_secret: Optional[str] = None,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Integration:
        """The asyncio form of create."""
        response = await _async(super().create_async)(
            platform=cast(Any, platform),
            hook_points=cast(Any, hook_points),
            signing_secret=signing_secret,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _integration(response)

    def list(  # type: ignore[override]
        self,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> IntegrationList:
        """Every integration, oldest first. Listings carry no secrets."""
        response = _sync(super().list)(
            retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return _integration_list(response)

    async def list_async(  # type: ignore[override]
        self,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> IntegrationList:
        """The asyncio form of list."""
        response = await _async(super().list_async)(
            retries=retries, server_url=server_url, timeout_ms=timeout_ms, http_headers=http_headers
        )
        return _integration_list(response)

    def delete(  # type: ignore[override]
        self,
        integration_id: str,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> ResponseMeta:
        """Delete an integration; its endpoint answers 404 from then on. Returns the response metadata."""
        response = _sync(super().delete)(
            integration_id=integration_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _deleted(response)

    async def delete_async(  # type: ignore[override]
        self,
        integration_id: str,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> ResponseMeta:
        """The asyncio form of delete."""
        response = await _async(super().delete_async)(
            integration_id=integration_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _deleted(response)

    def rotate(  # type: ignore[override]
        self,
        integration_id: str,
        *,
        signing_secret: Optional[str] = None,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Integration:
        """Replace an integration's secret.

        For Auth0 pass nothing and read the new secret, shown once. For WorkOS pass
        the regenerated signing_secret. The replaced secret is accepted until
        previous_secret_expires_at.
        """
        response = _sync(super().rotate)(
            integration_id=integration_id,
            signing_secret=signing_secret,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _integration(response)

    async def rotate_async(  # type: ignore[override]
        self,
        integration_id: str,
        *,
        signing_secret: Optional[str] = None,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Integration:
        """The asyncio form of rotate."""
        response = await _async(super().rotate_async)(
            integration_id=integration_id,
            signing_secret=signing_secret,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _integration(response)


def _answer(response: Any, convert: Callable[[Any, ResponseMeta], R]) -> R:
    """The model a generated response carries, with its headers as meta."""
    return convert(response.result, ResponseMeta.from_headers(response.headers))


def _integration(response: Any) -> Integration:
    if not isinstance(
        response, (models.operations.CreateIntegrationResponse, models.operations.RotateIntegrationSecretResponse)
    ):
        return response  # type: ignore[no-any-return]
    return as_integration(response.result, ResponseMeta.from_headers(response.headers))


def _integration_list(response: Any) -> IntegrationList:
    if not isinstance(response, models.operations.ListIntegrationsResponse):
        return response  # type: ignore[no-any-return]
    return as_integration_list(response.result, ResponseMeta.from_headers(response.headers))


def _deleted(response: Any) -> ResponseMeta:
    if not isinstance(response, models.operations.DeleteIntegrationResponse):
        return response  # type: ignore[no-any-return]
    return ResponseMeta.from_headers(response.headers)


class Requests(_Requests):
    """Bounded request diagnostics, without request bodies or secrets."""

    def list(  # type: ignore[override]
        self,
        *,
        from_: str,
        to: str,
        request_id: Optional[str] = None,
        route: Optional[str] = None,
        status: Optional[int] = None,
        limit: Optional[int] = 50,
        cursor: Optional[str] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> RequestDiagnosticPage:
        """Return the RequestDiagnosticPage directly, with headers on meta."""
        response = _sync(super().list)(
            from_=from_,
            to=to,
            request_id=request_id,
            route=route,
            status=status,
            limit=limit,
            cursor=cursor,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_request_diagnostic_page)

    async def list_async(  # type: ignore[override]
        self,
        *,
        from_: str,
        to: str,
        request_id: Optional[str] = None,
        route: Optional[str] = None,
        status: Optional[int] = None,
        limit: Optional[int] = 50,
        cursor: Optional[str] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> RequestDiagnosticPage:
        """Return the RequestDiagnosticPage directly, with headers on meta."""
        response = await _async(super().list_async)(
            from_=from_,
            to=to,
            request_id=request_id,
            route=route,
            status=status,
            limit=limit,
            cursor=cursor,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return _answer(response, as_request_diagnostic_page)


class _SafeLogger:
    """Passes the debug lines the generated client writes to a logger, without the API key or any body.

    The generated lines carry every request and response header (the Authorization
    header holds the key) and both bodies (which hold email addresses and names).
    This keeps the method, URL, status and request id.
    """

    def __init__(self, sink: Any) -> None:
        self._sink = sink

    def debug(self, msg: str, *args: Any, **kwargs: Any) -> None:
        if msg.startswith("Request:") and len(args) == 4:
            self._sink.debug("Request: %s %s", args[0], args[1])
        elif msg.startswith("Response:") and len(args) == 4:
            headers = args[2]
            request_id = headers.get("x-request-id") if hasattr(headers, "get") else None
            self._sink.debug("Response: %s %s (request %s)", args[0], args[1], request_id)
        elif not args:
            self._sink.debug(msg, **kwargs)


def _logger(debug_logger: Optional[Any]) -> Logger:
    if debug_logger is not None:
        return _SafeLogger(debug_logger)
    flag = os.environ.get("NORESPONSE_DEBUG", "")
    if os.environ.get("NORESPONSE_LOG") == "debug" or flag not in ("", "0", "false"):
        log = logging.getLogger("noresponse")
        if not log.handlers:
            log.addHandler(logging.StreamHandler())
        log.setLevel(logging.DEBUG)
        return _SafeLogger(log)
    return NoOpLogger()


def _checked_url(url: str) -> str:
    parts = urlsplit(url)
    if parts.query or parts.fragment or url.endswith(("?", "#")):
        raise ValueError("server_url has a query or fragment; pass the origin only")
    if parts.scheme != "https" and not (parts.scheme == "http" and parts.hostname in ("localhost", "127.0.0.1", "::1")):
        raise ValueError("server_url must use HTTPS (http is allowed only for localhost)")
    return url.rstrip("/")


class NoResponse(_NoResponse):
    """The NoResponse client.

    >>> nr = NoResponse()  # reads NORESPONSE_API_KEY
    >>> assessment = nr.assessments.create(
    ...     account_id="usr_8f2k1",
    ...     identifiers={"email": "jordan.lee@example.com"},
    ... )

    Use it as a context manager (``with`` or ``async with``) to close the HTTP
    clients it opened. Keep the API key on your server.
    """

    webhooks = webhook_verification
    """Webhook verification: ``nr.webhooks.construct_event(payload, headers, secrets)``."""

    assessments: Assessments  # type: ignore[assignment]
    accounts: Accounts  # type: ignore[assignment]
    requests: Requests  # type: ignore[assignment]
    keys: Keys  # type: ignore[assignment]
    settings: Settings  # type: ignore[assignment]
    key_usage: KeyUsage  # type: ignore[assignment]
    webhook_endpoints: WebhookEndpoints  # type: ignore[assignment]
    integrations: Integrations  # type: ignore[assignment]
    _sub_sdk_map: Dict[str, Any] = {
        "assessments": ("noresponse.client", "Assessments"),
        "accounts": ("noresponse.client", "Accounts"),
        "requests": ("noresponse.client", "Requests"),
        "keys": ("noresponse.client", "Keys"),
        "settings": ("noresponse.client", "Settings"),
        "key_usage": ("noresponse.client", "KeyUsage"),
        "webhook_endpoints": ("noresponse.client", "WebhookEndpoints"),
        "integrations": ("noresponse.client", "Integrations"),
    }

    def __init__(
        self,
        api_key: Optional[Union[str, Callable[[], Optional[str]]]] = None,
        *,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        server_idx: Optional[int] = None,
        url_params: Optional[Dict[str, str]] = None,
        debug_logger: Optional[Any] = None,
    ) -> None:
        """
        :param api_key: Your nrk_ key, or a function that returns it. Defaults to NORESPONSE_API_KEY.
        :param server_url: The API origin. Defaults to NORESPONSE_BASE_URL, then https://api.noresponse.org.
        :param timeout_ms: Timeout of each request in milliseconds. Defaults to 10 000; also settable per call.
        :param retry_config: Retry policy for every call. Defaults to backoff from 500 ms to 8 s for at most 30 s
            on connection errors, 408, 429 and every 5xx. Pass None to turn retries off.
        :param client: Your own httpx.Client, for a proxy or for tests.
        :param async_client: Your own httpx.AsyncClient.
        :param debug_logger: A logger (anything with a debug method) that receives one line per request and response:
            method, URL, status and request id. NORESPONSE_LOG=debug turns on the standard logger "noresponse".
            Headers and bodies are never logged.
        """
        key = api_key if api_key else os.environ.get("NORESPONSE_API_KEY")
        if not key:
            raise ValueError("No API key: pass api_key or set NORESPONSE_API_KEY")
        if isinstance(key, str) and ("\r" in key or "\n" in key):
            raise ValueError("api_key contains a line break")
        if timeout_ms is not None and (isinstance(timeout_ms, bool) or not isinstance(timeout_ms, int) or timeout_ms <= 0):
            raise ValueError("timeout_ms must be a positive integer")
        url = server_url or os.environ.get("NORESPONSE_BASE_URL")
        if url is None and server_idx is None:
            url = DEFAULT_BASE_URL
        super().__init__(
            api_key=key,
            server_idx=server_idx,
            url_params=url_params,
            server_url=_checked_url(url) if url else None,
            client=client,
            async_client=async_client,
            retry_config=retry_config,
            timeout_ms=timeout_ms if timeout_ms is not None else DEFAULT_TIMEOUT_MS,
            debug_logger=_logger(debug_logger),
        )
