# Agreement

## Example Usage

```python
from noresponse.models.shared import Agreement

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Agreement = "match"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"match"`
- `"partial"`
- `"mismatch"`
