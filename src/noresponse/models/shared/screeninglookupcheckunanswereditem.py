from __future__ import annotations
from .failurereason import FailureReason
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class ScreeningLookupCheckUnansweredItemTypedDict(TypedDict):
    connector: str
    r"""The id of the connector that did not answer: breach for the breach search."""
    reason: FailureReason
    r"""Why a signal or source did not produce a definite found/not_found. timed_out means the source missed the request deadline; a continuation may still settle it. deferred means the (source, identifier) pair is async-only and was not attempted on the synchronous path; a continuation settles it."""


class ScreeningLookupCheckUnansweredItem(BaseModel):
    connector: str
    r"""The id of the connector that did not answer: breach for the breach search."""

    reason: FailureReason
    r"""Why a signal or source did not produce a definite found/not_found. timed_out means the source missed the request deadline; a continuation may still settle it. deferred means the (source, identifier) pair is async-only and was not attempted on the synchronous path; a continuation settles it."""
