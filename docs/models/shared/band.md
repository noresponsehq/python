# Band

## Example Usage

```python
from noresponse.models.shared import Band

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Band = "low"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"low"`
- `"medium"`
- `"high"`
- `"critical"`
