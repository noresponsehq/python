from __future__ import annotations
from .reviewsubject import ReviewSubject, ReviewSubjectTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ReviewSubjectListTypedDict(TypedDict):
    r"""Retained tenant-local subject links and the current review version."""

    review_version: int
    items: List[ReviewSubjectTypedDict]


class ReviewSubjectList(BaseModel):
    r"""Retained tenant-local subject links and the current review version."""

    review_version: int

    items: List[ReviewSubject]
