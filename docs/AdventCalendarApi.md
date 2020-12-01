# gmodstore-sdk.AdventCalendarApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_advent_calendar_stats**](AdventCalendarApi.md#get_advent_calendar_stats) | **GET** /events/advent-calendar/stats | Fetch statistics relating to the advent calendar event


# **get_advent_calendar_stats**
> AdventCalendarStatsResponse get_advent_calendar_stats()

Fetch statistics relating to the advent calendar event

### Example

* Bearer (API Key) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import gmodstore-sdk
from gmodstore-sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.gmodstore.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = gmodstore-sdk.Configuration(
    host = "https://api.gmodstore.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gmodstore-sdk.AdventCalendarApi(api_client)
    
    try:
        # Fetch statistics relating to the advent calendar event
        api_response = api_instance.get_advent_calendar_stats()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdventCalendarApi->get_advent_calendar_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdventCalendarStatsResponse**](AdventCalendarStatsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully processed the request. |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |
**429** | Too many requests |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset - The UNIX timestamp at which your rate limit quota will reset. <br>  |
**0** | Something went wrong |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

