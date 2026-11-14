from __future__ import annotations
from .verdict import Verdict
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class RecordVerdictRequestTypedDict(TypedDict):
    r"""A reviewer's verdict on whether one of a person's lookup records is theirs."""

    record_id: str
    r"""One of the person's lookup records."""
    verdict: Verdict
    r"""A reviewer's overrule (POST .../people/{person_id}/records), which decides joined whatever the likelihood and sticks for as long as a lookup finds the same record. Absent when nobody overruled it."""


class RecordVerdictRequest(BaseModel):
    r"""A reviewer's verdict on whether one of a person's lookup records is theirs."""

    record_id: str
    r"""One of the person's lookup records."""

    verdict: Verdict
    r"""A reviewer's overrule (POST .../people/{person_id}/records), which decides joined whatever the likelihood and sticks for as long as a lookup finds the same record. Absent when nobody overruled it."""
