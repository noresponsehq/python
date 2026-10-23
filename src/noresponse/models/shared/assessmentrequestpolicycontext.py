from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AssessmentRequestPolicyContextTypedDict(TypedDict):
    r"""Optional policy inputs: region."""

    region: NotRequired[str]
    r"""ISO 3166-1 alpha-2 region of the signup, as the provider determines it."""


class AssessmentRequestPolicyContext(BaseModel):
    r"""Optional policy inputs: region."""

    region: Optional[str] = None
    r"""ISO 3166-1 alpha-2 region of the signup, as the provider determines it."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["region"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
