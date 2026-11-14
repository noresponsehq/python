from __future__ import annotations
from .group import Group, GroupTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class GroupListTypedDict(TypedDict):
    r"""Groups, newest first."""

    items: List[GroupTypedDict]
    next_before: NotRequired[str]
    r"""Pass as before to read the next, older page."""


class GroupList(BaseModel):
    r"""Groups, newest first."""

    items: List[Group]

    next_before: Optional[str] = None
    r"""Pass as before to read the next, older page."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["next_before"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
