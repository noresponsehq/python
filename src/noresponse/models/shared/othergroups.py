from __future__ import annotations
from .othergroup import OtherGroup, OtherGroupTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class OtherGroupsTypedDict(TypedDict):
    r"""Where else in the environment the person appears, read live from those groups: deleting one removes it here."""

    total: int
    r"""How many people of other groups match, of which items lists the 20 most recent."""
    items: List[OtherGroupTypedDict]
    r"""The 20 people of the most recent other groups, newest group first."""


class OtherGroups(BaseModel):
    r"""Where else in the environment the person appears, read live from those groups: deleting one removes it here."""

    total: int
    r"""How many people of other groups match, of which items lists the 20 most recent."""

    items: List[OtherGroup]
    r"""The 20 people of the most recent other groups, newest group first."""
