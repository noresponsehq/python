from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class OperationalAggregateBucketTypedDict(TypedDict):
    start: str
    attempts: int
    succeeded: int
    failed: int
    client_errors: int
    server_errors: int
    replays: int
    incomplete_writes: int
    unattributed_keys: int
    p50_ms: NotRequired[float]
    r"""Continuous percentile over retained attempts. Omitted when there are no captured samples."""
    p95_ms: NotRequired[float]
    r"""Continuous percentile over retained attempts. Omitted when there are no captured samples."""
    p99_ms: NotRequired[float]
    r"""Continuous percentile over retained attempts. Omitted when there are no captured samples."""


class OperationalAggregateBucket(BaseModel):
    start: str

    attempts: int

    succeeded: int

    failed: int

    client_errors: int

    server_errors: int

    replays: int

    incomplete_writes: int

    unattributed_keys: int

    p50_ms: Optional[float] = None
    r"""Continuous percentile over retained attempts. Omitted when there are no captured samples."""

    p95_ms: Optional[float] = None
    r"""Continuous percentile over retained attempts. Omitted when there are no captured samples."""

    p99_ms: Optional[float] = None
    r"""Continuous percentile over retained attempts. Omitted when there are no captured samples."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["p50_ms", "p95_ms", "p99_ms"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
