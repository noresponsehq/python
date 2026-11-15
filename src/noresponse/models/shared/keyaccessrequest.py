from __future__ import annotations
from noresponse.types import BaseModel
from typing import List, Literal
from typing_extensions import TypedDict


KeyAccessRequestDeniedAction = Literal[
    "evidence.read",
    "exports.read",
    "policy.publish",
]


class KeyAccessRequestTypedDict(TypedDict):
    denied_actions: List[KeyAccessRequestDeniedAction]
    r"""Explicit restrictions that override scope grants. An empty list restores the access supplied by the scopes. Rotation preserves these restrictions."""


class KeyAccessRequest(BaseModel):
    denied_actions: List[KeyAccessRequestDeniedAction]
    r"""Explicit restrictions that override scope grants. An empty list restores the access supplied by the scopes. Rotation preserves these restrictions."""
