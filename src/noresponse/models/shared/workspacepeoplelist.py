from __future__ import annotations
from .workspaceperson import WorkspacePerson, WorkspacePersonTypedDict
from noresponse.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List
from typing_extensions import TypedDict


class WorkspacePeopleListTypedDict(TypedDict):
    r"""List workspace people."""

    items: List[WorkspacePersonTypedDict]
    has_more: bool
    next_cursor: Nullable[str]


class WorkspacePeopleList(BaseModel):
    r"""List workspace people."""

    items: List[WorkspacePerson]

    has_more: bool

    next_cursor: Nullable[str]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                m[k] = val

        return m
