# gmodstore-sdk.AddonPurchasesApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_addon_purchase**](AddonPurchasesApi.md#create_addon_purchase) | **POST** /addons/{addon_id}/purchases | Create a purchase for an addon
[**get_addon_purchase**](AddonPurchasesApi.md#get_addon_purchase) | **GET** /addons/{addon_id}/purchases/{user_id} | Get a purchase of an addon by user
[**list_addon_purchases**](AddonPurchasesApi.md#list_addon_purchases) | **GET** /addons/{addon_id}/purchases | Fetch all purchases of an addon
[**update_addon_purchase**](AddonPurchasesApi.md#update_addon_purchase) | **PUT** /addons/{addon_id}/purchases/{user_id} | Update a purchase for an addon


# **create_addon_purchase**
> AddonPurchaseResponse create_addon_purchase(addon_id, new_addon_purchase, _with=_with)

Create a purchase for an addon

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
    api_instance = gmodstore-sdk.AddonPurchasesApi(api_client)
    addon_id = 56 # int | Id of the addon
new_addon_purchase = gmodstore-sdk.NewAddonPurchase() # NewAddonPurchase | 
_with = ['_with_example'] # list[str] | The relations you want to fetch with the `AddonPurchase` (optional)

    try:
        # Create a purchase for an addon
        api_response = api_instance.create_addon_purchase(addon_id, new_addon_purchase, _with=_with)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddonPurchasesApi->create_addon_purchase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **new_addon_purchase** | [**NewAddonPurchase**](NewAddonPurchase.md)|  | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the &#x60;AddonPurchase&#x60; | [optional] 

### Return type

[**AddonPurchaseResponse**](AddonPurchaseResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully processed the request. |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |
**429** | Too many requests |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset - The UNIX timestamp at which your rate limit quota will reset. <br>  |
**0** | Something went wrong |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addon_purchase**
> AddonPurchaseResponse get_addon_purchase(addon_id, user_id, _with=_with)

Get a purchase of an addon by user

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
    api_instance = gmodstore-sdk.AddonPurchasesApi(api_client)
    addon_id = 56 # int | Id of the addon
user_id = 56 # int | Id of the user
_with = ['_with_example'] # list[str] | The relations you want to fetch with the `AddonPurchase` (optional)

    try:
        # Get a purchase of an addon by user
        api_response = api_instance.get_addon_purchase(addon_id, user_id, _with=_with)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddonPurchasesApi->get_addon_purchase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **user_id** | **int**| Id of the user | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the &#x60;AddonPurchase&#x60; | [optional] 

### Return type

[**AddonPurchaseResponse**](AddonPurchaseResponse.md)

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

# **list_addon_purchases**
> AddonPurchaseListResponse list_addon_purchases(addon_id, _with=_with)

Fetch all purchases of an addon

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
    api_instance = gmodstore-sdk.AddonPurchasesApi(api_client)
    addon_id = 56 # int | Id of the addon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the `AddonPurchase` (optional)

    try:
        # Fetch all purchases of an addon
        api_response = api_instance.list_addon_purchases(addon_id, _with=_with)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddonPurchasesApi->list_addon_purchases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the &#x60;AddonPurchase&#x60; | [optional] 

### Return type

[**AddonPurchaseListResponse**](AddonPurchaseListResponse.md)

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

# **update_addon_purchase**
> AddonPurchaseResponse update_addon_purchase(addon_id, user_id, addon_purchase, _with=_with)

Update a purchase for an addon

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
    api_instance = gmodstore-sdk.AddonPurchasesApi(api_client)
    addon_id = 56 # int | Id of the addon
user_id = 56 # int | Id of the user
addon_purchase = gmodstore-sdk.AddonPurchase() # AddonPurchase | 
_with = ['_with_example'] # list[str] | The relations you want to fetch with the `AddonPurchase` (optional)

    try:
        # Update a purchase for an addon
        api_response = api_instance.update_addon_purchase(addon_id, user_id, addon_purchase, _with=_with)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddonPurchasesApi->update_addon_purchase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **user_id** | **int**| Id of the user | 
 **addon_purchase** | [**AddonPurchase**](AddonPurchase.md)|  | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the &#x60;AddonPurchase&#x60; | [optional] 

### Return type

[**AddonPurchaseResponse**](AddonPurchaseResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully processed the request. |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |
**429** | Too many requests |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset - The UNIX timestamp at which your rate limit quota will reset. <br>  |
**0** | Something went wrong |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

