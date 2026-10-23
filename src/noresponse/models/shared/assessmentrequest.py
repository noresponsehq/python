from __future__ import annotations
from .assessmentrequestclientcontext import (
    AssessmentRequestClientContext,
    AssessmentRequestClientContextTypedDict,
)
from .assessmentrequestidentifiers import (
    AssessmentRequestIdentifiers,
    AssessmentRequestIdentifiersTypedDict,
)
from .assessmentrequestissuedcredential import (
    AssessmentRequestIssuedCredential,
    AssessmentRequestIssuedCredentialTypedDict,
)
from .assessmentrequestpolicycontext import (
    AssessmentRequestPolicyContext,
    AssessmentRequestPolicyContextTypedDict,
)
from .authcontext import AuthContext, AuthContextTypedDict
from .responsemode import ResponseMode
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AssessmentRequestTypedDict(TypedDict):
    r"""POST /v1/assessments body. At least one of email, username or phone is required; name and ip only refine an assessment. No field carries a password, hash, token or breach value, and unknown members are refused. The email local part is kept as received and only the domain is lower-cased; the username is compared case-insensitively; the phone is strict E.164 and is assessed asynchronously. The whole body is capped at 32768 bytes. client_context holds bounded hints from the signup client; auth_context holds normalised claims from a session your backend has verified. Raw tokens are refused."""

    account_id: str
    r"""Your own opaque identifier for the account being checked, scoped to your tenant. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused, as is a JWT; a hex digest such as a SHA-256 is allowed. It travels only in request bodies. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""
    identifiers: AssessmentRequestIdentifiersTypedDict
    r"""At least one of email, username or phone. name and ip refine the match and travel beside a lookup identifier; a body with only name or ip is refused with 400."""
    policy_context: NotRequired[AssessmentRequestPolicyContextTypedDict]
    request_id: NotRequired[str]
    r"""An optional provider correlation id, echoed back. It is not an idempotency key. Refuses an exact-shape JWT or a bare 40, 64 or 128 character hex digest; a UUID is accepted."""
    deadline_ms: NotRequired[int]
    r"""Optional tighter budget, 50 to 3000 ms, measured from the moment the request reaches NoResponse. Absent means the 3000 ms ceiling; a value above it is refused with 400 rather than clamped."""
    response_mode: NotRequired[ResponseMode]
    r"""standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode."""
    client_context: NotRequired[AssessmentRequestClientContextTypedDict]
    r"""Optional context observed by your signup client. The server parses these hints into coarse features, leaves raw user_agent and opaque ids out of every answer, and weighs a mismatch with the other evidence."""
    auth_context: NotRequired[AuthContextTypedDict]
    r"""Normalised claims from a session your backend has already verified with WorkOS, Clerk, Auth0 or any OIDC provider. Pass the output of the SDK's auth adapters, not a raw token."""
    issued_credential: NotRequired[AssessmentRequestIssuedCredentialTypedDict]
    r"""Optional. When the signup gate issues an API key to the new account, send SHA-256 of that key, so later usage of the key, or a leaked copy, ties back to this assessment. Each SDK has a helper that computes it. Send only the hash: customer keys are high-entropy, so the hash reveals nothing about them. The assessment stores it, and no response, webhook or log carries it."""


class AssessmentRequest(BaseModel):
    r"""POST /v1/assessments body. At least one of email, username or phone is required; name and ip only refine an assessment. No field carries a password, hash, token or breach value, and unknown members are refused. The email local part is kept as received and only the domain is lower-cased; the username is compared case-insensitively; the phone is strict E.164 and is assessed asynchronously. The whole body is capped at 32768 bytes. client_context holds bounded hints from the signup client; auth_context holds normalised claims from a session your backend has verified. Raw tokens are refused."""

    account_id: str
    r"""Your own opaque identifier for the account being checked, scoped to your tenant. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused, as is a JWT; a hex digest such as a SHA-256 is allowed. It travels only in request bodies. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""

    identifiers: AssessmentRequestIdentifiers
    r"""At least one of email, username or phone. name and ip refine the match and travel beside a lookup identifier; a body with only name or ip is refused with 400."""

    policy_context: Optional[AssessmentRequestPolicyContext] = None

    request_id: Optional[str] = None
    r"""An optional provider correlation id, echoed back. It is not an idempotency key. Refuses an exact-shape JWT or a bare 40, 64 or 128 character hex digest; a UUID is accepted."""

    deadline_ms: Optional[int] = None
    r"""Optional tighter budget, 50 to 3000 ms, measured from the moment the request reaches NoResponse. Absent means the 3000 ms ceiling; a value above it is refused with 400 rather than clamped."""

    response_mode: Optional[ResponseMode] = None
    r"""standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode."""

    client_context: Optional[AssessmentRequestClientContext] = None
    r"""Optional context observed by your signup client. The server parses these hints into coarse features, leaves raw user_agent and opaque ids out of every answer, and weighs a mismatch with the other evidence."""

    auth_context: Optional[AuthContext] = None
    r"""Normalised claims from a session your backend has already verified with WorkOS, Clerk, Auth0 or any OIDC provider. Pass the output of the SDK's auth adapters, not a raw token."""

    issued_credential: Optional[AssessmentRequestIssuedCredential] = None
    r"""Optional. When the signup gate issues an API key to the new account, send SHA-256 of that key, so later usage of the key, or a leaked copy, ties back to this assessment. Each SDK has a helper that computes it. Send only the hash: customer keys are high-entropy, so the hash reveals nothing about them. The assessment stores it, and no response, webhook or log carries it."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "policy_context",
                "request_id",
                "deadline_ms",
                "response_mode",
                "client_context",
                "auth_context",
                "issued_credential",
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
