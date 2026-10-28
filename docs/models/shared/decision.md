# Decision

An assessment's own decision: block when its stored risk.block is true, otherwise its recommendation. It is not the account's decision or held-admission state.

## Example Usage

```python
from noresponse.models.shared import Decision

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Decision = "allow"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"allow"`
- `"step_up"`
- `"review"`
- `"block"`
