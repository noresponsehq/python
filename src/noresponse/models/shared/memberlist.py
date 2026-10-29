from __future__ import annotations
from .member import Member, MemberTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class MemberListTypedDict(TypedDict):
    r"""GET /v1/workspaces/{workspace_id}/members: the workspace's active members, oldest first, at most 100."""

    items: List[MemberTypedDict]


class MemberList(BaseModel):
    r"""GET /v1/workspaces/{workspace_id}/members: the workspace's active members, oldest first, at most 100."""

    items: List[Member]
