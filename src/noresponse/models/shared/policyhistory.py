from __future__ import annotations
from .policyhistoryitem import PolicyHistoryItem, PolicyHistoryItemTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PolicyHistoryTypedDict(TypedDict):
    r"""Immutable settings snapshots, newest first. history_complete is false when earlier versions predate capture. A restored version is published with a fresh version number. History is removed with the tenant."""

    items: List[PolicyHistoryItemTypedDict]
    has_more: bool
    history_complete: bool
    next_before_version: NotRequired[int]


class PolicyHistory(BaseModel):
    r"""Immutable settings snapshots, newest first. history_complete is false when earlier versions predate capture. A restored version is published with a fresh version number. History is removed with the tenant."""

    items: List[PolicyHistoryItem]

    has_more: bool

    history_complete: bool

    next_before_version: Optional[int] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["next_before_version"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
