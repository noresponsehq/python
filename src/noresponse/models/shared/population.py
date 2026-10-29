from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Population = Union[
    Literal[
        "first_answers",
        "retained_first_answers",
    ],
    UnrecognizedStr,
]
r"""first_answers uses anonymous counters that can include erased detail. retained_first_answers computes exact intersections over retained first answers within 31 days. Requests exceeding the 100000-record work budget are refused."""
