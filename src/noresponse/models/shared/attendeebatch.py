from __future__ import annotations
from .attendeebatchitem import AttendeeBatchItem, AttendeeBatchItemTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class AttendeeBatchTypedDict(TypedDict):
    r"""What the batch did, row by row."""

    created: int
    updated: int
    items: List[AttendeeBatchItemTypedDict]


class AttendeeBatch(BaseModel):
    r"""What the batch did, row by row."""

    created: int

    updated: int

    items: List[AttendeeBatchItem]
