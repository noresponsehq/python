from __future__ import annotations
from .investigation import Investigation, InvestigationTypedDict
from .personreview import PersonReview, PersonReviewTypedDict
from .screeningfinding import ScreeningFinding, ScreeningFindingTypedDict
from .screeninglookup import ScreeningLookup, ScreeningLookupTypedDict
from .screeningmedia import ScreeningMedia, ScreeningMediaTypedDict
from .screeningpost import ScreeningPost, ScreeningPostTypedDict
from .screeningprofile import ScreeningProfile, ScreeningProfileTypedDict
from .workspaceperson import WorkspacePerson, WorkspacePersonTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class InvestigationReportTypedDict(TypedDict):
    r"""Read an investigation and its evidence."""

    profiles: List[ScreeningProfileTypedDict]
    r"""The accounts this result matched, with how each was matched."""
    findings: List[ScreeningFindingTypedDict]
    r"""What this result flagged, most severe first, each citing its evidence."""
    posts: List[ScreeningPostTypedDict]
    r"""All posts retained for this result, including posts that no finding cites."""
    media: List[ScreeningMediaTypedDict]
    r"""All images and videos retained for this result, including media that no finding cites."""
    reviews: List[PersonReviewTypedDict]
    r"""Every recorded decision, oldest first."""
    person: WorkspacePersonTypedDict
    investigation: InvestigationTypedDict
    lookup: NotRequired[ScreeningLookupTypedDict]
    r"""What the signup check's lookups found for a person: account presence for the email, phone and usernames (the person's handles), the phone lookup, the email domain's registration and the breach search. Context and coverage for the reviewer, not a finding: nothing here sets a band or a match state."""
    evidence_restricted: NotRequired[bool]
    r"""True when evidence.read is explicitly denied. Submitted details, coverage, job status and decisions remain available. Collected records, profiles, findings, posts, media, discovered values and free-text decision notes are withheld."""


class InvestigationReport(BaseModel):
    r"""Read an investigation and its evidence."""

    profiles: List[ScreeningProfile]
    r"""The accounts this result matched, with how each was matched."""

    findings: List[ScreeningFinding]
    r"""What this result flagged, most severe first, each citing its evidence."""

    posts: List[ScreeningPost]
    r"""All posts retained for this result, including posts that no finding cites."""

    media: List[ScreeningMedia]
    r"""All images and videos retained for this result, including media that no finding cites."""

    reviews: List[PersonReview]
    r"""Every recorded decision, oldest first."""

    person: WorkspacePerson

    investigation: Investigation

    lookup: Optional[ScreeningLookup] = None
    r"""What the signup check's lookups found for a person: account presence for the email, phone and usernames (the person's handles), the phone lookup, the email domain's registration and the breach search. Context and coverage for the reviewer, not a finding: nothing here sets a band or a match state."""

    evidence_restricted: Optional[bool] = None
    r"""True when evidence.read is explicitly denied. Submitted details, coverage, job status and decisions remain available. Collected records, profiles, findings, posts, media, discovered values and free-text decision notes are withheld."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["lookup", "evidence_restricted"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
