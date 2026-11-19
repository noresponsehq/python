# LastError

## Example Usage

```python
from noresponse.models.shared import LastError

# Open enum: unrecognized values are captured as UnrecognizedStr
value: LastError = "screening_cap_exceeded"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"screening_cap_exceeded"`
- `"screening_unavailable"`
- `"person_not_found"`
- `"idempotency_key_reused"`
