from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class AuditSettingsRequestTypedDict(TypedDict):
    retention_days: int


class AuditSettingsRequest(BaseModel):
    retention_days: int
