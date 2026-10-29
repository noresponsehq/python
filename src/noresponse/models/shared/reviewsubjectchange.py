from __future__ import annotations
from .reviewsubject import ReviewSubject, ReviewSubjectTypedDict
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class ReviewSubjectChangeTypedDict(TypedDict):
    r"""The link and resulting review version."""

    review_version: int
    subject: ReviewSubjectTypedDict
    r"""A tenant-local investigation link. risk_version is the account risk version captured when the link was added. It does not assert a relationship or change feedback or enforcement."""


class ReviewSubjectChange(BaseModel):
    r"""The link and resulting review version."""

    review_version: int

    subject: ReviewSubject
    r"""A tenant-local investigation link. risk_version is the account risk version captured when the link was added. It does not assert a relationship or change feedback or enforcement."""
