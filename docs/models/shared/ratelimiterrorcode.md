# RateLimitErrorCode

Machine codes an HTTP 429 answer can carry.

## Example Usage

```python
from noresponse.models.shared import RateLimitErrorCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: RateLimitErrorCode = "rate_limited"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"rate_limited"`
