from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ErrorCode = Union[
    Literal[
        "not_answered",
        "no_source",
        "worker_attempts_exhausted",
    ],
    UnrecognizedStr,
]
r"""Why a failed search found nothing: its sources did not answer, none could be asked, or it could not run before its attempts were spent."""
