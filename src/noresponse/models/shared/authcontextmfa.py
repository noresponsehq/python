from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class AuthContextMfaTypedDict(TypedDict):
    r"""Normalized multi-factor evidence from a verified provider session."""

    present: NotRequired[bool]
    methods: NotRequired[List[str]]
    age_seconds: NotRequired[int]


class AuthContextMfa(BaseModel):
    r"""Normalized multi-factor evidence from a verified provider session."""

    present: Optional[bool] = None

    methods: Optional[List[str]] = None

    age_seconds: Optional[int] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["present", "methods", "age_seconds"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
