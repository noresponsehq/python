# SourceID

A NoResponse source: github (GitHub accounts), phone (the phone lookup), breach (breach exposure), rdap (the email domain's registration), mx (the email domain's mail servers), ipintel (IP intelligence) or an email account source that searches one platform for an account by email address (adobe, nvidia, wix, life360, zapier, google). google runs only for Gmail addresses.

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
- `"adobe"`
- `"nvidia"`
- `"wix"`
- `"life360"`
- `"zapier"`
- `"google"`
