from __future__ import annotations
from noresponse.models.shared import workspacepeoplelist as shared_workspacepeoplelist
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListWorkspacePeopleRequestTypedDict(TypedDict):
    limit: NotRequired[int]
    after: NotRequired[str]
    r"""Pass next_cursor from the prior page."""
    email: NotRequired[str]
    r"""Return only people whose email is this address, compared without case or surrounding spaces."""
    phone: NotRequired[str]
    r"""Return only people whose phone is this number, compared without surrounding spaces."""


class ListWorkspacePeopleRequest(BaseModel):
    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 100

    after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Pass next_cursor from the prior page."""

    email: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Return only people whose email is this address, compared without case or surrounding spaces."""

    phone: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Return only people whose phone is this number, compared without surrounding spaces."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["limit", "after", "email", "phone"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


class ListWorkspacePeopleResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_workspacepeoplelist.WorkspacePeopleListTypedDict


class ListWorkspacePeopleResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_workspacepeoplelist.WorkspacePeopleList
