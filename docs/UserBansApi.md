# gmodstore-sdk.UserBansApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_user_bans**](UserBansApi.md#list_user_bans) | **GET** /users/{user_id}/bans | Fetch all active bans associated with this user


# **list_user_bans**
> UserBanListResponse list_user_bans(user_id)

Fetch all active bans associated with this user

### Example

* Bearer (API Key) Authentication (bearerAuth):
```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import user_bans_api
from gmodstore-sdk.model.error_response import ErrorResponse
from gmodstore-sdk.model.user_ban_list_response import UserBanListResponse
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
    api_instance = user_bans_api.UserBansApi(api_client)
    user_id = 1 # int | Id of the user

    # example passing only required values which don't have defaults set
    try:
        # Fetch all active bans associated with this user
        api_response = api_instance.list_user_bans(user_id)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling UserBansApi->list_user_bans: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of the user |

### Return type

[**UserBanListResponse**](UserBanListResponse.md)

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

