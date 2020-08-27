# gmodstore_sdk.AddonStatsApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_addon_stats**](AddonStatsApi.md#get_addon_stats) | **GET** /addons/{addon_id}/stats | Fetch all the stats for an addon

# **get_addon_stats**
> InlineResponse2002 get_addon_stats(addon_id)

Fetch all the stats for an addon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.AddonStatsApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon

try:
    # Fetch all the stats for an addon
    api_response = api_instance.get_addon_stats(addon_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonStatsApi->get_addon_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

