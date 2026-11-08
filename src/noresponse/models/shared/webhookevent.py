from __future__ import annotations
from .accountdeletedevent import AccountDeletedEvent, AccountDeletedEventTypedDict
from .accountriskchangedevent import (
    AccountRiskChangedEvent,
    AccountRiskChangedEventTypedDict,
)
from .assessmentupdatedevent import (
    AssessmentUpdatedEvent,
    AssessmentUpdatedEventTypedDict,
)
from .attendeedecidedevent import AttendeeDecidedEvent, AttendeeDecidedEventTypedDict
from .attendeeflaggedevent import AttendeeFlaggedEvent, AttendeeFlaggedEventTypedDict
from .auditeventevent import AuditEventEvent, AuditEventEventTypedDict
from .endpointverificationevent import (
    EndpointVerificationEvent,
    EndpointVerificationEventTypedDict,
)
from .screeningcompletedevent import (
    ScreeningCompletedEvent,
    ScreeningCompletedEventTypedDict,
)
from .webhookendpointdisabledevent import (
    WebhookEndpointDisabledEvent,
    WebhookEndpointDisabledEventTypedDict,
)
from .workspacedeletedevent import WorkspaceDeletedEvent, WorkspaceDeletedEventTypedDict
from pydantic import Field
from typing import Union
from typing_extensions import Annotated, TypeAliasType


WebhookEventTypedDict = TypeAliasType(
    "WebhookEventTypedDict",
    Union[
        AssessmentUpdatedEventTypedDict,
        EndpointVerificationEventTypedDict,
        AccountDeletedEventTypedDict,
        WorkspaceDeletedEventTypedDict,
        WebhookEndpointDisabledEventTypedDict,
        AccountRiskChangedEventTypedDict,
        AuditEventEventTypedDict,
        ScreeningCompletedEventTypedDict,
        AttendeeFlaggedEventTypedDict,
        AttendeeDecidedEventTypedDict,
    ],
)
r"""The body of every webhook delivery: {id, type, created_at, data}, where type chooses the shape of data. Deliveries are at least once and unordered: deduplicate on id, and keep an assessment only when its detail.assessment_version is newer than the one you hold. GET /v1/assessments/{assessment_id} stays authoritative."""


WebhookEvent = Annotated[
    Union[
        AssessmentUpdatedEvent,
        EndpointVerificationEvent,
        AccountDeletedEvent,
        WorkspaceDeletedEvent,
        WebhookEndpointDisabledEvent,
        AccountRiskChangedEvent,
        AuditEventEvent,
        ScreeningCompletedEvent,
        AttendeeFlaggedEvent,
        AttendeeDecidedEvent,
    ],
    Field(discriminator="type"),
]
r"""The body of every webhook delivery: {id, type, created_at, data}, where type chooses the shape of data. Deliveries are at least once and unordered: deduplicate on id, and keep an assessment only when its detail.assessment_version is newer than the one you hold. GET /v1/assessments/{assessment_id} stays authoritative."""
