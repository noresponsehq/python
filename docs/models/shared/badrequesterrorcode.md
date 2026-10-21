# BadRequestErrorCode

Machine codes an HTTP 400 answer can carry.

## Example Usage

```python
from noresponse.models.shared import BadRequestErrorCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: BadRequestErrorCode = "invalid_request"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"invalid_request"`
- `"invalid_idempotency_key"`
- `"invalid_cursor"`
