# Lane

An evidence lane: accounts (account presence for email and username), phone, breach and ip.

## Example Usage

```python
from noresponse.models.shared import Lane

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Lane = "accounts"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"accounts"`
- `"phone"`
- `"breach"`
- `"ip"`
