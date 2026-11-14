from __future__ import annotations
from noresponse.models.shared import (
    grouplist as shared_grouplist,
    keyenvironment as shared_keyenvironment,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListGroupsRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    environment: shared_keyenvironment.KeyEnvironment
    r"""The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404."""
    limit: NotRequired[int]
    r"""At most this many items."""
    before: NotRequired[str]
    r"""Read groups older than this one."""


class ListGroupsRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    environment: Annotated[
        shared_keyenvironment.KeyEnvironment,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404."""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 20
    r"""At most this many items."""

    before: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Read groups older than this one."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["limit", "before"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


class ListGroupsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_grouplist.GroupListTypedDict


class ListGroupsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_grouplist.GroupList
