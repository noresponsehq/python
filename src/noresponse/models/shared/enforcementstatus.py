from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


EnforcementStatus = Union[
    Literal[
        "applied",
        "failed",
    ],
    UnrecognizedStr,
]
r"""applied when the identity provider accepted the action, failed when it refused it or could not be reached. Only applied counts as enforced."""
