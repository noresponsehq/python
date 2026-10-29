from __future__ import annotations
from .keyenvironment import KeyEnvironment
from .keykind import KeyKind
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Literal, Optional
from typing_extensions import NotRequired, TypedDict


KeyRequestScope = Literal[
    "assess",
    "history",
    "delete",
    "webhooks",
    "detailed",
    "integrations",
    "management",
    "audit",
    "usage",
    "investigate",
    "evidence",
    "exports",
    "audit_manage",
    "settings",
    "policy_publish",
    "members",
    "members_manage",
]


class KeyRequestTypedDict(TypedDict):
    r"""Creates a key whose scopes are bounded by the issuer capabilities in this environment. Delete is owner-only. A service key outlives its creator; a personal key belongs to the authenticated member and is revoked on membership or authority changes. request_id deduplicates creation: retry returns 200 metadata without the secret; changed parameters answer 409. Team scopes members and members_manage are explicitly workspace-wide, live-only, and delegated by a current full owner. Personal credentials cannot hold management or members_manage. Legacy management includes policy publication; use settings without policy_publish for configuration preparation and retention-only edits."""

    environment: KeyEnvironment
    r"""The environment the key belongs to. A live key assesses with live sources; a test key answers from the deterministic simulator."""
    scopes: List[KeyRequestScope]
    r"""The key's scopes, each at most once."""
    name: NotRequired[str]
    r"""Optional display name for this API key, at most 100 printable characters. Preserved on rotation."""
    purpose: NotRequired[str]
    r"""Optional operational purpose, at most 200 printable characters without leading or trailing whitespace. Do not put secrets or personal data here. Preserved on rotation and included in the creation request fingerprint; omitted for older credentials."""
    kind: NotRequired[KeyKind]
    expires_at: NotRequired[str]
    r"""Between one minute and 365 days from now."""
    request_id: NotRequired[str]
    r"""Caller-chosen identifier for one creation attempt, scoped to the issuing actor and environment. Use 1 to 256 printable ASCII characters without spaces. A retry with the same parameters returns the original key metadata with status 200 and no secret; changed parameters return 409."""


class KeyRequest(BaseModel):
    r"""Creates a key whose scopes are bounded by the issuer capabilities in this environment. Delete is owner-only. A service key outlives its creator; a personal key belongs to the authenticated member and is revoked on membership or authority changes. request_id deduplicates creation: retry returns 200 metadata without the secret; changed parameters answer 409. Team scopes members and members_manage are explicitly workspace-wide, live-only, and delegated by a current full owner. Personal credentials cannot hold management or members_manage. Legacy management includes policy publication; use settings without policy_publish for configuration preparation and retention-only edits."""

    environment: KeyEnvironment
    r"""The environment the key belongs to. A live key assesses with live sources; a test key answers from the deterministic simulator."""

    scopes: List[KeyRequestScope]
    r"""The key's scopes, each at most once."""

    name: Optional[str] = None
    r"""Optional display name for this API key, at most 100 printable characters. Preserved on rotation."""

    purpose: Optional[str] = None
    r"""Optional operational purpose, at most 200 printable characters without leading or trailing whitespace. Do not put secrets or personal data here. Preserved on rotation and included in the creation request fingerprint; omitted for older credentials."""

    kind: Optional[KeyKind] = None

    expires_at: Optional[str] = None
    r"""Between one minute and 365 days from now."""

    request_id: Optional[str] = None
    r"""Caller-chosen identifier for one creation attempt, scoped to the issuing actor and environment. Use 1 to 256 printable ASCII characters without spaces. A retry with the same parameters returns the original key metadata with status 200 and no secret; changed parameters return 409."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["name", "purpose", "kind", "expires_at", "request_id"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
