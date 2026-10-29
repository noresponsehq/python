from __future__ import annotations
from .invite import Invite, InviteTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class InviteListTypedDict(TypedDict):
    r"""GET /v1/workspaces/{workspace_id}/invites: the workspace's pending invites, oldest first, at most 50, with no token."""

    items: List[InviteTypedDict]


class InviteList(BaseModel):
    r"""GET /v1/workspaces/{workspace_id}/invites: the workspace's pending invites, oldest first, at most 50, with no token."""

    items: List[Invite]
