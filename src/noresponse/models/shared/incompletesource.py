from __future__ import annotations
from .incompletereason import IncompleteReason
from .lane import Lane
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class IncompleteSourceTypedDict(TypedDict):
    r"""One evidence lane that did not settle, and why. It names a lane, not a source. A lane that missed its deadline is timed_out rather than not_found."""

    lane: Lane
    r"""An evidence lane: accounts (account presence for email and username), phone, breach and ip."""
    reason: IncompleteReason
    r"""Why a lane did not settle. deferred means the lane is asynchronous and still running; a continuation settles it. timed_out means the lane missed its deadline. insufficient_evidence is a settled inconclusive signal rather than an incomplete lane."""


class IncompleteSource(BaseModel):
    r"""One evidence lane that did not settle, and why. It names a lane, not a source. A lane that missed its deadline is timed_out rather than not_found."""

    lane: Lane
    r"""An evidence lane: accounts (account presence for email and username), phone, breach and ip."""

    reason: IncompleteReason
    r"""Why a lane did not settle. deferred means the lane is asynchronous and still running; a continuation settles it. timed_out means the lane missed its deadline. insufficient_evidence is a settled inconclusive signal rather than an incomplete lane."""
