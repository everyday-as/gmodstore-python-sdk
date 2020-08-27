# gmodstore_sdk.UsersApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_self_user**](UsersApi.md#get_self_user) | **GET** /users/me | Fetches the current user (API Key Owner)
[**get_user**](UsersApi.md#get_user) | **GET** /users/{user_id} | Fetch a single user

# **get_self_user**
> UserResponse get_self_user(_with=_with)

Fetches the current user (API Key Owner)

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.UsersApi(gmodstore_sdk.ApiClient(configuration))
_with = ['_with_example'] # list[str] | The relations you want to fetch with the `User` (optional)

try:
    # Fetches the current user (API Key Owner)
    api_response = api_instance.get_self_user(_with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_self_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the &#x60;User&#x60; | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserResponse get_user(user_id, _with=_with)

Fetch a single user

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.UsersApi(gmodstore_sdk.ApiClient(configuration))
user_id = 789 # int | Id of the user
_with = ['_with_example'] # list[str] | The relations you want to fetch with the `User` (optional)

try:
    # Fetch a single user
    api_response = api_instance.get_user(user_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of the user | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the &#x60;User&#x60; | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

