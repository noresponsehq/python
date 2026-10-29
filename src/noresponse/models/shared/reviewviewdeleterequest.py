from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class ReviewViewDeleteRequestTypedDict(TypedDict):
    expected_version: int


class ReviewViewDeleteRequest(BaseModel):
    expected_version: int
