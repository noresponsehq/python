from __future__ import annotations
from .profilelead import ProfileLead, ProfileLeadTypedDict
from .profilestatement import ProfileStatement, ProfileStatementTypedDict
from .writtenprofileerrorcode import WrittenProfileErrorCode
from .writtenprofilestatus import WrittenProfileStatus
from noresponse.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class WrittenProfileTypedDict(TypedDict):
    status: WrittenProfileStatus
    r"""queued: the profile is being written. written: summary, statements and leads hold it. failed: it could not be written; error_code says why and no content is returned."""
    investigation_id: str
    r"""The investigation whose evidence the profile is written from."""
    queued_at: str
    finished_at: Nullable[str]
    statements: List[ProfileStatementTypedDict]
    r"""Each fact or inference with its certainty and the evidence it cites. Statements that cited evidence the writer was not sent are dropped before storage."""
    leads: List[ProfileLeadTypedDict]
    r"""Values worth searching next, each held by a linked record."""
    error_code: NotRequired[WrittenProfileErrorCode]
    r"""Present only when status is failed. no_writer: no profile writer serves this environment. refused: the model refused. not_written: the answer was not a profile, or no statement survived grounding. uncited_statement: a statement or lead cited a record the person does not hold. not_answered: the writer did not answer. worker_attempts_exhausted: the worker stopped retrying."""
    summary: NotRequired[str]
    r"""Present when written: a few plain sentences with the most useful picture first."""


class WrittenProfile(BaseModel):
    status: WrittenProfileStatus
    r"""queued: the profile is being written. written: summary, statements and leads hold it. failed: it could not be written; error_code says why and no content is returned."""

    investigation_id: str
    r"""The investigation whose evidence the profile is written from."""

    queued_at: str

    finished_at: Nullable[str]

    statements: List[ProfileStatement]
    r"""Each fact or inference with its certainty and the evidence it cites. Statements that cited evidence the writer was not sent are dropped before storage."""

    leads: List[ProfileLead]
    r"""Values worth searching next, each held by a linked record."""

    error_code: Optional[WrittenProfileErrorCode] = None
    r"""Present only when status is failed. no_writer: no profile writer serves this environment. refused: the model refused. not_written: the answer was not a profile, or no statement survived grounding. uncited_statement: a statement or lead cited a record the person does not hold. not_answered: the writer did not answer. worker_attempts_exhausted: the worker stopped retrying."""

    summary: Optional[str] = None
    r"""Present when written: a few plain sentences with the most useful picture first."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["error_code", "summary"])
        nullable_fields = set(["finished_at"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))
            is_nullable_and_explicitly_set = (
                k in nullable_fields
                and (self.__pydantic_fields_set__.intersection({n}))  # pylint: disable=no-member
            )

            if val != UNSET_SENTINEL:
                if (
                    val is not None
                    or k not in optional_fields
                    or is_nullable_and_explicitly_set
                ):
                    m[k] = val

        return m
