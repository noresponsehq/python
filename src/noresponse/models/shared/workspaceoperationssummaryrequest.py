from __future__ import annotations
from .auditsettingsenvironment import AuditSettingsEnvironment
from noresponse.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class WorkspaceOperationsSummaryRequestTypedDict(TypedDict):
    r"""Read a past [from,to) interval of at most 31 days. The complete retained populations must fit a combined 100000-row budget and a 1500ms SQL statement budget. No pagination or sampled totals; choose a shorter interval after a row-budget refusal."""

    environment: AuditSettingsEnvironment
    from_: str
    to: str


class WorkspaceOperationsSummaryRequest(BaseModel):
    r"""Read a past [from,to) interval of at most 31 days. The complete retained populations must fit a combined 100000-row budget and a 1500ms SQL statement budget. No pagination or sampled totals; choose a shorter interval after a row-budget refusal."""

    environment: AuditSettingsEnvironment

    from_: Annotated[str, pydantic.Field(alias="from")]

    to: str


try:
    WorkspaceOperationsSummaryRequest.model_rebuild()
except NameError:
    pass
