from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Status = Union[
    Literal[
        "complete",
        "partial",
        "pending",
    ],
    UnrecognizedStr,
]
r"""Processing state, separate from evidence coverage. complete: final; nothing is still running, but unsupported, failed or unanswered lanes remain in incomplete_sources. partial: a recommendation exists and evidence is incomplete; assessment_url identifies continuing work when present. pending: no recommendation yet; poll or wait for the webhook. Finished processing does not mean all sources answered."""
