from __future__ import annotations
from .handleplatform import HandlePlatform
from .screeningnotanalysedcount import (
    ScreeningNotAnalysedCount,
    ScreeningNotAnalysedCountTypedDict,
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
    items_not_analysed: NotRequired[int]
    r"""Items read that the analyser could not analyse. Above zero, the attendee is partial: a finding may be missing from them."""
    not_analysed_by_reason: NotRequired[List[ScreeningNotAnalysedCountTypedDict]]
    r"""items_not_analysed split by reason, each reason once with at least one item."""
    period_from: NotRequired[str]
    r"""The oldest item read on any platform."""
    period_to: NotRequired[str]
    r"""The newest item read on any platform."""
    not_searched: NotRequired[List[HandlePlatform]]
    r"""Requested platforms where the attendee gave the screening nothing to look up, such as no handle for a platform that reads supplied handles only. Nothing looked and nothing failed: such a platform is not in platforms, is not none_found and does not make the attendee partial."""


class ScreeningCoverage(BaseModel):
    r"""The denominator of a screening: accounts found, how many could be read, items read and the period they span, so a clean result is distinct from a person nobody could see."""

    accounts_found: int

    accounts_accessible: int

    items_read: int

    platforms: List[ScreeningPlatformCoverage]

    items_not_analysed: Optional[int] = None
    r"""Items read that the analyser could not analyse. Above zero, the attendee is partial: a finding may be missing from them."""

    not_analysed_by_reason: Optional[List[ScreeningNotAnalysedCount]] = None
    r"""items_not_analysed split by reason, each reason once with at least one item."""

    period_from: Optional[str] = None
    r"""The oldest item read on any platform."""

    period_to: Optional[str] = None
    r"""The newest item read on any platform."""

    not_searched: Optional[List[HandlePlatform]] = None
    r"""Requested platforms where the attendee gave the screening nothing to look up, such as no handle for a platform that reads supplied handles only. Nothing looked and nothing failed: such a platform is not in platforms, is not none_found and does not make the attendee partial."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "items_not_analysed",
                "not_analysed_by_reason",
                "period_from",
                "period_to",
                "not_searched",
            ]
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
