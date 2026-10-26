# FootprintFamily

The source-neutral kind of evidence: account_presence (an account found on a site), auth_provider (the account at your auth provider), breach (breach and credential tables), breach_abuse (abuse and fraud communities' tables) and code_hosting (a code hosting profile).

## Example Usage

```python
from noresponse.models.shared import FootprintFamily

# Open enum: unrecognized values are captured as UnrecognizedStr
value: FootprintFamily = "account_presence"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"account_presence"`
- `"auth_provider"`
- `"breach"`
- `"breach_abuse"`
- `"code_hosting"`
