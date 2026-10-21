from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


BreachExposed = Union[
    Literal[
        "email",
        "username",
        "name",
        "password",
        "password_hash",
        "phone",
        "address",
        "dob",
        "ip",
        "payment",
        "security_qa",
    ],
    UnrecognizedStr,
]
r"""The kind of data a breach table held beside the identifier. password means a plaintext password was present and password_hash means a hash, salt or token was present. The value itself is not stored or returned; the schema has no member for one."""
