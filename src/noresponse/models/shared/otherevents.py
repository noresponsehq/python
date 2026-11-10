from __future__ import annotations
from .otherevent import OtherEvent, OtherEventTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class OtherEventsTypedDict(TypedDict):
    r"""Where else in the environment the attendee appears, read live from those events: deleting one removes it here."""

    total: int
    r"""How many attendees of other events match, of which items lists the 20 most recent."""
    items: List[OtherEventTypedDict]
    r"""The 20 attendees of the most recent other events, newest event first."""


class OtherEvents(BaseModel):
    r"""Where else in the environment the attendee appears, read live from those events: deleting one removes it here."""

    total: int
    r"""How many attendees of other events match, of which items lists the 20 most recent."""

    items: List[OtherEvent]
    r"""The 20 attendees of the most recent other events, newest event first."""
