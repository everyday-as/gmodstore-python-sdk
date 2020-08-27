# gmodstore_sdk.UserTeamsApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_user_teams**](UserTeamsApi.md#list_user_teams) | **GET** /users/{user_id}/teams | Fetch all the teams of a user

# **list_user_teams**
> TeamListResponse list_user_teams(user_id, _with=_with)

Fetch all the teams of a user

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.UserTeamsApi(gmodstore_sdk.ApiClient(configuration))
user_id = 'user_id_example' # str | Id of the user
_with = ['_with_example'] # list[str] | The relations you want to fetch with the Team schema (optional)

try:
    # Fetch all the teams of a user
    api_response = api_instance.list_user_teams(user_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTeamsApi->list_user_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Id of the user | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the Team schema | [optional] 

### Return type

[**TeamListResponse**](TeamListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

