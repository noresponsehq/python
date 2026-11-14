from __future__ import annotations
from .principal import Principal, PrincipalTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class GroupRequestTypedDict(TypedDict):
    r"""Creates a group."""

    name: str
    r"""The group's name."""
    starts_at: str
    r"""When the group starts."""
    ends_at: NotRequired[str]
    r"""When the group ends, at or after its start; the start when omitted."""
    venue: NotRequired[str]
    r"""Where the group is held."""
    host: NotRequired[str]
    r"""The organisation hosting the group."""
    principals: NotRequired[List[PrincipalTypedDict]]
    r"""The people the group protects, at most 20."""
    topics: NotRequired[List[str]]
    r"""Sensitive topics the screening reads posts against, at most 50."""


class GroupRequest(BaseModel):
    r"""Creates a group."""

    name: str
    r"""The group's name."""

    starts_at: str
    r"""When the group starts."""

    ends_at: Optional[str] = None
    r"""When the group ends, at or after its start; the start when omitted."""

    venue: Optional[str] = None
    r"""Where the group is held."""

    host: Optional[str] = None
    r"""The organisation hosting the group."""

    principals: Optional[List[Principal]] = None
    r"""The people the group protects, at most 20."""

    topics: Optional[List[str]] = None
    r"""Sensitive topics the screening reads posts against, at most 50."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["ends_at", "venue", "host", "principals", "topics"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
