from __future__ import annotations
from .othergroups import OtherGroups, OtherGroupsTypedDict
from .person import Person, PersonTypedDict
from .personreview import PersonReview, PersonReviewTypedDict
from .screeningfinding import ScreeningFinding, ScreeningFindingTypedDict
from .screeninglookup import ScreeningLookup, ScreeningLookupTypedDict
from .screeningmedia import ScreeningMedia, ScreeningMediaTypedDict
from .screeningpost import ScreeningPost, ScreeningPostTypedDict
from .screeningprofile import ScreeningProfile, ScreeningProfileTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PersonReportTypedDict(TypedDict):
    r"""Everything known about one person, and where else in the environment they appear."""

    person: PersonTypedDict
    r"""A person and where their screening and review stand."""
    profiles: List[ScreeningProfileTypedDict]
    r"""The accounts the latest screening matched, with how each was matched."""
    findings: List[ScreeningFindingTypedDict]
    r"""What the latest screening flagged, most severe first, each citing its evidence."""
    posts: List[ScreeningPostTypedDict]
    r"""The posts the findings cite."""
    media: List[ScreeningMediaTypedDict]
    r"""The images and videos the findings cite."""
    reviews: List[PersonReviewTypedDict]
    r"""Every recorded decision, oldest first."""
    other_groups: OtherGroupsTypedDict
    r"""Where else in the environment the person appears, read live from those groups: deleting one removes it here."""
    lookup: NotRequired[ScreeningLookupTypedDict]
    r"""What the signup check's lookups found for a person: account presence for the email, phone and usernames (the person's handles), the phone lookup, the email domain's registration and the breach search. Context and coverage for the reviewer, not a finding: nothing here sets a band or a match state."""


class PersonReport(BaseModel):
    r"""Everything known about one person, and where else in the environment they appear."""

    person: Person
    r"""A person and where their screening and review stand."""

    profiles: List[ScreeningProfile]
    r"""The accounts the latest screening matched, with how each was matched."""

    findings: List[ScreeningFinding]
    r"""What the latest screening flagged, most severe first, each citing its evidence."""

    posts: List[ScreeningPost]
    r"""The posts the findings cite."""

    media: List[ScreeningMedia]
    r"""The images and videos the findings cite."""

    reviews: List[PersonReview]
    r"""Every recorded decision, oldest first."""

    other_groups: OtherGroups
    r"""Where else in the environment the person appears, read live from those groups: deleting one removes it here."""

    lookup: Optional[ScreeningLookup] = None
    r"""What the signup check's lookups found for a person: account presence for the email, phone and usernames (the person's handles), the phone lookup, the email domain's registration and the breach search. Context and coverage for the reviewer, not a finding: nothing here sets a band or a match state."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["lookup"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
