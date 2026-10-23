from __future__ import annotations
from noresponse.models.shared import (
    integration as shared_integration,
    integrationrotationrequest as shared_integrationrotationrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class RotateIntegrationSecretRequestTypedDict(TypedDict):
    integration_id: str
    r"""Path segment, matched case-sensitively. A value that does not match the integration_id shape, or another workspace's id, answers 404."""
    body: shared_integrationrotationrequest.IntegrationRotationRequestTypedDict


class RotateIntegrationSecretRequest(BaseModel):
    integration_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Path segment, matched case-sensitively. A value that does not match the integration_id shape, or another workspace's id, answers 404."""

    body: Annotated[
        shared_integrationrotationrequest.IntegrationRotationRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class RotateIntegrationSecretResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_integration.IntegrationTypedDict


class RotateIntegrationSecretResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_integration.Integration
