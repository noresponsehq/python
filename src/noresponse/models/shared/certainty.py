from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Certainty = Union[
    Literal[
        "confirmed",
        "likely",
        "possible",
    ],
    UnrecognizedStr,
]
r"""confirmed: a linked record or the searched identifier states it directly. likely: a strong inference. possible: a weak inference."""
