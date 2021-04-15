# gmodstore-sdk.CurrentAPIKeyApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_api_key**](CurrentAPIKeyApi.md#get_current_api_key) | **GET** /me | Get meta information about the current API key


# **get_current_api_key**
> AddonListResponse get_current_api_key(_with=_with)

Get meta information about the current API key

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
    api_instance = gmodstore-sdk.CurrentAPIKeyApi(api_client)
    _with = ['_with_example'] # list[str] | The relations you want to fetch with the `User` (optional)

    try:
        # Get meta information about the current API key
        api_response = api_instance.get_current_api_key(_with=_with)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CurrentAPIKeyApi->get_current_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the &#x60;User&#x60; | [optional] 

### Return type

[**AddonListResponse**](AddonListResponse.md)

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

