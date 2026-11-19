# Stage

## Example Usage

```python
from noresponse.models.shared import Stage

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Stage = "lookup"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"lookup"`
- `"lookup_typing"`
- `"platforms"`
- `"written"`
- `"late_platforms"`
- `"late_lookup"`
- `"ai_typing"`
- `"analysis"`
- `"rating"`
