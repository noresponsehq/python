# Decision

The decision of the assessment's latest stored revision: block when its stored risk.block is true, otherwise its recommendation. This is not the account's current decision or held-admission state. Combined with recommendation using AND.

## Example Usage

```python
from noresponse.models.shared import Decision
value: Decision = "allow"
```


## Values

- `"allow"`
- `"step_up"`
- `"review"`
- `"block"`
