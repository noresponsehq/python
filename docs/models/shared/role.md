# Role

A built-in capability set. Specialist roles are independent; effective access is returned by GET /v1/workspaces/{workspace_id}/capabilities.

## Example Usage

```python
from noresponse.models.shared import Role

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Role = "owner"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"owner"`
- `"admin"`
- `"developer"`
- `"viewer"`
- `"investigator"`
- `"auditor"`
- `"billing"`
