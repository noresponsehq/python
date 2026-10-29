# UsageCountFlow

assessments only.

## Example Usage

```python
from noresponse.models.shared import UsageCountFlow

# Open enum: unrecognized values are captured as UnrecognizedStr
value: UsageCountFlow = "account_creation"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"account_creation"`
- `"login"`
- `"purchase"`
