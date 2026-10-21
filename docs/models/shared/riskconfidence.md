# RiskConfidence

How much of the planned evidence answered; it says nothing about risk.

## Example Usage

```python
from noresponse.models.shared import RiskConfidence

# Open enum: unrecognized values are captured as UnrecognizedStr
value: RiskConfidence = "low"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"low"`
- `"medium"`
- `"high"`
