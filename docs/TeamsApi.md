# gmodstore_sdk.TeamsApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_team**](TeamsApi.md#get_team) | **GET** /teams/{team_id} | Fetch a single team

# **get_team**
> TeamResponse get_team(team_id, _with=_with)

Fetch a single team

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.TeamsApi(gmodstore_sdk.ApiClient(configuration))
team_id = 789 # int | Id of the team
_with = ['_with_example'] # list[str] | The relations you want to fetch with the Team schema (optional)

try:
    # Fetch a single team
    api_response = api_instance.get_team(team_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Id of the team | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the Team schema | [optional] 

### Return type

[**TeamResponse**](TeamResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

