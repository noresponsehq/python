from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class IdentifierSubmissionTypedDict(TypedDict):
    value: str
    r"""The original value submitted in assessment_id. Under canonical or mailbox matching the two accounts' values can differ."""
    assessment_id: str
    r"""Opaque, server-assigned assessment id: 'asm_' and a 26-character Crockford base32 ULID. Unique within the workspace; another workspace's assessment id answers 404."""
    submitted_at: str
    r"""When assessment_id was created."""


class IdentifierSubmission(BaseModel):
    value: str
    r"""The original value submitted in assessment_id. Under canonical or mailbox matching the two accounts' values can differ."""

    assessment_id: str
    r"""Opaque, server-assigned assessment id: 'asm_' and a 26-character Crockford base32 ULID. Unique within the workspace; another workspace's assessment id answers 404."""

    submitted_at: str
    r"""When assessment_id was created."""
