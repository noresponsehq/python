from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class WebhookKeyRotationRequestTypedDict(TypedDict):
    r"""POST /v1/webhooks/{endpoint_id}/rotate body: an empty object. The old key keeps verifying for 7 days."""


class WebhookKeyRotationRequest(BaseModel):
    r"""POST /v1/webhooks/{endpoint_id}/rotate body: an empty object. The old key keeps verifying for 7 days."""
