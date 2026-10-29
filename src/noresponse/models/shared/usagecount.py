from __future__ import annotations
from .auditsettingsenvironment import AuditSettingsEnvironment
from .metric import Metric
from .usagecountdepth import UsageCountDepth
from .usagecountflow import UsageCountFlow
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class UsageCountTypedDict(TypedDict):
    environment: AuditSettingsEnvironment
    day: str
    metric: Metric
    r"""assessments: assessments admitted. webhook_deliveries: events sent to endpoints, one per event per endpoint. key_usage_events: key-usage events accepted."""
    count: int
    flow: NotRequired[UsageCountFlow]
    r"""assessments only."""
    depth: NotRequired[UsageCountDepth]
    r"""assessments only."""


class UsageCount(BaseModel):
    environment: AuditSettingsEnvironment

    day: str

    metric: Metric
    r"""assessments: assessments admitted. webhook_deliveries: events sent to endpoints, one per event per endpoint. key_usage_events: key-usage events accepted."""

    count: int

    flow: Optional[UsageCountFlow] = None
    r"""assessments only."""

    depth: Optional[UsageCountDepth] = None
    r"""assessments only."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["flow", "depth"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
