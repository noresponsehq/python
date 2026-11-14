from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Rating = Union[
    Literal[
        "unique",
        "distinctive",
        "common",
    ],
    UnrecognizedStr,
]
r"""unique: an email or phone, which belongs to one person by design. distinctive: rare enough that a new search on it likely finds one person. common: shared by many people, so a search on it finds strangers. A new search is suggested for unique and distinctive values only; any value can still be searched."""
