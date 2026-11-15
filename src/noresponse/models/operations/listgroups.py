from __future__ import annotations
from noresponse.models.shared import grouplist as shared_grouplist
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListGroupsRequestTypedDict(TypedDict):
    limit: NotRequired[int]
    r"""At most this many items."""
    before: NotRequired[str]
    r"""Read groups older than this one."""


class ListGroupsRequest(BaseModel):
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
