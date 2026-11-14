from __future__ import annotations
from .personbatchitem import PersonBatchItem, PersonBatchItemTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class PersonBatchTypedDict(TypedDict):
    r"""What the batch did, row by row."""

    created: int
    updated: int
    items: List[PersonBatchItemTypedDict]


class PersonBatch(BaseModel):
    r"""What the batch did, row by row."""

    created: int

    updated: int

    items: List[PersonBatchItem]
