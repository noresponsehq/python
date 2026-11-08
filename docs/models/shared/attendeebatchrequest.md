# AttendeeBatchRequest

Adds or updates 1 to 500 attendees. A row naming an existing attendee of the event (the same external_id, else the same email, else the same phone) updates it.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `attendees`                                                              | List[[shared.AttendeeIdentity](../../models/shared/attendeeidentity.md)] | :heavy_check_mark:                                                       | N/A                                                                      |