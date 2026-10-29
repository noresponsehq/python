from __future__ import annotations
from noresponse.models.shared import customerexport as shared_customerexport
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class GetCustomerExportRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    export_id: str


class GetCustomerExportRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    export_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class GetCustomerExportResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_customerexport.CustomerExportTypedDict


class GetCustomerExportResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_customerexport.CustomerExport
