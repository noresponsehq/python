# HighestBand

## Example Usage

```python
from noresponse.models.shared import HighestBand

# Open enum: unrecognized values are captured as UnrecognizedStr
value: HighestBand = "critical"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"critical"`
- `"high"`
- `"moderate"`
- `"low"`
- `"info"`
