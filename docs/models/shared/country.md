# Country

IP country, phone country, breach countries and policy_context.region together. When the breach records give a country, the timezone and locale countries count too. The IP country of a proxy or hosting network does not count.

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
