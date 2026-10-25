# KeyEnvironment

The environment the key belongs to. A live key assesses with live sources; a test key answers from the deterministic simulator.

## Example Usage

```python
from noresponse.models.shared import KeyEnvironment

# Open enum: unrecognized values are captured as UnrecognizedStr
value: KeyEnvironment = "live"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"live"`
- `"test"`
