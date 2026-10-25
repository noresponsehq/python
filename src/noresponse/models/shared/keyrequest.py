from __future__ import annotations
from .keyenvironment import KeyEnvironment
from noresponse.types import BaseModel
from typing import List, Literal
from typing_extensions import TypedDict


KeyRequestScope = Literal[
    "assess",
    "history",
    "delete",
    "webhooks",
    "detailed",
    "integrations",
    "management",
]


class KeyRequestTypedDict(TypedDict):
    r"""POST /v1/workspaces/{workspace_id}/keys body. Creates an API key in one environment of the workspace with the scopes named, and returns its secret once. A live key needs the admin or owner role; a test key needs developer or above. An API key with the management scope creates keys in its own environment with scopes it holds itself. Each scope may appear once."""

    environment: KeyEnvironment
    r"""The environment the key belongs to. A live key assesses with live sources; a test key answers from the deterministic simulator."""
    scopes: List[KeyRequestScope]
    r"""The key's scopes, each at most once."""


class KeyRequest(BaseModel):
    r"""POST /v1/workspaces/{workspace_id}/keys body. Creates an API key in one environment of the workspace with the scopes named, and returns its secret once. A live key needs the admin or owner role; a test key needs developer or above. An API key with the management scope creates keys in its own environment with scopes it holds itself. Each scope may appear once."""

    environment: KeyEnvironment
    r"""The environment the key belongs to. A live key assesses with live sources; a test key answers from the deterministic simulator."""

    scopes: List[KeyRequestScope]
    r"""The key's scopes, each at most once."""
