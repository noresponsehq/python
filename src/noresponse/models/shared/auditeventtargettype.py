from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


AuditEventTargetType = Union[
    Literal[
        "workspace",
        "member",
        "invite",
        "key",
        "setting",
        "webhook_endpoint",
        "integration",
        "billing",
        "review",
    ],
    UnrecognizedStr,
]
r"""The kind of resource the change acted on."""
