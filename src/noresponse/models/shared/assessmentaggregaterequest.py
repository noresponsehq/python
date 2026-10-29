from __future__ import annotations
from .aggregatedimension import AggregateDimension
from .answerrevision import AnswerRevision
from .band import Band
from .bucket import Bucket
from .decision import Decision
from .flow import Flow
from .impact import Impact
from .lane import Lane
from .listmatch import ListMatch
from .population import Population
from .reasoncode import ReasonCode
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
    "score_outcomes",
    "late_flips",
]


class AssessmentAggregateRequestTypedDict(TypedDict):
    r"""Count this environment's assessments created in [from,to) by bucket, from counts kept as each assessment is first answered, not by scanning assessments. Each assessment counts once, by its first answer (the answer served when it was first answered); later revisions and late results do not count it again, and late_flips counts its later account decision changes. from and to start a bucket (an hour, or a day or a week from Monday that starts at midnight in time_zone, UTC by default), cover at most 366 days (31 for hour buckets, 92 for day and week buckets in a time_zone other than UTC) and from is inside the retention period. The filters are POST /v1/assessments/search's and describe the first answer, so a cell drills down to search with the same filters, revision first and the cell's bucket as from and to. Counts hold no identifier and stay when an assessment or account is deleted or erased; they expire with retention and go with the workspace. Reasons are counted by code and impact band, not by weight. No Idempotency-Key. Select retained_first_answers for exact facet filters and pairs over retained detail. This mode supports count, score_histogram and score_outcomes, and refuses late_flips. It has a 31-day and 100000-record work budget."""

    from_: str
    r"""The first bucket's start."""
    to: str
    r"""The end, excluded: the start of the bucket after the last."""
    bucket: Bucket
    r"""The period each count covers: an hour, or a day or a week (from Monday) in time_zone. Hour buckets are whole UTC hours in any time zone."""
    time_zone: NotRequired[str]
    r"""The IANA time zone whose local midnight starts each day and week bucket, such as Europe/London or Asia/Kolkata; daylight saving changes make those days 23 or 25 hours long. A name the zone database does not know is refused (400 invalid_request naming time_zone). Day and week buckets in a zone other than UTC cover at most 92 days (400 invalid_request naming to); a year of them reads too many hourly counts to answer in time. Hour buckets stay whole UTC hours. Bucket starts, from and to stay instants. With the default population, a zone whose local midnight falls inside a UTC hour (a half-hour offset such as Asia/Kolkata) is refused for day and week buckets, as those counts are kept by the hour; retained_first_answers counts it."""
    group_by: NotRequired[List[AggregateDimension]]
    r"""At most two dimensions to count by, of which at most one is reason, lane, country or asn. An assessment counts once in each of its reasons and incomplete lanes, so those groups can add up to more than the bucket's count. With population retained_first_answers, both dimensions can be facets; counts cover retained first answers only."""
    metrics: NotRequired[List[AssessmentAggregateRequestMetric]]
    r"""count: each bucket's count and groups. score_histogram: first answers by flow and 5-point score bucket. score_outcomes: the histogram's first answers that have a reported outcome, by flow, 5-point score bucket and the latest outcome reported for the assessment (POST /v1/assessments/{assessment_id}/outcomes); the rest of a bin has none reported. late_flips: changes of an assessment's account decision for its flow after its first answer, by from, to and delay."""
    limit: NotRequired[int]
    r"""The most groups answered: the largest over the whole range, then by value. groups_truncated says when there were more."""
    flow: NotRequired[Flow]
    r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""
    status: NotRequired[Status]
    r"""Processing state, separate from evidence coverage. complete: final; nothing is still running, but unsupported, failed or unanswered lanes remain in incomplete_sources. partial: a recommendation exists and evidence is incomplete; assessment_url identifies continuing work when present. pending: no recommendation yet; poll or wait for the webhook. Finished processing does not mean all sources answered."""
    recommendation: NotRequired[Recommendation]
    r"""The recommended action: allow, step_up or review. Your application applies it."""
    decision: NotRequired[Decision]
    r"""An assessment's own decision: block when its stored risk.block is true, otherwise its recommendation. It is not the account's decision or held-admission state."""
    revision: NotRequired[AnswerRevision]
    r"""Which answer of each assessment the filters describe: latest, the latest stored revision, or first, the first answer, as served when the assessment was first answered (POST /v1/assessments/aggregate counts first answers). A cell of an aggregate drills down to POST /v1/assessments/search with the same filters, revision first and the cell's bucket as from and to."""
    population: NotRequired[Population]
    r"""first_answers uses anonymous counters that can include erased detail. retained_first_answers computes exact intersections over retained first answers within 31 days. Requests exceeding the 100000-record work budget are refused."""
    band: NotRequired[Band]
    reason: NotRequired[ReasonCode]
    r"""A stable reason code. New codes may appear; ignore any you do not know."""
    impact: NotRequired[Impact]
    r"""The selected reason's served impact band. Requires reason."""
    lane: NotRequired[Lane]
    r"""An evidence lane: accounts (account presence for email and username), phone, breach, domain (the email domain's registration) and ip."""
    country: NotRequired[str]
    asn: NotRequired[int]
    score_min: NotRequired[int]
    r"""Inclusive lower score bound. Pending answers without a score do not match."""
    score_max: NotRequired[int]
    r"""Inclusive upper score bound, at least score_min when both are supplied."""
    list_match: NotRequired[ListMatch]
    r"""The list action captured at the first answer. Requires revision first. Older answers without captured list state do not match, including none."""


class AssessmentAggregateRequest(BaseModel):
    r"""Count this environment's assessments created in [from,to) by bucket, from counts kept as each assessment is first answered, not by scanning assessments. Each assessment counts once, by its first answer (the answer served when it was first answered); later revisions and late results do not count it again, and late_flips counts its later account decision changes. from and to start a bucket (an hour, or a day or a week from Monday that starts at midnight in time_zone, UTC by default), cover at most 366 days (31 for hour buckets, 92 for day and week buckets in a time_zone other than UTC) and from is inside the retention period. The filters are POST /v1/assessments/search's and describe the first answer, so a cell drills down to search with the same filters, revision first and the cell's bucket as from and to. Counts hold no identifier and stay when an assessment or account is deleted or erased; they expire with retention and go with the workspace. Reasons are counted by code and impact band, not by weight. No Idempotency-Key. Select retained_first_answers for exact facet filters and pairs over retained detail. This mode supports count, score_histogram and score_outcomes, and refuses late_flips. It has a 31-day and 100000-record work budget."""

    from_: Annotated[str, pydantic.Field(alias="from")]
    r"""The first bucket's start."""

    to: str
    r"""The end, excluded: the start of the bucket after the last."""

    bucket: Bucket
    r"""The period each count covers: an hour, or a day or a week (from Monday) in time_zone. Hour buckets are whole UTC hours in any time zone."""

    time_zone: Optional[str] = "UTC"
    r"""The IANA time zone whose local midnight starts each day and week bucket, such as Europe/London or Asia/Kolkata; daylight saving changes make those days 23 or 25 hours long. A name the zone database does not know is refused (400 invalid_request naming time_zone). Day and week buckets in a zone other than UTC cover at most 92 days (400 invalid_request naming to); a year of them reads too many hourly counts to answer in time. Hour buckets stay whole UTC hours. Bucket starts, from and to stay instants. With the default population, a zone whose local midnight falls inside a UTC hour (a half-hour offset such as Asia/Kolkata) is refused for day and week buckets, as those counts are kept by the hour; retained_first_answers counts it."""

    group_by: Optional[List[AggregateDimension]] = None
    r"""At most two dimensions to count by, of which at most one is reason, lane, country or asn. An assessment counts once in each of its reasons and incomplete lanes, so those groups can add up to more than the bucket's count. With population retained_first_answers, both dimensions can be facets; counts cover retained first answers only."""

    metrics: Optional[List[AssessmentAggregateRequestMetric]] = None
    r"""count: each bucket's count and groups. score_histogram: first answers by flow and 5-point score bucket. score_outcomes: the histogram's first answers that have a reported outcome, by flow, 5-point score bucket and the latest outcome reported for the assessment (POST /v1/assessments/{assessment_id}/outcomes); the rest of a bin has none reported. late_flips: changes of an assessment's account decision for its flow after its first answer, by from, to and delay."""

    limit: Optional[int] = 20
    r"""The most groups answered: the largest over the whole range, then by value. groups_truncated says when there were more."""

    flow: Optional[Flow] = None
    r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""

    status: Optional[Status] = None
    r"""Processing state, separate from evidence coverage. complete: final; nothing is still running, but unsupported, failed or unanswered lanes remain in incomplete_sources. partial: a recommendation exists and evidence is incomplete; assessment_url identifies continuing work when present. pending: no recommendation yet; poll or wait for the webhook. Finished processing does not mean all sources answered."""

    recommendation: Optional[Recommendation] = None
    r"""The recommended action: allow, step_up or review. Your application applies it."""

    decision: Optional[Decision] = None
    r"""An assessment's own decision: block when its stored risk.block is true, otherwise its recommendation. It is not the account's decision or held-admission state."""

    revision: Optional[AnswerRevision] = None
    r"""Which answer of each assessment the filters describe: latest, the latest stored revision, or first, the first answer, as served when the assessment was first answered (POST /v1/assessments/aggregate counts first answers). A cell of an aggregate drills down to POST /v1/assessments/search with the same filters, revision first and the cell's bucket as from and to."""

    population: Optional[Population] = None
    r"""first_answers uses anonymous counters that can include erased detail. retained_first_answers computes exact intersections over retained first answers within 31 days. Requests exceeding the 100000-record work budget are refused."""

    band: Optional[Band] = None

    reason: Optional[ReasonCode] = None
    r"""A stable reason code. New codes may appear; ignore any you do not know."""

    impact: Optional[Impact] = None
    r"""The selected reason's served impact band. Requires reason."""

    lane: Optional[Lane] = None
    r"""An evidence lane: accounts (account presence for email and username), phone, breach, domain (the email domain's registration) and ip."""

    country: Optional[str] = None

    asn: Optional[int] = None

    score_min: Optional[int] = None
    r"""Inclusive lower score bound. Pending answers without a score do not match."""

    score_max: Optional[int] = None
    r"""Inclusive upper score bound, at least score_min when both are supplied."""

    list_match: Optional[ListMatch] = None
    r"""The list action captured at the first answer. Requires revision first. Older answers without captured list state do not match, including none."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "time_zone",
                "group_by",
                "metrics",
                "limit",
                "flow",
                "status",
                "recommendation",
                "decision",
                "revision",
                "population",
                "band",
                "reason",
                "impact",
                "lane",
                "country",
                "asn",
                "score_min",
                "score_max",
                "list_match",
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
