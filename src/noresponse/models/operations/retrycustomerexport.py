from __future__ import annotations
from noresponse.models.shared import (
    customerexport as shared_customerexport,
    customerexportactionrequest as shared_customerexportactionrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class RetryCustomerExportRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    export_id: str
    body: shared_customerexportactionrequest.CustomerExportActionRequestTypedDict


class RetryCustomerExportRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    export_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    body: Annotated[
        shared_customerexportactionrequest.CustomerExportActionRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class RetryCustomerExportResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_customerexport.CustomerExportTypedDict


class RetryCustomerExportResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_customerexport.CustomerExport
