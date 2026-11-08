from __future__ import annotations
from .principal import Principal, PrincipalTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class EventUpdateTypedDict(TypedDict):
    r"""Changes the fields it names; at least one besides expected_version."""

    name: NotRequired[str]
    r"""The event's name."""
    starts_at: NotRequired[str]
    r"""When the event starts."""
    ends_at: NotRequired[str]
    r"""When the event ends, at or after its start; the start when omitted."""
    venue: NotRequired[str]
    r"""Where the event is held."""
    host: NotRequired[str]
    r"""The organisation hosting the event."""
    principals: NotRequired[List[PrincipalTypedDict]]
    r"""The people the event protects, at most 20."""
    topics: NotRequired[List[str]]
    r"""Sensitive topics the screening reads posts against, at most 50."""
    expected_version: NotRequired[int]
    r"""When present, the change applies only if the event is still at this version (409 event_conflict otherwise)."""


class EventUpdate(BaseModel):
    r"""Changes the fields it names; at least one besides expected_version."""

    name: Optional[str] = None
    r"""The event's name."""

    starts_at: Optional[str] = None
    r"""When the event starts."""

    ends_at: Optional[str] = None
    r"""When the event ends, at or after its start; the start when omitted."""

    venue: Optional[str] = None
    r"""Where the event is held."""

    host: Optional[str] = None
    r"""The organisation hosting the event."""

    principals: Optional[List[Principal]] = None
    r"""The people the event protects, at most 20."""

    topics: Optional[List[str]] = None
    r"""Sensitive topics the screening reads posts against, at most 50."""

    expected_version: Optional[int] = None
    r"""When present, the change applies only if the event is still at this version (409 event_conflict otherwise)."""

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
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
