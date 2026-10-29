from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class OutcomesByOutcomeTypedDict(TypedDict):
    r"""Current customer-reported labels, not independently established ground truth. Missing keys mean zero. Unknown is an explicit report; absent or expired feedback is unreported."""

    confirmed_abuse: NotRequired[int]
    account_takeover: NotRequired[int]
    chargeback: NotRequired[int]
    false_positive: NotRequired[int]
    legitimate: NotRequired[int]
    unknown: NotRequired[int]


class OutcomesByOutcome(BaseModel):
    r"""Current customer-reported labels, not independently established ground truth. Missing keys mean zero. Unknown is an explicit report; absent or expired feedback is unreported."""

    confirmed_abuse: Optional[int] = None

    account_takeover: Optional[int] = None

    chargeback: Optional[int] = None

    false_positive: Optional[int] = None

    legitimate: Optional[int] = None

    unknown: Optional[int] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "confirmed_abuse",
                "account_takeover",
                "chargeback",
                "false_positive",
                "legitimate",
                "unknown",
            ]
        )
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
