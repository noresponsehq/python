# ConflictErrorCode

Machine codes an HTTP 409 answer can carry.

## Example Usage

```python
from noresponse.models.shared import ConflictErrorCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ConflictErrorCode = "idempotency_key_reused"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"idempotency_key_reused"`
- `"key_rotation_in_progress"`
