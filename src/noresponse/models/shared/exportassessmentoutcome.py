from __future__ import annotations
from .outcome import Outcome
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ExportAssessmentOutcomeTypedDict(TypedDict):
    r"""Structured fields of a retained per-assessment outcome. Legacy notes remain private as promised by the existing outcome contract."""

    id: str
    r"""Opaque, server-assigned id of one recorded outcome: 'out_' and a 26-character Crockford base32 ULID. Unique within the workspace."""
    assessment_id: str
    r"""Opaque, server-assigned assessment id: 'asm_' and a 26-character Crockford base32 ULID. Unique within the workspace; another workspace's assessment id answers 404."""
    outcome: Outcome
    r"""What the provider later learned about the assessed account. confirmed_abuse, account_takeover and chargeback report abuse; false_positive and legitimate withdraw an earlier abuse report of this workspace for the assessment; unknown is recorded only. Outcomes are append-only and the latest one recorded for an assessment wins."""
    observed_at: str
    received_at: str
    external_ref: NotRequired[str]
    r"""Your own opaque reference for the outcome, such as a case or ticket id. Stored as given and not interpreted; keep direct identifiers out of it."""


class ExportAssessmentOutcome(BaseModel):
    r"""Structured fields of a retained per-assessment outcome. Legacy notes remain private as promised by the existing outcome contract."""

    id: str
    r"""Opaque, server-assigned id of one recorded outcome: 'out_' and a 26-character Crockford base32 ULID. Unique within the workspace."""

    assessment_id: str
    r"""Opaque, server-assigned assessment id: 'asm_' and a 26-character Crockford base32 ULID. Unique within the workspace; another workspace's assessment id answers 404."""

    outcome: Outcome
    r"""What the provider later learned about the assessed account. confirmed_abuse, account_takeover and chargeback report abuse; false_positive and legitimate withdraw an earlier abuse report of this workspace for the assessment; unknown is recorded only. Outcomes are append-only and the latest one recorded for an assessment wins."""

    observed_at: str

    received_at: str

    external_ref: Optional[str] = None
    r"""Your own opaque reference for the outcome, such as a case or ticket id. Stored as given and not interpreted; keep direct identifiers out of it."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["external_ref"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
