# gmodstore-sdk.AddonCouponsApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_addon_coupon**](AddonCouponsApi.md#create_addon_coupon) | **POST** /addons/{addon_id}/coupons | Create an addon coupon
[**delete_addon_coupon**](AddonCouponsApi.md#delete_addon_coupon) | **DELETE** /addons/{addon_id}/coupons/{coupon_id} | Destroy an addon&#39;s coupon
[**get_addon_coupon**](AddonCouponsApi.md#get_addon_coupon) | **GET** /addons/{addon_id}/coupons/{coupon_id} | Fetch an addon&#39;s coupon
[**list_addon_coupons**](AddonCouponsApi.md#list_addon_coupons) | **GET** /addons/{addon_id}/coupons | Fetch all the coupons for an addon
[**update_addon_coupon**](AddonCouponsApi.md#update_addon_coupon) | **PUT** /addons/{addon_id}/coupons/{coupon_id} | Update an addon&#39;s coupon


# **create_addon_coupon**
> AddonCouponResponse create_addon_coupon(addon_id, addon_coupon, _with=_with)

Create an addon coupon

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
    api_instance = gmodstore-sdk.AddonCouponsApi(api_client)
    addon_id = 56 # int | Id of the addon
addon_coupon = gmodstore-sdk.AddonCoupon() # AddonCoupon | 
_with = ['_with_example'] # list[str] | The relations you want to fetch with the `AddonCoupon` (optional)

    try:
        # Create an addon coupon
        api_response = api_instance.create_addon_coupon(addon_id, addon_coupon, _with=_with)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddonCouponsApi->create_addon_coupon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **addon_coupon** | [**AddonCoupon**](AddonCoupon.md)|  | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the &#x60;AddonCoupon&#x60; | [optional] 

### Return type

[**AddonCouponResponse**](AddonCouponResponse.md)

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

# **delete_addon_coupon**
> delete_addon_coupon(addon_id, coupon_id)

Destroy an addon's coupon

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
    api_instance = gmodstore-sdk.AddonCouponsApi(api_client)
    addon_id = 56 # int | Id of the addon
coupon_id = 56 # int | Id of the coupon

    try:
        # Destroy an addon's coupon
        api_instance.delete_addon_coupon(addon_id, coupon_id)
    except ApiException as e:
        print("Exception when calling AddonCouponsApi->delete_addon_coupon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **coupon_id** | **int**| Id of the coupon | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully processed the request. |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |
**429** | Too many requests |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset - The UNIX timestamp at which your rate limit quota will reset. <br>  |
**0** | Something went wrong |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addon_coupon**
> AddonCouponResponse get_addon_coupon(addon_id, coupon_id, _with=_with)

Fetch an addon's coupon

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
    api_instance = gmodstore-sdk.AddonCouponsApi(api_client)
    addon_id = 56 # int | Id of the addon
coupon_id = 56 # int | Id of the coupon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the `AddonCoupon` (optional)

    try:
        # Fetch an addon's coupon
        api_response = api_instance.get_addon_coupon(addon_id, coupon_id, _with=_with)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddonCouponsApi->get_addon_coupon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **coupon_id** | **int**| Id of the coupon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the &#x60;AddonCoupon&#x60; | [optional] 

### Return type

[**AddonCouponResponse**](AddonCouponResponse.md)

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

# **list_addon_coupons**
> AddonCouponListResponse list_addon_coupons(addon_id, _with=_with)

Fetch all the coupons for an addon

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
    api_instance = gmodstore-sdk.AddonCouponsApi(api_client)
    addon_id = 56 # int | Id of the addon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the `AddonCoupon` (optional)

    try:
        # Fetch all the coupons for an addon
        api_response = api_instance.list_addon_coupons(addon_id, _with=_with)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddonCouponsApi->list_addon_coupons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the &#x60;AddonCoupon&#x60; | [optional] 

### Return type

[**AddonCouponListResponse**](AddonCouponListResponse.md)

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

# **update_addon_coupon**
> AddonCouponResponse update_addon_coupon(addon_id, coupon_id, addon_coupon, _with=_with)

Update an addon's coupon

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
    api_instance = gmodstore-sdk.AddonCouponsApi(api_client)
    addon_id = 56 # int | Id of the addon
coupon_id = 56 # int | Id of the coupon
addon_coupon = gmodstore-sdk.AddonCoupon() # AddonCoupon | 
_with = ['_with_example'] # list[str] | The relations you want to fetch with the `AddonCoupon` (optional)

    try:
        # Update an addon's coupon
        api_response = api_instance.update_addon_coupon(addon_id, coupon_id, addon_coupon, _with=_with)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddonCouponsApi->update_addon_coupon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **coupon_id** | **int**| Id of the coupon | 
 **addon_coupon** | [**AddonCoupon**](AddonCoupon.md)|  | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the &#x60;AddonCoupon&#x60; | [optional] 

### Return type

[**AddonCouponResponse**](AddonCouponResponse.md)

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

