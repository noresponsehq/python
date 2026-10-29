# Source

## Example Usage

```python
from noresponse.models.shared import Source

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Source = "requests"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"requests"`
- `"webhook_attempts"`
