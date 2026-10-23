from __future__ import annotations
from noresponse.models.shared import (
    webhookreplay as shared_webhookreplay,
    webhookreplayrequest as shared_webhookreplayrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class ReplayWebhookDeliveryRequestTypedDict(TypedDict):
    endpoint_id: str
    r"""The endpoint's whe_ id. An id that is unknown, malformed or another workspace's answers 404."""
    event_id: str
    r"""The evt_ id of a delivery the endpoint's log holds, as GET /v1/webhooks/{endpoint_id}/deliveries lists it. An id that is malformed, not sent to this endpoint, past the log's retention or another workspace's answers 404."""
    body: shared_webhookreplayrequest.WebhookReplayRequestTypedDict


class ReplayWebhookDeliveryRequest(BaseModel):
    endpoint_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The endpoint's whe_ id. An id that is unknown, malformed or another workspace's answers 404."""

    event_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The evt_ id of a delivery the endpoint's log holds, as GET /v1/webhooks/{endpoint_id}/deliveries lists it. An id that is malformed, not sent to this endpoint, past the log's retention or another workspace's answers 404."""

    body: Annotated[
        shared_webhookreplayrequest.WebhookReplayRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class ReplayWebhookDeliveryResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_webhookreplay.WebhookReplayTypedDict


class ReplayWebhookDeliveryResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_webhookreplay.WebhookReplay
