# FindingBand

How severe a finding is, most severe first.

## Example Usage

```python
from noresponse.models.shared import FindingBand

# Open enum: unrecognized values are captured as UnrecognizedStr
value: FindingBand = "critical"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"critical"`
- `"high"`
- `"moderate"`
- `"low"`
- `"info"`
