# Confidence

Ordinal confidence in the recommendation under the current policy: low, medium, high or unavailable.

## Example Usage

```python
from noresponse.models.shared import Confidence

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Confidence = "low"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"low"`
- `"medium"`
- `"high"`
- `"unavailable"`
