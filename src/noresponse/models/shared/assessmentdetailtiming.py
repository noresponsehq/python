from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class AssessmentDetailTimingTypedDict(TypedDict):
    deadline_ms: int
    r"""The budget the server applied to the synchronous answer."""
    elapsed_ms: int
    r"""Server time from HTTP ingress to this revision of the assessment."""


class AssessmentDetailTiming(BaseModel):
    deadline_ms: int
    r"""The budget the server applied to the synchronous answer."""

    elapsed_ms: int
    r"""Server time from HTTP ingress to this revision of the assessment."""
