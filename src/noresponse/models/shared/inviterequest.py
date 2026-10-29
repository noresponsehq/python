from __future__ import annotations
from .role import Role
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Literal, Optional
from typing_extensions import NotRequired, TypedDict


InviteRequestEnvironment = Literal[
    "live",
    "test",
]


InviteRequestDeniedAction = Literal[
    "evidence.read",
    "exports.read",
    "policy.publish",
]


class InviteRequestTypedDict(TypedDict):
    r"""POST /v1/workspaces/{workspace_id}/invites body. Creates an invite for role and returns its token once. email is where the console sends the token and is not checked against the user who accepts. With external_user_id set, only that user can accept."""

    role: Role
    r"""A built-in capability set. Specialist roles are independent; effective access is returned by GET /v1/workspaces/{workspace_id}/capabilities."""
    email: NotRequired[str]
    r"""Where the console sends the invite. Informational: it is not matched against the accepting user."""
    external_user_id: NotRequired[str]
    r"""The user's id at the identity provider the console signs people in with: 1 to 256 printable ASCII characters with no space, compared exactly."""
    environments: NotRequired[List[InviteRequestEnvironment]]
    r"""Allowed data environments. Invites default to both. Omitted on member PATCH preserves the current grants; owners retain both."""
    denied_actions: NotRequired[List[InviteRequestDeniedAction]]
    r"""Independent removals from a built-in preset: sensitive evidence, exports, or active policy publication. Owners retain full authority. Omitted member updates preserve exclusions."""


class InviteRequest(BaseModel):
    r"""POST /v1/workspaces/{workspace_id}/invites body. Creates an invite for role and returns its token once. email is where the console sends the token and is not checked against the user who accepts. With external_user_id set, only that user can accept."""

    role: Role
    r"""A built-in capability set. Specialist roles are independent; effective access is returned by GET /v1/workspaces/{workspace_id}/capabilities."""

    email: Optional[str] = None
    r"""Where the console sends the invite. Informational: it is not matched against the accepting user."""

    external_user_id: Optional[str] = None
    r"""The user's id at the identity provider the console signs people in with: 1 to 256 printable ASCII characters with no space, compared exactly."""

    environments: Optional[List[InviteRequestEnvironment]] = None
    r"""Allowed data environments. Invites default to both. Omitted on member PATCH preserves the current grants; owners retain both."""

    denied_actions: Optional[List[InviteRequestDeniedAction]] = None
    r"""Independent removals from a built-in preset: sensitive evidence, exports, or active policy publication. Owners retain full authority. Omitted member updates preserve exclusions."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            ["email", "external_user_id", "environments", "denied_actions"]
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
