from __future__ import annotations
from noresponse.models.shared import (
    customerexport as shared_customerexport,
    customerexportrequest as shared_customerexportrequest,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateCustomerExportRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    body: shared_customerexportrequest.CustomerExportRequestTypedDict
    idempotency_key: NotRequired[str]


class CreateCustomerExportRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    body: Annotated[
        shared_customerexportrequest.CustomerExportRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    idempotency_key: Annotated[
        Optional[str],
        pydantic.Field(alias="Idempotency-Key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["Idempotency-Key"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


class CreateCustomerExportResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_customerexport.CustomerExportTypedDict


class CreateCustomerExportResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_customerexport.CustomerExport
