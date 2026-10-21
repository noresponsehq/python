from __future__ import annotations
from .failurereason import FailureReason
from .freshness import Freshness
from .identifierkind import IdentifierKind
from .phoneenrichment import PhoneEnrichment, PhoneEnrichmentTypedDict
from .signaloutcome import SignalOutcome
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class SignalTypedDict(TypedDict):
    type: str
    r"""Signal kind, for example account_presence or breach_exposure. New kinds may appear; ignore any you do not know."""
    identifier: IdentifierKind
    r"""Which submitted identifier a signal concerns. ip is a selector of breach_exposure only."""
    outcome: SignalOutcome
    r"""Per-signal outcome. A source that timed out, was blocked or errored reports blocked, unavailable or inconclusive with a reason and is listed in incomplete_sources; not_found is a definite absence."""
    source_id: str
    r"""Opaque, tenant-scoped projection of the source that produced a signal. It stays stable for your tenant while the projection key is unchanged and reveals no upstream provider, feed, breach table or source record."""
    freshness: Freshness
    r"""Freshness class of the evidence behind a signal. unknown whenever no evidence was obtained."""
    reason: NotRequired[FailureReason]
    r"""Why a signal or source did not produce a definite found/not_found. timed_out means the source missed the request deadline; a continuation may still settle it. deferred means the (source, identifier) pair is async-only and was not attempted on the synchronous path; a continuation settles it."""
    evidence_ref: NotRequired[str]
    r"""Opaque pointer to evidence NoResponse holds for this signal. It carries no breach value, credential or page body."""
    observed_at: NotRequired[str]
    r"""When the evidence was first observed."""
    last_checked_at: NotRequired[str]
    r"""When the source was last queried for this identifier."""
    enrichment: NotRequired[PhoneEnrichmentTypedDict]
    r"""Facts about the number only: line type, carrier and country. The upstream provider, its scores and its verdicts stay internal."""


class Signal(BaseModel):
    type: str
    r"""Signal kind, for example account_presence or breach_exposure. New kinds may appear; ignore any you do not know."""

    identifier: IdentifierKind
    r"""Which submitted identifier a signal concerns. ip is a selector of breach_exposure only."""

    outcome: SignalOutcome
    r"""Per-signal outcome. A source that timed out, was blocked or errored reports blocked, unavailable or inconclusive with a reason and is listed in incomplete_sources; not_found is a definite absence."""

    source_id: str
    r"""Opaque, tenant-scoped projection of the source that produced a signal. It stays stable for your tenant while the projection key is unchanged and reveals no upstream provider, feed, breach table or source record."""

    freshness: Freshness
    r"""Freshness class of the evidence behind a signal. unknown whenever no evidence was obtained."""

    reason: Optional[FailureReason] = None
    r"""Why a signal or source did not produce a definite found/not_found. timed_out means the source missed the request deadline; a continuation may still settle it. deferred means the (source, identifier) pair is async-only and was not attempted on the synchronous path; a continuation settles it."""

    evidence_ref: Optional[str] = None
    r"""Opaque pointer to evidence NoResponse holds for this signal. It carries no breach value, credential or page body."""

    observed_at: Optional[str] = None
    r"""When the evidence was first observed."""

    last_checked_at: Optional[str] = None
    r"""When the source was last queried for this identifier."""

    enrichment: Optional[PhoneEnrichment] = None
    r"""Facts about the number only: line type, carrier and country. The upstream provider, its scores and its verdicts stay internal."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            ["reason", "evidence_ref", "observed_at", "last_checked_at", "enrichment"]
        )
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
