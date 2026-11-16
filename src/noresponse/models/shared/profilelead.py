from __future__ import annotations
from .profilecitation import ProfileCitation, ProfileCitationTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ProfileLeadTypedDict(TypedDict):
    value: str
    r"""A value copied exactly from a linked record that the person was not searched by."""
    kind: str
    why: str
    evidence: List[ProfileCitationTypedDict]


class ProfileLead(BaseModel):
    value: str
    r"""A value copied exactly from a linked record that the person was not searched by."""

    kind: str

    why: str

    evidence: List[ProfileCitation]
