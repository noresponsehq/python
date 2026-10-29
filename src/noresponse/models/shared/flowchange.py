from __future__ import annotations
from .admission import Admission
from .onexpiry import OnExpiry
from .usagecountdepth import UsageCountDepth
from noresponse.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class FlowChangeTypedDict(TypedDict):
    r"""A change to one flow. A field left out keeps the value in force. Thresholds set on login or purchase start from the values in force, account_creation's while it inherits them. After the change, 0 < step_up < review <= 100 and block is off or review <= block <= 100."""

    step_up: NotRequired[int]
    review: NotRequired[int]
    block: NotRequired[Nullable[int]]
    r"""The score from which the decision is block; null turns blocking off."""
    default_depth: NotRequired[UsageCountDepth]
    r"""assessments only."""
    inherits_account_creation: NotRequired[bool]
    r"""Login or purchase only: drop the flow's own thresholds so it uses account_creation's again. Not combined with step_up, review or block. Send true; false is refused."""
    inherits_signup: NotRequired[bool]
    r"""Alias of inherits_account_creation, still accepted. Send true; false is refused."""
    admission: NotRequired[Admission]
    r"""immediate (the default): an assessment of this flow is decided from the evidence its answer has, and later evidence may change the decision. held: while the account's current assessment of this flow has not completed, the account's decision for the flow is held, and the final decision arrives as account.risk_changed when the investigation completes or hold_seconds pass, whichever is first. Each flow has its own admission."""
    hold_seconds: NotRequired[int]
    r"""How long a held flow's assessment is held after it was created, 30 to 86400 seconds (default 300). Kept while the flow is immediate."""
    on_expiry: NotRequired[OnExpiry]
    r"""The decision a held assessment takes when hold_seconds pass before its investigation completes, unless the evidence so far gives a stricter one (default review). It is announced as account.risk_changed like any other change, so an expired hold is always announced. A hosted provider hook, which cannot wait, answers a held account by it at once: deny for block, allow otherwise. Kept while the flow is immediate."""


class FlowChange(BaseModel):
    r"""A change to one flow. A field left out keeps the value in force. Thresholds set on login or purchase start from the values in force, account_creation's while it inherits them. After the change, 0 < step_up < review <= 100 and block is off or review <= block <= 100."""

    step_up: Optional[int] = None

    review: Optional[int] = None

    block: OptionalNullable[int] = UNSET
    r"""The score from which the decision is block; null turns blocking off."""

    default_depth: Optional[UsageCountDepth] = None
    r"""assessments only."""

    inherits_account_creation: Optional[bool] = None
    r"""Login or purchase only: drop the flow's own thresholds so it uses account_creation's again. Not combined with step_up, review or block. Send true; false is refused."""

    inherits_signup: Annotated[
        Optional[bool],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = None
    r"""Alias of inherits_account_creation, still accepted. Send true; false is refused."""

    admission: Optional[Admission] = None
    r"""immediate (the default): an assessment of this flow is decided from the evidence its answer has, and later evidence may change the decision. held: while the account's current assessment of this flow has not completed, the account's decision for the flow is held, and the final decision arrives as account.risk_changed when the investigation completes or hold_seconds pass, whichever is first. Each flow has its own admission."""

    hold_seconds: Optional[int] = None
    r"""How long a held flow's assessment is held after it was created, 30 to 86400 seconds (default 300). Kept while the flow is immediate."""

    on_expiry: Optional[OnExpiry] = None
    r"""The decision a held assessment takes when hold_seconds pass before its investigation completes, unless the evidence so far gives a stricter one (default review). It is announced as account.risk_changed like any other change, so an expired hold is always announced. A hosted provider hook, which cannot wait, answers a held account by it at once: deny for block, allow otherwise. Kept while the flow is immediate."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "step_up",
                "review",
                "block",
                "default_depth",
                "inherits_account_creation",
                "inherits_signup",
                "admission",
                "hold_seconds",
                "on_expiry",
            ]
        )
        nullable_fields = set(["block"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))
            is_nullable_and_explicitly_set = (
                k in nullable_fields
                and (self.__pydantic_fields_set__.intersection({n}))  # pylint: disable=no-member
            )

            if val != UNSET_SENTINEL:
                if (
                    val is not None
                    or k not in optional_fields
                    or is_nullable_and_explicitly_set
                ):
                    m[k] = val

        return m
