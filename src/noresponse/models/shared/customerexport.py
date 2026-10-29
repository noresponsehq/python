from __future__ import annotations
from .customerexportrequestkind import CustomerExportRequestKind
from .customerexportstatus import CustomerExportStatus
from .environment import Environment
from .responsemode import ResponseMode
from noresponse.types import BaseModel, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CustomerExportTypedDict(TypedDict):
    r"""Request an asynchronous customer export."""

    id: str
    kind: CustomerExportRequestKind
    environment: Environment
    response_mode: ResponseMode
    r"""standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode."""
    status: CustomerExportStatus
    created_at: str
    expires_at: str
    records: int
    bytes_: int
    chunks: int
    attempts: int
    generation: int
    request_sha256: str
    snapshot_at: NotRequired[str]
    finished_at: NotRequired[str]
    error_code: NotRequired[str]


class CustomerExport(BaseModel):
    r"""Request an asynchronous customer export."""

    id: str

    kind: CustomerExportRequestKind

    environment: Environment

    response_mode: ResponseMode
    r"""standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode."""

    status: CustomerExportStatus

    created_at: str

    expires_at: str

    records: int

    bytes_: Annotated[int, pydantic.Field(alias="bytes")]

    chunks: int

    attempts: int

    generation: int

    request_sha256: str

    snapshot_at: Optional[str] = None

    finished_at: Optional[str] = None

    error_code: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["snapshot_at", "finished_at", "error_code"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


try:
    CustomerExport.model_rebuild()
except NameError:
    pass
