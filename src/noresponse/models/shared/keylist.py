from __future__ import annotations
from .key import Key, KeyTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class KeyListTypedDict(TypedDict):
    r"""GET /v1/workspaces/{workspace_id}/keys: the keys of both of the workspace's environments, newest first, at most 200 of each, revoked and expired keys included. No item carries a secret."""

    items: List[KeyTypedDict]


class KeyList(BaseModel):
    r"""GET /v1/workspaces/{workspace_id}/keys: the keys of both of the workspace's environments, newest first, at most 200 of each, revoked and expired keys included. No item carries a secret."""

    items: List[Key]
