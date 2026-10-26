from __future__ import annotations
from .direction import Direction
from .impact import Impact
from .reasoncode import ReasonCode
from .reasonidentifier import ReasonIdentifier
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountRiskReasonTypedDict(TypedDict):
    r"""One reason that fired. direction is whether it raises or lowers the score, or is neutral (informational, it moves nothing). impact is a coarse band of how much it moves the score: none for a neutral reason, otherwise low, medium or high."""

    code: ReasonCode
    r"""A stable reason code. New codes may appear; ignore any you do not know."""
    direction: Direction
    impact: Impact
    identifier: NotRequired[ReasonIdentifier]
    r"""The submitted identifier or client context field a reason concerns; absent when it concerns the whole assessment. Client context is a claimed hint, not a device fingerprint."""
    weight: Literal[0]
    r"""Deprecated and always 0: the policy's weights are not published. It is sent so that SDK versions that require it keep reading reasons. Read direction and impact."""


class AccountRiskReason(BaseModel):
    r"""One reason that fired. direction is whether it raises or lowers the score, or is neutral (informational, it moves nothing). impact is a coarse band of how much it moves the score: none for a neutral reason, otherwise low, medium or high."""

    code: ReasonCode
    r"""A stable reason code. New codes may appear; ignore any you do not know."""

    direction: Direction

    impact: Impact

    identifier: Optional[ReasonIdentifier] = None
    r"""The submitted identifier or client context field a reason concerns; absent when it concerns the whole assessment. Client context is a claimed hint, not a device fingerprint."""

    weight: Annotated[
        Annotated[Optional[Literal[0]], AfterValidator(validate_const(0))],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="weight",
        ),
    ] = 0
    r"""Deprecated and always 0: the policy's weights are not published. It is sent so that SDK versions that require it keep reading reasons. Read direction and impact."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["identifier", "weight"])
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
    AccountRiskReason.model_rebuild()
except NameError:
    pass
