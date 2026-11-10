from __future__ import annotations
from .attendeerole import AttendeeRole
from .handle import Handle, HandleTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class AttendeeIdentityTypedDict(TypedDict):
    r"""What you know about an attendee. Stored encrypted under the workspace's key."""

    name: str
    r"""The attendee's full name."""
    external_id: NotRequired[str]
    r"""Your own id for the attendee, unique within the event. A later row with the same external id updates this attendee."""
    email: NotRequired[str]
    r"""The attendee's email."""
    phone: NotRequired[str]
    r"""The attendee's phone in E.164 form."""
    company: NotRequired[str]
    r"""Where the attendee works."""
    city: NotRequired[str]
    r"""Where the attendee lives."""
    handles: NotRequired[List[HandleTypedDict]]
    r"""Accounts the attendee is known to hold, at most 20."""
    role: NotRequired[AttendeeRole]
    r"""The attendee's role at the event: guest (a ticket holder), crew, vendor or press. Leave it out when you do not know it: an attendee without one has no role, not guest. A later row naming the same attendee replaces it, and a change of role alone keeps the attendee's screening results."""


class AttendeeIdentity(BaseModel):
    r"""What you know about an attendee. Stored encrypted under the workspace's key."""

    name: str
    r"""The attendee's full name."""

    external_id: Optional[str] = None
    r"""Your own id for the attendee, unique within the event. A later row with the same external id updates this attendee."""

    email: Optional[str] = None
    r"""The attendee's email."""

    phone: Optional[str] = None
    r"""The attendee's phone in E.164 form."""

    company: Optional[str] = None
    r"""Where the attendee works."""

    city: Optional[str] = None
    r"""Where the attendee lives."""

    handles: Optional[List[Handle]] = None
    r"""Accounts the attendee is known to hold, at most 20."""

    role: Optional[AttendeeRole] = None
    r"""The attendee's role at the event: guest (a ticket holder), crew, vendor or press. Leave it out when you do not know it: an attendee without one has no role, not guest. A later row naming the same attendee replaces it, and a change of role alone keeps the attendee's screening results."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            ["external_id", "email", "phone", "company", "city", "handles", "role"]
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
