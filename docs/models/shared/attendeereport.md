# AttendeeReport

Everything known about one attendee.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `attendee`                                                           | [shared.Attendee](../../models/shared/attendee.md)                   | :heavy_check_mark:                                                   | An attendee and where their screening and review stand.              |
| `profiles`                                                           | List[[shared.Profile](../../models/shared/profile.md)]               | :heavy_check_mark:                                                   | The accounts the screening matched, with how each was matched.       |
| `findings`                                                           | List[[shared.Finding](../../models/shared/finding.md)]               | :heavy_check_mark:                                                   | What the screening flagged, with its evidence.                       |
| `reviews`                                                            | List[[shared.AttendeeReview](../../models/shared/attendeereview.md)] | :heavy_check_mark:                                                   | Every recorded decision, oldest first.                               |