from __future__ import annotations
from .auditsettingsenvironment import AuditSettingsEnvironment
from .grouptype import GroupType
from .principal import Principal, PrincipalTypedDict
from noresponse.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class GroupTypedDict(TypedDict):
    r"""A workspace group for a building, organization or event. Dates are optional and do not control person retention."""

    id: str
    environment: AuditSettingsEnvironment
    name: str
    r"""The group's name."""
    type: GroupType
    r"""What the group's people share: an event, an organisation, a place or another attribute."""
    attribute: str
    r"""The attribute its people share. Empty when none was given."""
    starts_at: Nullable[str]
    r"""Optional event start; null for an ongoing group."""
    ends_at: Nullable[str]
    r"""Optional event end; requires starts_at and must be at or after it. Null when no end is set."""
    principals: List[PrincipalTypedDict]
    r"""The people the group protects."""
    topics: List[str]
    r"""Sensitive topics."""
    people: int
    r"""How many people the group holds."""
    version: int
    r"""Goes up by one with every change."""
    created_by: str
    r"""The member or key label that created the group."""
    created_at: str
    updated_at: str
    venue: NotRequired[str]
    r"""Where the group is held."""
    host: NotRequired[str]
    r"""The organisation hosting the group."""


class Group(BaseModel):
    r"""A workspace group for a building, organization or event. Dates are optional and do not control person retention."""

    id: str

    environment: AuditSettingsEnvironment

    name: str
    r"""The group's name."""

    type: GroupType
    r"""What the group's people share: an event, an organisation, a place or another attribute."""

    attribute: str
    r"""The attribute its people share. Empty when none was given."""

    starts_at: Nullable[str]
    r"""Optional event start; null for an ongoing group."""

    ends_at: Nullable[str]
    r"""Optional event end; requires starts_at and must be at or after it. Null when no end is set."""

    principals: List[Principal]
    r"""The people the group protects."""

    topics: List[str]
    r"""Sensitive topics."""

    people: int
    r"""How many people the group holds."""

    version: int
    r"""Goes up by one with every change."""

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
        nullable_fields = set(["starts_at", "ends_at"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))
            is_nullable_and_explicitly_set = (
                k in nullable_fields
                and (self.__pydantic_fields_set__.intersection({n}))  # pylint: disable=no-member
            )

            if val != UNSET_SENTINEL:
                if (
                    val is not None
                    or k not in optional_fields
                    or is_nullable_and_explicitly_set
                ):
                    m[k] = val

        return m
