from __future__ import annotations
from .basis import Basis
from .certainty import Certainty
from .profilecitation import ProfileCitation, ProfileCitationTypedDict
from .topic import Topic
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ProfileStatementTypedDict(TypedDict):
    topic: Topic
    text: str
    certainty: Certainty
    r"""confirmed: a linked record or the searched identifier states it directly. likely: a strong inference. possible: a weak inference."""
    basis: Basis
    r"""stated: read from a record. inferred: reasoned from several facts. absence: every source answered and none found it."""
    alternatives: List[str]
    r"""Other explanations to keep open for an inference."""
    evidence: List[ProfileCitationTypedDict]
    r"""Every record, post or check the statement rests on."""


class ProfileStatement(BaseModel):
    topic: Topic

    text: str

    certainty: Certainty
    r"""confirmed: a linked record or the searched identifier states it directly. likely: a strong inference. possible: a weak inference."""

    basis: Basis
    r"""stated: read from a record. inferred: reasoned from several facts. absence: every source answered and none found it."""

    alternatives: List[str]
    r"""Other explanations to keep open for an inference."""

    evidence: List[ProfileCitation]
    r"""Every record, post or check the statement rests on."""
