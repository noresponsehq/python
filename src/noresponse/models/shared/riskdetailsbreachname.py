from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class RiskDetailsBreachNameTypedDict(TypedDict):
    value: str
    seen_in: int


class RiskDetailsBreachName(BaseModel):
    value: str

    seen_in: int
