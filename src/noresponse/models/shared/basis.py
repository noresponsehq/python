from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Basis = Union[
    Literal[
        "stated",
        "inferred",
        "absence",
    ],
    UnrecognizedStr,
]
r"""stated: read from a record. inferred: reasoned from several facts. absence: every source answered and none found it."""
