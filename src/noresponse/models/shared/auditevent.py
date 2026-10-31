from __future__ import annotations
from .auditeventtarget import AuditEventTarget, AuditEventTargetTypedDict
from .auditsettingsenvironment import AuditSettingsEnvironment
from .customerexportrequestfilteroutcome import CustomerExportRequestFilterOutcome
from .environment import Environment
from .keyactor import KeyActor, KeyActorTypedDict
from .useractor import UserActor, UserActorTypedDict
from functools import partial
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils.unions import parse_open_union
from pydantic import ConfigDict, model_serializer
from pydantic.functional_validators import BeforeValidator
from typing import Any, Dict, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


ActorTypedDict = TypeAliasType(
    "ActorTypedDict", Union[KeyActorTypedDict, UserActorTypedDict]
)


class UnknownActor(BaseModel):
    r"""A Actor variant the SDK doesn't recognize. Preserves the raw payload."""

    type: Literal["UNKNOWN"] = "UNKNOWN"
    raw: Any
    is_unknown: Literal[True] = True

    model_config = ConfigDict(frozen=True)


_ACTOR_VARIANTS: dict[str, Any] = {
    "user": UserActor,
    "api_key": KeyActor,
}


Actor = Annotated[
    Union[UserActor, KeyActor, UnknownActor],
    BeforeValidator(
        partial(
            parse_open_union,
            disc_key="type",
            variants=_ACTOR_VARIANTS,
            unknown_cls=UnknownActor,
            union_name="Actor",
        )
    ),
]


class AuditEventTypedDict(TypedDict):
    r"""One privileged workspace action with its actor, target, outcome and time. Successful data changes commit their audit evidence atomically. Sensitive exports record access before returning bytes. Details exclude secrets and subject identifiers."""

    id: str
    r"""Opaque, server-assigned event id: aud_ and a 26-character ULID."""
    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""
    environment: AuditSettingsEnvironment
    action: str
    r"""What happened, as resource.verb: workspace.created, member.role_changed, member.removed, invite.created, invite.revoked, invite.accepted, key.rotated, webhook_endpoint.created, webhook_endpoint.deleted, webhook_endpoint.secret_rotated, integration.created, integration.deleted, integration.secret_rotated, list_entry.created, list_entry.deleted, webhook_endpoint.test_sent, webhook_endpoint.verification_requested, webhook_endpoint.delivery_replayed, assessment.created, assessment.outcome_recorded, assessment.deleted, account.outcome_recorded, account.enforcement_recorded, account.deleted, account.exported. A change with no finer name carries the permission it used, such as keys.live.write. A member's read of raw evidence is breach_records.read or review_locations.read, with the assessment and counts and no value. New actions may appear; treat an unknown one as a change to its target."""
    outcome: CustomerExportRequestFilterOutcome
    actor: ActorTypedDict
    target: AuditEventTargetTypedDict
    created_at: str
    detail: NotRequired[Dict[str, str]]
    r"""At most 8 short facts about the change, keyed by lowercase names: the role a member was given or accepted (role), the invite an accepted member used (invite_id), the key that replaced a rotated one (new_key_id), the assessment a member's change acted on (assessment_id). Absent when there are none."""
    affected_environment: NotRequired[Environment]
    request_id: NotRequired[str]
    r"""Validated request correlation id, also returned in X-Request-ID, linking this event to request diagnostics. Absent on historical events without correlation."""


class AuditEvent(BaseModel):
    r"""One privileged workspace action with its actor, target, outcome and time. Successful data changes commit their audit evidence atomically. Sensitive exports record access before returning bytes. Details exclude secrets and subject identifiers."""

    id: str
    r"""Opaque, server-assigned event id: aud_ and a 26-character ULID."""

    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""

    environment: AuditSettingsEnvironment

    action: str
    r"""What happened, as resource.verb: workspace.created, member.role_changed, member.removed, invite.created, invite.revoked, invite.accepted, key.rotated, webhook_endpoint.created, webhook_endpoint.deleted, webhook_endpoint.secret_rotated, integration.created, integration.deleted, integration.secret_rotated, list_entry.created, list_entry.deleted, webhook_endpoint.test_sent, webhook_endpoint.verification_requested, webhook_endpoint.delivery_replayed, assessment.created, assessment.outcome_recorded, assessment.deleted, account.outcome_recorded, account.enforcement_recorded, account.deleted, account.exported. A change with no finer name carries the permission it used, such as keys.live.write. A member's read of raw evidence is breach_records.read or review_locations.read, with the assessment and counts and no value. New actions may appear; treat an unknown one as a change to its target."""

    outcome: CustomerExportRequestFilterOutcome

    actor: Actor

    target: AuditEventTarget

    created_at: str

    detail: Optional[Dict[str, str]] = None
    r"""At most 8 short facts about the change, keyed by lowercase names: the role a member was given or accepted (role), the invite an accepted member used (invite_id), the key that replaced a rotated one (new_key_id), the assessment a member's change acted on (assessment_id). Absent when there are none."""

    affected_environment: Optional[Environment] = None

    request_id: Optional[str] = None
    r"""Validated request correlation id, also returned in X-Request-ID, linking this event to request diagnostics. Absent on historical events without correlation."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["detail", "affected_environment", "request_id"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
