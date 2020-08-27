# gmodstore_sdk.AddonCouponsApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_addon_coupon**](AddonCouponsApi.md#create_addon_coupon) | **POST** /addons/{addon_id}/coupons | Create an addon coupon
[**delete_addon_coupon**](AddonCouponsApi.md#delete_addon_coupon) | **DELETE** /addons/{addon_id}/coupons/{coupon_id} | Destroy an addon&#x27;s coupon
[**get_addon_coupon**](AddonCouponsApi.md#get_addon_coupon) | **GET** /addons/{addon_id}/coupons/{coupon_id} | Fetch an addon&#x27;s coupon
[**list_addon_coupons**](AddonCouponsApi.md#list_addon_coupons) | **GET** /addons/{addon_id}/coupons | Fetch all the coupons for an addon
[**update_addon_coupon**](AddonCouponsApi.md#update_addon_coupon) | **PUT** /addons/{addon_id}/coupons/{coupon_id} | Update an addon&#x27;s coupon

# **create_addon_coupon**
> AddonCouponResponse create_addon_coupon(body, addon_id, _with=_with)

Create an addon coupon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.AddonCouponsApi(gmodstore_sdk.ApiClient(configuration))
body = gmodstore_sdk.AddonCoupon() # AddonCoupon | 
addon_id = 789 # int | Id of the addon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the `AddonCoupon` (optional)

try:
    # Create an addon coupon
    api_response = api_instance.create_addon_coupon(body, addon_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonCouponsApi->create_addon_coupon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddonCoupon**](AddonCoupon.md)|  | 
 **addon_id** | **int**| Id of the addon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the &#x60;AddonCoupon&#x60; | [optional] 

### Return type

[**AddonCouponResponse**](AddonCouponResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_addon_coupon**
> delete_addon_coupon(addon_id, coupon_id)

Destroy an addon's coupon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.AddonCouponsApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
coupon_id = 789 # int | Id of the coupon

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addon_coupon**
> AddonCouponResponse get_addon_coupon(addon_id, coupon_id, _with=_with)

Fetch an addon's coupon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.AddonCouponsApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
coupon_id = 789 # int | Id of the coupon
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_addon_coupons**
> AddonCouponListResponse list_addon_coupons(addon_id, _with=_with)

Fetch all the coupons for an addon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.AddonCouponsApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_addon_coupon**
> AddonCouponResponse update_addon_coupon(body, addon_id, coupon_id, _with=_with)

Update an addon's coupon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.AddonCouponsApi(gmodstore_sdk.ApiClient(configuration))
body = gmodstore_sdk.AddonCoupon() # AddonCoupon | 
addon_id = 789 # int | Id of the addon
coupon_id = 789 # int | Id of the coupon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the `AddonCoupon` (optional)

try:
    # Update an addon's coupon
    api_response = api_instance.update_addon_coupon(body, addon_id, coupon_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonCouponsApi->update_addon_coupon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddonCoupon**](AddonCoupon.md)|  | 
 **addon_id** | **int**| Id of the addon | 
 **coupon_id** | **int**| Id of the coupon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the &#x60;AddonCoupon&#x60; | [optional] 

### Return type

[**AddonCouponResponse**](AddonCouponResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

