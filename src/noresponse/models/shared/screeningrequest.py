from __future__ import annotations
from .screeningdepth import ScreeningDepth
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ScreeningRequestTypedDict(TypedDict):
    r"""Screens the group's people no screening has reached and everyone on watch or escalated."""

    depth: ScreeningDepth
    platforms: NotRequired[List[str]]
    r"""The platforms to search. Leave it out for a full search: every platform a connector serves in the environment when the screening starts, which the screening then lists."""


class ScreeningRequest(BaseModel):
    r"""Screens the group's people no screening has reached and everyone on watch or escalated."""

    depth: ScreeningDepth

    platforms: Optional[List[str]] = None
    r"""The platforms to search. Leave it out for a full search: every platform a connector serves in the environment when the screening starts, which the screening then lists."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["platforms"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
