from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class SourceCountTypedDict(TypedDict):
    asked: int
    answered: int


class SourceCount(BaseModel):
    asked: int

    answered: int
