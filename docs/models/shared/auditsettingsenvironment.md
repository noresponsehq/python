# AuditSettingsEnvironment

## Example Usage

```python
from noresponse.models.shared import AuditSettingsEnvironment

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AuditSettingsEnvironment = "live"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"live"`
- `"test"`
