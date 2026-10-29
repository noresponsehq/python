from __future__ import annotations
from .reviewsubjectkind import ReviewSubjectKind
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ReviewSubjectTypedDict(TypedDict):
    r"""A tenant-local investigation link. risk_version is the account risk version captured when the link was added. It does not assert a relationship or change feedback or enforcement."""

    id: str
    kind: ReviewSubjectKind
    account_id: str
    risk_version: int
    reason: str
    created_by: str
    created_at: str
    assessment_id: NotRequired[str]
    assessment_version: NotRequired[int]
    credential_id: NotRequired[str]


class ReviewSubject(BaseModel):
    r"""A tenant-local investigation link. risk_version is the account risk version captured when the link was added. It does not assert a relationship or change feedback or enforcement."""

    id: str

    kind: ReviewSubjectKind

    account_id: str

    risk_version: int

    reason: str

    created_by: str

    created_at: str

    assessment_id: Optional[str] = None

    assessment_version: Optional[int] = None

    credential_id: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["assessment_id", "assessment_version", "credential_id"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
