from __future__ import annotations
from .screeningcoveragesources import (
    ScreeningCoverageSources,
    ScreeningCoverageSourcesTypedDict,
)
from .screeningcoveragetiming import (
    ScreeningCoverageTiming,
    ScreeningCoverageTimingTypedDict,
)
from .screeningplatformcoverage import (
    ScreeningPlatformCoverage,
    ScreeningPlatformCoverageTypedDict,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ScreeningCoverageTypedDict(TypedDict):
    r"""The denominator of a screening: accounts found, how many could be read, items read and the period they span, so a clean result is distinct from a person nobody could see."""

    accounts_found: int
    accounts_accessible: int
    items_read: int
    platforms: List[ScreeningPlatformCoverageTypedDict]
    period_from: NotRequired[str]
    r"""The oldest item read on any platform."""
    period_to: NotRequired[str]
    r"""The newest item read on any platform."""
    not_searched: NotRequired[List[str]]
    r"""Requested platforms where the person gave the screening nothing to look up, such as no handle for a platform that reads supplied handles only. Nothing looked and nothing failed: such a platform is not in platforms, is not none_found and does not make the person partial."""
    sources: NotRequired[ScreeningCoverageSourcesTypedDict]
    r"""How many sources this search asked and how many answered, across the lookup stage (sources asked whether an account exists for an identifier) and the platform stage (profiles read on each platform). A source that answered may have found nothing; one that did not answer failed or ran out of time."""
    timing: NotRequired[ScreeningCoverageTimingTypedDict]
    r"""How long this search's latest attempt took, stage by stage. started_at minus the investigation's creation is the time spent queued or retrying."""


class ScreeningCoverage(BaseModel):
    r"""The denominator of a screening: accounts found, how many could be read, items read and the period they span, so a clean result is distinct from a person nobody could see."""

    accounts_found: int

    accounts_accessible: int

    items_read: int

    platforms: List[ScreeningPlatformCoverage]

    period_from: Optional[str] = None
    r"""The oldest item read on any platform."""

    period_to: Optional[str] = None
    r"""The newest item read on any platform."""

    not_searched: Optional[List[str]] = None
    r"""Requested platforms where the person gave the screening nothing to look up, such as no handle for a platform that reads supplied handles only. Nothing looked and nothing failed: such a platform is not in platforms, is not none_found and does not make the person partial."""

    sources: Optional[ScreeningCoverageSources] = None
    r"""How many sources this search asked and how many answered, across the lookup stage (sources asked whether an account exists for an identifier) and the platform stage (profiles read on each platform). A source that answered may have found nothing; one that did not answer failed or ran out of time."""

    timing: Optional[ScreeningCoverageTiming] = None
    r"""How long this search's latest attempt took, stage by stage. started_at minus the investigation's creation is the time spent queued or retrying."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            ["period_from", "period_to", "not_searched", "sources", "timing"]
        )
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
