from __future__ import annotations
from .role import Role
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Literal, Optional
from typing_extensions import NotRequired, TypedDict


MemberUpdateRequestEnvironment = Literal[
    "live",
    "test",
]


MemberUpdateRequestDeniedAction = Literal[
    "evidence.read",
    "exports.read",
    "policy.publish",
]


class MemberUpdateRequestTypedDict(TypedDict):
    r"""PATCH /v1/workspaces/{workspace_id}/members/{member_id} body: the member's new role. The workspace's last owner cannot be demoted."""

    role: Role
    r"""A built-in capability set. Specialist roles are independent; effective access is returned by GET /v1/workspaces/{workspace_id}/capabilities."""
    environments: NotRequired[List[MemberUpdateRequestEnvironment]]
    r"""Allowed data environments. Invites default to both. Omitted on member PATCH preserves the current grants; owners retain both."""
    denied_actions: NotRequired[List[MemberUpdateRequestDeniedAction]]
    r"""Independent removals from a built-in preset: sensitive evidence, exports, or active policy publication. Owners retain full authority. Omitted member updates preserve exclusions."""


class MemberUpdateRequest(BaseModel):
    r"""PATCH /v1/workspaces/{workspace_id}/members/{member_id} body: the member's new role. The workspace's last owner cannot be demoted."""

    role: Role
    r"""A built-in capability set. Specialist roles are independent; effective access is returned by GET /v1/workspaces/{workspace_id}/capabilities."""

    environments: Optional[List[MemberUpdateRequestEnvironment]] = None
    r"""Allowed data environments. Invites default to both. Omitted on member PATCH preserves the current grants; owners retain both."""

    denied_actions: Optional[List[MemberUpdateRequestDeniedAction]] = None
    r"""Independent removals from a built-in preset: sensitive evidence, exports, or active policy publication. Owners retain full authority. Omitted member updates preserve exclusions."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["environments", "denied_actions"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
