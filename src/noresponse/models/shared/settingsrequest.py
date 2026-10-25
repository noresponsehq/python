from __future__ import annotations
from .settingsrequestflows import SettingsRequestFlows, SettingsRequestFlowsTypedDict
from .sourceid import SourceID
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class SettingsRequestTypedDict(TypedDict):
    r"""PATCH /v1/workspaces/{workspace_id}/settings/{environment} body. Changes only what it names, in one transaction; a policy change is one new policy_version. Needs the admin or owner role, or an API key with the management scope for its own environment."""

    retention_days: NotRequired[int]
    refused_sources: NotRequired[List[SourceID]]
    r"""Replaces the refused sources; [] refuses none. A change applies to new assessments within a minute."""
    flows: NotRequired[SettingsRequestFlowsTypedDict]
    r"""Use account_creation or its deprecated alias signup, not both."""


class SettingsRequest(BaseModel):
    r"""PATCH /v1/workspaces/{workspace_id}/settings/{environment} body. Changes only what it names, in one transaction; a policy change is one new policy_version. Needs the admin or owner role, or an API key with the management scope for its own environment."""

    retention_days: Optional[int] = None

    refused_sources: Optional[List[SourceID]] = None
    r"""Replaces the refused sources; [] refuses none. A change applies to new assessments within a minute."""

    flows: Optional[SettingsRequestFlows] = None
    r"""Use account_creation or its deprecated alias signup, not both."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["retention_days", "refused_sources", "flows"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
