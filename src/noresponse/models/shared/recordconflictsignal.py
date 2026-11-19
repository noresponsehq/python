from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


RecordConflictSignal = Union[Literal["anchors_disagree",], UnrecognizedStr]
r"""anchors_disagree: records found by two of the identifiers you gave clash with each other, so those identifiers may belong to different people."""
