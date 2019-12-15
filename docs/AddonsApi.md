# gmodstore_sdk.AddonsApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addons_addon_id_get**](AddonsApi.md#addons_addon_id_get) | **GET** /addons/{addon_id} | Fetch a single addon
[**addons_get**](AddonsApi.md#addons_get) | **GET** /addons | Fetch all the addons that you have access to

# **addons_addon_id_get**
> InlineResponse2001 addons_addon_id_get(addon_id, _with=_with)

Fetch a single addon

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
api_instance = gmodstore_sdk.AddonsApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the Addon schema (optional)

try:
    # Fetch a single addon
    api_response = api_instance.addons_addon_id_get(addon_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonsApi->addons_addon_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the Addon schema | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_get**
> InlineResponse200 addons_get(_with=_with)

Fetch all the addons that you have access to

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
api_instance = gmodstore_sdk.AddonsApi(gmodstore_sdk.ApiClient(configuration))
_with = ['_with_example'] # list[str] | The relations you want to fetch with the Addon schema (optional)

try:
    # Fetch all the addons that you have access to
    api_response = api_instance.addons_get(_with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonsApi->addons_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the Addon schema | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

