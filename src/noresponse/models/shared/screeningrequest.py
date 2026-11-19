from __future__ import annotations
from .screeningdepth import ScreeningDepth
from noresponse.types import BaseModel, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ScreeningRequestTypedDict(TypedDict):
    r"""Screens the group's people no screening has reached."""

    depth: ScreeningDepth
    platforms: NotRequired[List[str]]
    r"""Deprecated: leave it out. Without it the screening is a full search: every platform a connector serves in the environment when the screening starts, which the screening then lists, each searched only with the identifiers its connector takes. A list sent here still limits the screening until a later contract release removes the field."""


class ScreeningRequest(BaseModel):
    r"""Screens the group's people no screening has reached."""

    depth: ScreeningDepth

    platforms: Annotated[
        Optional[List[str]],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = None
    r"""Deprecated: leave it out. Without it the screening is a full search: every platform a connector serves in the environment when the screening starts, which the screening then lists, each searched only with the identifiers its connector takes. A list sent here still limits the screening until a later contract release removes the field."""

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
