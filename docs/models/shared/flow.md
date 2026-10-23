# Flow

The customer event an assessment is made for: signup (a new account), login (a returning sign-in) or purchase (a payment or credit grant). The account's risk is reported with the decision for this flow.

## Example Usage

```python
from noresponse.models.shared import Flow

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Flow = "signup"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"signup"`
- `"login"`
- `"purchase"`
