# InvestigationStatus

## Example Usage

```python
from noresponse.models.shared import InvestigationStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: InvestigationStatus = "queued"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"queued"`
- `"running"`
- `"completed"`
- `"partial"`
- `"failed"`
- `"cancelled"`
- `"unknown"`
