from __future__ import annotations
from .flowsettings import FlowSettings, FlowSettingsTypedDict
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class SettingsFlowsTypedDict(TypedDict):
    account_creation: FlowSettingsTypedDict
    r"""One flow's policy in force. A score below step_up is allow, below review step_up, and from review review; from block, when present, the decision is block. admission says when the flow's decision is final."""
    login: FlowSettingsTypedDict
    r"""One flow's policy in force. A score below step_up is allow, below review step_up, and from review review; from block, when present, the decision is block. admission says when the flow's decision is final."""
    purchase: FlowSettingsTypedDict
    r"""One flow's policy in force. A score below step_up is allow, below review step_up, and from review review; from block, when present, the decision is block. admission says when the flow's decision is final."""


class SettingsFlows(BaseModel):
    account_creation: FlowSettings
    r"""One flow's policy in force. A score below step_up is allow, below review step_up, and from review review; from block, when present, the decision is block. admission says when the flow's decision is final."""

    login: FlowSettings
    r"""One flow's policy in force. A score below step_up is allow, below review step_up, and from review review; from block, when present, the decision is block. admission says when the flow's decision is final."""

    purchase: FlowSettings
    r"""One flow's policy in force. A score below step_up is allow, below review step_up, and from review review; from block, when present, the decision is block. admission says when the flow's decision is final."""
