from __future__ import annotations
from .investigation import Investigation, InvestigationTypedDict
from noresponse.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List
from typing_extensions import TypedDict


class InvestigationsListTypedDict(TypedDict):
    r"""List investigation history."""

    items: List[InvestigationTypedDict]
    has_more: bool
    next_cursor: Nullable[str]


class InvestigationsList(BaseModel):
    r"""List investigation history."""

    items: List[Investigation]

    has_more: bool

    next_cursor: Nullable[str]

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
