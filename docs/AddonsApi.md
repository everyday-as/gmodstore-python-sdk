# gmodstore-sdk.AddonsApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_addon**](AddonsApi.md#get_addon) | **GET** /addons/{addon_id} | Fetch a single addon
[**list_self_addons**](AddonsApi.md#list_self_addons) | **GET** /addons | Fetch all the addons that you have access to


# **get_addon**
> AddonResponse get_addon(addon_id)

Fetch a single addon

### Example

* Bearer (API Key) Authentication (bearerAuth):
```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import addons_api
from gmodstore-sdk.model.addon_response import AddonResponse
from gmodstore-sdk.model.error_response import ErrorResponse
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
    api_instance = addons_api.AddonsApi(api_client)
    addon_id = 1 # int | Id of the addon
    _with = [
        "latest_version",
    ] # [str] | The relations you want to fetch with the `Addon` (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch a single addon
        api_response = api_instance.get_addon(addon_id)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonsApi->get_addon: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch a single addon
        api_response = api_instance.get_addon(addon_id, _with=_with)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonsApi->get_addon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon |
 **_with** | **[str]**| The relations you want to fetch with the &#x60;Addon&#x60; | [optional]

### Return type

[**AddonResponse**](AddonResponse.md)

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

# **list_self_addons**
> AddonListResponse list_self_addons()

Fetch all the addons that you have access to

### Example

* Bearer (API Key) Authentication (bearerAuth):
```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import addons_api
from gmodstore-sdk.model.error_response import ErrorResponse
from gmodstore-sdk.model.addon_list_response import AddonListResponse
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
    api_instance = addons_api.AddonsApi(api_client)
    _with = [
        "latest_version",
    ] # [str] | The relations you want to fetch with the `Addon` (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all the addons that you have access to
        api_response = api_instance.list_self_addons(_with=_with)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonsApi->list_self_addons: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_with** | **[str]**| The relations you want to fetch with the &#x60;Addon&#x60; | [optional]

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

