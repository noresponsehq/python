from __future__ import annotations
from .recordconflictsignal import RecordConflictSignal
from noresponse.types import BaseModel, UnrecognizedStr
from typing import List, Literal, Union
from typing_extensions import TypedDict


Between = Union[
    Literal[
        "email",
        "phone",
    ],
    UnrecognizedStr,
]


class RecordConflictTypedDict(TypedDict):
    r"""Two identifiers you gave that lead to records of different people."""

    signal: RecordConflictSignal
    r"""anchors_disagree: records found by two of the identifiers you gave clash with each other, so those identifiers may belong to different people."""
    kind: str
    r"""The kind of value that clashes: person_name or born."""
    between: List[Between]
    r"""The two identifiers you gave whose records disagree."""
    records: List[str]
    r"""The ids of the two records that clash, in the order of between."""


class RecordConflict(BaseModel):
    r"""Two identifiers you gave that lead to records of different people."""

    signal: RecordConflictSignal
    r"""anchors_disagree: records found by two of the identifiers you gave clash with each other, so those identifiers may belong to different people."""

    kind: str
    r"""The kind of value that clashes: person_name or born."""

    between: List[Between]
    r"""The two identifiers you gave whose records disagree."""

    records: List[str]
    r"""The ids of the two records that clash, in the order of between."""
