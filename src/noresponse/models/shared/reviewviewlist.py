from __future__ import annotations
from .reviewview import ReviewView, ReviewViewTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ReviewViewListTypedDict(TypedDict):
    r"""List your private and shared review filters."""

    items: List[ReviewViewTypedDict]


class ReviewViewList(BaseModel):
    r"""List your private and shared review filters."""

    items: List[ReviewView]
