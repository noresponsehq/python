from __future__ import annotations
from .stage import Stage
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class StageTimeTypedDict(TypedDict):
    stage: Stage
    ms: int


class StageTime(BaseModel):
    stage: Stage

    ms: int
