from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


BreachConduct = Union[
    Literal[
        "chargeback",
        "declined_payment",
        "forum_sanction",
    ],
    UnrecognizedStr,
]
r"""What a breach table's rows record against the identifier: chargeback, one or more chargebacks; declined_payment, one or more declined payments; forum_sanction, a forum ban, warning or infraction. A category and not a value: the schema has no member for one."""
