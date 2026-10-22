from __future__ import annotations
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class DeleteWebhookEndpointRequestTypedDict(TypedDict):
    endpoint_id: str
    r"""The endpoint's whe_ id. An id that is unknown, malformed or another tenant's answers 404."""


class DeleteWebhookEndpointRequest(BaseModel):
    endpoint_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The endpoint's whe_ id. An id that is unknown, malformed or another tenant's answers 404."""


class DeleteWebhookEndpointResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]


class DeleteWebhookEndpointResponse(BaseModel):
    headers: Dict[str, List[str]]
