# AggregateGroupListMatch

The list action captured with the first answer. none means no matching entry was found. For retained_first_answers an absent field means the older assessment did not capture list state; this remains a separate group.

## Example Usage

```python
from noresponse.models.shared import AggregateGroupListMatch

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AggregateGroupListMatch = "block"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"block"`
- `"allow"`
- `"none"`
