from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class RiskDetailsPhoneNameTypedDict(TypedDict):
    value: str
    seen_by: int


class RiskDetailsPhoneName(BaseModel):
    value: str

    seen_by: int
