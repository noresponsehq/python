from __future__ import annotations
from .settingsrequestflows import SettingsRequestFlows, SettingsRequestFlowsTypedDict
from .sourceid import SourceID
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class SettingsRequestTypedDict(TypedDict):
    r"""Changes only named settings, atomically. Every successful write advances policy_version and retains an immutable settings snapshot. expected_policy_version optionally guards against stale edits; restore always requires it."""

    retention_days: NotRequired[int]
    refused_sources: NotRequired[List[SourceID]]
    r"""Replaces the refused sources; [] refuses none. A change applies to new assessments within a minute."""
    flows: NotRequired[SettingsRequestFlowsTypedDict]
    r"""Use account_creation or its deprecated alias signup, not both."""
    expected_policy_version: NotRequired[int]
    r"""Compare-and-set guard. A stale version returns 409 policy_version_conflict before any change; every settings write including retention advances the version."""
    change_reason: NotRequired[str]


class SettingsRequest(BaseModel):
    r"""Changes only named settings, atomically. Every successful write advances policy_version and retains an immutable settings snapshot. expected_policy_version optionally guards against stale edits; restore always requires it."""

    retention_days: Optional[int] = None

    refused_sources: Optional[List[SourceID]] = None
    r"""Replaces the refused sources; [] refuses none. A change applies to new assessments within a minute."""

    flows: Optional[SettingsRequestFlows] = None
    r"""Use account_creation or its deprecated alias signup, not both."""

    expected_policy_version: Optional[int] = None
    r"""Compare-and-set guard. A stale version returns 409 policy_version_conflict before any change; every settings write including retention advances the version."""

    change_reason: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "retention_days",
                "refused_sources",
                "flows",
                "expected_policy_version",
                "change_reason",
            ]
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
