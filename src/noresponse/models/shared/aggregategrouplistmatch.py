from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


AggregateGroupListMatch = Union[
    Literal[
        "block",
        "allow",
        "none",
    ],
    UnrecognizedStr,
]
r"""The list action captured with the first answer. none means no matching entry was found. For retained_first_answers an absent field means the older assessment did not capture list state; this remains a separate group."""
