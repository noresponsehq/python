from __future__ import annotations
from .auditstream import AuditStream, AuditStreamTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class AuditStreamListTypedDict(TypedDict):
    r"""Read audit stream subscriptions."""

    items: List[AuditStreamTypedDict]


class AuditStreamList(BaseModel):
    r"""Read audit stream subscriptions."""

    items: List[AuditStream]
