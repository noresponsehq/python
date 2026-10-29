# Confidence

Evidence coverage: how much of the planned source evidence gave a definite answer. This is not confidence that an identity is genuine, agreement between identifiers, a risk score or a probability. unavailable means no usable evidence answered; a terminal uncovered assessment can have this value and recommend review.

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
