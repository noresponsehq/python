# IPSummaryType

The address's network type.

## Example Usage

```python
from noresponse.models.shared import IPSummaryType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: IPSummaryType = "residential"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"residential"`
- `"hosting"`
- `"vpn"`
- `"proxy"`
- `"tor"`
- `"mobile"`
- `"unknown"`
