# gmodstore_sdk.UserBansApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_user_bans**](UserBansApi.md#list_user_bans) | **GET** /users/{user_id}/bans | Fetch all active bans associated with this user

# **list_user_bans**
> BanListResponse list_user_bans(user_id)

Fetch all active bans associated with this user

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.UserBansApi(gmodstore_sdk.ApiClient(configuration))
user_id = 'user_id_example' # str | Id of the user

try:
    # Fetch all active bans associated with this user
    api_response = api_instance.list_user_bans(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserBansApi->list_user_bans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Id of the user | 

### Return type

[**BanListResponse**](BanListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

