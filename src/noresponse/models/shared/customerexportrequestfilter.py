from __future__ import annotations
from .customerexportrequestfilteroutcome import CustomerExportRequestFilterOutcome
from .environment import Environment
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CustomerExportRequestFilterTypedDict(TypedDict):
    action: NotRequired[str]
    actor: NotRequired[str]
    target_type: NotRequired[str]
    target_id: NotRequired[str]
    environment: NotRequired[Environment]
    outcome: NotRequired[CustomerExportRequestFilterOutcome]
    since: NotRequired[str]
    until: NotRequired[str]


class CustomerExportRequestFilter(BaseModel):
    action: Optional[str] = None

    actor: Optional[str] = None

    target_type: Optional[str] = None

    target_id: Optional[str] = None

    environment: Optional[Environment] = None

    outcome: Optional[CustomerExportRequestFilterOutcome] = None

    since: Optional[str] = None

    until: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "action",
                "actor",
                "target_type",
                "target_id",
                "environment",
                "outcome",
                "since",
                "until",
            ]
        )
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
