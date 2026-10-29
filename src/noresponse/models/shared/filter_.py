from __future__ import annotations
from .priority import Priority
from .reviewstatus import ReviewStatus
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class FilterTypedDict(TypedDict):
    status: NotRequired[ReviewStatus]
    priority: NotRequired[Priority]
    assignee: NotRequired[str]
    unassigned: NotRequired[bool]
    assignee_principal_id: NotRequired[str]


class Filter(BaseModel):
    status: Optional[ReviewStatus] = None

    priority: Optional[Priority] = None

    assignee: Optional[str] = None

    unassigned: Optional[bool] = None

    assignee_principal_id: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            ["status", "priority", "assignee", "unassigned", "assignee_principal_id"]
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
