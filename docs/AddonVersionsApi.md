# gmodstore_sdk.AddonVersionsApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addons_addon_id_versions_get**](AddonVersionsApi.md#addons_addon_id_versions_get) | **GET** /addons/{addon_id}/versions | Fetch all the versions of an addon
[**addons_addon_id_versions_post**](AddonVersionsApi.md#addons_addon_id_versions_post) | **POST** /addons/{addon_id}/versions | Create a new version for an addon
[**addons_addon_id_versions_version_id_download_get**](AddonVersionsApi.md#addons_addon_id_versions_version_id_download_get) | **GET** /addons/{addon_id}/versions/{version_id}/download | Generate a download token for a specific version of an addon
[**addons_addon_id_versions_version_id_get**](AddonVersionsApi.md#addons_addon_id_versions_version_id_get) | **GET** /addons/{addon_id}/versions/{version_id} | Fetch a specific version of an addon
[**addons_addon_id_versions_version_id_put**](AddonVersionsApi.md#addons_addon_id_versions_version_id_put) | **PUT** /addons/{addon_id}/versions/{version_id} | Update a version of an addon

# **addons_addon_id_versions_get**
> InlineResponse2007 addons_addon_id_versions_get(addon_id, _with=_with)

Fetch all the versions of an addon

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
api_instance = gmodstore_sdk.AddonVersionsApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonVersion schema (optional)

try:
    # Fetch all the versions of an addon
    api_response = api_instance.addons_addon_id_versions_get(addon_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonVersionsApi->addons_addon_id_versions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonVersion schema | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_addon_id_versions_post**
> InlineResponse2012 addons_addon_id_versions_post(name, changelog, file, addon_id, _with=_with)

Create a new version for an addon

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
api_instance = gmodstore_sdk.AddonVersionsApi(gmodstore_sdk.ApiClient(configuration))
name = 'name_example' # str | 
changelog = 'changelog_example' # str | 
file = 'file_example' # str | 
addon_id = 789 # int | Id of the addon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonVersion schema (optional)

try:
    # Create a new version for an addon
    api_response = api_instance.addons_addon_id_versions_post(name, changelog, file, addon_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonVersionsApi->addons_addon_id_versions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **changelog** | **str**|  | 
 **file** | **str**|  | 
 **addon_id** | **int**| Id of the addon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonVersion schema | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_addon_id_versions_version_id_download_get**
> InlineResponse2008 addons_addon_id_versions_version_id_download_get(addon_id, version_id)

Generate a download token for a specific version of an addon

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
api_instance = gmodstore_sdk.AddonVersionsApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
version_id = 789 # int | Id of the version

try:
    # Generate a download token for a specific version of an addon
    api_response = api_instance.addons_addon_id_versions_version_id_download_get(addon_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonVersionsApi->addons_addon_id_versions_version_id_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **version_id** | **int**| Id of the version | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_addon_id_versions_version_id_get**
> InlineResponse2012 addons_addon_id_versions_version_id_get(addon_id, version_id, _with=_with)

Fetch a specific version of an addon

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
api_instance = gmodstore_sdk.AddonVersionsApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
version_id = 789 # int | Id of the version
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonVersion schema (optional)

try:
    # Fetch a specific version of an addon
    api_response = api_instance.addons_addon_id_versions_version_id_get(addon_id, version_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonVersionsApi->addons_addon_id_versions_version_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **version_id** | **int**| Id of the version | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonVersion schema | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_addon_id_versions_version_id_put**
> InlineResponse2012 addons_addon_id_versions_version_id_put(name, changelog, file, addon_id, version_id, _with=_with)

Update a version of an addon

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
api_instance = gmodstore_sdk.AddonVersionsApi(gmodstore_sdk.ApiClient(configuration))
name = 'name_example' # str | 
changelog = 'changelog_example' # str | 
file = 'file_example' # str | 
addon_id = 789 # int | Id of the addon
version_id = 789 # int | Id of the version
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonVersion schema (optional)

try:
    # Update a version of an addon
    api_response = api_instance.addons_addon_id_versions_version_id_put(name, changelog, file, addon_id, version_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonVersionsApi->addons_addon_id_versions_version_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **changelog** | **str**|  | 
 **file** | **str**|  | 
 **addon_id** | **int**| Id of the addon | 
 **version_id** | **int**| Id of the version | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonVersion schema | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

