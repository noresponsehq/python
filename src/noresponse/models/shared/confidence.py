from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Confidence = Union[
    Literal[
        "low",
        "medium",
        "high",
        "unavailable",
    ],
    UnrecognizedStr,
]
r"""Evidence coverage: how much of the planned source evidence gave a definite answer. This is not confidence that an identity is genuine, agreement between identifiers, a risk score or a probability. unavailable means no usable evidence answered; a terminal uncovered assessment can have this value and recommend review."""
