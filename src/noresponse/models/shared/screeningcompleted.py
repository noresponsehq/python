from __future__ import annotations
from .screeningcompletedbyband import (
    ScreeningCompletedByBand,
    ScreeningCompletedByBandTypedDict,
)
from .screeningcompletedstatus import ScreeningCompletedStatus
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ScreeningCompletedTypedDict(TypedDict):
    r"""A screening of a group finished. It counts only the people this screening set out to reach, not who they are: read the roster with GET /v1/workspaces/{workspace_id}/groups/{environment}/{group_id}/people, filtered by band, to act on them. people_screened + partial_coverage = people_total, people_flagged is the sum of by_band, no_footprint counts screened people with no flag whose accounts were not found, and no_profile_to_check those the screening had nothing to look up for on any requested platform. A cancelled screening sends no event."""

    screening_id: str
    r"""The screening that finished."""
    group_id: str
    r"""The group it screened."""
    status: ScreeningCompletedStatus
    r"""completed reached every person; partial left some not fully covered (partial_coverage); failed covered nobody."""
    people_total: int
    r"""Every person the screening set out to reach: those no screening had reached and those on watch or escalated."""
    people_screened: int
    r"""People the screening covered, flagged or not."""
    people_flagged: int
    r"""Screened people with a finding: the sum of by_band."""
    by_band: ScreeningCompletedByBandTypedDict
    r"""Screened people by the band of their most severe finding."""
    no_footprint: int
    r"""Screened people with no finding whose accounts were not found (match_state none_found). A clean result for someone with no visible accounts is not the same as a clean result for someone whose accounts were read."""
    partial_coverage: int
    r"""People the screening did not fully cover. Read each one's coverage on its person."""
    finished_at: str
    r"""When the screening finished; equal to the event's created_at."""
    error_code: NotRequired[str]
    r"""Why a partial or failed screening stopped before reaching everyone, as the screening resource says: expired, worker_attempts_exhausted, attempts_exhausted or screening_unavailable."""
    no_profile_to_check: NotRequired[int]
    r"""Screened people with no profile to check: the list gave nothing to look up on any requested platform, such as no handle, so nobody looked for a profile (no_profile_to_check on the person). Not in no_footprint, and not partial: nothing failed. Their lookups are on their reports."""


class ScreeningCompleted(BaseModel):
    r"""A screening of a group finished. It counts only the people this screening set out to reach, not who they are: read the roster with GET /v1/workspaces/{workspace_id}/groups/{environment}/{group_id}/people, filtered by band, to act on them. people_screened + partial_coverage = people_total, people_flagged is the sum of by_band, no_footprint counts screened people with no flag whose accounts were not found, and no_profile_to_check those the screening had nothing to look up for on any requested platform. A cancelled screening sends no event."""

    screening_id: str
    r"""The screening that finished."""

    group_id: str
    r"""The group it screened."""

    status: ScreeningCompletedStatus
    r"""completed reached every person; partial left some not fully covered (partial_coverage); failed covered nobody."""

    people_total: int
    r"""Every person the screening set out to reach: those no screening had reached and those on watch or escalated."""

    people_screened: int
    r"""People the screening covered, flagged or not."""

    people_flagged: int
    r"""Screened people with a finding: the sum of by_band."""

    by_band: ScreeningCompletedByBand
    r"""Screened people by the band of their most severe finding."""

    no_footprint: int
    r"""Screened people with no finding whose accounts were not found (match_state none_found). A clean result for someone with no visible accounts is not the same as a clean result for someone whose accounts were read."""

    partial_coverage: int
    r"""People the screening did not fully cover. Read each one's coverage on its person."""

    finished_at: str
    r"""When the screening finished; equal to the event's created_at."""

    error_code: Optional[str] = None
    r"""Why a partial or failed screening stopped before reaching everyone, as the screening resource says: expired, worker_attempts_exhausted, attempts_exhausted or screening_unavailable."""

    no_profile_to_check: Optional[int] = None
    r"""Screened people with no profile to check: the list gave nothing to look up on any requested platform, such as no handle, so nobody looked for a profile (no_profile_to_check on the person). Not in no_footprint, and not partial: nothing failed. Their lookups are on their reports."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["error_code", "no_profile_to_check"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
