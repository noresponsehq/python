import json
import re
import time
from pathlib import Path

import httpx
import pytest

from noresponse import KeyUsageBatch, KeyUsageBuffer, KeyUsageStats, NoResponse, hash_issued_credential
from noresponse.utils import BackoffStrategy, RetryConfig

FIXTURES = Path(__file__).parent / "fixtures"
KEY = "nrk_0TESTKEY00000000000000000_" + "s" * 43
RECEIPT = json.loads((FIXTURES / "valid/key-usage-batch.json").read_text())
ISSUED = "sk_issued_to_account_7f3a9c_0123456789"
HASH = hash_issued_credential(ISSUED)
UUID = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$")
FAST_RETRY = RetryConfig("backoff", BackoffStrategy(1, 5, 1.1, 2000), True)


def answer(body, status=202, headers=None):
    return httpx.Response(status, content=json.dumps(body).encode(),
                          headers={"content-type": "application/json", "x-request-id": "a" * 32, **(headers or {})})


def problem(status, code):
    body = {"type": f"https://docs.noresponse.org/problems/{code}", "title": "Problem", "status": status,
            "detail": code, "code": code, "request_id": "b" * 32}
    return httpx.Response(status, content=json.dumps(body).encode(),
                          headers={"content-type": "application/problem+json", "x-request-id": "b" * 32})


def make(responses=None, **options):
    seen = []

    def handler(request):
        seen.append(request)
        if responses is None:
            return answer(RECEIPT)
        item = responses[min(len(seen), len(responses)) - 1]
        return item

    transport = httpx.MockTransport(handler)
    sdk = NoResponse(KEY, server_url="https://api.example.test", client=httpx.Client(transport=transport),
                     async_client=httpx.AsyncClient(transport=transport), **options)
    return sdk, seen


def body(request):
    return json.loads(request.content)


def fact(i=0, **extra):
    return {"key_sha256": HASH, "ip": f"203.0.113.{i % 250}", "user_agent": "curl/8.7.1", "model": "gpt-4o-mini",
            "input_tokens": 10, "output_tokens": 2, **extra}


def wait_for(condition, seconds=2.0):
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        if condition():
            return True
        time.sleep(0.01)
    return condition()


def test_record_posts_one_batch_with_an_idempotency_key_and_meta():
    sdk, seen = make([answer(RECEIPT, headers={"Idempotent-Replayed": "true"})])
    batch = sdk.key_usage.record(events=[{"key_sha256": HASH, "ip": "203.0.113.24", "occurred_at": "2026-10-23T09:14:07Z"}])
    assert isinstance(batch, KeyUsageBatch)
    assert batch.id == RECEIPT["id"] and batch.accepted == RECEIPT["accepted"]
    assert batch.meta.idempotent_replayed is True
    assert seen[0].method == "POST" and seen[0].url.path == "/v1/key_usage/batches"
    assert UUID.match(seen[0].headers["idempotency-key"])
    assert body(seen[0])["events"][0]["key_sha256"] == HASH


def test_record_async():
    import asyncio

    sdk, seen = make()
    batch = asyncio.run(sdk.key_usage.record_async(events=[{"key_sha256": HASH, "ip": "203.0.113.24",
                                                            "occurred_at": "2026-10-23T09:14:07Z"}]))
    assert batch.id == RECEIPT["id"] and len(seen) == 1


def test_buffer_sends_once_batch_size_facts_are_queued():
    sdk, seen = make()
    buffer = sdk.key_usage.buffer(batch_size=3, flush_interval=60, flush_at_exit=False)
    buffer.record(**fact(1))
    buffer.record(**fact(2))
    time.sleep(0.05)
    assert seen == []
    buffer.record(**fact(3))
    assert wait_for(lambda: len(seen) == 1)
    assert len(body(seen[0])["events"]) == 3
    assert wait_for(lambda: buffer.stats().sent == 3)
    assert buffer.stats() == KeyUsageStats(queued=0, sent=3, dropped=0, failed=0, invalid=0)
    buffer.close()


def test_buffer_sends_on_its_interval():
    sdk, seen = make()
    buffer = sdk.key_usage.buffer(flush_interval=0.05, flush_at_exit=False)
    buffer.record(**fact())
    assert wait_for(lambda: len(seen) == 1)
    buffer.close()


def test_close_sends_what_is_queued_and_refuses_later_facts():
    sdk, seen = make()
    buffer = sdk.key_usage.buffer(flush_interval=60, flush_at_exit=False)
    buffer.record(**fact(1))
    buffer.record(**fact(2))
    assert buffer.close(timeout=5) is True
    assert len(seen) == 1 and len(body(seen[0])["events"]) == 2
    buffer.record(**fact(3))
    assert buffer.stats().dropped == 1 and len(seen) == 1


def test_a_full_queue_drops_the_oldest_facts_and_counts_them():
    sdk, seen = make()
    buffer = sdk.key_usage.buffer(max_queue=3, batch_size=500, flush_interval=60, flush_at_exit=False)
    for i in range(1, 6):
        buffer.record(**fact(i))
    assert buffer.stats() == KeyUsageStats(queued=3, sent=0, dropped=2, failed=0, invalid=0)
    buffer.close()
    assert [event["ip"] for event in body(seen[0])["events"]] == ["203.0.113.3", "203.0.113.4", "203.0.113.5"]


def test_record_does_not_raise_and_counts_garbage_as_invalid():
    sdk, seen = make()
    buffer = sdk.key_usage.buffer(flush_interval=60, flush_at_exit=False)
    garbage = [
        {"ip": None}, {"ip": "203.0.113.1"}, {"ip": "203.0.113.1", "key_sha256": "nothex"}, {"ip": 4, "key_sha256": HASH},
        {"ip": "203.0.113.1", "key_sha256": HASH, "occurred_at": "yesterday"}, {"ip": "203.0.113.1", "key": ""},
        {"ip": "1", "key_sha256": HASH}, {"ip": "203.0.113.1", "key_sha256": HASH, "occurred_at": 12},
    ]
    for value in garbage:
        buffer.record(**value)
    assert buffer.stats().invalid == len(garbage)
    # Bad optional values are left out, not the fact.
    buffer.record(key_sha256=HASH.upper(), ip="203.0.113.9", model="bad model!", input_tokens=-1, output_tokens=True,
                  user_agent="a\nb" + "c" * 600)
    buffer.close()
    event = body(seen[0])["events"][0]
    assert event["key_sha256"] == HASH
    assert "model" not in event and "input_tokens" not in event and "output_tokens" not in event
    assert len(event["user_agent"]) == 512 and "\n" not in event["user_agent"]


def test_a_raw_key_is_hashed_in_process_and_not_sent():
    sdk, seen = make()
    buffer = sdk.key_usage.buffer(flush_interval=60, flush_at_exit=False)
    buffer.record(key=ISSUED, ip="203.0.113.24")
    buffer.close()
    assert ISSUED.encode() not in seen[0].content and ISSUED not in str(seen[0].headers)
    assert body(seen[0])["events"][0]["key_sha256"] == HASH


def test_batches_split_at_500_events_and_at_256_kib():
    sdk, seen = make()
    buffer = sdk.key_usage.buffer(batch_size=500, flush_interval=60, max_queue=100_000, flush_at_exit=False)
    for _ in range(1200):
        buffer.record(key_sha256=HASH, ip="203.0.113.1")
    buffer.flush(timeout=10)
    assert sum(len(body(r)["events"]) for r in seen) == 1200
    assert all(len(body(r)["events"]) <= 500 for r in seen)
    seen.clear()
    for _ in range(500):
        buffer.record(key_sha256=HASH, ip="203.0.113.1", user_agent="u" * 512, model="m" * 128)
    buffer.close(timeout=10)
    assert len(seen) >= 2
    assert sum(len(body(r)["events"]) for r in seen) == 500
    assert all(len(r.content) <= 256 * 1024 for r in seen)


def test_a_retried_batch_keeps_its_idempotency_key_and_each_batch_gets_its_own():
    sdk, seen = make([problem(503, "service_unavailable"), answer(RECEIPT), answer(RECEIPT)], retry_config=FAST_RETRY)
    buffer = sdk.key_usage.buffer(flush_interval=60, flush_at_exit=False)
    buffer.record(**fact(1))
    buffer.flush(timeout=5)
    buffer.record(**fact(2))
    buffer.close(timeout=5)
    assert len(seen) == 3
    assert seen[0].headers["idempotency-key"] == seen[1].headers["idempotency-key"]
    assert seen[1].headers["idempotency-key"] != seen[2].headers["idempotency-key"]
    assert buffer.stats().sent == 2


def test_a_failed_batch_is_counted_and_reported_and_the_buffer_keeps_going():
    errors = []
    sdk, seen = make([problem(400, "invalid_request"), answer(RECEIPT)])
    buffer = sdk.key_usage.buffer(flush_interval=60, on_error=errors.append, flush_at_exit=False)
    buffer.record(**fact(1))
    buffer.flush(timeout=5)
    buffer.record(**fact(2))
    buffer.close(timeout=5)
    assert len(seen) == 2 and len(errors) == 1
    assert buffer.stats() == KeyUsageStats(queued=0, sent=1, dropped=0, failed=1, invalid=0)


def test_sampling_records_a_share_of_facts_and_sends_the_rate():
    sdk, seen = make()
    draws = iter([0.1, 0.9, 0.2, 0.8])
    buffer = KeyUsageBuffer(sdk.key_usage, sample_rate=0.5, rng=lambda: next(draws), flush_interval=60, flush_at_exit=False)
    for i in range(4):
        buffer.record(**fact(i))
    buffer.close()
    events = body(seen[0])["events"]
    assert len(events) == 2 and all(event["sample_rate"] == 0.5 for event in events)


def test_options_are_checked_when_the_buffer_is_made():
    sdk, _ = make()
    for options in ({"batch_size": 501}, {"sample_rate": 0}, {"flush_interval": -1}, {"max_queue": 0}):
        with pytest.raises(ValueError):
            sdk.key_usage.buffer(flush_at_exit=False, **options)
