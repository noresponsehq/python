# Recommendation

The recommended action: allow, step_up or review. Your application applies it.

## Example Usage

```python
from noresponse.models.shared import Recommendation

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Recommendation = "allow"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"allow"`
- `"step_up"`
- `"review"`
