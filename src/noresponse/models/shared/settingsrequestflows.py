from __future__ import annotations
from .flowchange import FlowChange, FlowChangeTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class SettingsRequestFlowsTypedDict(TypedDict):
    r"""Use account_creation or its deprecated alias signup, not both."""

    account_creation: NotRequired[FlowChangeTypedDict]
    r"""A change to one flow. A field left out keeps the value in force. Thresholds set on login or purchase start from the values in force, account_creation's while it inherits them. After the change, 0 < step_up < review <= 100 and block is off or review <= block <= 100."""
    login: NotRequired[FlowChangeTypedDict]
    r"""A change to one flow. A field left out keeps the value in force. Thresholds set on login or purchase start from the values in force, account_creation's while it inherits them. After the change, 0 < step_up < review <= 100 and block is off or review <= block <= 100."""
    purchase: NotRequired[FlowChangeTypedDict]
    r"""A change to one flow. A field left out keeps the value in force. Thresholds set on login or purchase start from the values in force, account_creation's while it inherits them. After the change, 0 < step_up < review <= 100 and block is off or review <= block <= 100."""
    signup: NotRequired[FlowChangeTypedDict]
    r"""A change to one flow. A field left out keeps the value in force. Thresholds set on login or purchase start from the values in force, account_creation's while it inherits them. After the change, 0 < step_up < review <= 100 and block is off or review <= block <= 100."""


class SettingsRequestFlows(BaseModel):
    r"""Use account_creation or its deprecated alias signup, not both."""

    account_creation: Optional[FlowChange] = None
    r"""A change to one flow. A field left out keeps the value in force. Thresholds set on login or purchase start from the values in force, account_creation's while it inherits them. After the change, 0 < step_up < review <= 100 and block is off or review <= block <= 100."""

    login: Optional[FlowChange] = None
    r"""A change to one flow. A field left out keeps the value in force. Thresholds set on login or purchase start from the values in force, account_creation's while it inherits them. After the change, 0 < step_up < review <= 100 and block is off or review <= block <= 100."""

    purchase: Optional[FlowChange] = None
    r"""A change to one flow. A field left out keeps the value in force. Thresholds set on login or purchase start from the values in force, account_creation's while it inherits them. After the change, 0 < step_up < review <= 100 and block is off or review <= block <= 100."""

    signup: Optional[FlowChange] = None
    r"""A change to one flow. A field left out keeps the value in force. Thresholds set on login or purchase start from the values in force, account_creation's while it inherits them. After the change, 0 < step_up < review <= 100 and block is off or review <= block <= 100."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["account_creation", "login", "purchase", "signup"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
