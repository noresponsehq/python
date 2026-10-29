from __future__ import annotations
from .reviewsubjectkind import ReviewSubjectKind
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ReviewSubjectRequestTypedDict(TypedDict):
    r"""An assessment link also requires assessment_id and assessment_version; an issued_credential link also requires credential_id. Every reference must belong to account_id in this environment. Other kinds reject those fields."""

    kind: ReviewSubjectKind
    account_id: str
    reason: str
    expected_version: int
    assessment_id: NotRequired[str]
    assessment_version: NotRequired[int]
    credential_id: NotRequired[str]


class ReviewSubjectRequest(BaseModel):
    r"""An assessment link also requires assessment_id and assessment_version; an issued_credential link also requires credential_id. Every reference must belong to account_id in this environment. Other kinds reject those fields."""

    kind: ReviewSubjectKind

    account_id: str

    reason: str

    expected_version: int

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
