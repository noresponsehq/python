from __future__ import annotations
from noresponse.models.shared import (
    webhooktest as shared_webhooktest,
    webhooktestrequest as shared_webhooktestrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class SendWebhookTestEventRequestTypedDict(TypedDict):
    endpoint_id: str
    r"""The endpoint's whe_ id. An id that is unknown, malformed or another tenant's answers 404."""
    body: shared_webhooktestrequest.WebhookTestRequestTypedDict


class SendWebhookTestEventRequest(BaseModel):
    endpoint_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The endpoint's whe_ id. An id that is unknown, malformed or another tenant's answers 404."""

    body: Annotated[
        shared_webhooktestrequest.WebhookTestRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class SendWebhookTestEventResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_webhooktest.WebhookTestTypedDict


class SendWebhookTestEventResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_webhooktest.WebhookTest
