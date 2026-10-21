from __future__ import annotations
from .platform import Platform
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AssessmentRequestClientContextTypedDict(TypedDict):
    r"""Optional context observed by your signup client. The server parses these hints into coarse features, leaves raw user_agent and opaque ids out of every answer, and weighs a mismatch with the other evidence."""

    timezone: NotRequired[str]
    r"""IANA time-zone name such as Europe/London or America/Los_Angeles. Fixed numeric offsets are not accepted."""
    locale: NotRequired[str]
    r"""BCP 47 locale, for example en-AU. Treat as a presentation hint, not a nationality signal."""
    platform: NotRequired[Platform]
    r"""Client platform. Closed vocabulary keeps integrations stable."""
    app_version: NotRequired[str]
    r"""Customer application version, without build metadata that contains secrets."""
    user_agent: NotRequired[str]
    r"""The raw User-Agent header of the signup request, at most 512 characters. It is parsed into coarse features and left out of every answer."""
    device_id: NotRequired[str]
    r"""Tenant-scoped opaque identifier your application mints and rotates when the account or device changes. Send an id of your own, not a hardware fingerprint."""
    session_id: NotRequired[str]
    r"""Opaque signup session identifier. It is used for tenant-scoped velocity and replay checks only."""
    form_duration_ms: NotRequired[int]
    r"""Elapsed time from form start to submit. Values below three seconds are a weak automation hint, weighed with the other evidence."""
    client_observed_at: NotRequired[str]
    r"""RFC 3339 timestamp observed by the client. Server ingress time remains authoritative; a large clock skew is only a low-confidence feature."""


class AssessmentRequestClientContext(BaseModel):
    r"""Optional context observed by your signup client. The server parses these hints into coarse features, leaves raw user_agent and opaque ids out of every answer, and weighs a mismatch with the other evidence."""

    timezone: Optional[str] = None
    r"""IANA time-zone name such as Europe/London or America/Los_Angeles. Fixed numeric offsets are not accepted."""

    locale: Optional[str] = None
    r"""BCP 47 locale, for example en-AU. Treat as a presentation hint, not a nationality signal."""

    platform: Optional[Platform] = None
    r"""Client platform. Closed vocabulary keeps integrations stable."""

    app_version: Optional[str] = None
    r"""Customer application version, without build metadata that contains secrets."""

    user_agent: Optional[str] = None
    r"""The raw User-Agent header of the signup request, at most 512 characters. It is parsed into coarse features and left out of every answer."""

    device_id: Optional[str] = None
    r"""Tenant-scoped opaque identifier your application mints and rotates when the account or device changes. Send an id of your own, not a hardware fingerprint."""

    session_id: Optional[str] = None
    r"""Opaque signup session identifier. It is used for tenant-scoped velocity and replay checks only."""

    form_duration_ms: Optional[int] = None
    r"""Elapsed time from form start to submit. Values below three seconds are a weak automation hint, weighed with the other evidence."""

    client_observed_at: Optional[str] = None
    r"""RFC 3339 timestamp observed by the client. Server ingress time remains authoritative; a large clock skew is only a low-confidence feature."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "timezone",
                "locale",
                "platform",
                "app_version",
                "user_agent",
                "device_id",
                "session_id",
                "form_duration_ms",
                "client_observed_at",
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
