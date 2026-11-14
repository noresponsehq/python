from __future__ import annotations
from .screeningcompleted import ScreeningCompleted, ScreeningCompletedTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ScreeningCompletedEventTypedDict(TypedDict):
    r"""The screening.completed event."""

    id: str
    r"""The event id, equal to the NR-Webhook-Id header and across redeliveries and every endpoint the event fans out to."""
    created_at: str
    r"""When the event was created. Equal across redeliveries; the signing timestamp header is per delivery."""
    data: ScreeningCompletedTypedDict
    r"""A screening of a group finished. It counts only the people this screening set out to reach, not who they are: read the roster with GET /v1/workspaces/{workspace_id}/groups/{environment}/{group_id}/people, filtered by band, to act on them. people_screened + partial_coverage = people_total, people_flagged is the sum of by_band, no_footprint counts screened people with no flag whose accounts were not found, and no_profile_to_check those the screening had nothing to look up for on any requested platform. A cancelled screening sends no event."""
    type: Literal["screening.completed"]
    r"""Always screening.completed."""
    test: NotRequired[bool]
    r"""Present, and true, only on an event sent by POST /v1/webhooks/{endpoint_id}/test: its data is a fixed example assessment, not one of the workspace's, so a receiver acknowledges it and applies nothing. Real events have no test member."""


class ScreeningCompletedEvent(BaseModel):
    r"""The screening.completed event."""

    id: str
    r"""The event id, equal to the NR-Webhook-Id header and across redeliveries and every endpoint the event fans out to."""

    created_at: str
    r"""When the event was created. Equal across redeliveries; the signing timestamp header is per delivery."""

    data: ScreeningCompleted
    r"""A screening of a group finished. It counts only the people this screening set out to reach, not who they are: read the roster with GET /v1/workspaces/{workspace_id}/groups/{environment}/{group_id}/people, filtered by band, to act on them. people_screened + partial_coverage = people_total, people_flagged is the sum of by_band, no_footprint counts screened people with no flag whose accounts were not found, and no_profile_to_check those the screening had nothing to look up for on any requested platform. A cancelled screening sends no event."""

    type: Annotated[
        Annotated[
            Literal["screening.completed"],
            AfterValidator(validate_const("screening.completed")),
        ],
        pydantic.Field(alias="type"),
    ] = "screening.completed"
    r"""Always screening.completed."""

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
    ScreeningCompletedEvent.model_rebuild()
except NameError:
    pass
