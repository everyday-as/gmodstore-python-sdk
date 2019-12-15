# gmodstore_sdk.UserBansApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_user_id_bans_get**](UserBansApi.md#users_user_id_bans_get) | **GET** /users/{user_id}/bans | Fetch all active bans associated with this user

# **users_user_id_bans_get**
> InlineResponse20012 users_user_id_bans_get(user_id)

Fetch all active bans associated with this user

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
api_instance = gmodstore_sdk.UserBansApi(gmodstore_sdk.ApiClient(configuration))
user_id = 'user_id_example' # str | Id of the user

try:
    # Fetch all active bans associated with this user
    api_response = api_instance.users_user_id_bans_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserBansApi->users_user_id_bans_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Id of the user | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

