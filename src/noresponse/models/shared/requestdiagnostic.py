from __future__ import annotations
from .decisionreceipt import DecisionReceipt, DecisionReceiptTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RequestDiagnosticTypedDict(TypedDict):
    r"""One authenticated HTTP attempt. An attempt id is independent of the caller correlation id. No raw body, path parameter, credential or source payload is retained. write_complete means the server wrote/flushed its response, not proof the client processed it. Collection is bounded best effort; ii_signup_request_diagnostic_failures_total exposes gaps. Retained for seven days or the shorter environment retention."""

    id: str
    request_id: str
    route: str
    http_status: int
    duration_ms: int
    started_at: str
    completed_at: str
    expires_at: str
    idempotent_replayed: bool
    write_complete: bool
    error_code: NotRequired[str]
    decision: NotRequired[DecisionReceiptTypedDict]
    r"""The decision prepared for one HTTP attempt. Its account field preserves the account decision returned for that attempt, even after subsequent changes."""
    api_key_id: NotRequired[str]
    r"""Public authenticated API key identifier. Absent for member requests and older unattributed diagnostics."""


class RequestDiagnostic(BaseModel):
    r"""One authenticated HTTP attempt. An attempt id is independent of the caller correlation id. No raw body, path parameter, credential or source payload is retained. write_complete means the server wrote/flushed its response, not proof the client processed it. Collection is bounded best effort; ii_signup_request_diagnostic_failures_total exposes gaps. Retained for seven days or the shorter environment retention."""

    id: str

    request_id: str

    route: str

    http_status: int

    duration_ms: int

    started_at: str

    completed_at: str

    expires_at: str

    idempotent_replayed: bool

    write_complete: bool

    error_code: Optional[str] = None

    decision: Optional[DecisionReceipt] = None
    r"""The decision prepared for one HTTP attempt. Its account field preserves the account decision returned for that attempt, even after subsequent changes."""

    api_key_id: Optional[str] = None
    r"""Public authenticated API key identifier. Absent for member requests and older unattributed diagnostics."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["error_code", "decision", "api_key_id"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
