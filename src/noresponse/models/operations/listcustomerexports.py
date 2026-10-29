from __future__ import annotations
from noresponse.models.shared import (
    customerexportlist as shared_customerexportlist,
    customerexportrequestkind as shared_customerexportrequestkind,
    environment as shared_environment,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Awaitable, Callable, Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class ListCustomerExportsRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    kind: shared_customerexportrequestkind.CustomerExportRequestKind
    environment: shared_environment.Environment
    limit: NotRequired[int]
    cursor: NotRequired[str]


class ListCustomerExportsRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    kind: Annotated[
        shared_customerexportrequestkind.CustomerExportRequestKind,
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]

    environment: Annotated[
        shared_environment.Environment,
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 25

    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["limit", "cursor"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


class ListCustomerExportsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_customerexportlist.CustomerExportListTypedDict


class ListCustomerExportsResponse(BaseModel):
    next: Union[
        Callable[[], Optional[ListCustomerExportsResponse]],
        Callable[[], Awaitable[Optional[ListCustomerExportsResponse]]],
    ]

    headers: Dict[str, List[str]]

    result: shared_customerexportlist.CustomerExportList
