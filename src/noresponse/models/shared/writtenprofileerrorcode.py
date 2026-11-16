from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


WrittenProfileErrorCode = Union[
    Literal[
        "no_writer",
        "refused",
        "not_written",
        "uncited_statement",
        "not_answered",
        "worker_attempts_exhausted",
    ],
    UnrecognizedStr,
]
r"""Present only when status is failed. no_writer: no profile writer serves this environment. refused: the model refused. not_written: the answer was not a profile, or no statement survived grounding. uncited_statement: a statement or lead cited a record the person does not hold. not_answered: the writer did not answer. worker_attempts_exhausted: the worker stopped retrying."""
