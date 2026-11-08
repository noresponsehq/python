from __future__ import annotations
from noresponse.models.shared import (
    attendeelist as shared_attendeelist,
    keyenvironment as shared_keyenvironment,
    listattendeesband as shared_listattendeesband,
    listattendeesdecision as shared_listattendeesdecision,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListAttendeesRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    environment: shared_keyenvironment.KeyEnvironment
    r"""The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404."""
    event_id: str
    limit: NotRequired[int]
    r"""At most this many attendees."""
    after: NotRequired[str]
    r"""Read attendees after this one."""
    band: NotRequired[shared_listattendeesband.ListAttendeesBand]
    r"""Only attendees whose highest finding has this band; none for attendees with no finding."""
    decision: NotRequired[shared_listattendeesdecision.ListAttendeesDecision]
    r"""Only attendees with this decision; undecided for none yet."""


class ListAttendeesRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    environment: Annotated[
        shared_keyenvironment.KeyEnvironment,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404."""

    event_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 100
    r"""At most this many attendees."""

    after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Read attendees after this one."""

    band: Annotated[
        Optional[shared_listattendeesband.ListAttendeesBand],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Only attendees whose highest finding has this band; none for attendees with no finding."""

    decision: Annotated[
        Optional[shared_listattendeesdecision.ListAttendeesDecision],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Only attendees with this decision; undecided for none yet."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["limit", "after", "band", "decision"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


class ListAttendeesResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_attendeelist.AttendeeListTypedDict


class ListAttendeesResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_attendeelist.AttendeeList
