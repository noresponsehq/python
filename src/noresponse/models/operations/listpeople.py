from __future__ import annotations
from noresponse.models.shared import (
    keyenvironment as shared_keyenvironment,
    listpeopleband as shared_listpeopleband,
    listpeopledecision as shared_listpeopledecision,
    listpeoplerole as shared_listpeoplerole,
    personlist as shared_personlist,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListPeopleRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    environment: shared_keyenvironment.KeyEnvironment
    r"""The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404."""
    group_id: str
    limit: NotRequired[int]
    r"""At most this many people."""
    after: NotRequired[str]
    r"""Read people after this one."""
    band: NotRequired[shared_listpeopleband.ListPeopleBand]
    r"""Only people whose highest finding has this band; none for people with no finding."""
    decision: NotRequired[shared_listpeopledecision.ListPeopleDecision]
    r"""Only people with this decision; undecided for none yet."""
    role: NotRequired[shared_listpeoplerole.ListPeopleRole]
    r"""Only people with this role; unstated for people whose role was not given."""


class ListPeopleRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    environment: Annotated[
        shared_keyenvironment.KeyEnvironment,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404."""

    group_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 100
    r"""At most this many people."""

    after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Read people after this one."""

    band: Annotated[
        Optional[shared_listpeopleband.ListPeopleBand],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Only people whose highest finding has this band; none for people with no finding."""

    decision: Annotated[
        Optional[shared_listpeopledecision.ListPeopleDecision],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Only people with this decision; undecided for none yet."""

    role: Annotated[
        Optional[shared_listpeoplerole.ListPeopleRole],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Only people with this role; unstated for people whose role was not given."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["limit", "after", "band", "decision", "role"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


class ListPeopleResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_personlist.PersonListTypedDict


class ListPeopleResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_personlist.PersonList
