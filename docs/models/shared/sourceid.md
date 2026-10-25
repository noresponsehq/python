# SourceID

A NoResponse source: github (GitHub accounts), phone (the phone lookup), breach (breach exposure), rdap (the email domain's registration), mx (the email domain's mail servers) or ipintel (IP intelligence).

## Example Usage

```python
from noresponse.models.shared import SourceID

# Open enum: unrecognized values are captured as UnrecognizedStr
value: SourceID = "github"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"github"`
- `"phone"`
- `"breach"`
- `"rdap"`
- `"mx"`
- `"ipintel"`
