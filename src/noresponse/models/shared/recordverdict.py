from __future__ import annotations
from .verdict import Verdict
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class RecordVerdictTypedDict(TypedDict):
    r"""A recorded verdict on one record. A later verdict on the same record replaces it."""

    record_id: str
    verdict: Verdict
    r"""A reviewer's overrule (POST .../people/{person_id}/records), which decides joined whatever the likelihood and sticks for as long as a lookup finds the same record. Absent when nobody overruled it."""
    decided_by: str
    decided_at: str


class RecordVerdict(BaseModel):
    r"""A recorded verdict on one record. A later verdict on the same record replaces it."""

    record_id: str

    verdict: Verdict
    r"""A reviewer's overrule (POST .../people/{person_id}/records), which decides joined whatever the likelihood and sticks for as long as a lookup finds the same record. Absent when nobody overruled it."""

    decided_by: str

    decided_at: str
