# Priority

## Example Usage

```python
from noresponse.models.shared import Priority

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Priority = "low"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"low"`
- `"normal"`
- `"high"`
- `"urgent"`
