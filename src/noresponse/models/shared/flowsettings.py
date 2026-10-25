from __future__ import annotations
from .admission import Admission
from .defaultdepth import DefaultDepth
from .onexpiry import OnExpiry
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class FlowSettingsTypedDict(TypedDict):
    r"""One flow's policy in force. A score below step_up is allow, below review step_up, and from review review; from block, when present, the decision is block. admission says when the flow's decision is final."""

    step_up: int
    review: int
    default_depth: DefaultDepth
    r"""The depth a request for this flow that names none is served at. Defaults: full for account_creation and purchase, quick for login."""
    inherits_account_creation: bool
    r"""true while this flow has no thresholds of its own and uses account_creation's, the default for login and purchase. Always false for signup."""
    admission: Admission
    r"""immediate (the default): an assessment of this flow is decided from the evidence its answer has, and later evidence may change the decision. held: while the account's current assessment of this flow has not completed, the account's decision for the flow is held, and the final decision arrives as account.risk_changed when the investigation completes or hold_seconds pass, whichever is first. Each flow has its own admission."""
    hold_seconds: int
    r"""How long a held flow's assessment is held after it was created, 30 to 86400 seconds (default 300). Kept while the flow is immediate."""
    on_expiry: OnExpiry
    r"""The decision a held assessment takes when hold_seconds pass before its investigation completes, unless the evidence so far gives a stricter one (default review). It is announced as account.risk_changed like any other change, so an expired hold is always announced. A hosted provider hook, which cannot wait, answers a held account by it at once: deny for block, allow otherwise. Kept while the flow is immediate."""
    block: NotRequired[int]
    r"""The score from which the decision is block. Absent while blocking is off, the default."""


class FlowSettings(BaseModel):
    r"""One flow's policy in force. A score below step_up is allow, below review step_up, and from review review; from block, when present, the decision is block. admission says when the flow's decision is final."""

    step_up: int

    review: int

    default_depth: DefaultDepth
    r"""The depth a request for this flow that names none is served at. Defaults: full for account_creation and purchase, quick for login."""

    inherits_account_creation: bool
    r"""true while this flow has no thresholds of its own and uses account_creation's, the default for login and purchase. Always false for signup."""

    admission: Admission
    r"""immediate (the default): an assessment of this flow is decided from the evidence its answer has, and later evidence may change the decision. held: while the account's current assessment of this flow has not completed, the account's decision for the flow is held, and the final decision arrives as account.risk_changed when the investigation completes or hold_seconds pass, whichever is first. Each flow has its own admission."""

    hold_seconds: int
    r"""How long a held flow's assessment is held after it was created, 30 to 86400 seconds (default 300). Kept while the flow is immediate."""

    on_expiry: OnExpiry
    r"""The decision a held assessment takes when hold_seconds pass before its investigation completes, unless the evidence so far gives a stricter one (default review). It is announced as account.risk_changed like any other change, so an expired hold is always announced. A hosted provider hook, which cannot wait, answers a held account by it at once: deny for block, allow otherwise. Kept while the flow is immediate."""

    block: Optional[int] = None
    r"""The score from which the decision is block. Absent while blocking is off, the default."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["block"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
