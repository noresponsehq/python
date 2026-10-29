from __future__ import annotations
from .erasurereceiptkind import ErasureReceiptKind
from .erasurereceipttarget import ErasureReceiptTarget, ErasureReceiptTargetTypedDict
from .listchangestate import ListChangeState
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ErasureReceiptTypedDict(TypedDict):
    r"""Acknowledged propagation of a retained erasure record in the calling environment. Pending means the target has not acknowledged completion. Completion covers these serving-system targets only; backup and point-in-time recovery copies expire according to their own retention policy. This receipt contains no subject id or digest. Workspace teardown revokes customer credentials, so obtain required receipts before teardown."""

    id: str
    r"""Opaque, server-issued erasure receipt id. It contains no subject identifier."""
    kind: ErasureReceiptKind
    status: ListChangeState
    assessments_deleted: int
    requested_at: str
    targets: List[ErasureReceiptTargetTypedDict]
    backup_policy: str
    completed_at: NotRequired[str]


class ErasureReceipt(BaseModel):
    r"""Acknowledged propagation of a retained erasure record in the calling environment. Pending means the target has not acknowledged completion. Completion covers these serving-system targets only; backup and point-in-time recovery copies expire according to their own retention policy. This receipt contains no subject id or digest. Workspace teardown revokes customer credentials, so obtain required receipts before teardown."""

    id: str
    r"""Opaque, server-issued erasure receipt id. It contains no subject identifier."""

    kind: ErasureReceiptKind

    status: ListChangeState

    assessments_deleted: int

    requested_at: str

    targets: List[ErasureReceiptTarget]

    backup_policy: str

    completed_at: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["completed_at"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
