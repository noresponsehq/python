"""A person's report returns the contract's records as typed models."""
import asyncio

from noresponse.models.shared import PersonReport, Record

from test_client import answer, fixture, make

REPORT = fixture("valid/person-report-records.json")
GROUP, PERSON = REPORT["person"]["group_id"], REPORT["person"]["id"]


def check(report, seen):
    assert isinstance(report, PersonReport)
    assert seen[0].method == "GET"
    assert seen[0].url.path == f"/v1/groups/{GROUP}/people/{PERSON}"

    account, row = report.lookup.records
    assert isinstance(account, Record)
    assert account.source.kind == "platform" and account.source.site == "github.com"
    assert account.matched[0].by == "username" and account.matched[0].field == "login"
    assert account.observed_at == "2026-11-14T10:01:40Z"
    handle = next(field for field in account.fields if field.role == "handle")
    assert handle.kind == "username" and handle.value == "jordan-ellis"
    assert handle.distinctive.rating == "distinctive"
    name = next(field for field in account.fields if field.role == "display_name")
    assert (name.original, name.value) == ("Jordan  Ellis", "Jordan Ellis")
    hireable = next(field for field in account.fields if field.field == "hireable")
    assert hireable.role is None, "a field only its source returns has no role"
    assert account.likelihood == 0.74 and account.agreed == ["name", "twitter_username"]
    assert account.joined is True and account.verdict == "joined"

    assert (row.source.kind, row.source.table, row.source.date_) == ("site_breach", "FORUM_EXAMPLE_NET_2019", "2019-03")
    by_field = {field.field: field for field in row.fields}
    assert by_field["password"].kind == "password" and by_field["password"].value == "Leeds1990!"
    assert by_field["password_hash"].detail == "bcrypt"
    assert by_field["lastip"].role == "last_ip" and by_field["lastip"].value == "203.0.113.5"
    assert by_field["birthday"].value is None and by_field["birthday"].original == "07/03/1990"
    assert by_field["email"].distinctive.rating == "unique"
    assert row.likelihood == 0.8 and row.verdict is None

    remaining = report.lookup.remaining[0]
    assert (remaining.source.kind, remaining.by, remaining.rows) == ("credential_list", "username", 37)


def test_a_persons_report_returns_typed_records():
    nr, seen = make([answer(REPORT)])
    response = nr.groups.get_person(group_id=GROUP, person_id=PERSON)
    check(response.result, seen)


def test_a_persons_report_returns_typed_records_async():
    nr, seen = make([answer(REPORT)])
    response = asyncio.run(nr.groups.get_person_async(group_id=GROUP, person_id=PERSON))
    check(response.result, seen)
