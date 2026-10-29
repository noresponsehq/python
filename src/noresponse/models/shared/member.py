from __future__ import annotations
from .memberstatus import MemberStatus
from .role import Role
from noresponse.types import BaseModel, UNSET_SENTINEL, UnrecognizedStr
from pydantic import model_serializer
from typing import List, Literal, Optional, Union
from typing_extensions import NotRequired, TypedDict


MemberEnvironment = Union[
    Literal[
        "live",
        "test",
    ],
    UnrecognizedStr,
]


MemberDeniedAction = Union[
    Literal[
        "evidence.read",
        "exports.read",
        "policy.publish",
    ],
    UnrecognizedStr,
]


class MemberTypedDict(TypedDict):
    r"""One member of a workspace: an external user id holding one role. A removed member loses every permission at once."""

    id: str
    r"""Opaque, server-assigned member id: mem_ and a 26-character ULID. It stays the same when a removed member is invited back."""
    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""
    external_user_id: str
    r"""The user's id at the identity provider the console signs people in with: 1 to 256 printable ASCII characters with no space, compared exactly."""
    role: Role
    r"""A built-in capability set. Specialist roles are independent; effective access is returned by GET /v1/workspaces/{workspace_id}/capabilities."""
    status: MemberStatus
    r"""Listed and returned members are active."""
    created_at: str
    updated_at: str
    environments: NotRequired[List[MemberEnvironment]]
    r"""Allowed data environments. Invites default to both. Omitted on member PATCH preserves the current grants; owners retain both."""
    denied_actions: NotRequired[List[MemberDeniedAction]]
    r"""Independent removals from a built-in preset: sensitive evidence, exports, or active policy publication. Owners retain full authority. Omitted member updates preserve exclusions."""
    principal_id: NotRequired[str]
    r"""Immutable internal workspace principal, equal to member id, preserved across explicit provider-identity migrations."""
    display_name: NotRequired[str]
    r"""Informational display name. Authentication and provider identity use the verified subject binding."""
    unverified_email: NotRequired[str]
    r"""Unverified contact address for display. Empty clears it; a supplied value must be an address. Identity linking uses the verified provider subject."""


class Member(BaseModel):
    r"""One member of a workspace: an external user id holding one role. A removed member loses every permission at once."""

    id: str
    r"""Opaque, server-assigned member id: mem_ and a 26-character ULID. It stays the same when a removed member is invited back."""

    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""

    external_user_id: str
    r"""The user's id at the identity provider the console signs people in with: 1 to 256 printable ASCII characters with no space, compared exactly."""

    role: Role
    r"""A built-in capability set. Specialist roles are independent; effective access is returned by GET /v1/workspaces/{workspace_id}/capabilities."""

    status: MemberStatus
    r"""Listed and returned members are active."""

    created_at: str

    updated_at: str

    environments: Optional[List[MemberEnvironment]] = None
    r"""Allowed data environments. Invites default to both. Omitted on member PATCH preserves the current grants; owners retain both."""

    denied_actions: Optional[List[MemberDeniedAction]] = None
    r"""Independent removals from a built-in preset: sensitive evidence, exports, or active policy publication. Owners retain full authority. Omitted member updates preserve exclusions."""

    principal_id: Optional[str] = None
    r"""Immutable internal workspace principal, equal to member id, preserved across explicit provider-identity migrations."""

    display_name: Optional[str] = None
    r"""Informational display name. Authentication and provider identity use the verified subject binding."""

    unverified_email: Optional[str] = None
    r"""Unverified contact address for display. Empty clears it; a supplied value must be an address. Identity linking uses the verified provider subject."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "environments",
                "denied_actions",
                "principal_id",
                "display_name",
                "unverified_email",
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
