from __future__ import annotations
from .sourcecount import SourceCount, SourceCountTypedDict
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class ScreeningCoverageSourcesTypedDict(TypedDict):
    r"""How many sources this search asked and how many answered, across the lookup stage (sources asked whether an account exists for an identifier) and the platform stage (profiles read on each platform). A source that answered may have found nothing; one that did not answer failed or ran out of time."""

    asked: int
    r"""Lookup sources plus platforms asked."""
    answered: int
    r"""Lookup sources plus platforms that answered."""
    lookups: SourceCountTypedDict
    platforms: SourceCountTypedDict


class ScreeningCoverageSources(BaseModel):
    r"""How many sources this search asked and how many answered, across the lookup stage (sources asked whether an account exists for an identifier) and the platform stage (profiles read on each platform). A source that answered may have found nothing; one that did not answer failed or ran out of time."""

    asked: int
    r"""Lookup sources plus platforms asked."""

    answered: int
    r"""Lookup sources plus platforms that answered."""

    lookups: SourceCount

    platforms: SourceCount
