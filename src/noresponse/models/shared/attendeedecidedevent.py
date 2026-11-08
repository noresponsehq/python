from __future__ import annotations
from .attendeedecided import AttendeeDecided, AttendeeDecidedTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AttendeeDecidedEventTypedDict(TypedDict):
    r"""The attendee.decided event."""

    id: str
    r"""The event id, equal to the NR-Webhook-Id header and across redeliveries and every endpoint the event fans out to."""
    created_at: str
    r"""When the event was created. Equal across redeliveries; the signing timestamp header is per delivery."""
    data: AttendeeDecidedTypedDict
    r"""A reviewer recorded a decision on an attendee. The decision's note stays in the API. Sent once per recorded review; an attendee's latest review is its decision, so order by decided_at."""
    type: Literal["attendee.decided"]
    r"""Always attendee.decided."""
    test: NotRequired[bool]
    r"""Present, and true, only on an event sent by POST /v1/webhooks/{endpoint_id}/test: its data is a fixed example assessment, not one of the workspace's, so a receiver acknowledges it and applies nothing. Real events have no test member."""


class AttendeeDecidedEvent(BaseModel):
    r"""The attendee.decided event."""

    id: str
    r"""The event id, equal to the NR-Webhook-Id header and across redeliveries and every endpoint the event fans out to."""

    created_at: str
    r"""When the event was created. Equal across redeliveries; the signing timestamp header is per delivery."""

    data: AttendeeDecided
    r"""A reviewer recorded a decision on an attendee. The decision's note stays in the API. Sent once per recorded review; an attendee's latest review is its decision, so order by decided_at."""

    type: Annotated[
        Annotated[
            Literal["attendee.decided"],
            AfterValidator(validate_const("attendee.decided")),
        ],
        pydantic.Field(alias="type"),
    ] = "attendee.decided"
    r"""Always attendee.decided."""

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
    AttendeeDecidedEvent.model_rebuild()
except NameError:
    pass
