from __future__ import annotations
from .auditsettingsenvironment import AuditSettingsEnvironment
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class WorkspaceDeletedTypedDict(TypedDict):
    r"""Terminal for the receiving endpoint's environment: its workspace was deleted. Every key of the environment already answers 401, its assessments and accounts are gone, and no further event follows. The workspace id is not reused, so a later event naming it cannot arrive."""

    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""
    environment: AuditSettingsEnvironment
    deleted_at: str
    r"""When the deletion took effect, equal to deleted_at in the DELETE answer."""


class WorkspaceDeleted(BaseModel):
    r"""Terminal for the receiving endpoint's environment: its workspace was deleted. Every key of the environment already answers 401, its assessments and accounts are gone, and no further event follows. The workspace id is not reused, so a later event naming it cannot arrive."""

    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""

    environment: AuditSettingsEnvironment

    deleted_at: str
    r"""When the deletion took effect, equal to deleted_at in the DELETE answer."""
