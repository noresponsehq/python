# ScreeningNotAnalysedReason

Why an item read was not analysed. video: a video, whose caption alone is read. image_unavailable: the image could not be fetched from the platform. image_unsupported: not a JPEG, PNG, GIF or WebP image, or too large to send. image_limit: past the most images one attendee's analysis reads. refused: the model declined to read it. unfinished: the model cut its batch short or answered outside the schema, or the request was rejected. unverified: a finding cited it with words it does not contain or an image it did not describe. unspecified: the analyser gave no reason.

## Example Usage

```python
from noresponse.models.shared import ScreeningNotAnalysedReason

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ScreeningNotAnalysedReason = "video"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"video"`
- `"image_unavailable"`
- `"image_unsupported"`
- `"image_limit"`
- `"refused"`
- `"unfinished"`
- `"unverified"`
- `"unspecified"`
