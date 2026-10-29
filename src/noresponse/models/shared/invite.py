from __future__ import annotations
from .role import Role
from noresponse.types import BaseModel, UNSET_SENTINEL, UnrecognizedStr
from pydantic import model_serializer
from typing import List, Literal, Optional, Union
from typing_extensions import NotRequired, TypedDict


InviteEnvironment = Union[
    Literal[
        "live",
        "test",
    ],
    UnrecognizedStr,
]


InviteDeniedAction = Union[
    Literal[
        "evidence.read",
        "exports.read",
        "policy.publish",
    ],
    UnrecognizedStr,
]


class InviteTypedDict(TypedDict):
    r"""A pending workspace invitation. Creating or reissuing it returns a token once; lists omit it. The token can be accepted once before expiry and is invalidated on revocation or reissue. Token state does not establish email delivery."""

    id: str
    r"""Opaque, server-assigned invite id: inv_ and a 26-character ULID."""
    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""
    role: Role
    r"""A built-in capability set. Specialist roles are independent; effective access is returned by GET /v1/workspaces/{workspace_id}/capabilities."""
    created_by: str
    r"""The stable member id that issued this invite, or the authenticated live API key prefix for members_manage automation. Reissuing preserves the original creator; the audit event names the reissuing actor."""
    created_at: str
    expires_at: str
    email: NotRequired[str]
    r"""Where the console sends the invite. Informational: it is not matched against the accepting user."""
    external_user_id: NotRequired[str]
    r"""The user's id at the identity provider the console signs people in with: 1 to 256 printable ASCII characters with no space, compared exactly."""
    token: NotRequired[str]
    r"""The invite token: nrinv_, the invite id's ULID, _ and 43 unpadded base64url characters (32 random bytes). The new member's console sends it to POST /v1/invites/accept."""
    environments: NotRequired[List[InviteEnvironment]]
    r"""Allowed data environments. Invites default to both. Omitted on member PATCH preserves the current grants; owners retain both."""
    denied_actions: NotRequired[List[InviteDeniedAction]]
    r"""Independent removals from a built-in preset: sensitive evidence, exports, or active policy publication. Owners retain full authority. Omitted member updates preserve exclusions."""
    reissued_at: NotRequired[str]
    r"""Last token reissue, not proof of email delivery."""


class Invite(BaseModel):
    r"""A pending workspace invitation. Creating or reissuing it returns a token once; lists omit it. The token can be accepted once before expiry and is invalidated on revocation or reissue. Token state does not establish email delivery."""

    id: str
    r"""Opaque, server-assigned invite id: inv_ and a 26-character ULID."""

    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""

    role: Role
    r"""A built-in capability set. Specialist roles are independent; effective access is returned by GET /v1/workspaces/{workspace_id}/capabilities."""

    created_by: str
    r"""The stable member id that issued this invite, or the authenticated live API key prefix for members_manage automation. Reissuing preserves the original creator; the audit event names the reissuing actor."""

    created_at: str

    expires_at: str

    email: Optional[str] = None
    r"""Where the console sends the invite. Informational: it is not matched against the accepting user."""

    external_user_id: Optional[str] = None
    r"""The user's id at the identity provider the console signs people in with: 1 to 256 printable ASCII characters with no space, compared exactly."""

    token: Optional[str] = None
    r"""The invite token: nrinv_, the invite id's ULID, _ and 43 unpadded base64url characters (32 random bytes). The new member's console sends it to POST /v1/invites/accept."""

    environments: Optional[List[InviteEnvironment]] = None
    r"""Allowed data environments. Invites default to both. Omitted on member PATCH preserves the current grants; owners retain both."""

    denied_actions: Optional[List[InviteDeniedAction]] = None
    r"""Independent removals from a built-in preset: sensitive evidence, exports, or active policy publication. Owners retain full authority. Omitted member updates preserve exclusions."""

    reissued_at: Optional[str] = None
    r"""Last token reissue, not proof of email delivery."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "email",
                "external_user_id",
                "token",
                "environments",
                "denied_actions",
                "reissued_at",
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
