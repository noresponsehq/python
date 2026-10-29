from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Role = Union[
    Literal[
        "owner",
        "admin",
        "developer",
        "viewer",
        "investigator",
        "auditor",
        "billing",
    ],
    UnrecognizedStr,
]
r"""A built-in capability set. Specialist roles are independent; effective access is returned by GET /v1/workspaces/{workspace_id}/capabilities."""
