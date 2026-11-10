# ScreeningStatus

partial finished with some attendees or platforms not covered; attendees_failed and attendees_partial count them.

## Example Usage

```python
from noresponse.models.shared import ScreeningStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ScreeningStatus = "queued"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"queued"`
- `"running"`
- `"completed"`
- `"partial"`
- `"failed"`
- `"cancelled"`
