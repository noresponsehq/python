# Namespace

Required for username: the username submitted by this customer in this workspace/environment. It does not name or join a source platform. Omit for email and phone.

## Example Usage

```python
from noresponse.models.shared import Namespace

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Namespace = "customer"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"customer"`
