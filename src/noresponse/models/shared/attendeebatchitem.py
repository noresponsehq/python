from __future__ import annotations
from .attendeebatchitemoutcome import AttendeeBatchItemOutcome
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class AttendeeBatchItemTypedDict(TypedDict):
    index: int
    r"""The row's position in the request."""
    id: str
    outcome: AttendeeBatchItemOutcome
    r"""unchanged: the row matched an attendee with the same details."""


class AttendeeBatchItem(BaseModel):
    index: int
    r"""The row's position in the request."""

    id: str

    outcome: AttendeeBatchItemOutcome
    r"""unchanged: the row matched an attendee with the same details."""
