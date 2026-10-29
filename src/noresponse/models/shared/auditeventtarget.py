from __future__ import annotations
from .auditeventtargettype import AuditEventTargetType
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AuditEventTargetTypedDict(TypedDict):
    type: AuditEventTargetType
    r"""The kind of resource the change acted on."""
    id: NotRequired[str]
    r"""The resource's id, when it has one."""


class AuditEventTarget(BaseModel):
    type: AuditEventTargetType
    r"""The kind of resource the change acted on."""

    id: Optional[str] = None
    r"""The resource's id, when it has one."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["id"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
