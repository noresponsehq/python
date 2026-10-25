from __future__ import annotations
from .enforcementaction import EnforcementAction
from .enforcementprovider import EnforcementProvider
from .enforcementstate import EnforcementState
from .enforcementstatus import EnforcementStatus
from .flow import Flow
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class EnforcementTypedDict(TypedDict):
    r"""The answer of POST /v1/accounts/{account_id}/enforcements: one enforcement of one of the calling workspace's accounts, kept once per (account, risk_version, flow, action). The first report answers 201 with the new record. A repeat answers 200 with the record as first stored, whatever the repeat's state_before, status, provider or error_code. The one exception is a stored failed record followed by an applied report: the record becomes applied, keeps its id and created_at, takes the applied report's state_before and provider, drops error_code and answers 201, so a successful retry after a failure is recorded. Only an applied record at the account's current risk_version takes the account out of GET /v1/accounts?unenforced=true."""

    id: str
    r"""Opaque, server-assigned id of one recorded enforcement: 'enf_' and 26 Crockford base32 characters. Unique within the workspace."""
    account_id: str
    r"""The account_id of the request path."""
    risk_version: int
    r"""The account's risk_version the workspace acted on. It can be older than the account's current risk_version: such a record is kept and does not count for unenforced."""
    flow: Flow
    r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""
    action: EnforcementAction
    r"""What the workspace did in its identity provider: revoke_sessions (signed the account out everywhere), restrict (limited what the account can do), unrestrict (lifted an earlier restriction), fail_onboarding (stopped an account that was still onboarding), reject_activation (refused to activate a provisional account), activate (let a held onboarding or provisional account in) or none (decided to take no action)."""
    state_before: EnforcementState
    r"""The account's state in the workspace's identity provider just before the action: onboarding, provisional (created, not yet activated), active, restricted or rejected."""
    status: EnforcementStatus
    r"""applied when the identity provider accepted the action, failed when it refused it or could not be reached. Only applied counts as enforced."""
    provider: EnforcementProvider
    r"""The identity provider the action ran in; custom for the workspace's own user store."""
    created_at: str
    r"""When NoResponse first recorded this enforcement, in UTC. A failed record that becomes applied keeps it."""
    error_code: NotRequired[str]
    r"""Why a failed action failed, as a short code of the workspace's choosing (lower-case letters, digits, '_', '.' and '-'), such as the identity provider's error code. Allowed only with status failed: with status applied it answers 400 invalid_request. Keep personal data out of it."""


class Enforcement(BaseModel):
    r"""The answer of POST /v1/accounts/{account_id}/enforcements: one enforcement of one of the calling workspace's accounts, kept once per (account, risk_version, flow, action). The first report answers 201 with the new record. A repeat answers 200 with the record as first stored, whatever the repeat's state_before, status, provider or error_code. The one exception is a stored failed record followed by an applied report: the record becomes applied, keeps its id and created_at, takes the applied report's state_before and provider, drops error_code and answers 201, so a successful retry after a failure is recorded. Only an applied record at the account's current risk_version takes the account out of GET /v1/accounts?unenforced=true."""

    id: str
    r"""Opaque, server-assigned id of one recorded enforcement: 'enf_' and 26 Crockford base32 characters. Unique within the workspace."""

    account_id: str
    r"""The account_id of the request path."""

    risk_version: int
    r"""The account's risk_version the workspace acted on. It can be older than the account's current risk_version: such a record is kept and does not count for unenforced."""

    flow: Flow
    r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""

    action: EnforcementAction
    r"""What the workspace did in its identity provider: revoke_sessions (signed the account out everywhere), restrict (limited what the account can do), unrestrict (lifted an earlier restriction), fail_onboarding (stopped an account that was still onboarding), reject_activation (refused to activate a provisional account), activate (let a held onboarding or provisional account in) or none (decided to take no action)."""

    state_before: EnforcementState
    r"""The account's state in the workspace's identity provider just before the action: onboarding, provisional (created, not yet activated), active, restricted or rejected."""

    status: EnforcementStatus
    r"""applied when the identity provider accepted the action, failed when it refused it or could not be reached. Only applied counts as enforced."""

    provider: EnforcementProvider
    r"""The identity provider the action ran in; custom for the workspace's own user store."""

    created_at: str
    r"""When NoResponse first recorded this enforcement, in UTC. A failed record that becomes applied keeps it."""

    error_code: Optional[str] = None
    r"""Why a failed action failed, as a short code of the workspace's choosing (lower-case letters, digits, '_', '.' and '-'), such as the identity provider's error code. Allowed only with status failed: with status applied it answers 400 invalid_request. Keep personal data out of it."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["error_code"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
