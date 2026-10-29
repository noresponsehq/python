# ErasureReceiptTargetName

## Example Usage

```python
from noresponse.models.shared import ErasureReceiptTargetName

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ErasureReceiptTargetName = "serving"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"serving"`
- `"outbox"`
- `"cache"`
- `"downstream_projection"`
