# Basis

stated: read from a record. inferred: reasoned from several facts. absence: every source answered and none found it.

## Example Usage

```python
from noresponse.models.shared import Basis

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Basis = "stated"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"stated"`
- `"inferred"`
- `"absence"`
