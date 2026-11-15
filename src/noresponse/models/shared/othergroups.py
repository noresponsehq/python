from __future__ import annotations
from .othergroup import OtherGroup, OtherGroupTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class OtherGroupsTypedDict(TypedDict):
    r"""Where else in the environment the person appears, read live from those groups: deleting one removes it here."""

    total: int
    r"""How many other groups include this person, of which items lists the 20 most recent."""
    items: List[OtherGroupTypedDict]
    r"""This person's memberships in the 20 most recent other groups, newest group first."""


class OtherGroups(BaseModel):
    r"""Where else in the environment the person appears, read live from those groups: deleting one removes it here."""

    total: int
    r"""How many other groups include this person, of which items lists the 20 most recent."""

    items: List[OtherGroup]
    r"""This person's memberships in the 20 most recent other groups, newest group first."""
