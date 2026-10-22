from __future__ import annotations
from noresponse.models.shared import (
    webhookkeyrotation as shared_webhookkeyrotation,
    webhookkeyrotationrequest as shared_webhookkeyrotationrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class RotateWebhookSigningKeyRequestTypedDict(TypedDict):
    endpoint_id: str
    r"""The endpoint's whe_ id. An id that is unknown, malformed or another tenant's answers 404."""
    body: shared_webhookkeyrotationrequest.WebhookKeyRotationRequestTypedDict


class RotateWebhookSigningKeyRequest(BaseModel):
    endpoint_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The endpoint's whe_ id. An id that is unknown, malformed or another tenant's answers 404."""

    body: Annotated[
        shared_webhookkeyrotationrequest.WebhookKeyRotationRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class RotateWebhookSigningKeyResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_webhookkeyrotation.WebhookKeyRotationTypedDict


class RotateWebhookSigningKeyResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_webhookkeyrotation.WebhookKeyRotation
