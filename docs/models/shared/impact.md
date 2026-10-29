# Impact

The selected reason's served impact band. Requires reason.

## Example Usage

```python
from noresponse.models.shared import Impact

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Impact = "none"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"none"`
- `"low"`
- `"medium"`
- `"high"`
