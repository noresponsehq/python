import json

from test_client import answer, make


def test_group_dates_distinguish_omission_null_and_dates():
    group = dict(id="grp_example", environment="test", name="Harbour building", starts_at=None, ends_at=None, principals=[], topics=[], people=0, version=1, created_by="test", created_at="2026-11-15T10:00:00Z", updated_at="2026-11-15T10:00:00Z")
    sdk, seen = make([answer(group, 201), answer(group)])
    created = sdk.groups.create(name=group["name"]).result
    assert created.starts_at is None
    assert created.ends_at is None
    sdk.groups.update(group["id"], name="Harbour organization")
    sdk.groups.update(group["id"], starts_at="2026-12-03T09:00:00Z", ends_at="2026-12-03T17:00:00Z")
    sdk.groups.update(group["id"], starts_at=None, ends_at=None)
    assert [json.loads(request.content) for request in seen] == [
        {"name": group["name"]}, {"name": "Harbour organization"},
        {"starts_at": "2026-12-03T09:00:00Z", "ends_at": "2026-12-03T17:00:00Z"},
        {"starts_at": None, "ends_at": None},
    ]


def test_related_ongoing_group_decodes_null_start():
    from noresponse.models.shared.othergroup import OtherGroup
    group = OtherGroup.model_validate_json('{"group_id":"grp_building","group_name":"Harbour building","group_starts_at":null,"person_id":"per_example","matched_on":["person_id"],"match_state":"unscreened","decision":null}')
    assert group.group_starts_at is None
