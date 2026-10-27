from __future__ import annotations
from .listentry import ListEntry, ListEntryTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ListEntryListTypedDict(TypedDict):
    r"""GET /v1/workspaces/{workspace_id}/lists/{environment}: every entry of the environment's list, newest first. An environment holds at most 10,000 entries."""

    items: List[ListEntryTypedDict]


class ListEntryList(BaseModel):
    r"""GET /v1/workspaces/{workspace_id}/lists/{environment}: every entry of the environment's list, newest first. An environment holds at most 10,000 entries."""

    items: List[ListEntry]
