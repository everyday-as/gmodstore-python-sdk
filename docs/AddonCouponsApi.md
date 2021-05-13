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
> AddonCouponResponse create_addon_coupon(addon_id, addon_coupon)

Create an addon coupon

### Example

* Bearer (API Key) Authentication (bearerAuth):
```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import addon_coupons_api
from gmodstore-sdk.model.addon_coupon_response import AddonCouponResponse
from gmodstore-sdk.model.error_response import ErrorResponse
from gmodstore-sdk.model.addon_coupon import AddonCoupon
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
    api_instance = addon_coupons_api.AddonCouponsApi(api_client)
    addon_id = 1 # int | Id of the addon
    addon_coupon = AddonCoupon(
        code="code_example",
        percent=1,
        max_uses=1,
        expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        bound_user_id=1,
    ) # AddonCoupon | 
    _with = [
        "addon",
    ] # [str] | The relations you want to fetch with the `AddonCoupon` (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an addon coupon
        api_response = api_instance.create_addon_coupon(addon_id, addon_coupon)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonCouponsApi->create_addon_coupon: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an addon coupon
        api_response = api_instance.create_addon_coupon(addon_id, addon_coupon, _with=_with)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonCouponsApi->create_addon_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon |
 **addon_coupon** | [**AddonCoupon**](AddonCoupon.md)|  |
 **_with** | **[str]**| The relations you want to fetch with the &#x60;AddonCoupon&#x60; | [optional]

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
import time
import gmodstore-sdk
from gmodstore-sdk.api import addon_coupons_api
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
    api_instance = addon_coupons_api.AddonCouponsApi(api_client)
    addon_id = 1 # int | Id of the addon
    coupon_id = 1 # int | Id of the coupon

    # example passing only required values which don't have defaults set
    try:
        # Destroy an addon's coupon
        api_instance.delete_addon_coupon(addon_id, coupon_id)
    except gmodstore-sdk.ApiException as e:
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
> AddonCouponResponse get_addon_coupon(addon_id, coupon_id)

Fetch an addon's coupon

### Example

* Bearer (API Key) Authentication (bearerAuth):
```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import addon_coupons_api
from gmodstore-sdk.model.addon_coupon_response import AddonCouponResponse
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
    api_instance = addon_coupons_api.AddonCouponsApi(api_client)
    addon_id = 1 # int | Id of the addon
    coupon_id = 1 # int | Id of the coupon
    _with = [
        "addon",
    ] # [str] | The relations you want to fetch with the `AddonCoupon` (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch an addon's coupon
        api_response = api_instance.get_addon_coupon(addon_id, coupon_id)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonCouponsApi->get_addon_coupon: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch an addon's coupon
        api_response = api_instance.get_addon_coupon(addon_id, coupon_id, _with=_with)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonCouponsApi->get_addon_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon |
 **coupon_id** | **int**| Id of the coupon |
 **_with** | **[str]**| The relations you want to fetch with the &#x60;AddonCoupon&#x60; | [optional]

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
> AddonCouponListResponse list_addon_coupons(addon_id)

Fetch all the coupons for an addon

### Example

* Bearer (API Key) Authentication (bearerAuth):
```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import addon_coupons_api
from gmodstore-sdk.model.error_response import ErrorResponse
from gmodstore-sdk.model.addon_coupon_list_response import AddonCouponListResponse
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
    api_instance = addon_coupons_api.AddonCouponsApi(api_client)
    addon_id = 1 # int | Id of the addon
    _with = [
        "addon",
    ] # [str] | The relations you want to fetch with the `AddonCoupon` (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch all the coupons for an addon
        api_response = api_instance.list_addon_coupons(addon_id)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonCouponsApi->list_addon_coupons: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all the coupons for an addon
        api_response = api_instance.list_addon_coupons(addon_id, _with=_with)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonCouponsApi->list_addon_coupons: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon |
 **_with** | **[str]**| The relations you want to fetch with the &#x60;AddonCoupon&#x60; | [optional]

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
> AddonCouponResponse update_addon_coupon(addon_id, coupon_id, addon_coupon)

Update an addon's coupon

### Example

* Bearer (API Key) Authentication (bearerAuth):
```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import addon_coupons_api
from gmodstore-sdk.model.addon_coupon_response import AddonCouponResponse
from gmodstore-sdk.model.error_response import ErrorResponse
from gmodstore-sdk.model.addon_coupon import AddonCoupon
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
    api_instance = addon_coupons_api.AddonCouponsApi(api_client)
    addon_id = 1 # int | Id of the addon
    coupon_id = 1 # int | Id of the coupon
    addon_coupon = AddonCoupon(
        code="code_example",
        percent=1,
        max_uses=1,
        expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        bound_user_id=1,
    ) # AddonCoupon | 
    _with = [
        "addon",
    ] # [str] | The relations you want to fetch with the `AddonCoupon` (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an addon's coupon
        api_response = api_instance.update_addon_coupon(addon_id, coupon_id, addon_coupon)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonCouponsApi->update_addon_coupon: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an addon's coupon
        api_response = api_instance.update_addon_coupon(addon_id, coupon_id, addon_coupon, _with=_with)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonCouponsApi->update_addon_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon |
 **coupon_id** | **int**| Id of the coupon |
 **addon_coupon** | [**AddonCoupon**](AddonCoupon.md)|  |
 **_with** | **[str]**| The relations you want to fetch with the &#x60;AddonCoupon&#x60; | [optional]

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

