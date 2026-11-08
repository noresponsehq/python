from __future__ import annotations
from .attendeedecision import AttendeeDecision
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class AttendeeDecidedTypedDict(TypedDict):
    r"""A reviewer recorded a decision on an attendee. The decision's note stays in the API. Sent once per recorded review; an attendee's latest review is its decision, so order by decided_at."""

    event_id: str
    r"""The attendee's event."""
    attendee_id: str
    r"""The attendee decided on."""
    review_id: str
    r"""The recorded review."""
    decision: AttendeeDecision
    decided_by: str
    r"""Who decided: the member's external user id, or the API key's label, as the attendee's decided_by."""
    decided_at: str
    r"""When the decision was recorded; equal to the event's created_at."""


class AttendeeDecided(BaseModel):
    r"""A reviewer recorded a decision on an attendee. The decision's note stays in the API. Sent once per recorded review; an attendee's latest review is its decision, so order by decided_at."""

    event_id: str
    r"""The attendee's event."""

    attendee_id: str
    r"""The attendee decided on."""

    review_id: str
    r"""The recorded review."""

    decision: AttendeeDecision

    decided_by: str
    r"""Who decided: the member's external user id, or the API key's label, as the attendee's decided_by."""

    decided_at: str
    r"""When the decision was recorded; equal to the event's created_at."""
