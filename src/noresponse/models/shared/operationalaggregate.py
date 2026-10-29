from __future__ import annotations
from .operationalaggregatebucket import (
    OperationalAggregateBucket,
    OperationalAggregateBucketTypedDict,
)
from .operationalaggregatequeue import (
    OperationalAggregateQueue,
    OperationalAggregateQueueTypedDict,
)
from .operationalaggregatetotals import (
    OperationalAggregateTotals,
    OperationalAggregateTotalsTypedDict,
)
from .requestaggregaterequestbucket import RequestAggregateRequestBucket
from .source import Source
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class OperationalAggregateTypedDict(TypedDict):
    r"""One repeatable-read snapshot of retained request diagnostics or webhook attempts. Capture can have gaps and these counts are not a billing ledger. Unattributed keys include older requests and member requests. Queue state is current retained work, not a delivery success denominator."""

    source: Source
    from_: str
    to: str
    as_of: str
    retained_from: str
    retention_days: int
    bucket: RequestAggregateRequestBucket
    totals: OperationalAggregateTotalsTypedDict
    buckets: List[OperationalAggregateBucketTypedDict]
    r"""Nonempty UTC buckets in ascending order. Counts include all retained matching attempts, without the log page limit."""
    schema_version: Literal["1"]
    capture: Literal["best_effort"]
    population: Literal["retained_attempts"]
    queue: NotRequired[OperationalAggregateQueueTypedDict]
    r"""Current retained delivery queue, independent of the requested attempt window and status filter. Endpoint filter applies. Does not prove customer enforcement execution."""


class OperationalAggregate(BaseModel):
    r"""One repeatable-read snapshot of retained request diagnostics or webhook attempts. Capture can have gaps and these counts are not a billing ledger. Unattributed keys include older requests and member requests. Queue state is current retained work, not a delivery success denominator."""

    source: Source

    from_: Annotated[str, pydantic.Field(alias="from")]

    to: str

    as_of: str

    retained_from: str

    retention_days: int

    bucket: RequestAggregateRequestBucket

    totals: OperationalAggregateTotals

    buckets: List[OperationalAggregateBucket]
    r"""Nonempty UTC buckets in ascending order. Counts include all retained matching attempts, without the log page limit."""

    schema_version: Annotated[
        Annotated[Literal["1"], AfterValidator(validate_const("1"))],
        pydantic.Field(alias="schema_version"),
    ] = "1"

    capture: Annotated[
        Annotated[
            Literal["best_effort"], AfterValidator(validate_const("best_effort"))
        ],
        pydantic.Field(alias="capture"),
    ] = "best_effort"

    population: Annotated[
        Annotated[
            Literal["retained_attempts"],
            AfterValidator(validate_const("retained_attempts")),
        ],
        pydantic.Field(alias="population"),
    ] = "retained_attempts"

    queue: Optional[OperationalAggregateQueue] = None
    r"""Current retained delivery queue, independent of the requested attempt window and status filter. Endpoint filter applies. Does not prove customer enforcement execution."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["queue"])
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
    OperationalAggregate.model_rebuild()
except NameError:
    pass
