from __future__ import annotations
from .listchangestate import ListChangeState
from .listentry import ListEntry, ListEntryTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ListChangeTypedDict(TypedDict):
    r"""A committed bulk list change and bounded notification progress, available while propagation is pending and for 24 hours after all propagation completes. References count an account once per changed list entry and are not unique accounts. No endpoint delivery or customer enforcement is implied by completed."""

    id: str
    created_at: str
    state: ListChangeState
    added: List[ListEntryTypedDict]
    removed: List[str]
    pending_propagations: int
    processed_account_references: int


class ListChange(BaseModel):
    r"""A committed bulk list change and bounded notification progress, available while propagation is pending and for 24 hours after all propagation completes. References count an account once per changed list entry and are not unique accounts. No endpoint delivery or customer enforcement is implied by completed."""

    id: str

    created_at: str

    state: ListChangeState

    added: List[ListEntry]

    removed: List[str]

    pending_propagations: int

    processed_account_references: int
