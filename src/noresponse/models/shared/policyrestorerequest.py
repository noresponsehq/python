from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class PolicyRestoreRequestTypedDict(TypedDict):
    r"""Publish a captured configuration as a new version. Version checks and publication are atomic. Longer retention does not revive expired records, and restored policy does not undo customer enforcement."""

    version: int
    expected_policy_version: int
    change_reason: str


class PolicyRestoreRequest(BaseModel):
    r"""Publish a captured configuration as a new version. Version checks and publication are atomic. Longer retention does not revive expired records, and restored policy does not undo customer enforcement."""

    version: int

    expected_policy_version: int

    change_reason: str
