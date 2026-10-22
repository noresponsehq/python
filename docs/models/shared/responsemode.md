# ResponseMode

standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode.

## Example Usage

```python
from noresponse.models.shared import ResponseMode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ResponseMode = "standard"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"standard"`
- `"detailed"`
