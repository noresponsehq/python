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
- `"webhook_endpoint_limit_reached"`
- `"webhook_endpoint_unverified"`
- `"too_many_integrations"`
- `"risk_version_ahead"`
- `"key_limit_reached"`
- `"self_revocation"`
- `"list_entry_exists"`
- `"list_limit_reached"`
- `"list_entry_too_broad"`
