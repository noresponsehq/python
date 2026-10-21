"""Public entry points for the hand-written Python SDK helpers."""

from __future__ import annotations

from .assessments import Assessments
from .sdk import NoResponse
from .wait import DEFAULT_WAIT_SECONDS, WaitTimeoutError, wait, wait_async
from .webhooks import (
    AssessmentExpired,
    EndpointVerification,
    WebhookEvent,
    WebhookVerificationError,
    construct_event,
    verification_response,
)


def _wait(self: Assessments, assessment_id: str, *, timeout: float = DEFAULT_WAIT_SECONDS):
    return wait(self, assessment_id, timeout=timeout)


async def _wait_async(self: Assessments, assessment_id: str, *, timeout: float = DEFAULT_WAIT_SECONDS):
    return await wait_async(self, assessment_id, timeout=timeout)


if not hasattr(Assessments, "wait"):
    Assessments.wait = _wait  # type: ignore[attr-defined,method-assign]
    Assessments.wait_async = _wait_async  # type: ignore[attr-defined,method-assign]


__all__ = [
    "NoResponse",
    "Assessments",
    "WaitTimeoutError",
    "construct_event",
    "verification_response",
    "WebhookVerificationError",
    "WebhookEvent",
    "AssessmentExpired",
    "EndpointVerification",
]
