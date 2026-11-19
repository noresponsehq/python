# Significance

One rule ranks every change: identity changes (accounts, breaches, identifiers) are high, profile fields are medium, new posts are low.

## Example Usage

```python
from noresponse.models.shared import Significance

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Significance = "high"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"high"`
- `"medium"`
- `"low"`
