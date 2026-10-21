<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from noresponse import NoResponse
import os


with NoResponse(
    api_key=os.getenv("NORESPONSE_API_KEY", ""),
) as no_response:

    res = no_response.assessments.create(idempotency_key="<value>", account_id="acct_7f3a9c", identifiers={
        "email": "new.user@example.com",
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from noresponse import NoResponse
import os

async def main():

    async with NoResponse(
        api_key=os.getenv("NORESPONSE_API_KEY", ""),
    ) as no_response:

        res = await no_response.assessments.create_async(idempotency_key="<value>", account_id="acct_7f3a9c", identifiers={
            "email": "new.user@example.com",
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->