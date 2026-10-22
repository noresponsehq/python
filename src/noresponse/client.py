"""The NoResponse client. Hand-written; not generated.

A thin layer over the generated operations that makes the common path short:

* the API key and server URL come from NORESPONSE_API_KEY and NORESPONSE_BASE_URL;
* create and record_outcome generate an idempotency_key when you leave it out,
  and every retry of that call sends the same one;
* methods return the model itself (an Assessment, not a response envelope), with
  the response headers on its meta attribute;
* connection failures and timeouts raise APIConnectionError and APITimeoutError;
* query returns an AssessmentPage you can iterate across pages.

Each method has an async twin with the suffix _async.
"""

from __future__ import annotations

import functools
import logging
import os
import uuid
from typing import Any, Awaitable, Callable, Dict, Mapping, Optional, TypeVar, Union, cast
from urllib.parse import urlsplit

import httpx
from typing_extensions import ParamSpec

from . import models
from .assessments import Assessments as _Assessments
from .errors import APIConnectionError, APITimeoutError
from .httpclient import AsyncHttpClient, HttpClient
from .keys import Keys as _Keys
from .responses import (
    Assessment,
    AssessmentOutcome,
    AssessmentPage,
    KeyRotation,
    ResponseMeta,
    as_assessment,
    as_outcome,
    as_rotation,
)
from .sdk import NoResponse as _NoResponse
from .types import UNSET, OptionalNullable
from .utils import RetryConfig
from .utils.logger import Logger, NoOpLogger
from ._wait import DEFAULT_WAIT_SECONDS, wait, wait_async
from .webhooks import Webhook

__all__ = ["DEFAULT_BASE_URL", "DEFAULT_TIMEOUT_MS", "Assessments", "Keys", "NoResponse"]

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
    """Signup and gateway assessments."""

    # create ---------------------------------------------------------------

    def create(  # type: ignore[override]
        self,
        *,
        account_id: str,
        identifiers: Identifiers,
        idempotency_key: Optional[str] = None,
        policy_context: Optional[PolicyContext] = None,
        request_id: Optional[str] = None,
        deadline_ms: Optional[int] = None,
        response_mode: Optional[models.shared.ResponseMode] = None,
        client_context: Optional[ClientContext] = None,
        auth_context: Optional[AuthContext] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Assessment:
        """Assess a signup, login or other event for abuse.

        The result is the assessment whether the API answered 200 (complete or
        partial) or 202 (pending: apply your own fallback, then wait() or take
        the webhook). idempotency_key is generated when omitted and is sent
        again on every retry of this call; pass your own, derived from your
        signup attempt, so that a retry from your side replays the same
        assessment instead of starting new work.
        """
        response = _sync(super().create)(
            idempotency_key=_key(idempotency_key),
            account_id=account_id,
            identifiers=cast(Any, identifiers),
            policy_context=policy_context,
            request_id=request_id,
            deadline_ms=deadline_ms,
            response_mode=response_mode,
            client_context=client_context,
            auth_context=auth_context,
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
        identifiers: Identifiers,
        idempotency_key: Optional[str] = None,
        policy_context: Optional[PolicyContext] = None,
        request_id: Optional[str] = None,
        deadline_ms: Optional[int] = None,
        response_mode: Optional[models.shared.ResponseMode] = None,
        client_context: Optional[ClientContext] = None,
        auth_context: Optional[AuthContext] = None,
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
            policy_context=policy_context,
            request_id=request_id,
            deadline_ms=deadline_ms,
            response_mode=response_mode,
            client_context=client_context,
            auth_context=auth_context,
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
        """Poll get() until the assessment is no longer pending.

        Sleeps for the Retry-After the API sends between polls, at least one
        second, and raises APITimeoutError (a WaitTimeoutError, whose last
        attribute is the final pending assessment) after timeout seconds.
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


def _assessment(response: Any) -> Assessment:
    # A raw-response wrapper (with_raw_response) hands back its own object untouched.
    if not isinstance(response, (models.operations.CreateAssessmentResponse, models.operations.GetAssessmentResponse)):
        return response  # type: ignore[no-any-return]
    return as_assessment(response.result, ResponseMeta.from_headers(response.headers))


def _outcome(response: Any) -> AssessmentOutcome:
    if not isinstance(response, models.operations.RecordAssessmentOutcomeResponse):
        return response  # type: ignore[no-any-return]
    return as_outcome(response.result, ResponseMeta.from_headers(response.headers))


def _page(response: models.operations.QueryAccountAssessmentsResponse, fetch: Callable[[str], Any]) -> AssessmentPage:
    body = response.result
    return AssessmentPage(
        account_id=body.account_id,
        items=[as_assessment(item) for item in body.items],
        next_cursor=body.next_cursor or None,
        retention_days=body.retention_days,
        meta=ResponseMeta.from_headers(response.headers),
        fetch=fetch,
    )


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


def _rotation(response: Any) -> KeyRotation:
    if not isinstance(response, models.operations.RotateAPIKeyResponse):
        return response  # type: ignore[no-any-return]
    return as_rotation(response.result, ResponseMeta.from_headers(response.headers))


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

    webhooks = Webhook
    """Webhook verification: ``nr.webhooks.construct_event(payload, headers, secrets)``."""

    assessments: Assessments  # type: ignore[assignment]
    keys: Keys  # type: ignore[assignment]
    _sub_sdk_map: Dict[str, Any] = {
        "assessments": ("noresponse.client", "Assessments"),
        "keys": ("noresponse.client", "Keys"),
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
