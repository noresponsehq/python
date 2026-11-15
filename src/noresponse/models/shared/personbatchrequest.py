from __future__ import annotations
from .personidentity import PersonIdentity, PersonIdentityTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class PersonBatchRequestTypedDict(TypedDict):
    r"""Adds 1 to 500 workspace people to the group. Reuses an explicit person_id or external_id. Matching email or phone values only suggest people; automatic merging is disabled."""

    people: List[PersonIdentityTypedDict]


class PersonBatchRequest(BaseModel):
    r"""Adds 1 to 500 workspace people to the group. Reuses an explicit person_id or external_id. Matching email or phone values only suggest people; automatic merging is disabled."""

    people: List[PersonIdentity]
