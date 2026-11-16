from __future__ import annotations
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


class GroupUpdateTypedDict(TypedDict):
    r"""Updates a group. Dates describe an optional event and do not control person retention."""

    name: NotRequired[str]
    r"""The group's name."""
    starts_at: NotRequired[Nullable[str]]
    r"""Optional event start; null for an ongoing group. Omit to keep the current value; send null to clear it."""
    ends_at: NotRequired[Nullable[str]]
    r"""Optional event end; requires starts_at and must be at or after it. Null when no end is set. Omit to keep the current value; send null to clear it."""
    venue: NotRequired[str]
    r"""Where the group is held."""
    host: NotRequired[str]
    r"""The organisation hosting the group."""
    principals: NotRequired[List[PrincipalTypedDict]]
    r"""The people the group protects, at most 20."""
    topics: NotRequired[List[str]]
    r"""Sensitive topics the screening reads posts against, at most 50."""
    expected_version: NotRequired[int]
    r"""When present, the change applies only if the group is still at this version (409 group_conflict otherwise)."""


class GroupUpdate(BaseModel):
    r"""Updates a group. Dates describe an optional event and do not control person retention."""

    name: Optional[str] = None
    r"""The group's name."""

    starts_at: OptionalNullable[str] = UNSET
    r"""Optional event start; null for an ongoing group. Omit to keep the current value; send null to clear it."""

    ends_at: OptionalNullable[str] = UNSET
    r"""Optional event end; requires starts_at and must be at or after it. Null when no end is set. Omit to keep the current value; send null to clear it."""

    venue: Optional[str] = None
    r"""Where the group is held."""

    host: Optional[str] = None
    r"""The organisation hosting the group."""

    principals: Optional[List[Principal]] = None
    r"""The people the group protects, at most 20."""

    topics: Optional[List[str]] = None
    r"""Sensitive topics the screening reads posts against, at most 50."""

    expected_version: Optional[int] = None
    r"""When present, the change applies only if the group is still at this version (409 group_conflict otherwise)."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "name",
                "starts_at",
                "ends_at",
                "venue",
                "host",
                "principals",
                "topics",
                "expected_version",
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
