# AuditEventTargetType

The kind of resource the change acted on.

## Example Usage

```python
from noresponse.models.shared import AuditEventTargetType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AuditEventTargetType = "workspace"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"workspace"`
- `"member"`
- `"invite"`
- `"key"`
- `"setting"`
- `"webhook_endpoint"`
- `"integration"`
- `"billing"`
- `"review"`
