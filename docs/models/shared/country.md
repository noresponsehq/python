# Country

IP country, phone country, breach countries and policy_context.region together.

## Example Usage

```python
from noresponse.models.shared import Country

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Country = "consistent"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"consistent"`
- `"mismatch"`
- `"unknown"`
