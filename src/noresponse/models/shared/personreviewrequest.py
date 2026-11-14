from __future__ import annotations
from .persondecision import PersonDecision
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PersonReviewRequestTypedDict(TypedDict):
    r"""Records a decision on a person."""

    decision: PersonDecision
    note: NotRequired[str]
    r"""Why, for the venue team and later reviewers."""


class PersonReviewRequest(BaseModel):
    r"""Records a decision on a person."""

    decision: PersonDecision

    note: Optional[str] = None
    r"""Why, for the venue team and later reviewers."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["note"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
