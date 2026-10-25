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
r"""The submitted email or username whose own search matched the table. A submitted full name is searched as well, and what it finds feeds the identity's reasons rather than this list."""
