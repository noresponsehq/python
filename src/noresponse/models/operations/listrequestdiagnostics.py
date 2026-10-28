from __future__ import annotations
from noresponse.models.shared import (
    requestdiagnosticpage as shared_requestdiagnosticpage,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListRequestDiagnosticsRequestTypedDict(TypedDict):
    from_: str
    r"""Inclusive start of a range of at most seven days."""
    to: str
    r"""Exclusive end of the range."""
    request_id: NotRequired[str]
    r"""Optional filter or paging parameter."""
    route: NotRequired[str]
    r"""Optional filter or paging parameter."""
    status: NotRequired[int]
    r"""Optional filter or paging parameter."""
    limit: NotRequired[int]
    r"""Optional filter or paging parameter."""
    cursor: NotRequired[str]
    r"""Optional filter or paging parameter."""


class ListRequestDiagnosticsRequest(BaseModel):
    from_: Annotated[
        str,
        pydantic.Field(alias="from"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Inclusive start of a range of at most seven days."""

    to: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Exclusive end of the range."""

    request_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional filter or paging parameter."""

    route: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional filter or paging parameter."""

    status: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional filter or paging parameter."""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 50
    r"""Optional filter or paging parameter."""

    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional filter or paging parameter."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["request_id", "route", "status", "limit", "cursor"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


class ListRequestDiagnosticsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_requestdiagnosticpage.RequestDiagnosticPageTypedDict


class ListRequestDiagnosticsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_requestdiagnosticpage.RequestDiagnosticPage
