from __future__ import annotations
from .policyevaluation import PolicyEvaluation, PolicyEvaluationTypedDict
from .report import Report, ReportTypedDict
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class PolicyEvaluationResultTypedDict(TypedDict):
    r"""The evaluation report and its provenance. A no_change report cannot authorise publication."""

    evaluation: PolicyEvaluationTypedDict
    report: ReportTypedDict


class PolicyEvaluationResult(BaseModel):
    r"""The evaluation report and its provenance. A no_change report cannot authorise publication."""

    evaluation: PolicyEvaluation

    report: Report
