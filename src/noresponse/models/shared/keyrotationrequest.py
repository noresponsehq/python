from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class KeyRotationRequestTypedDict(TypedDict):
    r"""POST /v1/keys/rotate body. The tenant and the key being rotated are the API key that signs the request, so neither is a body member. An empty object takes the default overlap."""

    overlap_seconds: NotRequired[int]
    r"""How long the presented key keeps working beside the new one, from 60 seconds to 7 days. Default 86400 (24 hours). At the end of the overlap the presented key stops authenticating."""


class KeyRotationRequest(BaseModel):
    r"""POST /v1/keys/rotate body. The tenant and the key being rotated are the API key that signs the request, so neither is a body member. An empty object takes the default overlap."""

    overlap_seconds: Optional[int] = None
    r"""How long the presented key keeps working beside the new one, from 60 seconds to 7 days. Default 86400 (24 hours). At the end of the overlap the presented key stops authenticating."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["overlap_seconds"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
