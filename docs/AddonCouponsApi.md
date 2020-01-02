# gmodstore_sdk.AddonCouponsApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addons_addon_id_coupons_coupon_id_delete**](AddonCouponsApi.md#addons_addon_id_coupons_coupon_id_delete) | **DELETE** /addons/{addon_id}/coupons/{coupon_id} | Destroy an addon&#x27;s coupon
[**addons_addon_id_coupons_coupon_id_get**](AddonCouponsApi.md#addons_addon_id_coupons_coupon_id_get) | **GET** /addons/{addon_id}/coupons/{coupon_id} | Fetch an addon&#x27;s coupon
[**addons_addon_id_coupons_coupon_id_put**](AddonCouponsApi.md#addons_addon_id_coupons_coupon_id_put) | **PUT** /addons/{addon_id}/coupons/{coupon_id} | Update an addon&#x27;s coupon
[**addons_addon_id_coupons_get**](AddonCouponsApi.md#addons_addon_id_coupons_get) | **GET** /addons/{addon_id}/coupons | Fetch all the coupons for an addon
[**addons_addon_id_coupons_post**](AddonCouponsApi.md#addons_addon_id_coupons_post) | **POST** /addons/{addon_id}/coupons | Create an addon coupon

# **addons_addon_id_coupons_coupon_id_delete**
> addons_addon_id_coupons_coupon_id_delete(addon_id, coupon_id)

Destroy an addon's coupon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = gmodstore_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = gmodstore_sdk.AddonCouponsApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
coupon_id = 789 # int | Id of the coupon

try:
    # Destroy an addon's coupon
    api_instance.addons_addon_id_coupons_coupon_id_delete(addon_id, coupon_id)
except ApiException as e:
    print("Exception when calling AddonCouponsApi->addons_addon_id_coupons_coupon_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **coupon_id** | **int**| Id of the coupon | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_addon_id_coupons_coupon_id_get**
> InlineResponse201 addons_addon_id_coupons_coupon_id_get(addon_id, coupon_id, _with=_with)

Fetch an addon's coupon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = gmodstore_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = gmodstore_sdk.AddonCouponsApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
coupon_id = 789 # int | Id of the coupon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonCoupon schema (optional)

try:
    # Fetch an addon's coupon
    api_response = api_instance.addons_addon_id_coupons_coupon_id_get(addon_id, coupon_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonCouponsApi->addons_addon_id_coupons_coupon_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **coupon_id** | **int**| Id of the coupon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonCoupon schema | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_addon_id_coupons_coupon_id_put**
> InlineResponse201 addons_addon_id_coupons_coupon_id_put(body, addon_id, coupon_id, _with=_with)

Update an addon's coupon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = gmodstore_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = gmodstore_sdk.AddonCouponsApi(gmodstore_sdk.ApiClient(configuration))
body = NULL # object | 
addon_id = 789 # int | Id of the addon
coupon_id = 789 # int | Id of the coupon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonCoupon schema (optional)

try:
    # Update an addon's coupon
    api_response = api_instance.addons_addon_id_coupons_coupon_id_put(body, addon_id, coupon_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonCouponsApi->addons_addon_id_coupons_coupon_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **addon_id** | **int**| Id of the addon | 
 **coupon_id** | **int**| Id of the coupon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonCoupon schema | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_addon_id_coupons_get**
> InlineResponse2003 addons_addon_id_coupons_get(addon_id, _with=_with)

Fetch all the coupons for an addon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = gmodstore_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = gmodstore_sdk.AddonCouponsApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonCoupon schema (optional)

try:
    # Fetch all the coupons for an addon
    api_response = api_instance.addons_addon_id_coupons_get(addon_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonCouponsApi->addons_addon_id_coupons_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonCoupon schema | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_addon_id_coupons_post**
> InlineResponse201 addons_addon_id_coupons_post(body, addon_id, _with=_with)

Create an addon coupon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = gmodstore_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = gmodstore_sdk.AddonCouponsApi(gmodstore_sdk.ApiClient(configuration))
body = NULL # object | 
addon_id = 789 # int | Id of the addon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonCoupon schema (optional)

try:
    # Create an addon coupon
    api_response = api_instance.addons_addon_id_coupons_post(body, addon_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonCouponsApi->addons_addon_id_coupons_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **addon_id** | **int**| Id of the addon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonCoupon schema | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

