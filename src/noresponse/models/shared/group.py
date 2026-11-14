from __future__ import annotations
from .auditsettingsenvironment import AuditSettingsEnvironment
from .principal import Principal, PrincipalTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class GroupTypedDict(TypedDict):
    r"""A group and its screening context."""

    id: str
    environment: AuditSettingsEnvironment
    name: str
    r"""The group's name."""
    starts_at: str
    r"""When the group starts."""
    ends_at: str
    r"""When the group ends, at or after its start; the start when omitted."""
    principals: List[PrincipalTypedDict]
    r"""The people the group protects."""
    topics: List[str]
    r"""Sensitive topics."""
    people: int
    r"""How many people the group holds."""
    version: int
    r"""Goes up by one with every change."""
    purge_after: str
    r"""When raw collected items and unmatched candidate profiles are purged: 30 days after the group ends."""
    created_by: str
    r"""The member or key label that created the group."""
    created_at: str
    updated_at: str
    venue: NotRequired[str]
    r"""Where the group is held."""
    host: NotRequired[str]
    r"""The organisation hosting the group."""


class Group(BaseModel):
    r"""A group and its screening context."""

    id: str

    environment: AuditSettingsEnvironment

    name: str
    r"""The group's name."""

    starts_at: str
    r"""When the group starts."""

    ends_at: str
    r"""When the group ends, at or after its start; the start when omitted."""

    principals: List[Principal]
    r"""The people the group protects."""

    topics: List[str]
    r"""Sensitive topics."""

    people: int
    r"""How many people the group holds."""

    version: int
    r"""Goes up by one with every change."""

    purge_after: str
    r"""When raw collected items and unmatched candidate profiles are purged: 30 days after the group ends."""

    created_by: str
    r"""The member or key label that created the group."""

    created_at: str

    updated_at: str

    venue: Optional[str] = None
    r"""Where the group is held."""

    host: Optional[str] = None
    r"""The organisation hosting the group."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["venue", "host"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
