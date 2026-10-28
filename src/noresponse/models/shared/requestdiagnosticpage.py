from __future__ import annotations
from .requestdiagnostic import RequestDiagnostic, RequestDiagnosticTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class RequestDiagnosticPageTypedDict(TypedDict):
    r"""Authenticated attempts in a bounded interval, newest first. Keep the same filters when paging."""

    items: List[RequestDiagnosticTypedDict]
    next_cursor: NotRequired[str]


class RequestDiagnosticPage(BaseModel):
    r"""Authenticated attempts in a bounded interval, newest first. Keep the same filters when paging."""

    items: List[RequestDiagnostic]

    next_cursor: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["next_cursor"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
