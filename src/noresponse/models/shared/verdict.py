from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Verdict = Union[
    Literal[
        "joined",
        "rejected",
    ],
    UnrecognizedStr,
]
r"""A reviewer's overrule (POST .../people/{person_id}/records), which decides joined whatever the likelihood and sticks for as long as a lookup finds the same record. Absent when nobody overruled it."""
