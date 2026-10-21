# Keys

## Overview

Your own API keys.

### Available Operations

* [rotate](#rotate) - Rotate the API key that signs the request.

## rotate

Mints a new key with the same scopes as the key that signs the request and returns it once. The presented key keeps working for overlap_seconds (default 24 hours, from 60 seconds to 7 days), then answers 401. A key accepts one rotation: rotating again with a key already in its overlap answers 409 key_rotation_in_progress, so rotate with the new key. Rotation is not idempotent: a retry after a lost answer mints another key.

### Example Usage: default

<!-- UsageSnippet language="python" operationID="rotateApiKey" method="post" path="/v1/keys/rotate" example="default" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.keys.rotate()

    # Handle response
    print(res)

```
### Example Usage: one_hour

<!-- UsageSnippet language="python" operationID="rotateApiKey" method="post" path="/v1/keys/rotate" example="one_hour" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.keys.rotate(overlap_seconds=3600)

    # Handle response
    print(res)

```
### Example Usage: rotated

<!-- UsageSnippet language="python" operationID="rotateApiKey" method="post" path="/v1/keys/rotate" example="rotated" -->
```python
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.keys.rotate()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                           | Type                                                                                                                                                                                | Required                                                                                                                                                                            | Description                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `overlap_seconds`                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                  | How long the presented key keeps working beside the new one, from 60 seconds to 7 days. Default 86400 (24 hours). At the end of the overlap the presented key stops authenticating. |

### Response

**[operations.RotateAPIKeyResponse](../../models/operations/rotateapikeyresponse.md)**

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