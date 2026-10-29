from __future__ import annotations
from .resolution import Resolution, ResolutionTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ReviewResolutionListTypedDict(TypedDict):
    r"""Read immutable review resolution history."""

    items: List[ResolutionTypedDict]
    next_before_version: NotRequired[int]


class ReviewResolutionList(BaseModel):
    r"""Read immutable review resolution history."""

    items: List[Resolution]

    next_before_version: Optional[int] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["next_before_version"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
