from __future__ import annotations
from .aggregatedimension import AggregateDimension
from .answerrevision import AnswerRevision
from .bucket import Bucket
from .decision import Decision
from .flow import Flow
from .recommendation import Recommendation
from .status import Status
from noresponse.types import BaseModel, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


AssessmentAggregateRequestMetric = Literal[
    "count",
    "score_histogram",
    "late_flips",
]


class AssessmentAggregateRequestTypedDict(TypedDict):
    r"""Count this environment's assessments created in [from,to) by bucket, from counts kept as each assessment is first answered, not by scanning assessments. Each assessment counts once, by its first answer (the answer served when it was first answered); later revisions and late results do not count it again, and late_flips counts its later account decision changes. from and to start a bucket (an hour, a UTC day, or a week from Monday 00:00 UTC), cover at most 366 days (31 for hour buckets) and from is inside the retention period. The filters are POST /v1/assessments/search's and describe the first answer, so a cell drills down to search with the same filters, revision first and the cell's bucket as from and to. Counts hold no identifier and stay when an assessment or account is deleted or erased; they expire with retention and go with the workspace. Reasons are counted by code and impact band, not by weight. No Idempotency-Key."""

    from_: str
    r"""The first bucket's start."""
    to: str
    r"""The end, excluded: the start of the bucket after the last."""
    bucket: Bucket
    r"""The period each count covers, in UTC; a week starts on Monday."""
    group_by: NotRequired[List[AggregateDimension]]
    r"""At most two dimensions to count by, of which at most one is reason, lane, country or asn. An assessment counts once in each of its reasons and incomplete lanes, so those groups can add up to more than the bucket's count."""
    metrics: NotRequired[List[AssessmentAggregateRequestMetric]]
    r"""count: each bucket's count and groups. score_histogram: first answers by flow and 5-point score bucket. late_flips: changes of an assessment's account decision for its flow after its first answer, by from, to and delay."""
    limit: NotRequired[int]
    r"""The most groups answered: the largest over the whole range, then by value. groups_truncated says when there were more."""
    flow: NotRequired[Flow]
    r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""
    status: NotRequired[Status]
    r"""complete: final; nothing is still running. A lane that failed or missed its 10 s deadline stays listed in incomplete_sources, and confidence is lower. partial: a recommendation exists and at least one lane is still running or did not settle (see incomplete_sources). pending: nothing usable before the deadline; no recommendation yet, poll or wait for the webhook."""
    recommendation: NotRequired[Recommendation]
    r"""The recommended action: allow, step_up or review. Your application applies it."""
    decision: NotRequired[Decision]
    r"""An assessment's own decision: block when its stored risk.block is true, otherwise its recommendation. It is not the account's decision or held-admission state."""
    revision: NotRequired[AnswerRevision]
    r"""Which answer of each assessment the filters describe: latest, the latest stored revision, or first, the first answer, as served when the assessment was first answered (POST /v1/assessments/aggregate counts first answers). A cell of an aggregate drills down to POST /v1/assessments/search with the same filters, revision first and the cell's bucket as from and to."""


class AssessmentAggregateRequest(BaseModel):
    r"""Count this environment's assessments created in [from,to) by bucket, from counts kept as each assessment is first answered, not by scanning assessments. Each assessment counts once, by its first answer (the answer served when it was first answered); later revisions and late results do not count it again, and late_flips counts its later account decision changes. from and to start a bucket (an hour, a UTC day, or a week from Monday 00:00 UTC), cover at most 366 days (31 for hour buckets) and from is inside the retention period. The filters are POST /v1/assessments/search's and describe the first answer, so a cell drills down to search with the same filters, revision first and the cell's bucket as from and to. Counts hold no identifier and stay when an assessment or account is deleted or erased; they expire with retention and go with the workspace. Reasons are counted by code and impact band, not by weight. No Idempotency-Key."""

    from_: Annotated[str, pydantic.Field(alias="from")]
    r"""The first bucket's start."""

    to: str
    r"""The end, excluded: the start of the bucket after the last."""

    bucket: Bucket
    r"""The period each count covers, in UTC; a week starts on Monday."""

    group_by: Optional[List[AggregateDimension]] = None
    r"""At most two dimensions to count by, of which at most one is reason, lane, country or asn. An assessment counts once in each of its reasons and incomplete lanes, so those groups can add up to more than the bucket's count."""

    metrics: Optional[List[AssessmentAggregateRequestMetric]] = None
    r"""count: each bucket's count and groups. score_histogram: first answers by flow and 5-point score bucket. late_flips: changes of an assessment's account decision for its flow after its first answer, by from, to and delay."""

    limit: Optional[int] = 20
    r"""The most groups answered: the largest over the whole range, then by value. groups_truncated says when there were more."""

    flow: Optional[Flow] = None
    r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""

    status: Optional[Status] = None
    r"""complete: final; nothing is still running. A lane that failed or missed its 10 s deadline stays listed in incomplete_sources, and confidence is lower. partial: a recommendation exists and at least one lane is still running or did not settle (see incomplete_sources). pending: nothing usable before the deadline; no recommendation yet, poll or wait for the webhook."""

    recommendation: Optional[Recommendation] = None
    r"""The recommended action: allow, step_up or review. Your application applies it."""

    decision: Optional[Decision] = None
    r"""An assessment's own decision: block when its stored risk.block is true, otherwise its recommendation. It is not the account's decision or held-admission state."""

    revision: Optional[AnswerRevision] = None
    r"""Which answer of each assessment the filters describe: latest, the latest stored revision, or first, the first answer, as served when the assessment was first answered (POST /v1/assessments/aggregate counts first answers). A cell of an aggregate drills down to POST /v1/assessments/search with the same filters, revision first and the cell's bucket as from and to."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "group_by",
                "metrics",
                "limit",
                "flow",
                "status",
                "recommendation",
                "decision",
                "revision",
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


try:
    AssessmentAggregateRequest.model_rebuild()
except NameError:
    pass
