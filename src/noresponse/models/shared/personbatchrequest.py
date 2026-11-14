from __future__ import annotations
from .personidentity import PersonIdentity, PersonIdentityTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class PersonBatchRequestTypedDict(TypedDict):
    r"""Adds or updates 1 to 500 people. A row naming an existing person of the group (the same external_id, else the same email, else the same phone) updates it."""

    people: List[PersonIdentityTypedDict]


class PersonBatchRequest(BaseModel):
    r"""Adds or updates 1 to 500 people. A row naming an existing person of the group (the same external_id, else the same email, else the same phone) updates it."""

    people: List[PersonIdentity]
