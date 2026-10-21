# ConsistencyValue

How a submitted identifier agrees with what the evidence holds for the other identifiers. unknown is a definite 'cannot tell' (for example a truncated or too-common breach result); absent means the comparison was not made.

## Example Usage

```python
from noresponse.models.shared import ConsistencyValue

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ConsistencyValue = "match"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"match"`
- `"partial"`
- `"mismatch"`
- `"unknown"`
