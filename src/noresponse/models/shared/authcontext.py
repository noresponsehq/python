from __future__ import annotations
from .assurancelevel import AssuranceLevel
from .authcontextmfa import AuthContextMfa, AuthContextMfaTypedDict
from .hookpoint import HookPoint
from .transport import Transport
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class AuthContextTypedDict(TypedDict):
    r"""Normalised claims from a session your backend has already verified with WorkOS, Clerk, Auth0 or any OIDC provider. Pass the output of the SDK's auth adapters, not a raw token."""

    provider: str
    r"""Lowercase provider slug. WorkOS, Clerk and Auth0 have first-class adapters; every other provider uses a customer-specific OIDC slug. Provider brand is metadata; it does not change risk by itself."""
    issuer: str
    r"""The verified token issuer, normally the provider's HTTPS issuer URL."""
    subject: str
    r"""The verified stable subject identifier (`sub`), opaque to NoResponse. Required, except from a provider hook at pre_registration, where no user exists yet."""
    verified: bool
    r"""Whether the customer completed signature, issuer, audience and expiry validation before calling NoResponse. False contexts are accepted only as weak hints."""
    audience: NotRequired[str]
    r"""The verified audience/resource identifier used by the customer's API. Use audiences when the provider emits multiple values."""
    audiences: NotRequired[List[str]]
    r"""All verified audience/resource identifiers from an OAuth or OIDC token. The first value may also be copied to audience for simple integrations."""
    session_id: NotRequired[str]
    r"""The verified session identifier (`sid` or provider equivalent)."""
    organization_id: NotRequired[str]
    r"""The active organization or workspace identifier, when the provider issued one."""
    tenant_id: NotRequired[str]
    r"""The provider tenant identifier, when distinct from organization_id."""
    token_id: NotRequired[str]
    r"""The verified token identifier (`jti`), used for replay and rotation correlation."""
    issued_at: NotRequired[str]
    r"""Verified token issue time (`iat`)."""
    expires_at: NotRequired[str]
    r"""Verified token expiry (`exp`)."""
    session_created_at: NotRequired[str]
    r"""Creation time of the provider session from the verified backend session record (for example Clerk Session.createdAt or WorkOS Session.created_at). This is separate from token issuance and auth_time."""
    auth_time: NotRequired[str]
    r"""Verified end-user authentication time (`auth_time`), when present."""
    account_created_at: NotRequired[str]
    r"""Account creation time from the customer's verified provider record, when available."""
    email_verified: NotRequired[bool]
    r"""Whether the customer's provider asserts that the email identifier was verified."""
    phone_verified: NotRequired[bool]
    r"""Whether the customer's provider asserts that the phone identifier was verified."""
    assurance_level: NotRequired[AssuranceLevel]
    r"""Provider or OIDC assurance level, when the customer has mapped one."""
    impersonated: NotRequired[bool]
    r"""Whether the verified session is acting on behalf of another subject."""
    transport: NotRequired[Transport]
    r"""Where this context was derived. Backend is the trusted integration path; browser values are treated as weak hints. provider_hook is a hosted provider hook (an Auth0 or WorkOS Action) calling at hook_point; it needs hook_point and verified false, and its authentication facts are not scored."""
    hook_point: NotRequired[HookPoint]
    r"""The provider event a provider_hook context was sent for. pre_registration runs before the user exists, so subject and the request's account_id may be absent there. Sent only with transport provider_hook."""
    mfa: NotRequired[AuthContextMfaTypedDict]
    r"""Normalized multi-factor evidence from a verified provider session."""
    roles: NotRequired[List[str]]
    r"""Bounded role slugs from the verified provider; roles do not change risk by themselves."""
    scopes: NotRequired[List[str]]
    r"""Bounded scopes from the verified access token; scopes do not change risk by themselves."""


class AuthContext(BaseModel):
    r"""Normalised claims from a session your backend has already verified with WorkOS, Clerk, Auth0 or any OIDC provider. Pass the output of the SDK's auth adapters, not a raw token."""

    provider: str
    r"""Lowercase provider slug. WorkOS, Clerk and Auth0 have first-class adapters; every other provider uses a customer-specific OIDC slug. Provider brand is metadata; it does not change risk by itself."""

    issuer: str
    r"""The verified token issuer, normally the provider's HTTPS issuer URL."""

    subject: str
    r"""The verified stable subject identifier (`sub`), opaque to NoResponse. Required, except from a provider hook at pre_registration, where no user exists yet."""

    verified: bool
    r"""Whether the customer completed signature, issuer, audience and expiry validation before calling NoResponse. False contexts are accepted only as weak hints."""

    audience: Optional[str] = None
    r"""The verified audience/resource identifier used by the customer's API. Use audiences when the provider emits multiple values."""

    audiences: Optional[List[str]] = None
    r"""All verified audience/resource identifiers from an OAuth or OIDC token. The first value may also be copied to audience for simple integrations."""

    session_id: Optional[str] = None
    r"""The verified session identifier (`sid` or provider equivalent)."""

    organization_id: Optional[str] = None
    r"""The active organization or workspace identifier, when the provider issued one."""

    tenant_id: Optional[str] = None
    r"""The provider tenant identifier, when distinct from organization_id."""

    token_id: Optional[str] = None
    r"""The verified token identifier (`jti`), used for replay and rotation correlation."""

    issued_at: Optional[str] = None
    r"""Verified token issue time (`iat`)."""

    expires_at: Optional[str] = None
    r"""Verified token expiry (`exp`)."""

    session_created_at: Optional[str] = None
    r"""Creation time of the provider session from the verified backend session record (for example Clerk Session.createdAt or WorkOS Session.created_at). This is separate from token issuance and auth_time."""

    auth_time: Optional[str] = None
    r"""Verified end-user authentication time (`auth_time`), when present."""

    account_created_at: Optional[str] = None
    r"""Account creation time from the customer's verified provider record, when available."""

    email_verified: Optional[bool] = None
    r"""Whether the customer's provider asserts that the email identifier was verified."""

    phone_verified: Optional[bool] = None
    r"""Whether the customer's provider asserts that the phone identifier was verified."""

    assurance_level: Optional[AssuranceLevel] = None
    r"""Provider or OIDC assurance level, when the customer has mapped one."""

    impersonated: Optional[bool] = None
    r"""Whether the verified session is acting on behalf of another subject."""

    transport: Optional[Transport] = None
    r"""Where this context was derived. Backend is the trusted integration path; browser values are treated as weak hints. provider_hook is a hosted provider hook (an Auth0 or WorkOS Action) calling at hook_point; it needs hook_point and verified false, and its authentication facts are not scored."""

    hook_point: Optional[HookPoint] = None
    r"""The provider event a provider_hook context was sent for. pre_registration runs before the user exists, so subject and the request's account_id may be absent there. Sent only with transport provider_hook."""

    mfa: Optional[AuthContextMfa] = None
    r"""Normalized multi-factor evidence from a verified provider session."""

    roles: Optional[List[str]] = None
    r"""Bounded role slugs from the verified provider; roles do not change risk by themselves."""

    scopes: Optional[List[str]] = None
    r"""Bounded scopes from the verified access token; scopes do not change risk by themselves."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "audience",
                "audiences",
                "session_id",
                "organization_id",
                "tenant_id",
                "token_id",
                "issued_at",
                "expires_at",
                "session_created_at",
                "auth_time",
                "account_created_at",
                "email_verified",
                "phone_verified",
                "assurance_level",
                "impersonated",
                "transport",
                "hook_point",
                "mfa",
                "roles",
                "scopes",
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
