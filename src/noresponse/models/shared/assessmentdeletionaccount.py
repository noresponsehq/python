from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AssessmentDeletionAccountTypedDict(TypedDict):
    id: str
    r"""The account_id of the deleted assessment."""
    current_assessment_id: NotRequired[str]
    r"""The assessment the account's current risk now comes from. Absent when the account has no assessment with a decision left, and GET /v1/accounts/{account_id} then answers 404."""


class AssessmentDeletionAccount(BaseModel):
    id: str
    r"""The account_id of the deleted assessment."""

    current_assessment_id: Optional[str] = None
    r"""The assessment the account's current risk now comes from. Absent when the account has no assessment with a decision left, and GET /v1/accounts/{account_id} then answers 404."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["current_assessment_id"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
