from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class ReviewCommentTypedDict(TypedDict):
    id: str
    review_version: int
    body: str
    created_by: str
    created_at: str


class ReviewComment(BaseModel):
    id: str

    review_version: int

    body: str

    created_by: str

    created_at: str
