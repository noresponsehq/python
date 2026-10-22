from __future__ import annotations
from noresponse.models.shared import webhookendpointlist as shared_webhookendpointlist
from noresponse.types import BaseModel
from typing import Dict, List
from typing_extensions import TypedDict


class ListWebhookEndpointsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_webhookendpointlist.WebhookEndpointListTypedDict


class ListWebhookEndpointsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_webhookendpointlist.WebhookEndpointList
