# Freshness

Freshness class of the evidence behind a signal. unknown whenever no evidence was obtained.

## Example Usage

```python
from noresponse.models.shared import Freshness

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Freshness = "fresh"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"fresh"`
- `"stale"`
- `"unknown"`
