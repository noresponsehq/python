from __future__ import annotations
from noresponse.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import TypedDict


class ThresholdsTypedDict(TypedDict):
    step_up: int
    review: int
    block: Nullable[int]


class Thresholds(BaseModel):
    step_up: int

    review: int

    block: Nullable[int]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                m[k] = val

        return m
