from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


SchedulePeriod = Union[
    Literal[
        "daily",
        "weekly",
        "monthly",
        "off",
    ],
    UnrecognizedStr,
]
r"""How often the person is investigated again: daily, weekly or monthly, counted from when the schedule was set; off runs no scheduled investigation."""
