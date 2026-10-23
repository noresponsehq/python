import json
from pathlib import Path

import httpx
import pytest

import noresponse._wait as wait_module
from noresponse import NoResponse
from noresponse._wait import WaitTimeoutError, wait

FIXTURES = Path(__file__).parent / "fixtures"
PENDING = json.loads((FIXTURES / "valid/assessment-view-pending.json").read_text())
COMPLETE = json.loads((FIXTURES / "valid/assessment-view-complete.json").read_text())
ID = COMPLETE["id"]


def client(responses):
    seen = []

    def handler(request):
        seen.append(request)
        status, body, headers = responses[min(len(seen), len(responses)) - 1]
        return httpx.Response(status, json=body, headers=headers)

    sdk = NoResponse(api_key="nrk_test_" + "k" * 20, server_url="https://api.example.test",
                     client=httpx.Client(transport=httpx.MockTransport(handler)))
    return sdk, seen


@pytest.fixture
def sleeps(monkeypatch):
    slept = []
    clock = [0.0]
    monkeypatch.setattr(wait_module.time, "sleep", lambda s: (slept.append(s), clock.__setitem__(0, clock[0] + s)))
    monkeypatch.setattr(wait_module.time, "monotonic", lambda: clock[0])
    return slept


def test_wait_polls_until_complete_honouring_retry_after(sleeps):
    sdk, seen = client([(200, PENDING, {"Retry-After": "3"}), (200, PENDING, {"Retry-After": "0"}), (200, COMPLETE, {})])
    result = wait(sdk, ID)
    assert result.status == "complete"
    assert result.id == ID
    assert result.account is not None and result.account.risk.decision == COMPLETE["account"]["risk"]["decision"]
    assert sleeps == [3.0, 1.0]
    assert len(seen) == 3
    assert all(r.url.path == f"/v1/assessments/{ID}" for r in seen)
    assert seen[0].headers["authorization"] == "Bearer nrk_test_" + "k" * 20


def test_wait_times_out_with_the_last_pending_assessment(sleeps):
    sdk, _ = client([(200, PENDING, {"Retry-After": "2"})])
    with pytest.raises(WaitTimeoutError) as caught:
        wait(sdk, ID, timeout=5)
    assert caught.value.last.status == "pending"
    assert sleeps == [2.0, 2.0]


def test_retry_after_accepts_http_date():
    assert wait_module._retry_after(
        {"Retry-After": ["Wed, 21 Oct 2015 07:28:00 GMT"]},
        now=1445412475.0,
    ) == 5.0


PARTIAL = json.loads((FIXTURES / "valid/assessment-view-partial.json").read_text())


def test_wait_keeps_polling_a_partial_answer_until_complete(sleeps):
    sdk, seen = client([(200, PARTIAL, {}), (200, PARTIAL, {"Retry-After": "2"}), (200, COMPLETE, {})])
    result = wait(sdk, ID)
    assert result.status == "complete"
    assert sleeps == [1.0, 2.0]
    assert len(seen) == 3


def test_wait_returns_the_latest_partial_answer_at_the_timeout(sleeps):
    sdk, seen = client([(200, PENDING, {"Retry-After": "1"}), (200, PARTIAL, {})])
    result = wait(sdk, ID, timeout=3.5)
    assert result.status == "partial"
    assert result.id == PARTIAL["id"]
    assert sleeps == [1.0, 1.0, 1.0]
    assert len(seen) == 4


def test_wait_async_returns_the_latest_partial_answer_at_the_timeout(monkeypatch):
    import asyncio

    clock = [0.0]

    async def fake_sleep(seconds):
        clock[0] += seconds

    monkeypatch.setattr(wait_module.asyncio, "sleep", fake_sleep)
    monkeypatch.setattr(wait_module.time, "monotonic", lambda: clock[0])

    class Resource:
        calls = 0

        async def get_async(self, assessment_id, **_):
            Resource.calls += 1
            sdk, _ = client([(200, PARTIAL, {})])
            return sdk.assessments.get(assessment_id)

    result = asyncio.run(wait_module.wait_async(Resource(), ID, timeout=2.5))
    assert result.status == "partial"
    assert Resource.calls == 3
