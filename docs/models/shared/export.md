# Export

Retained review snapshot.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `exported_at`                                                      | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                | 2026-01-01T00:00:00Z                                               |
| `review`                                                           | [shared.Review](../../models/shared/review.md)                     | :heavy_check_mark:                                                 | N/A                                                                |                                                                    |
| `comments`                                                         | List[[shared.ReviewComment](../../models/shared/reviewcomment.md)] | :heavy_check_mark:                                                 | N/A                                                                |                                                                    |
| `resolutions`                                                      | List[[shared.Resolution](../../models/shared/resolution.md)]       | :heavy_check_mark:                                                 | N/A                                                                |                                                                    |
| `subjects`                                                         | List[[shared.ReviewSubject](../../models/shared/reviewsubject.md)] | :heavy_check_mark:                                                 | N/A                                                                |                                                                    |