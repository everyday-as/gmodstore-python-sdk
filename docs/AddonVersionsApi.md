# gmodstore_sdk.AddonVersionsApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_addon_version**](AddonVersionsApi.md#create_addon_version) | **POST** /addons/{addon_id}/versions | Create a new version for an addon
[**download_addon_version**](AddonVersionsApi.md#download_addon_version) | **GET** /addons/{addon_id}/versions/{version_id}/download | Generate a download token for a specific version of an addon
[**get_addon_version**](AddonVersionsApi.md#get_addon_version) | **GET** /addons/{addon_id}/versions/{version_id} | Fetch a specific version of an addon
[**list_addon_versions**](AddonVersionsApi.md#list_addon_versions) | **GET** /addons/{addon_id}/versions | Fetch all the versions of an addon
[**update_addon_version**](AddonVersionsApi.md#update_addon_version) | **PUT** /addons/{addon_id}/versions/{version_id} | Update a version of an addon

# **create_addon_version**
> InlineResponse2012 create_addon_version(name, changelog, file, release_type, addon_id, _with=_with)

Create a new version for an addon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.AddonVersionsApi(gmodstore_sdk.ApiClient(configuration))
name = 'name_example' # str | 
changelog = 'changelog_example' # str | 
file = 'file_example' # str | 
release_type = 'release_type_example' # str | 
addon_id = 789 # int | Id of the addon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonVersion schema (optional)

try:
    # Create a new version for an addon
    api_response = api_instance.create_addon_version(name, changelog, file, release_type, addon_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonVersionsApi->create_addon_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **changelog** | **str**|  | 
 **file** | **str**|  | 
 **release_type** | **str**|  | 
 **addon_id** | **int**| Id of the addon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonVersion schema | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_addon_version**
> InlineResponse2008 download_addon_version(addon_id, version_id)

Generate a download token for a specific version of an addon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.AddonVersionsApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
version_id = 789 # int | Id of the version

try:
    # Generate a download token for a specific version of an addon
    api_response = api_instance.download_addon_version(addon_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonVersionsApi->download_addon_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **version_id** | **int**| Id of the version | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addon_version**
> InlineResponse2012 get_addon_version(addon_id, version_id, _with=_with)

Fetch a specific version of an addon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.AddonVersionsApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
version_id = 789 # int | Id of the version
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonVersion schema (optional)

try:
    # Fetch a specific version of an addon
    api_response = api_instance.get_addon_version(addon_id, version_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonVersionsApi->get_addon_version: %s\n" % e)
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_addon_versions**
> InlineResponse2007 list_addon_versions(addon_id, _with=_with)

Fetch all the versions of an addon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.AddonVersionsApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonVersion schema (optional)

try:
    # Fetch all the versions of an addon
    api_response = api_instance.list_addon_versions(addon_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonVersionsApi->list_addon_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonVersion schema | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_addon_version**
> InlineResponse2012 update_addon_version(name, changelog, release_type, addon_id, version_id, _with=_with)

Update a version of an addon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.AddonVersionsApi(gmodstore_sdk.ApiClient(configuration))
name = 'name_example' # str | 
changelog = 'changelog_example' # str | 
release_type = 'release_type_example' # str | 
addon_id = 789 # int | Id of the addon
version_id = 789 # int | Id of the version
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonVersion schema (optional)

try:
    # Update a version of an addon
    api_response = api_instance.update_addon_version(name, changelog, release_type, addon_id, version_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonVersionsApi->update_addon_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **changelog** | **str**|  | 
 **release_type** | **str**|  | 
 **addon_id** | **int**| Id of the addon | 
 **version_id** | **int**| Id of the version | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonVersion schema | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

