"""The key usage buffer. Hand-written; not generated.

Your API gateway calls ``record`` once per request made with a key your signup
gate issued. The buffer keeps the facts in memory and a background thread
sends them to POST /v1/key_usage/batches: once ``batch_size`` facts are queued,
every ``flush_interval`` seconds, and on ``flush()``, ``close()`` or interpreter
exit. ``record`` does not block and does not raise. When the queue is full the
oldest fact is dropped and counted. A raw key passed as ``key`` is hashed here
and is not sent.
"""

from __future__ import annotations

import atexit
import json
import math
import random
import re
import threading
import time
import uuid
from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Deque, Dict, List, Optional, Protocol, Tuple, Union

from .issued_credential import hash_issued_credential

__all__ = [
    "DEFAULT_BATCH_SIZE",
    "DEFAULT_FLUSH_INTERVAL",
    "DEFAULT_MAX_QUEUE",
    "MAX_BATCH_BYTES",
    "MAX_BATCH_EVENTS",
    "KeyUsageBuffer",
    "KeyUsageStats",
]

MAX_BATCH_EVENTS = 500
"""Most events in one batch."""
MAX_BATCH_BYTES = 256 * 1024
"""Most bytes in one batch body."""
DEFAULT_BATCH_SIZE = 100
DEFAULT_FLUSH_INTERVAL = 5.0
DEFAULT_MAX_QUEUE = 10_000

_MAX_USER_AGENT = 512
_MAX_TOKENS = 1_000_000_000
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_MODEL = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/@+-]{0,127}$")
_CONTROL = re.compile(r"[\x00-\x1f\x7f]")
# The server reads at most MAX_BATCH_BYTES; keep a little room for the envelope.
_BODY_BUDGET = MAX_BATCH_BYTES - 64
_ENVELOPE_BYTES = len('{"events":[]}')


class _Sender(Protocol):
    def record(self, *, events: Any, idempotency_key: Optional[str] = ...) -> Any: ...


@dataclass(frozen=True)
class KeyUsageStats:
    """The buffer's counters."""

    queued: int
    """Facts waiting to be sent."""
    sent: int
    """Facts the API accepted or ignored."""
    dropped: int
    """Facts dropped because the queue was full or the buffer was closed."""
    failed: int
    """Facts whose batch failed after the client's retries."""
    invalid: int
    """Facts refused before queueing: no key, no IP, or an unreadable time."""


def _tokens(value: Any) -> Optional[int]:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0 or value > _MAX_TOKENS:
        return None
    return value


def _occurred(value: Any) -> Optional[str]:
    if value is None:
        moment = datetime.now(timezone.utc)
    elif isinstance(value, datetime):
        moment = value if value.tzinfo is not None else value.replace(tzinfo=timezone.utc)
    elif isinstance(value, str):
        try:
            moment = datetime.fromisoformat(value.replace("Z", "+00:00").replace("z", "+00:00"))
        except ValueError:
            return None
        if moment.tzinfo is None:
            moment = moment.replace(tzinfo=timezone.utc)
    else:
        return None
    return moment.astimezone(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def _event(
    key: Optional[str],
    key_sha256: Optional[str],
    ip: Any,
    user_agent: Any,
    model: Any,
    input_tokens: Any,
    output_tokens: Any,
    occurred_at: Any,
    sample_rate: float,
) -> Optional[Dict[str, Any]]:
    digest: Optional[str] = None
    if isinstance(key_sha256, str) and _SHA256.fullmatch(key_sha256.lower()):
        digest = key_sha256.lower()
    elif isinstance(key, str) and key:
        digest = hash_issued_credential(key)
    if digest is None or not isinstance(ip, str):
        return None
    address = ip.strip()
    if not 2 <= len(address) <= 64 or _CONTROL.search(address):
        return None
    when = _occurred(occurred_at)
    if when is None:
        return None
    event: Dict[str, Any] = {"key_sha256": digest, "ip": address, "occurred_at": when}
    if isinstance(user_agent, str):
        cleaned = _CONTROL.sub(" ", user_agent)[:_MAX_USER_AGENT].strip()
        if cleaned:
            event["user_agent"] = cleaned
    if isinstance(model, str) and _MODEL.fullmatch(model):
        event["model"] = model
    tokens_in, tokens_out = _tokens(input_tokens), _tokens(output_tokens)
    if tokens_in is not None:
        event["input_tokens"] = tokens_in
    if tokens_out is not None:
        event["output_tokens"] = tokens_out
    event["sample_rate"] = sample_rate
    return event


def _size(event: Dict[str, Any]) -> int:
    return len(json.dumps(event, separators=(",", ":"), ensure_ascii=False).encode("utf-8")) + 1


def _positive(value: Any, name: str, maximum: Optional[int] = None) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0 or (maximum is not None and value > maximum):
        bound = f" from 1 to {maximum}" if maximum is not None else ""
        raise ValueError(f"{name} must be a positive integer{bound}")
    return value


class KeyUsageBuffer:
    """Buffers key usage and sends it to POST /v1/key_usage/batches in the background.

    Make one per process with ``nr.key_usage.buffer()``, call ``record`` on every
    request made with an issued key, and ``close()`` on shutdown (an ``atexit``
    hook also sends what is left unless ``flush_at_exit=False``).
    """

    def __init__(
        self,
        sender: _Sender,
        *,
        batch_size: int = DEFAULT_BATCH_SIZE,
        flush_interval: float = DEFAULT_FLUSH_INTERVAL,
        max_queue: int = DEFAULT_MAX_QUEUE,
        sample_rate: float = 1.0,
        on_error: Optional[Callable[[BaseException], None]] = None,
        flush_at_exit: bool = True,
        rng: Optional[Callable[[], float]] = None,
    ) -> None:
        """
        :param batch_size: Send once this many facts are queued. Default 100, at most 500.
        :param flush_interval: Send whatever is queued this often, in seconds. Default 5.
        :param max_queue: Most facts held in memory. Default 10 000. When full, the oldest fact is dropped.
        :param sample_rate: Record this share of facts, above 0 and at most 1. Sent as sample_rate so totals stay right.
        :param on_error: Called with each error a background send hit; that batch's facts count as failed.
        :param flush_at_exit: Send what is queued when the interpreter exits. Default True.
        :param rng: The sampler's random source, for tests. Default random.random.
        """
        self._sender = sender
        self._batch_size = _positive(batch_size, "batch_size", MAX_BATCH_EVENTS)
        self._max_queue = _positive(max_queue, "max_queue")
        if isinstance(flush_interval, bool) or not isinstance(flush_interval, (int, float)) or not math.isfinite(flush_interval) or flush_interval <= 0:
            raise ValueError("flush_interval must be a positive number of seconds")
        self._interval = float(flush_interval)
        if isinstance(sample_rate, bool) or not isinstance(sample_rate, (int, float)) or not 0 < sample_rate <= 1:
            raise ValueError("sample_rate must be above 0 and at most 1")
        self._sample_rate = float(sample_rate)
        self._on_error = on_error
        self._rng = rng or random.random
        self._queue: Deque[Tuple[Dict[str, Any], int]] = deque()
        self._lock = threading.Condition()
        self._closed = False
        self._sending = 0
        self._flush_requested = False
        self._sent = self._dropped = self._failed = self._invalid = 0
        self._thread = threading.Thread(target=self._run, name="noresponse-key-usage", daemon=True)
        self._thread.start()
        self._exit_hook: Optional[Callable[[], None]] = None
        if flush_at_exit:
            self._exit_hook = self._at_exit
            atexit.register(self._exit_hook)

    def record(
        self,
        *,
        ip: str,
        key: Optional[str] = None,
        key_sha256: Optional[str] = None,
        user_agent: Optional[str] = None,
        model: Optional[str] = None,
        input_tokens: Optional[int] = None,
        output_tokens: Optional[int] = None,
        occurred_at: Union[datetime, str, None] = None,
    ) -> None:
        """Queue one fact. Does not block and does not raise.

        Pass the issued ``key`` (hashed here; it is not sent) or its ``key_sha256``.
        A fact without a key, an IP or a readable time is counted as invalid.
        """
        try:
            with self._lock:
                if self._closed:
                    self._dropped += 1
                    return
            if self._sample_rate < 1 and self._rng() >= self._sample_rate:
                return
            event = _event(key, key_sha256, ip, user_agent, model, input_tokens, output_tokens, occurred_at, self._sample_rate)
            with self._lock:
                if event is None:
                    self._invalid += 1
                    return
                while len(self._queue) >= self._max_queue:
                    self._queue.popleft()
                    self._dropped += 1
                self._queue.append((event, _size(event)))
                if len(self._queue) >= self._batch_size:
                    self._lock.notify_all()
        except Exception:  # noqa: BLE001 - record must not raise
            try:
                with self._lock:
                    self._invalid += 1
            except Exception:  # noqa: BLE001
                pass

    def flush(self, timeout: Optional[float] = None) -> bool:
        """Send everything queued now. Returns True once it was sent or failed, False if timeout passed first."""
        deadline = None if timeout is None else time.monotonic() + timeout
        with self._lock:
            self._flush_requested = True
            self._lock.notify_all()
            while self._queue or self._sending:
                if not self._thread.is_alive():
                    break
                remaining = None if deadline is None else deadline - time.monotonic()
                if remaining is not None and remaining <= 0:
                    return False
                self._lock.wait(remaining if remaining is not None else 0.5)
            return not self._queue and not self._sending

    def close(self, timeout: Optional[float] = None) -> bool:
        """Send what is queued, stop the thread and refuse later facts (counted as dropped)."""
        sent = self.flush(timeout)
        with self._lock:
            self._closed = True
            self._lock.notify_all()
        self._thread.join(timeout)
        if self._exit_hook is not None:
            atexit.unregister(self._exit_hook)
            self._exit_hook = None
        return sent

    def stats(self) -> KeyUsageStats:
        with self._lock:
            return KeyUsageStats(
                queued=len(self._queue), sent=self._sent, dropped=self._dropped, failed=self._failed, invalid=self._invalid
            )

    def __enter__(self) -> "KeyUsageBuffer":
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()

    def _at_exit(self) -> None:
        try:
            self.close(timeout=5.0)
        except Exception:  # noqa: BLE001 - exit must not fail
            pass

    def _run(self) -> None:
        next_flush = time.monotonic() + self._interval
        while True:
            with self._lock:
                while not self._closed and not self._flush_requested and len(self._queue) < self._batch_size:
                    remaining = next_flush - time.monotonic()
                    if remaining <= 0:
                        break
                    self._lock.wait(remaining)
                if self._closed and not self._queue:
                    self._lock.notify_all()
                    return
                self._flush_requested = False
                if time.monotonic() >= next_flush:
                    next_flush = time.monotonic() + self._interval
                batches = []
                while self._queue:
                    batches.append(self._take())
                self._sending += sum(len(batch) for batch in batches)
            for batch in batches:
                self._send(batch)
            with self._lock:
                self._lock.notify_all()

    def _take(self) -> List[Dict[str, Any]]:
        """The oldest facts that fit one batch: at most 500 events and MAX_BATCH_BYTES of body. Lock held."""
        size = _ENVELOPE_BYTES
        batch: List[Dict[str, Any]] = []
        while self._queue and len(batch) < MAX_BATCH_EVENTS:
            event, bytes_ = self._queue[0]
            if batch and size + bytes_ > _BODY_BUDGET:
                break
            self._queue.popleft()
            batch.append(event)
            size += bytes_
        return batch

    def _send(self, batch: List[Dict[str, Any]]) -> None:
        try:
            self._sender.record(events=batch, idempotency_key=str(uuid.uuid4()))
        except Exception as error:  # noqa: BLE001 - a failed batch is counted, not raised
            with self._lock:
                self._failed += len(batch)
                self._sending -= len(batch)
            if self._on_error is not None:
                try:
                    self._on_error(error)
                except Exception:  # noqa: BLE001
                    pass
            return
        with self._lock:
            self._sent += len(batch)
            self._sending -= len(batch)
