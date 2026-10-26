from __future__ import annotations
from .footprintfamily import FootprintFamily
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class FootprintTimelineTypedDict(TypedDict):
    r"""One identifier's dated footprint across every source: the first and last year any event was seen, the years between them, the latest year a source dated activity (omitted when none did), how many distinct sites and which kinds of evidence saw it."""

    first_seen_year: int
    last_seen_year: int
    span_years: int
    sites: int
    families: List[FootprintFamily]
    last_active_year: NotRequired[int]


class FootprintTimeline(BaseModel):
    r"""One identifier's dated footprint across every source: the first and last year any event was seen, the years between them, the latest year a source dated activity (omitted when none did), how many distinct sites and which kinds of evidence saw it."""

    first_seen_year: int

    last_seen_year: int

    span_years: int

    sites: int

    families: List[FootprintFamily]

    last_active_year: Optional[int] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["last_active_year"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
