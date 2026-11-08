from __future__ import annotations
from .attendeeflagged import AttendeeFlagged, AttendeeFlaggedTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AttendeeFlaggedEventTypedDict(TypedDict):
    r"""The attendee.flagged event."""

    id: str
    r"""The event id, equal to the NR-Webhook-Id header and across redeliveries and every endpoint the event fans out to."""
    created_at: str
    r"""When the event was created. Equal across redeliveries; the signing timestamp header is per delivery."""
    data: AttendeeFlaggedTypedDict
    r"""A screening recorded a finding on an attendee. It says which attendee and how severe, not what they posted, who they are or why: GET the attendee report for the findings. Sent once per screening that flags the attendee, so a re-screen of someone on watch announces them again."""
    type: Literal["attendee.flagged"]
    r"""Always attendee.flagged."""
    test: NotRequired[bool]
    r"""Present, and true, only on an event sent by POST /v1/webhooks/{endpoint_id}/test: its data is a fixed example assessment, not one of the workspace's, so a receiver acknowledges it and applies nothing. Real events have no test member."""


class AttendeeFlaggedEvent(BaseModel):
    r"""The attendee.flagged event."""

    id: str
    r"""The event id, equal to the NR-Webhook-Id header and across redeliveries and every endpoint the event fans out to."""

    created_at: str
    r"""When the event was created. Equal across redeliveries; the signing timestamp header is per delivery."""

    data: AttendeeFlagged
    r"""A screening recorded a finding on an attendee. It says which attendee and how severe, not what they posted, who they are or why: GET the attendee report for the findings. Sent once per screening that flags the attendee, so a re-screen of someone on watch announces them again."""

    type: Annotated[
        Annotated[
            Literal["attendee.flagged"],
            AfterValidator(validate_const("attendee.flagged")),
        ],
        pydantic.Field(alias="type"),
    ] = "attendee.flagged"
    r"""Always attendee.flagged."""

    test: Optional[bool] = None
    r"""Present, and true, only on an event sent by POST /v1/webhooks/{endpoint_id}/test: its data is a fixed example assessment, not one of the workspace's, so a receiver acknowledges it and applies nothing. Real events have no test member."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["test"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


try:
    AttendeeFlaggedEvent.model_rebuild()
except NameError:
    pass
