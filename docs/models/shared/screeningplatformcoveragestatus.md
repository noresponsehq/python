# ScreeningPlatformCoverageStatus

covered read at least one profile; none_found looked and found no account; inaccessible found accounts that are private or locked; failed could not finish looking; unavailable has no resolver or collector enabled.

## Example Usage

```python
from noresponse.models.shared import ScreeningPlatformCoverageStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ScreeningPlatformCoverageStatus = "covered"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"covered"`
- `"none_found"`
- `"inaccessible"`
- `"failed"`
- `"unavailable"`
