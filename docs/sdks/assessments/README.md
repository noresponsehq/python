# Assessments

## Overview

Signup and gateway assessments.

### Available Operations

* [create](#create) - Assess identifiers for a signup or gateway decision.
* [get](#get) - Poll the authoritative assessment of one assessment.
* [record_outcome](#record_outcome) - Report what was later learned about an assessed account.
* [query](#query) - Page through one account's unexpired assessments.

## create

Returns within the deadline (500 ms at most) with a complete, partial or pending assessment: 200 carries complete or partial, 202 carries pending with Location and Retry-After. A pending answer has no recommendation; apply your own fallback for pending, 429, 503 or a timeout. Requires the assess scope. Idempotency-Key is required and is bound to the body for 24 hours: the same key with the same body replays the latest assessment with Idempotent-Replayed: true and starts no new work; the same key with a different body answers 409 idempotency_key_reused. response_mode defaults to standard; detailed needs the detailed scope.

### Example Usage: complete

<!-- UsageSnippet language="python" operationID="createAssessment" method="post" path="/v1/assessments" example="complete" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.assessments.create(idempotency_key="<value>", account_id="<id>", identifiers={})

    # Handle response
    print(res)

```
### Example Usage: detailed

<!-- UsageSnippet language="python" operationID="createAssessment" method="post" path="/v1/assessments" example="detailed" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.assessments.create(idempotency_key="<value>", account_id="<id>", identifiers={})

    # Handle response
    print(res)

```
### Example Usage: full

<!-- UsageSnippet language="python" operationID="createAssessment" method="post" path="/v1/assessments" example="full" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.assessments.create(idempotency_key="<value>", account_id="acct_7f3a9c", identifiers={
        "email": "new.user@example.com",
        "username": "new_user_42",
        "phone": "+447700900123",
    }, policy_context={
        "flow": "signup",
        "region": "GB",
    }, request_id="req-2026-10-14-0001", deadline_ms=300)

    # Handle response
    print(res)

```
### Example Usage: minimal

<!-- UsageSnippet language="python" operationID="createAssessment" method="post" path="/v1/assessments" example="minimal" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.assessments.create(idempotency_key="<value>", account_id="acct_7f3a9c", identifiers={
        "email": "new.user@example.com",
    })

    # Handle response
    print(res)

```
### Example Usage: name_and_ip

<!-- UsageSnippet language="python" operationID="createAssessment" method="post" path="/v1/assessments" example="name_and_ip" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.assessments.create(idempotency_key="<value>", account_id="acct_8412", identifiers={
        "email": "jane.doe@example.com",
        "username": "janedoe",
        "phone": "+14155550123",
        "name": "Jane A. Doe",
        "ip": "73.162.18.45",
    }, policy_context={
        "flow": "signup",
        "region": "US",
    }, request_id="req_01", deadline_ms=500, response_mode="standard")

    # Handle response
    print(res)

```
### Example Usage: partial

<!-- UsageSnippet language="python" operationID="createAssessment" method="post" path="/v1/assessments" example="partial" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.assessments.create(idempotency_key="<value>", account_id="<id>", identifiers={})

    # Handle response
    print(res)

```
### Example Usage: standard

<!-- UsageSnippet language="python" operationID="createAssessment" method="post" path="/v1/assessments" example="standard" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.assessments.create(idempotency_key="<value>", account_id="<id>", identifiers={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `idempotency_key`                                                                                                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                         | Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the tenant principal and bound to the canonical body for 24 hours.                                                                                                                                                                                                                             |
| `account_id`                                                                                                                                                                                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                         | Your own opaque identifier for the account being checked, scoped to your tenant. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '\|' is accepted so an Auth0 user id such as 'auth0\|64abc' passes unchanged; '@', '+', '$' and whitespace are refused, as is a JWT; a hex digest such as a SHA-256 is allowed. It travels only in request bodies. |
| `identifiers`                                                                                                                                                                                                                                                                                                                                                                              | [shared.AssessmentRequestIdentifiers](../../models/shared/assessmentrequestidentifiers.md)                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                         | At least one of email, username or phone. name and ip refine the match and travel beside a lookup identifier; a body with only name or ip is refused with 400.                                                                                                                                                                                                                             |
| `policy_context`                                                                                                                                                                                                                                                                                                                                                                           | [Optional[shared.AssessmentRequestPolicyContext]](../../models/shared/assessmentrequestpolicycontext.md)                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                         | N/A                                                                                                                                                                                                                                                                                                                                                                                        |
| `request_id`                                                                                                                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                         | An optional provider correlation id, echoed back. It is not an idempotency key. Refuses an exact-shape JWT or a bare 40, 64 or 128 character hex digest; a UUID is accepted.                                                                                                                                                                                                               |
| `deadline_ms`                                                                                                                                                                                                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                         | Optional tighter budget, 50 to 500 ms, measured from the moment the request reaches NoResponse. Absent means the 500 ms ceiling; a value above it is refused with 400 rather than clamped.                                                                                                                                                                                                 |
| `response_mode`                                                                                                                                                                                                                                                                                                                                                                            | [Optional[shared.ResponseMode]](../../models/shared/responsemode.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                         | standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode.                                                                                                                                                                                                                                        |
| `client_context`                                                                                                                                                                                                                                                                                                                                                                           | [Optional[shared.AssessmentRequestClientContext]](../../models/shared/assessmentrequestclientcontext.md)                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                         | Optional context observed by your signup client. The server parses these hints into coarse features, leaves raw user_agent and opaque ids out of every answer, and weighs a mismatch with the other evidence.                                                                                                                                                                              |
| `auth_context`                                                                                                                                                                                                                                                                                                                                                                             | [Optional[shared.AuthContext]](../../models/shared/authcontext.md)                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                         | Normalised claims from a session your backend has already verified with WorkOS, Clerk, Auth0 or any OIDC provider. Pass the output of the SDK's auth adapters, not a raw token.                                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                        |

### Response

**[operations.CreateAssessmentResponse](../../models/operations/createassessmentresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.errors.BadRequestError       | 400                                 | application/problem+json            |
| models.errors.AuthenticationError   | 401                                 | application/problem+json            |
| models.errors.PermissionDeniedError | 403                                 | application/problem+json            |
| models.errors.NotFoundError         | 404                                 | application/problem+json            |
| models.errors.ConflictError         | 409                                 | application/problem+json            |
| models.errors.RateLimitError        | 429                                 | application/problem+json            |
| models.errors.APIStatusError        | 4XX, 5XX                            | \*/\*                               |

## get

Returns the highest assessment_version. Requires the assess or history scope. While status is pending, or partial with a source still running, the response carries Retry-After; poll no faster than it says. Another tenant's assessment, an unknown or expired assessment and a malformed assessment_id all answer 404 not_found. response_mode=detailed needs the detailed scope.

### Example Usage: complete

<!-- UsageSnippet language="python" operationID="getAssessment" method="get" path="/v1/assessments/{assessment_id}" example="complete" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.assessments.get(assessment_id="<id>")

    # Handle response
    print(res)

```
### Example Usage: detailed

<!-- UsageSnippet language="python" operationID="getAssessment" method="get" path="/v1/assessments/{assessment_id}" example="detailed" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.assessments.get(assessment_id="<id>")

    # Handle response
    print(res)

```
### Example Usage: partial

<!-- UsageSnippet language="python" operationID="getAssessment" method="get" path="/v1/assessments/{assessment_id}" example="partial" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.assessments.get(assessment_id="<id>")

    # Handle response
    print(res)

```
### Example Usage: pending

<!-- UsageSnippet language="python" operationID="getAssessment" method="get" path="/v1/assessments/{assessment_id}" example="pending" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.assessments.get(assessment_id="<id>")

    # Handle response
    print(res)

```
### Example Usage: standard

<!-- UsageSnippet language="python" operationID="getAssessment" method="get" path="/v1/assessments/{assessment_id}" example="standard" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.assessments.get(assessment_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `assessment_id`                                                                                                   | *str*                                                                                                             | :heavy_check_mark:                                                                                                | Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400. |
| `response_mode`                                                                                                   | [Optional[shared.ResponseMode]](../../models/shared/responsemode.md)                                              | :heavy_minus_sign:                                                                                                | Optional standard or separately authorised detailed customer view; raw is rejected.                               |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[operations.GetAssessmentResponse](../../models/operations/getassessmentresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.errors.BadRequestError       | 400                                 | application/problem+json            |
| models.errors.AuthenticationError   | 401                                 | application/problem+json            |
| models.errors.PermissionDeniedError | 403                                 | application/problem+json            |
| models.errors.NotFoundError         | 404                                 | application/problem+json            |
| models.errors.ConflictError         | 409                                 | application/problem+json            |
| models.errors.RateLimitError        | 429                                 | application/problem+json            |
| models.errors.APIStatusError        | 4XX, 5XX                            | \*/\*                               |

## record_outcome

Records what you later learned about an assessed account: confirmed_abuse, account_takeover and chargeback report abuse; false_positive and legitimate withdraw your earlier report; unknown is recorded only. Outcomes are append-only and the latest one wins. Requires the assess scope. Idempotency-Key is required and handled as on POST /v1/assessments: a retry with the same key and body answers the same record with Idempotent-Replayed: true; a different body answers 409. An unknown, expired or foreign assessment answers 404 not_found.

### Example Usage: abuse

<!-- UsageSnippet language="python" operationID="recordAssessmentOutcome" method="post" path="/v1/assessments/{assessment_id}/outcomes" example="abuse" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.assessments.record_outcome(assessment_id="<id>", idempotency_key="<value>", outcome="confirmed_abuse", observed_at="2026-10-20T05:00:00Z", external_ref="case-123", notes="Card testing from this account; closed by trust and safety.")

    # Handle response
    print(res)

```
### Example Usage: recorded

<!-- UsageSnippet language="python" operationID="recordAssessmentOutcome" method="post" path="/v1/assessments/{assessment_id}/outcomes" example="recorded" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.assessments.record_outcome(assessment_id="<id>", idempotency_key="<value>", outcome="legitimate")

    # Handle response
    print(res)

```
### Example Usage: withdrawn

<!-- UsageSnippet language="python" operationID="recordAssessmentOutcome" method="post" path="/v1/assessments/{assessment_id}/outcomes" example="withdrawn" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.assessments.record_outcome(assessment_id="<id>", idempotency_key="<value>", outcome="false_positive")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `assessment_id`                                                                                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                  | Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400.                                                                                                                                                                                                                   |
| `idempotency_key`                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                  | Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the tenant principal and bound to the canonical body for 24 hours.                                                                                                                                                                      |
| `outcome`                                                                                                                                                                                                                                                                                                                           | [shared.Outcome](../../models/shared/outcome.md)                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                  | What the provider later learned about the assessed account. confirmed_abuse, account_takeover and chargeback report abuse; false_positive and legitimate withdraw an earlier abuse report of this tenant for the assessment; unknown is recorded only. Outcomes are append-only and the latest one recorded for an assessment wins. |
| `observed_at`                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                  | When the provider observed the outcome. Defaults to when NoResponse received it.                                                                                                                                                                                                                                                    |
| `external_ref`                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                  | Your own opaque reference for the outcome, such as a case or ticket id. Stored as given and not interpreted; keep direct identifiers out of it.                                                                                                                                                                                     |
| `notes`                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                  | Free text for your own records, at most 500 characters. Stored only; it is left out of scoring and answers. Keep personal data out of it. Control characters other than tab and line breaks are refused.                                                                                                                            |
| `retries`                                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                 |

### Response

**[operations.RecordAssessmentOutcomeResponse](../../models/operations/recordassessmentoutcomeresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.errors.BadRequestError       | 400                                 | application/problem+json            |
| models.errors.AuthenticationError   | 401                                 | application/problem+json            |
| models.errors.PermissionDeniedError | 403                                 | application/problem+json            |
| models.errors.NotFoundError         | 404                                 | application/problem+json            |
| models.errors.ConflictError         | 409                                 | application/problem+json            |
| models.errors.RateLimitError        | 429                                 | application/problem+json            |
| models.errors.APIStatusError        | 4XX, 5XX                            | \*/\*                               |

## query

History is a POST with account_id in the body so an account identifier stays out of URLs and access logs. Requires the history scope. Read-only and safe to retry. Newest first, each at its latest assessment_version. An account with no assessments answers 200 with empty items. The cursor is opaque and bound to your tenant and the account; a tampered or expired cursor answers 400 invalid_cursor. response_mode=detailed needs the detailed scope.

### Example Usage: firstPage

<!-- UsageSnippet language="python" operationID="queryAccountAssessments" method="post" path="/v1/assessments/query" example="firstPage" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.assessments.query(account_id="acct_7f3a9c", limit=20)

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: page

<!-- UsageSnippet language="python" operationID="queryAccountAssessments" method="post" path="/v1/assessments/query" example="page" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.assessments.query(account_id="<id>", limit=20)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                                                                                                                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                         | Your own opaque identifier for the account being checked, scoped to your tenant. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '\|' is accepted so an Auth0 user id such as 'auth0\|64abc' passes unchanged; '@', '+', '$' and whitespace are refused, as is a JWT; a hex digest such as a SHA-256 is allowed. It travels only in request bodies. |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                         | N/A                                                                                                                                                                                                                                                                                                                                                                                        |
| `cursor`                                                                                                                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                         | next_cursor from the previous page, unchanged. Opaque, MAC'd and bound to the tenant and account_id.                                                                                                                                                                                                                                                                                       |
| `response_mode`                                                                                                                                                                                                                                                                                                                                                                            | [Optional[shared.ResponseMode]](../../models/shared/responsemode.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                         | standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode.                                                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                        |

### Response

**[operations.QueryAccountAssessmentsResponse](../../models/operations/queryaccountassessmentsresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.errors.BadRequestError       | 400                                 | application/problem+json            |
| models.errors.AuthenticationError   | 401                                 | application/problem+json            |
| models.errors.PermissionDeniedError | 403                                 | application/problem+json            |
| models.errors.NotFoundError         | 404                                 | application/problem+json            |
| models.errors.ConflictError         | 409                                 | application/problem+json            |
| models.errors.RateLimitError        | 429                                 | application/problem+json            |
| models.errors.APIStatusError        | 4XX, 5XX                            | \*/\*                               |