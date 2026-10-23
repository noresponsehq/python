from __future__ import annotations
from .integrationhookpoint import IntegrationHookPoint
from .integrationplatform import IntegrationPlatform
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class IntegrationTypedDict(TypedDict):
    r"""A hosted provider integration. Point the provider at url: a WorkOS user registration or authentication Action, or the NoResponse Auth0 Action, which sends secret as a bearer token. The answer allows or denies the event: deny only when the assessment's risk.block is true, and allow on every failure, so a fault on the NoResponse side lets the user through. secret is present only in the answers of POST /v1/integrations and POST /v1/integrations/{integration_id}/rotate for an Auth0 integration, and is not returned again."""

    integration_id: str
    r"""Opaque, server-assigned integration id: int_ and a 26-character Crockford base32 ULID. Another workspace's integration id answers 404."""
    platform: IntegrationPlatform
    r"""The authentication provider that calls the endpoint."""
    hook_points: List[IntegrationHookPoint]
    r"""Each hook point at most once."""
    url: str
    r"""The hosted endpoint, https://api.noresponse.org/hooks/{integration_id} in production."""
    created_at: str
    secret: NotRequired[str]
    r"""Auth0 only, and only when it is created or rotated: the shared secret the Auth0 Action sends as Authorization: Bearer <secret>. nri_ and 43 unpadded base64url characters (32 random bytes). Store it as an Auth0 Action secret."""
    rotated_at: NotRequired[str]
    r"""When the secret was last rotated; absent until the first rotation."""
    previous_secret_expires_at: NotRequired[str]
    r"""After a rotation, when the replaced secret stops being accepted; absent when no replaced secret is still accepted."""


class Integration(BaseModel):
    r"""A hosted provider integration. Point the provider at url: a WorkOS user registration or authentication Action, or the NoResponse Auth0 Action, which sends secret as a bearer token. The answer allows or denies the event: deny only when the assessment's risk.block is true, and allow on every failure, so a fault on the NoResponse side lets the user through. secret is present only in the answers of POST /v1/integrations and POST /v1/integrations/{integration_id}/rotate for an Auth0 integration, and is not returned again."""

    integration_id: str
    r"""Opaque, server-assigned integration id: int_ and a 26-character Crockford base32 ULID. Another workspace's integration id answers 404."""

    platform: IntegrationPlatform
    r"""The authentication provider that calls the endpoint."""

    hook_points: List[IntegrationHookPoint]
    r"""Each hook point at most once."""

    url: str
    r"""The hosted endpoint, https://api.noresponse.org/hooks/{integration_id} in production."""

    created_at: str

    secret: Optional[str] = None
    r"""Auth0 only, and only when it is created or rotated: the shared secret the Auth0 Action sends as Authorization: Bearer <secret>. nri_ and 43 unpadded base64url characters (32 random bytes). Store it as an Auth0 Action secret."""

    rotated_at: Optional[str] = None
    r"""When the secret was last rotated; absent until the first rotation."""

    previous_secret_expires_at: Optional[str] = None
    r"""After a rotation, when the replaced secret stops being accepted; absent when no replaced secret is still accepted."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["secret", "rotated_at", "previous_secret_expires_at"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
