from __future__ import annotations
from .persondecided import PersonDecided, PersonDecidedTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PersonDecidedEventTypedDict(TypedDict):
    r"""The person.decided event."""

    id: str
    r"""The event id, equal to the NR-Webhook-Id header and across redeliveries and every endpoint the event fans out to."""
    created_at: str
    r"""When the event was created. Equal across redeliveries; the signing timestamp header is per delivery."""
    data: PersonDecidedTypedDict
    r"""A reviewer recorded a decision on a person. The decision's note stays in the API. Sent once per recorded review; a person's latest review is its decision, so order by decided_at."""
    type: Literal["person.decided"]
    r"""Always person.decided."""
    test: NotRequired[bool]
    r"""Present, and true, only on an event sent by POST /v1/webhooks/{endpoint_id}/test: its data is a fixed example assessment, not one of the workspace's, so a receiver acknowledges it and applies nothing. Real events have no test member."""


class PersonDecidedEvent(BaseModel):
    r"""The person.decided event."""

    id: str
    r"""The event id, equal to the NR-Webhook-Id header and across redeliveries and every endpoint the event fans out to."""

    created_at: str
    r"""When the event was created. Equal across redeliveries; the signing timestamp header is per delivery."""

    data: PersonDecided
    r"""A reviewer recorded a decision on a person. The decision's note stays in the API. Sent once per recorded review; a person's latest review is its decision, so order by decided_at."""

    type: Annotated[
        Annotated[
            Literal["person.decided"], AfterValidator(validate_const("person.decided"))
        ],
        pydantic.Field(alias="type"),
    ] = "person.decided"
    r"""Always person.decided."""

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
    PersonDecidedEvent.model_rebuild()
except NameError:
    pass
