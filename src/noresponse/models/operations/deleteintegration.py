from __future__ import annotations
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class DeleteIntegrationRequestTypedDict(TypedDict):
    integration_id: str
    r"""Path segment, matched case-sensitively. A value that does not match the integration_id shape, or another tenant's id, answers 404."""


class DeleteIntegrationRequest(BaseModel):
    integration_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Path segment, matched case-sensitively. A value that does not match the integration_id shape, or another tenant's id, answers 404."""


class DeleteIntegrationResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]


class DeleteIntegrationResponse(BaseModel):
    headers: Dict[str, List[str]]
