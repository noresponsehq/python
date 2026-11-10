from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ScreeningLookupCheckStatus = Union[
    Literal[
        "found",
        "not_found",
        "partial",
        "not_covered",
    ],
    UnrecognizedStr,
]
r"""found: a source found the identifier. not_found: every source answered and none found it. partial: the sources that answered found nothing and the others did not answer. not_covered: no source answered. A lookup that failed reads partial or not_covered, not not_found."""
