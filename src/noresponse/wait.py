"""Wait for a pending assessment. Hand-written beside the generated client."""

from __future__ import annotations

import asyncio
import time
from datetime import timezone
from email.utils import parsedate_to_datetime
from typing import Any, Mapping, Sequence

from .models.shared.assessment import Assessment

__all__ = ["DEFAULT_WAIT_SECONDS", "WaitTimeoutError", "wait", "wait_async"]

DEFAULT_WAIT_SECONDS = 30.0


class WaitTimeoutError(TimeoutError):
    """The assessment was still pending when the wait ran out.

    last is the pending assessment from the final poll. The webhook delivers
    the result when it settles.
    """

    def __init__(self, assessment_id: str, last: Assessment) -> None:
        super().__init__(f"Assessment {assessment_id} is still pending")
        self.assessment_id = assessment_id
        self.last = last


def _retry_after(headers: Mapping[str, Sequence[str]], *, now: float | None = None) -> float:
    for name, values in headers.items():
        if name.lower() == "retry-after" and values:
            try:
                return max(1.0, float(values[0]))
            except ValueError:
                try:
                    retry_at = parsedate_to_datetime(values[0])
                except (TypeError, ValueError):
                    break
                if retry_at.tzinfo is None:
                    retry_at = retry_at.replace(tzinfo=timezone.utc)
                return max(1.0, retry_at.timestamp() - (time.time() if now is None else now))
    return 1.0


def _resource(client: Any) -> Any:
    return getattr(client, "assessments", client)


def wait(client: Any, assessment_id: str, *, timeout: float = DEFAULT_WAIT_SECONDS) -> Assessment:
    """Poll assessments.get until the assessment is no longer pending.

    Sleeps for the Retry-After the API sends between polls, at least 1 s, and
    raises WaitTimeoutError once timeout seconds have passed.
    """
    if timeout <= 0:
        raise ValueError("timeout must be positive")
    resource = _resource(client)
    deadline = time.monotonic() + timeout
    while True:
        remaining_ms = max(1, int((deadline - time.monotonic()) * 1000))
        response = resource.get(assessment_id, timeout_ms=remaining_ms)
        if response.result.status != "pending":
            return response.result
        delay = _retry_after(response.headers)
        if time.monotonic() + delay > deadline:
            raise WaitTimeoutError(assessment_id, response.result)
        time.sleep(delay)


async def wait_async(client: Any, assessment_id: str, *, timeout: float = DEFAULT_WAIT_SECONDS) -> Assessment:
    """The asyncio form of wait."""
    if timeout <= 0:
        raise ValueError("timeout must be positive")
    resource = _resource(client)
    deadline = time.monotonic() + timeout
    while True:
        remaining_ms = max(1, int((deadline - time.monotonic()) * 1000))
        response = await resource.get_async(assessment_id, timeout_ms=remaining_ms)
        if response.result.status != "pending":
            return response.result
        delay = _retry_after(response.headers)
        if time.monotonic() + delay > deadline:
            raise WaitTimeoutError(assessment_id, response.result)
        await asyncio.sleep(delay)
