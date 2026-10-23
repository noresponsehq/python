# Flow

The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow.

## Example Usage

```python
from noresponse.models.shared import Flow

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Flow = "account_creation"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"account_creation"`
- `"login"`
- `"purchase"`
