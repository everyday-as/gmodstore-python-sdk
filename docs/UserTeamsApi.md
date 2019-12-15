# gmodstore_sdk.UserTeamsApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_user_id_teams_get**](UserTeamsApi.md#users_user_id_teams_get) | **GET** /users/{user_id}/teams | Fetch all the teams of a user

# **users_user_id_teams_get**
> InlineResponse20011 users_user_id_teams_get(user_id, _with=_with)

Fetch all the teams of a user

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
api_instance = gmodstore_sdk.UserTeamsApi(gmodstore_sdk.ApiClient(configuration))
user_id = 'user_id_example' # str | Id of the user
_with = ['_with_example'] # list[str] | The relations you want to fetch with the Team schema (optional)

try:
    # Fetch all the teams of a user
    api_response = api_instance.users_user_id_teams_get(user_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTeamsApi->users_user_id_teams_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Id of the user | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the Team schema | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

