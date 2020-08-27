# gmodstore_sdk.UserPurchasesApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_user_purchases**](UserPurchasesApi.md#list_user_purchases) | **GET** /users/{user_id}/purchases | Fetch all purchases a user has made

# **list_user_purchases**
> AddonPurchaseListResponse list_user_purchases(user_id, _with=_with)

Fetch all purchases a user has made

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.UserPurchasesApi(gmodstore_sdk.ApiClient(configuration))
user_id = 789 # int | Id of the user
_with = ['_with_example'] # list[str] | The relations you want to fetch with the `AddonPurchase` (optional)

try:
    # Fetch all purchases a user has made
    api_response = api_instance.list_user_purchases(user_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserPurchasesApi->list_user_purchases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of the user | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the &#x60;AddonPurchase&#x60; | [optional] 

### Return type

[**AddonPurchaseListResponse**](AddonPurchaseListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

