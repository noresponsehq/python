from __future__ import annotations
from noresponse.models.shared import (
    webhookendpointcreated as shared_webhookendpointcreated,
)
from noresponse.types import BaseModel
from typing import Dict, List
from typing_extensions import TypedDict


class CreateWebhookEndpointResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_webhookendpointcreated.WebhookEndpointCreatedTypedDict


class CreateWebhookEndpointResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_webhookendpointcreated.WebhookEndpointCreated
