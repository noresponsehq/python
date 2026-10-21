from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


BreachSelector = Union[
    Literal[
        "email",
        "username",
        "ip",
    ],
    UnrecognizedStr,
]
r"""The submitted identifier a breach table matched on: email or username. Phone and name are not breach selectors."""
