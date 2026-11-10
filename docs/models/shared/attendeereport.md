# AttendeeReport

Everything known about one attendee.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `attendee`                                                                      | [shared.Attendee](../../models/shared/attendee.md)                              | :heavy_check_mark:                                                              | An attendee and where their screening and review stand.                         |
| `profiles`                                                                      | List[[shared.ScreeningProfile](../../models/shared/screeningprofile.md)]        | :heavy_check_mark:                                                              | The accounts the latest screening matched, with how each was matched.           |
| `findings`                                                                      | List[[shared.ScreeningFinding](../../models/shared/screeningfinding.md)]        | :heavy_check_mark:                                                              | What the latest screening flagged, most severe first, each citing its evidence. |
| `posts`                                                                         | List[[shared.ScreeningPost](../../models/shared/screeningpost.md)]              | :heavy_check_mark:                                                              | The posts the findings cite.                                                    |
| `media`                                                                         | List[[shared.ScreeningMedia](../../models/shared/screeningmedia.md)]            | :heavy_check_mark:                                                              | The images and videos the findings cite.                                        |
| `reviews`                                                                       | List[[shared.AttendeeReview](../../models/shared/attendeereview.md)]            | :heavy_check_mark:                                                              | Every recorded decision, oldest first.                                          |