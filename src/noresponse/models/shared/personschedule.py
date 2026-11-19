from __future__ import annotations
from .lasterror import LastError
from .scheduleperiod import SchedulePeriod
from noresponse.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import TypedDict


class PersonScheduleTypedDict(TypedDict):
    r"""The person's rerun schedule. Each due run starts a full investigation of the person, as POST /v1/investigations does, and its changes are stored as changes. The schedule lives in the database and the worker runs it, so it survives restarts and releases; each due run starts exactly one investigation."""

    period: SchedulePeriod
    r"""How often the person is investigated again: daily, weekly or monthly, counted from when the schedule was set; off runs no scheduled investigation."""
    next_run_at: Nullable[str]
    r"""When the next scheduled investigation starts, within a minute. null when the schedule is off."""
    last_investigation_id: Nullable[str]
    r"""The investigation the schedule last started. null before its first run."""
    last_error: Nullable[LastError]
    r"""Why the last due run started no investigation, as the problem code its start would have answered. null when the last due run started one, or none has come due. A run that started none is not retried: the schedule moves to its next period."""
    updated_at: Nullable[str]
    updated_by: Nullable[str]
    r"""Who last set the schedule."""


class PersonSchedule(BaseModel):
    r"""The person's rerun schedule. Each due run starts a full investigation of the person, as POST /v1/investigations does, and its changes are stored as changes. The schedule lives in the database and the worker runs it, so it survives restarts and releases; each due run starts exactly one investigation."""

    period: SchedulePeriod
    r"""How often the person is investigated again: daily, weekly or monthly, counted from when the schedule was set; off runs no scheduled investigation."""

    next_run_at: Nullable[str]
    r"""When the next scheduled investigation starts, within a minute. null when the schedule is off."""

    last_investigation_id: Nullable[str]
    r"""The investigation the schedule last started. null before its first run."""

    last_error: Nullable[LastError]
    r"""Why the last due run started no investigation, as the problem code its start would have answered. null when the last due run started one, or none has come due. A run that started none is not retried: the schedule moves to its next period."""

    updated_at: Nullable[str]

    updated_by: Nullable[str]
    r"""Who last set the schedule."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                m[k] = val

        return m
