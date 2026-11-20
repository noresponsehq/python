from __future__ import annotations
from .grouptype import GroupType
from .principal import Principal, PrincipalTypedDict
from noresponse.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class GroupRequestTypedDict(TypedDict):
    r"""Creates an ongoing group or an event with optional dates."""

    name: str
    r"""The group's name."""
    type: NotRequired[GroupType]
    r"""What the group's people share: an event, an organisation, a place or another attribute."""
    attribute: NotRequired[str]
    r"""The attribute its people share, such as the employer's or the place's name."""
    starts_at: NotRequired[Nullable[str]]
    r"""Optional event start; null for an ongoing group."""
    ends_at: NotRequired[Nullable[str]]
    r"""Optional event end; requires starts_at and must be at or after it. Null when no end is set."""
    venue: NotRequired[str]
    r"""Where the group is held."""
    host: NotRequired[str]
    r"""The organisation hosting the group."""
    principals: NotRequired[List[PrincipalTypedDict]]
    r"""The people the group protects, at most 20."""
    topics: NotRequired[List[str]]
    r"""Sensitive topics the screening reads posts against, at most 50."""


class GroupRequest(BaseModel):
    r"""Creates an ongoing group or an event with optional dates."""

    name: str
    r"""The group's name."""

    type: Optional[GroupType] = None
    r"""What the group's people share: an event, an organisation, a place or another attribute."""

    attribute: Optional[str] = None
    r"""The attribute its people share, such as the employer's or the place's name."""

    starts_at: OptionalNullable[str] = UNSET
    r"""Optional event start; null for an ongoing group."""

    ends_at: OptionalNullable[str] = UNSET
    r"""Optional event end; requires starts_at and must be at or after it. Null when no end is set."""

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
        optional_fields = set(
            [
                "type",
                "attribute",
                "starts_at",
                "ends_at",
                "venue",
                "host",
                "principals",
                "topics",
            ]
        )
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
