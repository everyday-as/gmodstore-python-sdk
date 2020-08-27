# gmodstore_sdk.AddonPurchasesApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_addon_purchase**](AddonPurchasesApi.md#create_addon_purchase) | **POST** /addons/{addon_id}/purchases | Create a purchase for an addon
[**get_addon_purchase**](AddonPurchasesApi.md#get_addon_purchase) | **GET** /addons/{addon_id}/purchases/{user_id} | Get a purchase of an addon by user
[**list_addon_purchases**](AddonPurchasesApi.md#list_addon_purchases) | **GET** /addons/{addon_id}/purchases | Fetch all purchases of an addon
[**update_addon_purchase**](AddonPurchasesApi.md#update_addon_purchase) | **PUT** /addons/{addon_id}/purchases/{user_id} | Update a purchase for an addon

# **create_addon_purchase**
> InlineResponse2011 create_addon_purchase(body, addon_id, _with=_with)

Create a purchase for an addon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.AddonPurchasesApi(gmodstore_sdk.ApiClient(configuration))
body = gmodstore_sdk.AddonPurchaseCreateBody() # AddonPurchaseCreateBody | 
addon_id = 789 # int | Id of the addon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonPurchase schema (optional)

try:
    # Create a purchase for an addon
    api_response = api_instance.create_addon_purchase(body, addon_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonPurchasesApi->create_addon_purchase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddonPurchaseCreateBody**](AddonPurchaseCreateBody.md)|  | 
 **addon_id** | **int**| Id of the addon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonPurchase schema | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addon_purchase**
> InlineResponse2011 get_addon_purchase(addon_id, user_id, _with=_with)

Get a purchase of an addon by user

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.AddonPurchasesApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
user_id = 'user_id_example' # str | Id of the user
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonPurchase schema (optional)

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
 **user_id** | **str**| Id of the user | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonPurchase schema | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_addon_purchases**
> InlineResponse2004 list_addon_purchases(addon_id, _with=_with)

Fetch all purchases of an addon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.AddonPurchasesApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonPurchase schema (optional)

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
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonPurchase schema | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_addon_purchase**
> InlineResponse2011 update_addon_purchase(body, addon_id, user_id, _with=_with)

Update a purchase for an addon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.AddonPurchasesApi(gmodstore_sdk.ApiClient(configuration))
body = gmodstore_sdk.AddonPurchaseUpdateBody() # AddonPurchaseUpdateBody | 
addon_id = 789 # int | Id of the addon
user_id = 'user_id_example' # str | Id of the user
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonPurchase schema (optional)

try:
    # Update a purchase for an addon
    api_response = api_instance.update_addon_purchase(body, addon_id, user_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonPurchasesApi->update_addon_purchase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddonPurchaseUpdateBody**](AddonPurchaseUpdateBody.md)|  | 
 **addon_id** | **int**| Id of the addon | 
 **user_id** | **str**| Id of the user | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonPurchase schema | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

