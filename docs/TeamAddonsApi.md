# gmodstore-sdk.TeamAddonsApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_team_addons**](TeamAddonsApi.md#list_team_addons) | **GET** /teams/{team_id}/addons | Fetch all the addons in the given team


# **list_team_addons**
> TeamAddonListResponse list_team_addons(team_id)

Fetch all the addons in the given team

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import team_addons_api
from gmodstore-sdk.model.error_response import ErrorResponse
from gmodstore-sdk.model.team_addon_list_response import TeamAddonListResponse
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
    api_instance = team_addons_api.TeamAddonsApi(api_client)
    team_id = 1 # int | Id of the team

    # example passing only required values which don't have defaults set
    try:
        # Fetch all the addons in the given team
        api_response = api_instance.list_team_addons(team_id)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling TeamAddonsApi->list_team_addons: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Id of the team |

### Return type

[**TeamAddonListResponse**](TeamAddonListResponse.md)

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

