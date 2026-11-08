from __future__ import annotations
from .attendeeidentity import AttendeeIdentity, AttendeeIdentityTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class AttendeeBatchRequestTypedDict(TypedDict):
    r"""Adds or updates 1 to 500 attendees. A row naming an existing attendee of the event (the same external_id, else the same email, else the same phone) updates it."""

    attendees: List[AttendeeIdentityTypedDict]


class AttendeeBatchRequest(BaseModel):
    r"""Adds or updates 1 to 500 attendees. A row naming an existing attendee of the event (the same external_id, else the same email, else the same phone) updates it."""

    attendees: List[AttendeeIdentity]
