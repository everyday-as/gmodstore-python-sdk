# gmodstore_sdk.TeamUsersApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_team_users**](TeamUsersApi.md#list_team_users) | **GET** /teams/{team_id}/users | Fetch all the users in the given team

# **list_team_users**
> InlineResponse20010 list_team_users(team_id, _with=_with)

Fetch all the users in the given team

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.TeamUsersApi(gmodstore_sdk.ApiClient(configuration))
team_id = 789 # int | Id of the team
_with = ['_with_example'] # list[str] | The relations you want to fetch with the TeamUser schema (optional)

try:
    # Fetch all the users in the given team
    api_response = api_instance.list_team_users(team_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamUsersApi->list_team_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Id of the team | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the TeamUser schema | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

