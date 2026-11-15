from __future__ import annotations
from .screeningdepth import ScreeningDepth
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class InvestigationRequestTypedDict(TypedDict):
    r"""Runs a new investigation against one retained workspace person."""

    depth: ScreeningDepth
    platforms: List[str]
    person_id: str


class InvestigationRequest(BaseModel):
    r"""Runs a new investigation against one retained workspace person."""

    depth: ScreeningDepth

    platforms: List[str]

    person_id: str
