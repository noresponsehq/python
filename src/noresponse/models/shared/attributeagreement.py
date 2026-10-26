from __future__ import annotations
from .agreement import Agreement
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class AttributeAgreementTypedDict(TypedDict):
    r"""How far independent sources agree on one attribute: values is the number of distinct values reported, support the tables and profiles reporting any, and agreement match (one value), partial (the most reported value holds more than half the support) or mismatch. The values themselves are not served."""

    agreement: Agreement
    values: int
    support: int


class AttributeAgreement(BaseModel):
    r"""How far independent sources agree on one attribute: values is the number of distinct values reported, support the tables and profiles reporting any, and agreement match (one value), partial (the most reported value holds more than half the support) or mismatch. The values themselves are not served."""

    agreement: Agreement

    values: int

    support: int
