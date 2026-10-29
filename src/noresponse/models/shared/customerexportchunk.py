from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CustomerExportChunkTypedDict(TypedDict):
    r"""Download one authorized export chunk."""

    export_id: str
    index: int
    generation: int
    sha256: str
    data: str
    r"""Base64-encoded UTF-8 JSON Lines, at most 256 KiB decoded. Each line is a typed customer export record. Decode and concatenate chunks in index order within the same generation."""
    next_chunk: NotRequired[int]


class CustomerExportChunk(BaseModel):
    r"""Download one authorized export chunk."""

    export_id: str

    index: int

    generation: int

    sha256: str

    data: str
    r"""Base64-encoded UTF-8 JSON Lines, at most 256 KiB decoded. Each line is a typed customer export record. Decode and concatenate chunks in index order within the same generation."""

    next_chunk: Optional[int] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["next_chunk"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
