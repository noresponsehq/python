# noresponse

The NoResponse client for Python. It assesses a signup or gateway event, polls a pending assessment, pages through an account's history, records what you later learned, rotates your API key and verifies webhooks.

Python 3.10 or later. Sync and asyncio. Fully typed (`py.typed`). The client is generated from the NoResponse OpenAPI document; the thin layer on top of it (defaults, response types, errors, wait, webhooks) is hand-written.

```sh
pip install noresponse
```

## Quick start

```python
from noresponse import NoResponse

nr = NoResponse()  # reads NORESPONSE_API_KEY

assessment = nr.assessments.create(
    account_id="usr_8f2k1",
    flow="signup",
    identifiers={"email": "jordan.lee@example.com", "name": "Jordan Lee", "ip": "81.2.69.160"},
)

if assessment.account is None:
    # The account's first assessment is still pending. Apply your fallback now, then wait or take the webhook.
    assessment = nr.assessments.wait(assessment.id)

if assessment.account is not None:
    print(assessment.account.risk.decision)  # allow, step_up, review or block
```

Keep the API key on your server. The client raises `ValueError` at construction without one.

Async code uses the same client with the `_async` methods:

```python
async with NoResponse() as nr:
    assessment = await nr.assessments.create_async(
        account_id="usr_8f2k1",
        identifiers={"email": "jordan.lee@example.com"},
    )
```

## Configuration

```python
import httpx
from noresponse import NoResponse

nr = NoResponse(
    "nrk_...",                                   # default: NORESPONSE_API_KEY
    server_url="https://api.noresponse.org",     # default; or NORESPONSE_BASE_URL
    timeout_ms=10_000,                           # per request
    retry_config=None,                           # None turns retries off
    client=httpx.Client(proxy="http://proxy:3128"),
)
```

| Argument | Default | Notes |
|---|---|---|
| `api_key` | `NORESPONSE_API_KEY` | A string, or a function that returns one. |
| `server_url` | `NORESPONSE_BASE_URL`, then `https://api.noresponse.org` | HTTPS, except localhost. |
| `timeout_ms` | 10 000 | Per request. Every method also takes `timeout_ms`. |
| `retry_config` | see [Retries](#retries) | Every method except `keys.rotate`, `integrations.create` and `integrations.rotate` also takes `retries`. |
| `client`, `async_client` | a new `httpx.Client` and `httpx.AsyncClient` | Your own, for a proxy, mTLS or tests. |
| `debug_logger` | off; `NORESPONSE_LOG=debug` logs to the `noresponse` logger | One line per request and response. See [Logging](#logging). |

Use the client as a context manager (`with` or `async with`) to close the HTTP clients it opened. Make one client per process and reuse it.

Every method also takes `server_url`, `timeout_ms` and `http_headers` for that call, and every method except `keys.rotate`, `integrations.create` and `integrations.rotate` takes `retries`. They are not idempotent, so they are never retried.

## Assessments

### Create

```python
assessment = nr.assessments.create(
    account_id="usr_8f2k1",                                    # your opaque account id
    flow="signup",                                             # signup, login or purchase
    depth="full",                                              # quick or full; full for signup and purchase, quick for login by default
    identifiers={"email": "jordan.lee@example.com"},           # email, username or phone; name and ip refine the match
    policy_context={"region": "AU"},
    client_context={"timezone": "Australia/Sydney", "platform": "web", "form_duration_ms": 1800},
    auth_context=auth_context,                                 # a verified session, see below
    response_mode="standard",                                  # detailed adds detail.signals and detail.risk.details (detailed scope)
    idempotency_key="signup-usr_8f2k1-0001",
)
```

The answer is the assessment whether the API answered 200 (complete or partial) or 202 (pending). `status` is `complete`, `partial` or `pending`. Act on `account.risk.decision`: `allow`, `step_up`, `review` or `block`, the account's current decision for this flow. `account` is `None` while the account's first assessment is pending. `detail` holds this assessment's own facts: `detail.risk`, `detail.recommendation`, `detail.signals`, `detail.assessment_version` and, while pending, `detail.assessment_url`.

The idempotency key is generated (a UUID) when you leave it out and is sent again on every retry of that call. Pass your own to make a retry of the same signup from your side replay the same assessment: the API answers the latest version with `meta.idempotent_replayed` true and starts no new work. The same key with a different body answers 409.

### Get and wait

```python
latest = nr.assessments.get(assessment.id)
settled = nr.assessments.wait(assessment.id, timeout=30)
```

`wait` polls `get` until the status is `complete`, sleeping the server's `Retry-After` (at least one second) between polls. After `timeout` seconds (default 30) it returns the latest answer if that is `partial`, with its status still `partial`, and raises `APITimeoutError` if the assessment is still `pending`. The error is a `WaitTimeoutError` whose `last` attribute is the final pending assessment. Pass `response_mode="detailed"` to either. In async code use `get_async` and `wait_async`.

### Query an account's history

```python
page = nr.assessments.query(account_id="usr_8f2k1", limit=20)
page.items       # assessment details, newest first, each at its latest version
page.has_more    # True when another page exists
page.next_page() # the next page, or None

for assessment in page:
    ...  # every assessment across every page
```

In async code, `page = await nr.assessments.query_async(...)`, then `async for assessment in page` and `await page.next_page_async()`.

### Read an account's current risk

An account is the `account_id` you send with your assessments. It holds one current risk: the risk of its latest assessment with a decision. Every assessment updates it.

```python
account = nr.accounts.get("usr_8f2k1")
account.risk.score               # 0 (safe) to 100 (risky)
account.risk.decision            # allow, step_up, review or block
account.decisions_by_flow.login  # a decision for signup, login and purchase
account.assessment_id            # the assessment the risk comes from

for assessment in nr.accounts.list_assessments("usr_8f2k1", limit=20):
    ...  # the same pages as assessments.query, newest first

erased = nr.accounts.delete("usr_8f2k1")  # an erasure request: every assessment of the account goes
erased.assessments_deleted               # 0 on a repeat
```

Every call needs the `history` scope. An account with no decided assessment raises `NotFoundError`. `list_assessments` puts the account id in the URL; use `assessments.query` to keep it in the request body. In async code use `get_async`, `list_assessments_async` and `delete_async`. A `delete` that removed something sends an `account.deleted` webhook.

### Record an outcome

```python
receipt = nr.assessments.record_outcome(
    assessment.id,
    outcome="chargeback",  # confirmed_abuse, account_takeover, chargeback, false_positive, legitimate or unknown
    observed_at="2026-10-20T10:00:00Z",
    external_ref="case-42",
)
```

Outcomes take an `idempotency_key` the same way `create` does.

### Delete one assessment

```python
removed = nr.assessments.delete(assessment.assessment_id)
removed.account.current_assessment_id  # the assessment the account's risk now comes from; None when none is left
```

It needs the `history` scope; in async code use `delete_async`. Afterwards `assessments.get` of it raises `NotFoundError`, and so does a repeat. To erase a whole account, use `accounts.delete`.

## Keys

```python
rotation = nr.keys.rotate(overlap_seconds=3600)
rotation.key                      # the new key, shown once
rotation.previous_key_expires_at  # when the key that signed the request stops working
```

The default overlap is 24 hours (minimum 60 seconds, maximum 7 days). Rotate with the new key next time.

## Integrations

A hosted integration is a WorkOS or Auth0 Action that NoResponse answers, so sign-ups and sign-ins are scored with no server of your own. These calls need a key with the `integrations` scope.

```python
integration = nr.integrations.create(platform="auth0")
integration.url     # point the Auth0 Action at this
integration.secret  # the Action's shared secret, shown once

nr.integrations.create(platform="workos", signing_secret=os.environ["WORKOS_ACTIONS_SECRET"])
listed = nr.integrations.list()  # listed.items, with no secrets
rotated = nr.integrations.rotate(integration.integration_id)  # Auth0: new secret; WorkOS: pass signing_secret
nr.integrations.delete(integration.integration_id)
```

`create` and `rotate` are not idempotent and are never retried. The replaced secret is accepted until `previous_secret_expires_at`. Each method has an `_async` twin.

## Response metadata

Every returned object carries `meta`, which is not part of the body and is left out of `model_dump()`:

```python
assessment.meta.request_id           # X-Request-ID, to quote when you contact us
assessment.meta.retry_after          # seconds, when the API sent Retry-After
assessment.meta.location             # the polling path of a pending assessment
assessment.meta.idempotent_replayed  # True when the answer replays an earlier request
```

Assessments that arrive by webhook or inside a page have an empty `meta`.

## Errors

Every API error extends `NoResponseError` and has the same attributes whatever the status: `status`, `type`, `title`, `detail`, `code`, `request_id`, `retry_after` and, on a 400, `invalid_params` (the offending fields). `str(error)` reads `HTTP 429 rate_limited: Rate limited. The tenant's assessment rate is exhausted; retry after the Retry-After interval. (request 0123456789abcdef0123456789abcdef)`. The raw `status_code`, `headers`, `body` and `raw_response` are there too.

| Class | When |
|---|---|
| `BadRequestError` | 400: the body or a header is malformed; see `invalid_params` and `code` |
| `AuthenticationError` | 401: missing, malformed, revoked or expired key |
| `PermissionDeniedError` | 403: the key lacks the operation's scope |
| `NotFoundError` | 404: unknown, expired or foreign assessment |
| `ConflictError` | 409: idempotency key reused with a different body, or a key already rotating |
| `RateLimitError` | 429: see `retry_after` |
| `APIStatusError` | any other 4xx or 5xx, including 503 |
| `ResponseValidationError` | a 2xx the client could not read (`code` is `invalid_response`) |
| `APIConnectionError` | DNS, TLS or connection failure |
| `APITimeoutError` | the request or a `wait` timed out; also an `APIConnectionError` and a `TimeoutError` |

```python
from noresponse import NoResponseError, RateLimitError, APIConnectionError

try:
    nr.assessments.create(account_id="usr_8f2k1", identifiers={"email": email})
except RateLimitError as error:
    schedule(error.retry_after)
except APIConnectionError:  # includes APITimeoutError
    fallback()
except NoResponseError as error:
    log(error.status, error.code, error.request_id)
```

The two transport errors do not extend `NoResponseError`, because no response exists to describe.

## Retries

Connection errors, 408, 429 and every 5xx are retried with exponential backoff (500 ms, doubling to 8 s between attempts) for at most 30 s in all. When the API sends `Retry-After`, the client sleeps that long instead. A POST sends the same `Idempotency-Key` on every attempt, so a retried create or outcome is recorded once. 409 and other 4xx are not retried.

Override per client with `retry_config`, or per call with `retries`:

```python
from noresponse.utils import BackoffStrategy, RetryConfig

nr.assessments.create(
    account_id="usr_8f2k1",
    identifiers={"email": email},
    retries=RetryConfig("backoff", BackoffStrategy(200, 2000, 2, 10_000), True),
)
nr.assessments.create(account_id="usr_8f2k1", identifiers={"email": email}, retries=None)  # no retries
```

## Issued keys

When your signup gate issues an API key to the new account, send only its hash, as `issued_credential.sha256`; the key itself never leaves your backend.

```python
from noresponse import hash_issued_credential

sha256 = hash_issued_credential(issued_key)  # 64 lower-case hex characters
```

## Key usage

Report each request made with an issued key, and NoResponse ties the key's usage back to the account it was issued to. A key used from 20 or more IP addresses, or 3 or more countries, within 24 hours puts `shared_api_key` in that account's risk. Keep one buffer per process in your API gateway and record every request; it needs a key with the `assess` scope.

```python
usage = nr.key_usage.buffer()  # sends every 5 s, or once 100 facts are queued

@app.middleware("http")
async def report_usage(request, call_next):
    usage.record(
        key=request.headers.get("authorization", "").removeprefix("Bearer "),  # hashed here; the key is not sent
        ip=request.client.host,
        user_agent=request.headers.get("user-agent"),
    )
    return await call_next(request)
```

`record` does not block and does not raise; a background thread sends the batches, and the buffer sends what is left when the interpreter exits (`flush_at_exit=False` turns that off; call `usage.close()` yourself). Pass `key_sha256` instead of `key` when you already hold the hash, and `model`, `input_tokens`, `output_tokens` and `occurred_at` when you have them. Options: `batch_size` (default 100, at most 500), `flush_interval` (seconds, default 5), `max_queue` (default 10 000; when full, the oldest fact is dropped), `sample_rate` (record a share of requests, such as 0.1) and `on_error` (called when a batch fails after retries). `usage.stats()` returns `queued`, `sent`, `dropped`, `failed` and `invalid`. Each batch carries its own `Idempotency-Key`, sent again on every retry, so a retried batch is counted once. `nr.key_usage.record(events=[...])` (or `record_async`) sends one batch yourself.

## Webhooks

Register your endpoint with a key that has the `webhooks` scope. The signing secret is shown only in this answer, so store it, then send the verification challenge:

```python
created = nr.webhook_endpoints.create(url="https://app.example.com/webhooks/noresponse")
secret_store.write(created.signing_secret.key_id, created.signing_secret.secret)
check = nr.webhook_endpoints.send_test_event(created.endpoint.endpoint_id, event="endpoint.verification")  # check.verified
nr.webhook_endpoints.send_test_event(created.endpoint.endpoint_id, event="assessment.updated")  # event.test is True
```

`list()`, `rotate_signing_key(endpoint_id)` (the old key verifies for 7 more days) and `delete(endpoint_id)` manage it afterwards.

Verify the exact bytes you received, then act on the typed event. `secrets` maps each `whk_` key id to its secret; hold both during a rotation.

```python
import os
from noresponse import Webhook, WebhookVerificationError
from noresponse import AccountDeleted, AssessmentExpired, Assessment

SECRETS = {
    os.environ["NORESPONSE_WEBHOOK_KEY_ID"]: os.environ["NORESPONSE_WEBHOOK_SECRET"],
    # During a rotation, add the previous key id and secret here as well.
}

@app.post("/webhooks/noresponse")  # FastAPI: await request.body() is the raw body
async def handler(request: Request) -> Response:
    try:
        event = Webhook.construct_event(await request.body(), request.headers, SECRETS)
    except WebhookVerificationError:
        return Response(status_code=400)
    if event.type == "endpoint.verification":
        return JSONResponse(Webhook.verification_response(event))
    if event.test:  # send_test_event's fixed example assessment: apply nothing
        return Response(status_code=204)
    if isinstance(event.data, AccountDeleted):  # type "account.deleted": you erased it with accounts.delete
        forget_account(event.data.account_id)
    elif isinstance(event.data, AssessmentExpired):
        forget(event.data.assessment_id)  # GET now answers 404
    elif isinstance(event.data, Assessment) and is_newer(event.data):  # keep the highest detail.assessment_version per assessment
        apply(event.data)  # the full assessment, as assessments.get returns it
    return Response(status_code=204)
```

`construct_event(payload, headers, secrets, tolerance_seconds=300)` takes the raw body (`bytes` or the exact text) and any header mapping or list of pairs, and refuses a repeated signature header, a delivery older than 300 seconds, an unknown key id or a bad signature with a `WebhookVerificationError` whose `code` says which. Deliveries are at least once: deduplicate on `event.id`. The same functions are on `Webhook`, on `nr.webhooks` and in the `noresponse` namespace.

### Late results

An assessment can be revised after you allowed the signup. `handle_late_result` verifies the delivery with `construct_event`, applies your policy and acts through your auth provider's admin API:

```python
from noresponse import clerk_actions, handle_late_result  # or workos_actions, auth0_actions

provider = clerk_actions(os.environ["CLERK_SECRET_KEY"])
result = handle_late_result(raw_body, request.headers, SECRETS, provider, policy={"review": "ban"})
```

The policy maps the account's decision (`account.risk.decision`) to an action. The default revokes sessions on `review` and `block` and does nothing otherwise. A pending assessment acts on nothing: its account decision comes from an earlier assessment. `ban` blocks the user in Clerk and Auth0; WorkOS has no block, so its ban deletes the user permanently. Pass `resolve_user_id` when the provider's user id is not your `account_id`. A test event from `send_test_event` acts on nothing. A refused provider call raises `ProviderActionError`; answer the webhook with a 5xx so we retry it. A provider 404 means the user or session is already gone and counts as done, so a repeated delivery is safe.

If your app has its own login, `log_only_actions()` logs what it would revoke or ban (to the `noresponse.late_results` logger at WARNING, or pass `log`) and calls nothing. Use it to try the handler, then subclass `LateResultProvider` with a `name` and the two methods `revoke_sessions(user_id)` and `ban(user_id)`.

## Logging

Set `NORESPONSE_LOG=debug`, or pass `debug_logger`, to get one line per request and response: method, URL, status and request id. The API key, other headers and bodies are kept out of the log.

## Raw responses

`nr.assessments.with_raw_response.get(...)` returns an object with `status_code`, `headers`, `request_id` and `http_response`. Its `parse()` returns the generated envelope, whose `result` is the model. Use it when you need the status line or every header.

## Support

Documentation: https://docs.noresponse.org. Issues: https://github.com/noresponsehq/python/issues. Quote `meta.request_id` or `error.request_id` when you write to us.

Apache-2.0.
