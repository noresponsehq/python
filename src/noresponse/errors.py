"""Error classes and the fields every API error shares. Hand-written; not generated.

Every HTTP error the API returns is an instance of NoResponseError, with one
subclass per status: BadRequestError (400), AuthenticationError (401),
PermissionDeniedError (403), NotFoundError (404), ConflictError (409) and
RateLimitError (429). Any other 4xx or 5xx, and a 2xx the client could not read,
is an APIStatusError or a ResponseValidationError.

Whatever the status, a NoResponseError answers the same attributes: status,
type, title, detail, code, request_id, retry_after and invalid_params. They are
read from the problem document; a body that is not a problem document leaves
them None.

A request that never gets an answer raises APIConnectionError (DNS, TLS, reset)
or APITimeoutError (the request, or wait(), ran out of time). Neither extends
NoResponseError, because no response exists to describe.
"""

from __future__ import annotations

from typing import Optional

from .models.errors import (
    APIStatusError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    NoResponseError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    ResponseValidationError,
)

__all__ = [
    "APIConnectionError",
    "APIStatusError",
    "APITimeoutError",
    "AuthenticationError",
    "BadRequestError",
    "ConflictError",
    "NoResponseError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitError",
    "ResponseValidationError",
]


class APIConnectionError(Exception):
    """The request did not reach the API or no answer came back.

    cause is the underlying httpx error. The request may or may not have been
    processed: a create or outcome call is safe to repeat with the same
    idempotency_key.
    """

    def __init__(self, message: str = "Connection error", *, cause: Optional[BaseException] = None) -> None:
        super().__init__(message)
        self.cause = cause


class APITimeoutError(APIConnectionError, TimeoutError):
    """The request, or a wait, ran out of time."""

    def __init__(self, message: str = "Request timed out", *, cause: Optional[BaseException] = None) -> None:
        super().__init__(message, cause=cause)
