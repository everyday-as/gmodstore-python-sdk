# gmodstore_sdk.AddonPurchasesApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addons_addon_id_purchases_get**](AddonPurchasesApi.md#addons_addon_id_purchases_get) | **GET** /addons/{addon_id}/purchases | Fetch all purchases of an addon
[**addons_addon_id_purchases_post**](AddonPurchasesApi.md#addons_addon_id_purchases_post) | **POST** /addons/{addon_id}/purchases | Create a purchase for an addon
[**addons_addon_id_purchases_user_id_get**](AddonPurchasesApi.md#addons_addon_id_purchases_user_id_get) | **GET** /addons/{addon_id}/purchases/{user_id} | Get a purchase of an addon by user
[**addons_addon_id_purchases_user_id_put**](AddonPurchasesApi.md#addons_addon_id_purchases_user_id_put) | **PUT** /addons/{addon_id}/purchases/{user_id} | Update a purchase for an addon

# **addons_addon_id_purchases_get**
> InlineResponse2004 addons_addon_id_purchases_get(addon_id, _with=_with)

Fetch all purchases of an addon

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
api_instance = gmodstore_sdk.AddonPurchasesApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonPurchase schema (optional)

try:
    # Fetch all purchases of an addon
    api_response = api_instance.addons_addon_id_purchases_get(addon_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonPurchasesApi->addons_addon_id_purchases_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonPurchase schema | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_addon_id_purchases_post**
> InlineResponse2011 addons_addon_id_purchases_post(body, addon_id, _with=_with)

Create a purchase for an addon

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
api_instance = gmodstore_sdk.AddonPurchasesApi(gmodstore_sdk.ApiClient(configuration))
body = NULL # object | 
addon_id = 789 # int | Id of the addon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonPurchase schema (optional)

try:
    # Create a purchase for an addon
    api_response = api_instance.addons_addon_id_purchases_post(body, addon_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonPurchasesApi->addons_addon_id_purchases_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **addon_id** | **int**| Id of the addon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonPurchase schema | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_addon_id_purchases_user_id_get**
> InlineResponse2011 addons_addon_id_purchases_user_id_get(addon_id, user_id, _with=_with)

Get a purchase of an addon by user

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
api_instance = gmodstore_sdk.AddonPurchasesApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
user_id = 'user_id_example' # str | Id of the user
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonPurchase schema (optional)

try:
    # Get a purchase of an addon by user
    api_response = api_instance.addons_addon_id_purchases_user_id_get(addon_id, user_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonPurchasesApi->addons_addon_id_purchases_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **user_id** | **str**| Id of the user | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonPurchase schema | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_addon_id_purchases_user_id_put**
> InlineResponse2011 addons_addon_id_purchases_user_id_put(body, addon_id, user_id, _with=_with)

Update a purchase for an addon

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
api_instance = gmodstore_sdk.AddonPurchasesApi(gmodstore_sdk.ApiClient(configuration))
body = NULL # object | 
addon_id = 789 # int | Id of the addon
user_id = 'user_id_example' # str | Id of the user
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonPurchase schema (optional)

try:
    # Update a purchase for an addon
    api_response = api_instance.addons_addon_id_purchases_user_id_put(body, addon_id, user_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonPurchasesApi->addons_addon_id_purchases_user_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **addon_id** | **int**| Id of the addon | 
 **user_id** | **str**| Id of the user | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonPurchase schema | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

