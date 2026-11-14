from __future__ import annotations
from .persondecision import PersonDecision
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class PersonDecidedTypedDict(TypedDict):
    r"""A reviewer recorded a decision on a person. The decision's note stays in the API. Sent once per recorded review; a person's latest review is its decision, so order by decided_at."""

    group_id: str
    r"""The person's group."""
    person_id: str
    r"""The person decided on."""
    review_id: str
    r"""The recorded review."""
    decision: PersonDecision
    decided_by: str
    r"""Who decided: the member's external user id, or the API key's label, as the person's decided_by."""
    decided_at: str
    r"""When the decision was recorded; equal to the event's created_at."""


class PersonDecided(BaseModel):
    r"""A reviewer recorded a decision on a person. The decision's note stays in the API. Sent once per recorded review; a person's latest review is its decision, so order by decided_at."""

    group_id: str
    r"""The person's group."""

    person_id: str
    r"""The person decided on."""

    review_id: str
    r"""The recorded review."""

    decision: PersonDecision

    decided_by: str
    r"""Who decided: the member's external user id, or the API key's label, as the person's decided_by."""

    decided_at: str
    r"""When the decision was recorded; equal to the event's created_at."""
