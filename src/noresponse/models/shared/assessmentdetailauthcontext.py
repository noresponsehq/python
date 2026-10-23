from __future__ import annotations
from .hookpoint import HookPoint
from .transport import Transport
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AssessmentDetailAuthContextTypedDict(TypedDict):
    r"""The identity fields of the auth context the assessment was made with, echoed for the workspace's own correlation: the request's auth_context, or the one a hosted provider hook (POST /hooks/{integration_id}) built, with transport provider_hook and its hook_point. Present exactly when the request carried an auth_context, and the same on every revision of the assessment. Values are as the request or the hook sent them; tokens, timestamps, roles and scopes are not echoed, and the echo does not change the score."""

    provider: str
    r"""The provider slug the context named."""
    issuer: str
    r"""The issuer the context named."""
    verified: bool
    r"""The verified flag the context carried. A provider_hook context is always false."""
    transport: Transport
    r"""Where the context was derived: backend (also when the request named no transport), browser, or provider_hook for a hosted provider hook."""
    subject: NotRequired[str]
    r"""The subject the context named; absent when it named none (a pre_registration hook)."""
    session_id: NotRequired[str]
    r"""The session identifier the context named, when it named one."""
    organization_id: NotRequired[str]
    r"""The organization identifier the context named, when it named one."""
    hook_point: NotRequired[HookPoint]
    r"""The provider event a provider_hook context was sent for; absent for any other transport."""


class AssessmentDetailAuthContext(BaseModel):
    r"""The identity fields of the auth context the assessment was made with, echoed for the workspace's own correlation: the request's auth_context, or the one a hosted provider hook (POST /hooks/{integration_id}) built, with transport provider_hook and its hook_point. Present exactly when the request carried an auth_context, and the same on every revision of the assessment. Values are as the request or the hook sent them; tokens, timestamps, roles and scopes are not echoed, and the echo does not change the score."""

    provider: str
    r"""The provider slug the context named."""

    issuer: str
    r"""The issuer the context named."""

    verified: bool
    r"""The verified flag the context carried. A provider_hook context is always false."""

    transport: Transport
    r"""Where the context was derived: backend (also when the request named no transport), browser, or provider_hook for a hosted provider hook."""

    subject: Optional[str] = None
    r"""The subject the context named; absent when it named none (a pre_registration hook)."""

    session_id: Optional[str] = None
    r"""The session identifier the context named, when it named one."""

    organization_id: Optional[str] = None
    r"""The organization identifier the context named, when it named one."""

    hook_point: Optional[HookPoint] = None
    r"""The provider event a provider_hook context was sent for; absent for any other transport."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            ["subject", "session_id", "organization_id", "hook_point"]
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
