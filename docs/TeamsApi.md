# gmodstore_sdk.TeamsApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_team_id_get**](TeamsApi.md#teams_team_id_get) | **GET** /teams/{team_id} | Fetch a single team

# **teams_team_id_get**
> InlineResponse2008 teams_team_id_get(team_id, _with=_with)

Fetch a single team

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
api_instance = gmodstore_sdk.TeamsApi(gmodstore_sdk.ApiClient(configuration))
team_id = 789 # int | Id of the team
_with = ['_with_example'] # list[str] | The relations you want to fetch with the Team schema (optional)

try:
    # Fetch a single team
    api_response = api_instance.teams_team_id_get(team_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_team_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Id of the team | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the Team schema | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

