from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class AuditStreamReplayRequestTypedDict(TypedDict):
    event_id: str
    r"""Opaque, workspace-scoped webhook event id. A redelivery of the same event carries the same event_id, so consumers deduplicate on it."""


class AuditStreamReplayRequest(BaseModel):
    event_id: str
    r"""Opaque, workspace-scoped webhook event id. A redelivery of the same event carries the same event_id, so consumers deduplicate on it."""
