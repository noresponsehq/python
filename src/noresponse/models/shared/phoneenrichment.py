from __future__ import annotations
from .phoneenrichmentfields import PhoneEnrichmentFields, PhoneEnrichmentFieldsTypedDict
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class PhoneEnrichmentTypedDict(TypedDict):
    r"""Facts about the number only: line type, carrier and country. The upstream provider, its scores and its verdicts stay internal."""

    fields: PhoneEnrichmentFieldsTypedDict


class PhoneEnrichment(BaseModel):
    r"""Facts about the number only: line type, carrier and country. The upstream provider, its scores and its verdicts stay internal."""

    fields: PhoneEnrichmentFields
