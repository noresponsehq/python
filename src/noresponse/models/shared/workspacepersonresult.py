from __future__ import annotations
from .personmatch import PersonMatch, PersonMatchTypedDict
from .workspaceperson import WorkspacePerson, WorkspacePersonTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class WorkspacePersonResultTypedDict(TypedDict):
    r"""Create or reuse a workspace person."""

    person: WorkspacePersonTypedDict
    suggested_matches: List[PersonMatchTypedDict]
    created: bool


class WorkspacePersonResult(BaseModel):
    r"""Create or reuse a workspace person."""

    person: WorkspacePerson

    suggested_matches: List[PersonMatch]

    created: bool
