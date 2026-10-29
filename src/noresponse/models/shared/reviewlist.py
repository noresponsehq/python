from __future__ import annotations
from .review import Review, ReviewTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ReviewListTypedDict(TypedDict):
    r"""List retained account reviews."""

    items: List[ReviewTypedDict]
    next_cursor: NotRequired[str]


class ReviewList(BaseModel):
    r"""List retained account reviews."""

    items: List[Review]

    next_cursor: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["next_cursor"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
