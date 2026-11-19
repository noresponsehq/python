from __future__ import annotations
from .othergroups import OtherGroups, OtherGroupsTypedDict
from .person import Person, PersonTypedDict
from .personreview import PersonReview, PersonReviewTypedDict
from .screeninglookup import ScreeningLookup, ScreeningLookupTypedDict
from .screeningmedia import ScreeningMedia, ScreeningMediaTypedDict
from .screeningpost import ScreeningPost, ScreeningPostTypedDict
from .screeningprofile import ScreeningProfile, ScreeningProfileTypedDict
from .search import Search, SearchTypedDict
from .suggestedsearch import SuggestedSearch, SuggestedSearchTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PersonReportTypedDict(TypedDict):
    r"""Everything known about one person, and where else in the environment they appear."""

    person: PersonTypedDict
    r"""A person and where their screening and review stand."""
    profiles: List[ScreeningProfileTypedDict]
    r"""The accounts this result matched, with how each was matched."""
    posts: List[ScreeningPostTypedDict]
    r"""All posts retained for this result."""
    media: List[ScreeningMediaTypedDict]
    r"""All images and videos retained for this result."""
    reviews: List[PersonReviewTypedDict]
    r"""Every recorded decision, oldest first."""
    suggested_searches: List[SuggestedSearchTypedDict]
    r"""The searches enrichment would start on this person in this group, likeliest record first. Group screening follows the environment's enrichment setting, with suggest as its mode while the workspace has not set one. In off mode the list is empty. In suggest mode enrichment starts none of them by itself; in automatic mode it starts them as its limits allow. Empty when evidence.read is denied."""
    other_groups: OtherGroupsTypedDict
    r"""Where else in the environment the person appears, read live from those groups: deleting one removes it here."""
    lookup: NotRequired[ScreeningLookupTypedDict]
    r"""What the signup check's lookups found for a person: account presence for the email, phone and usernames (the person's handles), the phone lookup, the email domain's registration and the breach search. Nothing here sets a match state."""
    searches: NotRequired[List[SearchTypedDict]]
    r"""The searches on this person's values in this group, newest first: each names the value, the record and field it came from, and the search that found that record. Absent when nothing was searched."""
    evidence_restricted: NotRequired[bool]
    r"""True when evidence.read is explicitly denied. Submitted details, coverage, job status and decisions remain available. Collected records, profiles, posts, media, discovered values and free-text decision notes are withheld."""


class PersonReport(BaseModel):
    r"""Everything known about one person, and where else in the environment they appear."""

    person: Person
    r"""A person and where their screening and review stand."""

    profiles: List[ScreeningProfile]
    r"""The accounts this result matched, with how each was matched."""

    posts: List[ScreeningPost]
    r"""All posts retained for this result."""

    media: List[ScreeningMedia]
    r"""All images and videos retained for this result."""

    reviews: List[PersonReview]
    r"""Every recorded decision, oldest first."""

    suggested_searches: List[SuggestedSearch]
    r"""The searches enrichment would start on this person in this group, likeliest record first. Group screening follows the environment's enrichment setting, with suggest as its mode while the workspace has not set one. In off mode the list is empty. In suggest mode enrichment starts none of them by itself; in automatic mode it starts them as its limits allow. Empty when evidence.read is denied."""

    other_groups: OtherGroups
    r"""Where else in the environment the person appears, read live from those groups: deleting one removes it here."""

    lookup: Optional[ScreeningLookup] = None
    r"""What the signup check's lookups found for a person: account presence for the email, phone and usernames (the person's handles), the phone lookup, the email domain's registration and the breach search. Nothing here sets a match state."""

    searches: Optional[List[Search]] = None
    r"""The searches on this person's values in this group, newest first: each names the value, the record and field it came from, and the search that found that record. Absent when nothing was searched."""

    evidence_restricted: Optional[bool] = None
    r"""True when evidence.read is explicitly denied. Submitted details, coverage, job status and decisions remain available. Collected records, profiles, posts, media, discovered values and free-text decision notes are withheld."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["lookup", "searches", "evidence_restricted"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
