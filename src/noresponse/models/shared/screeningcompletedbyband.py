from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class ScreeningCompletedByBandTypedDict(TypedDict):
    r"""Screened attendees by the band of their most severe finding."""

    critical: int
    high: int
    moderate: int
    low: int
    info: int


class ScreeningCompletedByBand(BaseModel):
    r"""Screened attendees by the band of their most severe finding."""

    critical: int

    high: int

    moderate: int

    low: int

    info: int
