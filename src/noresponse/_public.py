"""The public entry points of the package. Hand-written; not generated.

The generated __init__ imports everything from here last, so these names replace
the generated client of the same name: NoResponse here is the client in
client.py, which wraps the generated one.
"""

from __future__ import annotations

from .client import Assessments, Keys, NoResponse
from .auth import from_auth0, from_clerk, from_firebase, from_oidc, from_supabase, from_workos
from .errors import (
    APIConnectionError,
    APIStatusError,
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    NoResponseError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    ResponseValidationError,
)
from .models.shared import AuthContext, AuthContextTypedDict
from .responses import Assessment, AssessmentOutcome, AssessmentPage, KeyRotation, ResponseMeta
from ._wait import DEFAULT_WAIT_SECONDS, WaitTimeoutError, wait, wait_async
from .webhooks import (
    AssessmentExpired,
    EndpointVerification,
    Webhook,
    WebhookEvent,
    WebhookVerificationError,
    construct_event,
    verification_response,
)

__all__ = [
    "NoResponse",
    "Assessments",
    "Keys",
    "Assessment",
    "AssessmentOutcome",
    "AssessmentPage",
    "KeyRotation",
    "ResponseMeta",
    "AuthContext",
    "AuthContextTypedDict",
    "NoResponseError",
    "APIStatusError",
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "RateLimitError",
    "ResponseValidationError",
    "APIConnectionError",
    "APITimeoutError",
    "WaitTimeoutError",
    "DEFAULT_WAIT_SECONDS",
    "wait",
    "wait_async",
    "Webhook",
    "from_workos",
    "from_clerk",
    "from_auth0",
    "from_supabase",
    "from_firebase",
    "from_oidc",
    "construct_event",
    "verification_response",
    "WebhookVerificationError",
    "WebhookEvent",
    "AssessmentExpired",
    "EndpointVerification",
]
