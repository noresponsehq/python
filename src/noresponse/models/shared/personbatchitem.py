from __future__ import annotations
from .personbatchitemoutcome import PersonBatchItemOutcome
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class PersonBatchItemTypedDict(TypedDict):
    index: int
    r"""The row's position in the request."""
    id: str
    outcome: PersonBatchItemOutcome
    r"""unchanged: the row matched a person with the same details."""


class PersonBatchItem(BaseModel):
    index: int
    r"""The row's position in the request."""

    id: str

    outcome: PersonBatchItemOutcome
    r"""unchanged: the row matched a person with the same details."""
