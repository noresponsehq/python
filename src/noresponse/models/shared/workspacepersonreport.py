from __future__ import annotations
from .handle import Handle, HandleTypedDict
from .investigation import Investigation, InvestigationTypedDict
from .personchange import PersonChange, PersonChangeTypedDict
from .persongroup import PersonGroup, PersonGroupTypedDict
from .personschedule import PersonSchedule, PersonScheduleTypedDict
from .screeninglookup import ScreeningLookup, ScreeningLookupTypedDict
from .screeningmedia import ScreeningMedia, ScreeningMediaTypedDict
from .screeningpost import ScreeningPost, ScreeningPostTypedDict
from .screeningprofile import ScreeningProfile, ScreeningProfileTypedDict
from .search import Search, SearchTypedDict
from .suggestedsearch import SuggestedSearch, SuggestedSearchTypedDict
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
    groups: List[PersonGroupTypedDict]
    r"""Every group this person belongs to in this environment, most recently added first, with their role in each. A person can belong to any number of groups; removing them from a group or deleting the group removes it here."""
    profiles: List[ScreeningProfileTypedDict]
    r"""The accounts this result matched, with how each was matched."""
    posts: List[ScreeningPostTypedDict]
    r"""All posts retained for this result."""
    media: List[ScreeningMediaTypedDict]
    r"""All images and videos retained for this result."""
    suggested_searches: List[SuggestedSearchTypedDict]
    r"""The searches enrichment would start on this person, likeliest record first, under the environment's enrichment setting for a person's own investigation. In off mode the list is empty. In suggest mode enrichment starts none of them by itself; in automatic mode it starts them as its limits allow. Empty when evidence.read is denied."""
    evidence_investigation: Nullable[InvestigationTypedDict]
    r"""The most recent retained completed or partial investigation, or a migrated result whose original per-person status is unknown. The evidence below belongs to this investigation. Read investigation history for earlier results and pending jobs."""
    changes: List[PersonChangeTypedDict]
    r"""What changed between each settled investigation of this person and the one before it, unreviewed first, then most significant, then newest. The first investigation records no changes. When evidence.read is denied, before and after are withheld."""
    schedule: PersonScheduleTypedDict
    r"""The person's rerun schedule. Each due run starts a full investigation of the person, as POST /v1/investigations with no platforms does, and its changes are stored as changes. The schedule lives in the database and the worker runs it, so it survives restarts and releases; each due run starts exactly one investigation."""
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
    username: NotRequired[str]
    r"""A username the person uses, with no platform. A search looks it up on every platform that finds accounts by username."""
    handles: NotRequired[List[HandleTypedDict]]
    r"""Accounts the person is known to hold, at most 20."""
    lookup: NotRequired[ScreeningLookupTypedDict]
    r"""What the signup check's lookups found for a person: account presence for the email, phone and usernames (the person's handles), the phone lookup, the email domain's registration and the breach search. Nothing here sets a match state."""
    searches: NotRequired[List[SearchTypedDict]]
    r"""Every search on this person's values, newest first, whether a person started it or enrichment did: each names the value, the record and field it came from, and the search that found that record. Absent when nothing was searched."""
    evidence_restricted: NotRequired[bool]
    r"""True when evidence.read is explicitly denied. Submitted details, coverage, job status and decisions remain available. Collected records, profiles, posts, media, discovered values and free-text decision notes are withheld."""


class WorkspacePersonReport(BaseModel):
    r"""Read a workspace person."""

    id: str

    created_at: str

    updated_at: str

    expires_at: str
    r"""The time the workspace retention policy removes this person, their evidence and investigation history. Shortening workspace retention can move this time earlier."""

    groups: List[PersonGroup]
    r"""Every group this person belongs to in this environment, most recently added first, with their role in each. A person can belong to any number of groups; removing them from a group or deleting the group removes it here."""

    profiles: List[ScreeningProfile]
    r"""The accounts this result matched, with how each was matched."""

    posts: List[ScreeningPost]
    r"""All posts retained for this result."""

    media: List[ScreeningMedia]
    r"""All images and videos retained for this result."""

    suggested_searches: List[SuggestedSearch]
    r"""The searches enrichment would start on this person, likeliest record first, under the environment's enrichment setting for a person's own investigation. In off mode the list is empty. In suggest mode enrichment starts none of them by itself; in automatic mode it starts them as its limits allow. Empty when evidence.read is denied."""

    evidence_investigation: Nullable[Investigation]
    r"""The most recent retained completed or partial investigation, or a migrated result whose original per-person status is unknown. The evidence below belongs to this investigation. Read investigation history for earlier results and pending jobs."""

    changes: List[PersonChange]
    r"""What changed between each settled investigation of this person and the one before it, unreviewed first, then most significant, then newest. The first investigation records no changes. When evidence.read is denied, before and after are withheld."""

    schedule: PersonSchedule
    r"""The person's rerun schedule. Each due run starts a full investigation of the person, as POST /v1/investigations with no platforms does, and its changes are stored as changes. The schedule lives in the database and the worker runs it, so it survives restarts and releases; each due run starts exactly one investigation."""

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

    username: Optional[str] = None
    r"""A username the person uses, with no platform. A search looks it up on every platform that finds accounts by username."""

    handles: Optional[List[Handle]] = None
    r"""Accounts the person is known to hold, at most 20."""

    lookup: Optional[ScreeningLookup] = None
    r"""What the signup check's lookups found for a person: account presence for the email, phone and usernames (the person's handles), the phone lookup, the email domain's registration and the breach search. Nothing here sets a match state."""

    searches: Optional[List[Search]] = None
    r"""Every search on this person's values, newest first, whether a person started it or enrichment did: each names the value, the record and field it came from, and the search that found that record. Absent when nothing was searched."""

    evidence_restricted: Optional[bool] = None
    r"""True when evidence.read is explicitly denied. Submitted details, coverage, job status and decisions remain available. Collected records, profiles, posts, media, discovered values and free-text decision notes are withheld."""

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
                "username",
                "handles",
                "lookup",
                "searches",
                "evidence_restricted",
            ]
        )
        nullable_fields = set(["evidence_investigation"])
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
