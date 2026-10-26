# FootprintTimeline

One identifier's dated footprint across every source: the first and last year any event was seen, the years between them, the latest year a source dated activity (omitted when none did), how many distinct sites and which kinds of evidence saw it.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `first_seen_year`                                                      | *int*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `last_seen_year`                                                       | *int*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `span_years`                                                           | *int*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `last_active_year`                                                     | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |
| `sites`                                                                | *int*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `families`                                                             | List[[shared.FootprintFamily](../../models/shared/footprintfamily.md)] | :heavy_check_mark:                                                     | N/A                                                                    |