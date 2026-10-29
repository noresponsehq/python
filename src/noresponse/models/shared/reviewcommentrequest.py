from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class ReviewCommentRequestTypedDict(TypedDict):
    expected_version: int
    body: str


class ReviewCommentRequest(BaseModel):
    expected_version: int

    body: str
