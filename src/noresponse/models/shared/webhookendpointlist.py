from __future__ import annotations
from .webhookendpoint import WebhookEndpoint, WebhookEndpointTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class WebhookEndpointListTypedDict(TypedDict):
    r"""GET /v1/webhooks answer: every endpoint of the calling workspace, in every state, ordered by endpoint_id. A workspace holds at most 5, so there is no page."""

    items: List[WebhookEndpointTypedDict]


class WebhookEndpointList(BaseModel):
    r"""GET /v1/webhooks answer: every endpoint of the calling workspace, in every state, ordered by endpoint_id. A workspace holds at most 5, so there is no page."""

    items: List[WebhookEndpoint]
