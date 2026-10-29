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
- `"outcome_conflict"`
- `"credential_conflict"`
- `"binding_conflict"`
- `"list_entry_exists"`
- `"list_limit_reached"`
- `"list_entry_too_broad"`
- `"policy_version_conflict"`
- `"review_version_conflict"`
- `"review_exists"`
- `"review_limit_reached"`
- `"export_conflict"`
- `"evaluation_conflict"`
- `"evaluation_no_proposal"`
- `"evaluation_limit_reached"`
- `"already_member"`
- `"member_limit_reached"`
