from __future__ import annotations
from .footprintcoherence import FootprintCoherence, FootprintCoherenceTypedDict
from .footprintfamily import FootprintFamily
from .footprinttimeline import FootprintTimeline, FootprintTimelineTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class FootprintTypedDict(TypedDict):
    r"""How long and how widely the signup's email and username have existed, and how far independent sources agree on the person behind them, in years and counts only. families are the kinds of evidence that found either identifier. Omitted when nothing found them: a footprint lookup that failed makes no claim, and absence is no_digital_footprint's to state."""

    families: List[FootprintFamily]
    email: NotRequired[FootprintTimelineTypedDict]
    r"""One identifier's dated footprint across every source: the first and last year any event was seen, the years between them, the latest year a source dated activity (omitted when none did), how many distinct sites and which kinds of evidence saw it."""
    username: NotRequired[FootprintTimelineTypedDict]
    r"""One identifier's dated footprint across every source: the first and last year any event was seen, the years between them, the latest year a source dated activity (omitted when none did), how many distinct sites and which kinds of evidence saw it."""
    coherence: NotRequired[FootprintCoherenceTypedDict]


class Footprint(BaseModel):
    r"""How long and how widely the signup's email and username have existed, and how far independent sources agree on the person behind them, in years and counts only. families are the kinds of evidence that found either identifier. Omitted when nothing found them: a footprint lookup that failed makes no claim, and absence is no_digital_footprint's to state."""

    families: List[FootprintFamily]

    email: Optional[FootprintTimeline] = None
    r"""One identifier's dated footprint across every source: the first and last year any event was seen, the years between them, the latest year a source dated activity (omitted when none did), how many distinct sites and which kinds of evidence saw it."""

    username: Optional[FootprintTimeline] = None
    r"""One identifier's dated footprint across every source: the first and last year any event was seen, the years between them, the latest year a source dated activity (omitted when none did), how many distinct sites and which kinds of evidence saw it."""

    coherence: Optional[FootprintCoherence] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["email", "username", "coherence"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
