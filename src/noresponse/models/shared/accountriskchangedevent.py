from __future__ import annotations
from .accountriskchanged import AccountRiskChanged, AccountRiskChangedTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountRiskChangedEventTypedDict(TypedDict):
    r"""The account.risk_changed event."""

    id: str
    r"""The event id, equal to the NR-Webhook-Id header and across redeliveries and every endpoint the event fans out to."""
    created_at: str
    r"""When the event was created. Equal across redeliveries; the signing timestamp header is per delivery."""
    data: AccountRiskChangedTypedDict
    r"""The account's decision for at least one flow changed. account is the account as GET /v1/accounts/{account_id} answers it for the revision that made the change: its new score, decision, reasons and decisions_by_flow, and the assessment the risk comes from. previous_decisions_by_flow are the decisions it replaced, so account.decisions_by_flow differs from them for at least one flow. On the account's first decision, previous_decisions_by_flow is allow for every flow. Events of one account are not ordered: account.risk_version orders them, so keep the account with the highest risk_version and ignore an event whose account is older than the one held."""
    type: Literal["account.risk_changed"]
    r"""Always account.risk_changed."""
    test: NotRequired[bool]
    r"""Present, and true, only on an event sent by POST /v1/webhooks/{endpoint_id}/test: its data is a fixed example assessment, not one of the workspace's, so a receiver acknowledges it and applies nothing. Real events have no test member."""


class AccountRiskChangedEvent(BaseModel):
    r"""The account.risk_changed event."""

    id: str
    r"""The event id, equal to the NR-Webhook-Id header and across redeliveries and every endpoint the event fans out to."""

    created_at: str
    r"""When the event was created. Equal across redeliveries; the signing timestamp header is per delivery."""

    data: AccountRiskChanged
    r"""The account's decision for at least one flow changed. account is the account as GET /v1/accounts/{account_id} answers it for the revision that made the change: its new score, decision, reasons and decisions_by_flow, and the assessment the risk comes from. previous_decisions_by_flow are the decisions it replaced, so account.decisions_by_flow differs from them for at least one flow. On the account's first decision, previous_decisions_by_flow is allow for every flow. Events of one account are not ordered: account.risk_version orders them, so keep the account with the highest risk_version and ignore an event whose account is older than the one held."""

    type: Annotated[
        Annotated[
            Literal["account.risk_changed"],
            AfterValidator(validate_const("account.risk_changed")),
        ],
        pydantic.Field(alias="type"),
    ] = "account.risk_changed"
    r"""Always account.risk_changed."""

    test: Optional[bool] = None
    r"""Present, and true, only on an event sent by POST /v1/webhooks/{endpoint_id}/test: its data is a fixed example assessment, not one of the workspace's, so a receiver acknowledges it and applies nothing. Real events have no test member."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["test"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


try:
    AccountRiskChangedEvent.model_rebuild()
except NameError:
    pass
