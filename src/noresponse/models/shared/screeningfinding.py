from __future__ import annotations
from .findingband import FindingBand
from .findingcategory import FindingCategory
from .screeningmediaobservation import (
    ScreeningMediaObservation,
    ScreeningMediaObservationTypedDict,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ScreeningFindingTypedDict(TypedDict):
    r"""Something the analyser flagged. band is capped by the strongest match among the profiles of its evidence: possible at most moderate, probable at most high. capped_from is the band the analyser gave when the cap lowered it."""

    id: str
    category: FindingCategory
    r"""What a finding is about: a direct threat to the principal or the event, intent to harm without a named target, fixation on the principal, a grievance against the host, research into the venue, route or security, weapons tied to any of these, disruption or protest planning toward this event, violent extremist content or identification, prior harassment or stalking of staff or principals, or posting the principal's addresses or movements."""
    band: FindingBand
    r"""How severe a finding is, most severe first."""
    confidence: float
    rationale: str
    evidence: List[str]
    r"""The posts and media that support the finding."""
    analyser: str
    r"""The resolver, collector or analyser that produced a record, by its catalogue name."""
    model: str
    spend_minor: int
    r"""What the analysis cost, in US cents."""
    created_at: str
    capped_from: NotRequired[FindingBand]
    r"""How severe a finding is, most severe first."""
    quote: NotRequired[str]
    r"""The exact words of the first evidence item that the finding rests on, as the analyser quoted them."""
    media_observations: NotRequired[List[ScreeningMediaObservationTypedDict]]
    r"""What the analyser saw in each image among evidence that the finding rests on. Unlike quote, an observation cannot be checked against the record: judge it against the image at the media item's permalink."""


class ScreeningFinding(BaseModel):
    r"""Something the analyser flagged. band is capped by the strongest match among the profiles of its evidence: possible at most moderate, probable at most high. capped_from is the band the analyser gave when the cap lowered it."""

    id: str

    category: FindingCategory
    r"""What a finding is about: a direct threat to the principal or the event, intent to harm without a named target, fixation on the principal, a grievance against the host, research into the venue, route or security, weapons tied to any of these, disruption or protest planning toward this event, violent extremist content or identification, prior harassment or stalking of staff or principals, or posting the principal's addresses or movements."""

    band: FindingBand
    r"""How severe a finding is, most severe first."""

    confidence: float

    rationale: str

    evidence: List[str]
    r"""The posts and media that support the finding."""

    analyser: str
    r"""The resolver, collector or analyser that produced a record, by its catalogue name."""

    model: str

    spend_minor: int
    r"""What the analysis cost, in US cents."""

    created_at: str

    capped_from: Optional[FindingBand] = None
    r"""How severe a finding is, most severe first."""

    quote: Optional[str] = None
    r"""The exact words of the first evidence item that the finding rests on, as the analyser quoted them."""

    media_observations: Optional[List[ScreeningMediaObservation]] = None
    r"""What the analyser saw in each image among evidence that the finding rests on. Unlike quote, an observation cannot be checked against the record: judge it against the image at the media item's permalink."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["capped_from", "quote", "media_observations"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
