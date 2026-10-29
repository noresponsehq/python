from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class CostTypedDict(TypedDict):
    allow: float
    step_up: float
    review: float
    block: float


class Cost(BaseModel):
    allow: float

    step_up: float

    review: float

    block: float
