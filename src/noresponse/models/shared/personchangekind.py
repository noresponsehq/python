from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


PersonChangeKind = Union[
    Literal[
        "account_added",
        "account_removed",
        "breach_added",
        "breach_removed",
        "identifier_added",
        "identifier_removed",
        "field_changed",
        "posts_added",
    ],
    UnrecognizedStr,
]
r"""account_added and account_removed: an account or profile appeared or disappeared. breach_added and breach_removed: a breach record appeared or disappeared. identifier_added and identifier_removed: an email, phone, username, name or account id on an account the person already held. field_changed: another field on such an account. posts_added: new posts, counted in count."""
