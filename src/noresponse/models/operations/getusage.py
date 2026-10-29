from __future__ import annotations
from noresponse.models.shared import usage as shared_usage
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetUsageRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    from_: NotRequired[str]
    r"""The first UTC day, as YYYY-MM-DD."""
    to: NotRequired[str]
    r"""The last UTC day, included, as YYYY-MM-DD; no later than today."""


class GetUsageRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    from_: Annotated[
        Optional[str],
        pydantic.Field(alias="from"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The first UTC day, as YYYY-MM-DD."""

    to: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The last UTC day, included, as YYYY-MM-DD; no later than today."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["from", "to"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


class GetUsageResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_usage.UsageTypedDict


class GetUsageResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_usage.Usage
