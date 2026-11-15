from __future__ import annotations
from .investigationcompletedstatus import InvestigationCompletedStatus
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class InvestigationCompletedTypedDict(TypedDict):
    investigation_id: str
    person_id: str
    status: InvestigationCompletedStatus
    finished_at: str
    error_code: NotRequired[str]


class InvestigationCompleted(BaseModel):
    investigation_id: str

    person_id: str

    status: InvestigationCompletedStatus

    finished_at: str

    error_code: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["error_code"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
