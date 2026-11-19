from __future__ import annotations
from .stage import Stage
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class StageTimeTypedDict(TypedDict):
    stage: Stage
    r"""ai_typing and analysis appear only on searches recorded before the engine stopped analysing results."""
    ms: int


class StageTime(BaseModel):
    stage: Stage
    r"""ai_typing and analysis appear only on searches recorded before the engine stopped analysing results."""

    ms: int
