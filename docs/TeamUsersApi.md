# gmodstore_sdk.TeamUsersApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_team_id_users_get**](TeamUsersApi.md#teams_team_id_users_get) | **GET** /teams/{team_id}/users | Fetch all the users in the given team

# **teams_team_id_users_get**
> InlineResponse20010 teams_team_id_users_get(team_id, _with=_with)

Fetch all the users in the given team

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
api_instance = gmodstore_sdk.TeamUsersApi(gmodstore_sdk.ApiClient(configuration))
team_id = 789 # int | Id of the team
_with = ['_with_example'] # list[str] | The relations you want to fetch with the TeamUser schema (optional)

try:
    # Fetch all the users in the given team
    api_response = api_instance.teams_team_id_users_get(team_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamUsersApi->teams_team_id_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Id of the team | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the TeamUser schema | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

