from __future__ import annotations
from .publication import Publication, PublicationTypedDict
from .settings import Settings, SettingsTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PolicyHistoryItemTypedDict(TypedDict):
    settings: SettingsTypedDict
    r"""One environment's settings: how long its assessments are kept, and for each flow the risk thresholds that decide it and the depth a request that names none is served at, and the sources it refuses. Live and test each have their own. A flow without thresholds of its own uses account_creation's (inherits_account_creation). Every change is recorded in the audit log as settings.updated, with who made it."""
    recorded_at: NotRequired[str]
    r"""Capture time, not a backfilled activation time. Absent only for the current configuration before its first capture."""
    change_reason: NotRequired[str]
    restored_from: NotRequired[int]
    evaluation: NotRequired[PublicationTypedDict]
    r"""Immutable publication provenance remains in policy history after evaluation evidence expires. SHA-256 values identify the frozen manifest, evaluator semantic input, cohort, and canonical result separately."""


class PolicyHistoryItem(BaseModel):
    settings: Settings
    r"""One environment's settings: how long its assessments are kept, and for each flow the risk thresholds that decide it and the depth a request that names none is served at, and the sources it refuses. Live and test each have their own. A flow without thresholds of its own uses account_creation's (inherits_account_creation). Every change is recorded in the audit log as settings.updated, with who made it."""

    recorded_at: Optional[str] = None
    r"""Capture time, not a backfilled activation time. Absent only for the current configuration before its first capture."""

    change_reason: Optional[str] = None

    restored_from: Optional[int] = None

    evaluation: Optional[Publication] = None
    r"""Immutable publication provenance remains in policy history after evaluation evidence expires. SHA-256 values identify the frozen manifest, evaluator semantic input, cohort, and canonical result separately."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            ["recorded_at", "change_reason", "restored_from", "evaluation"]
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
