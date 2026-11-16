from __future__ import annotations
from .handle import Handle, HandleTypedDict
from .investigation import Investigation, InvestigationTypedDict
from .screeningfinding import ScreeningFinding, ScreeningFindingTypedDict
from .screeninglookup import ScreeningLookup, ScreeningLookupTypedDict
from .screeningmedia import ScreeningMedia, ScreeningMediaTypedDict
from .screeningpost import ScreeningPost, ScreeningPostTypedDict
from .screeningprofile import ScreeningProfile, ScreeningProfileTypedDict
from .search import Search, SearchTypedDict
from .writtenprofile import WrittenProfile, WrittenProfileTypedDict
from noresponse.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class WorkspacePersonReportTypedDict(TypedDict):
    r"""Read a workspace person."""

    id: str
    created_at: str
    updated_at: str
    expires_at: str
    r"""The time the workspace retention policy removes this person, their evidence and investigation history. Shortening workspace retention can move this time earlier."""
    profiles: List[ScreeningProfileTypedDict]
    r"""The accounts this result matched, with how each was matched."""
    findings: List[ScreeningFindingTypedDict]
    r"""What this result flagged, most severe first, each citing its evidence."""
    posts: List[ScreeningPostTypedDict]
    r"""All posts retained for this result, including posts that no finding cites."""
    media: List[ScreeningMediaTypedDict]
    r"""All images and videos retained for this result, including media that no finding cites."""
    evidence_investigation: Nullable[InvestigationTypedDict]
    r"""The most recent retained completed or partial investigation, or a migrated result whose original per-person status is unknown. The evidence below belongs to this investigation. Read investigation history for earlier results and pending jobs."""
    written_profile: Nullable[WrittenProfileTypedDict]
    r"""An investigator's profile of this person, written from the evidence of a settled investigation. Null until an investigation completes or partially completes, and null when evidence.read is denied."""
    external_id: NotRequired[str]
    r"""Your reference for this person within the workspace environment. Only an explicit reference or person_id can reuse an existing person."""
    name: NotRequired[str]
    email: NotRequired[str]
    r"""The person's email."""
    phone: NotRequired[str]
    r"""The person's phone in E.164 form."""
    company: NotRequired[str]
    r"""Where the person works."""
    city: NotRequired[str]
    r"""Where the person lives."""
    handles: NotRequired[List[HandleTypedDict]]
    r"""Accounts the person is known to hold, at most 20."""
    lookup: NotRequired[ScreeningLookupTypedDict]
    r"""What the signup check's lookups found for a person: account presence for the email, phone and usernames (the person's handles), the phone lookup, the email domain's registration and the breach search. Context and coverage for the reviewer, not a finding: nothing here sets a band or a match state."""
    searches: NotRequired[List[SearchTypedDict]]
    r"""Every search on this person's values, newest first, whether a person started it or enrichment did: each names the value, the record and field it came from, and the search that found that record. Absent when nothing was searched."""
    evidence_restricted: NotRequired[bool]
    r"""True when evidence.read is explicitly denied. Submitted details, coverage, job status and decisions remain available. Collected records, profiles, findings, posts, media, discovered values and free-text decision notes are withheld."""


class WorkspacePersonReport(BaseModel):
    r"""Read a workspace person."""

    id: str

    created_at: str

    updated_at: str

    expires_at: str
    r"""The time the workspace retention policy removes this person, their evidence and investigation history. Shortening workspace retention can move this time earlier."""

    profiles: List[ScreeningProfile]
    r"""The accounts this result matched, with how each was matched."""

    findings: List[ScreeningFinding]
    r"""What this result flagged, most severe first, each citing its evidence."""

    posts: List[ScreeningPost]
    r"""All posts retained for this result, including posts that no finding cites."""

    media: List[ScreeningMedia]
    r"""All images and videos retained for this result, including media that no finding cites."""

    evidence_investigation: Nullable[Investigation]
    r"""The most recent retained completed or partial investigation, or a migrated result whose original per-person status is unknown. The evidence below belongs to this investigation. Read investigation history for earlier results and pending jobs."""

    written_profile: Nullable[WrittenProfile]
    r"""An investigator's profile of this person, written from the evidence of a settled investigation. Null until an investigation completes or partially completes, and null when evidence.read is denied."""

    external_id: Optional[str] = None
    r"""Your reference for this person within the workspace environment. Only an explicit reference or person_id can reuse an existing person."""

    name: Optional[str] = None

    email: Optional[str] = None
    r"""The person's email."""

    phone: Optional[str] = None
    r"""The person's phone in E.164 form."""

    company: Optional[str] = None
    r"""Where the person works."""

    city: Optional[str] = None
    r"""Where the person lives."""

    handles: Optional[List[Handle]] = None
    r"""Accounts the person is known to hold, at most 20."""

    lookup: Optional[ScreeningLookup] = None
    r"""What the signup check's lookups found for a person: account presence for the email, phone and usernames (the person's handles), the phone lookup, the email domain's registration and the breach search. Context and coverage for the reviewer, not a finding: nothing here sets a band or a match state."""

    searches: Optional[List[Search]] = None
    r"""Every search on this person's values, newest first, whether a person started it or enrichment did: each names the value, the record and field it came from, and the search that found that record. Absent when nothing was searched."""

    evidence_restricted: Optional[bool] = None
    r"""True when evidence.read is explicitly denied. Submitted details, coverage, job status and decisions remain available. Collected records, profiles, findings, posts, media, discovered values and free-text decision notes are withheld."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "external_id",
                "name",
                "email",
                "phone",
                "company",
                "city",
                "handles",
                "lookup",
                "searches",
                "evidence_restricted",
            ]
        )
        nullable_fields = set(["evidence_investigation", "written_profile"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))
            is_nullable_and_explicitly_set = (
                k in nullable_fields
                and (self.__pydantic_fields_set__.intersection({n}))  # pylint: disable=no-member
            )

            if val != UNSET_SENTINEL:
                if (
                    val is not None
                    or k not in optional_fields
                    or is_nullable_and_explicitly_set
                ):
                    m[k] = val

        return m
