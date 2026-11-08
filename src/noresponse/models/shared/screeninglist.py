from __future__ import annotations
from .screening import Screening, ScreeningTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ScreeningListTypedDict(TypedDict):
    r"""Screenings, newest first."""

    items: List[ScreeningTypedDict]
    next_before: NotRequired[str]
    r"""Pass as before to read the next, older page."""


class ScreeningList(BaseModel):
    r"""Screenings, newest first."""

    items: List[Screening]

    next_before: Optional[str] = None
    r"""Pass as before to read the next, older page."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["next_before"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
