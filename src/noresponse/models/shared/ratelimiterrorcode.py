from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


RateLimitErrorCode = Union[
    Literal[
        "rate_limited",
        "assessment_budget_exhausted",
        "export_limit_reached",
    ],
    UnrecognizedStr,
]
r"""Machine codes an HTTP 429 answer can carry."""
