# gmodstore-sdk.AddonVersionsApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_addon_version**](AddonVersionsApi.md#create_addon_version) | **POST** /addons/{addon_id}/versions | Create a new version for an addon
[**download_addon_version**](AddonVersionsApi.md#download_addon_version) | **GET** /addons/{addon_id}/versions/{version_id}/download | Generate a download token for a specific version of an addon
[**get_addon_version**](AddonVersionsApi.md#get_addon_version) | **GET** /addons/{addon_id}/versions/{version_id} | Fetch a specific version of an addon
[**list_addon_versions**](AddonVersionsApi.md#list_addon_versions) | **GET** /addons/{addon_id}/versions | Fetch all the versions of an addon
[**update_addon_version**](AddonVersionsApi.md#update_addon_version) | **PUT** /addons/{addon_id}/versions/{version_id} | Update a version of an addon


# **create_addon_version**
> AddonVersionResponse create_addon_version(addon_id, new_addon_version)

Create a new version for an addon

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import addon_versions_api
from gmodstore-sdk.model.new_addon_version import NewAddonVersion
from gmodstore-sdk.model.error_response import ErrorResponse
from gmodstore-sdk.model.addon_version_response import AddonVersionResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.gmodstore.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = gmodstore-sdk.Configuration(
    host = "https://api.gmodstore.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = addon_versions_api.AddonVersionsApi(api_client)
    addon_id = 1 # int | Id of the addon
    new_addon_version = NewAddonVersion(
        name="name_example",
        changelog="changelog_example",
        file=open('/path/to/file', 'rb'),
        release_type=AddonVersionReleaseType("stable"),
    ) # NewAddonVersion | 
    _with = [
        "addon",
    ] # [str] | The relations you want to fetch with the `AddonVersion` (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new version for an addon
        api_response = api_instance.create_addon_version(addon_id, new_addon_version)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonVersionsApi->create_addon_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new version for an addon
        api_response = api_instance.create_addon_version(addon_id, new_addon_version, _with=_with)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonVersionsApi->create_addon_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon |
 **new_addon_version** | [**NewAddonVersion**](NewAddonVersion.md)|  |
 **_with** | **[str]**| The relations you want to fetch with the &#x60;AddonVersion&#x60; | [optional]

### Return type

[**AddonVersionResponse**](AddonVersionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully processed the request. |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |
**429** | Too many requests |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset - The UNIX timestamp at which your rate limit quota will reset. <br>  |
**0** | Something went wrong |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_addon_version**
> AddonDownloadResponse download_addon_version(addon_id, version_id)

Generate a download token for a specific version of an addon

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import addon_versions_api
from gmodstore-sdk.model.addon_download_response import AddonDownloadResponse
from gmodstore-sdk.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.gmodstore.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = gmodstore-sdk.Configuration(
    host = "https://api.gmodstore.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = addon_versions_api.AddonVersionsApi(api_client)
    addon_id = 1 # int | Id of the addon
    version_id = 1 # int | Id of the version

    # example passing only required values which don't have defaults set
    try:
        # Generate a download token for a specific version of an addon
        api_response = api_instance.download_addon_version(addon_id, version_id)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonVersionsApi->download_addon_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon |
 **version_id** | **int**| Id of the version |

### Return type

[**AddonDownloadResponse**](AddonDownloadResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully processed the request. |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |
**429** | Too many requests |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset - The UNIX timestamp at which your rate limit quota will reset. <br>  |
**0** | Something went wrong |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addon_version**
> AddonVersionResponse get_addon_version(addon_id, version_id)

Fetch a specific version of an addon

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import addon_versions_api
from gmodstore-sdk.model.error_response import ErrorResponse
from gmodstore-sdk.model.addon_version_response import AddonVersionResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.gmodstore.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = gmodstore-sdk.Configuration(
    host = "https://api.gmodstore.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = addon_versions_api.AddonVersionsApi(api_client)
    addon_id = 1 # int | Id of the addon
    version_id = 1 # int | Id of the version
    _with = [
        "addon",
    ] # [str] | The relations you want to fetch with the `AddonVersion` (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch a specific version of an addon
        api_response = api_instance.get_addon_version(addon_id, version_id)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonVersionsApi->get_addon_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch a specific version of an addon
        api_response = api_instance.get_addon_version(addon_id, version_id, _with=_with)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonVersionsApi->get_addon_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon |
 **version_id** | **int**| Id of the version |
 **_with** | **[str]**| The relations you want to fetch with the &#x60;AddonVersion&#x60; | [optional]

### Return type

[**AddonVersionResponse**](AddonVersionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully processed the request. |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |
**429** | Too many requests |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset - The UNIX timestamp at which your rate limit quota will reset. <br>  |
**0** | Something went wrong |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_addon_versions**
> AddonVersionListResponse list_addon_versions(addon_id)

Fetch all the versions of an addon

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import addon_versions_api
from gmodstore-sdk.model.error_response import ErrorResponse
from gmodstore-sdk.model.addon_version_list_response import AddonVersionListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.gmodstore.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = gmodstore-sdk.Configuration(
    host = "https://api.gmodstore.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = addon_versions_api.AddonVersionsApi(api_client)
    addon_id = 1 # int | Id of the addon
    _with = [
        "addon",
    ] # [str] | The relations you want to fetch with the `AddonVersion` (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch all the versions of an addon
        api_response = api_instance.list_addon_versions(addon_id)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonVersionsApi->list_addon_versions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all the versions of an addon
        api_response = api_instance.list_addon_versions(addon_id, _with=_with)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonVersionsApi->list_addon_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon |
 **_with** | **[str]**| The relations you want to fetch with the &#x60;AddonVersion&#x60; | [optional]

### Return type

[**AddonVersionListResponse**](AddonVersionListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully processed the request. |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |
**429** | Too many requests |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset - The UNIX timestamp at which your rate limit quota will reset. <br>  |
**0** | Something went wrong |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_addon_version**
> AddonVersionResponse update_addon_version(addon_id, version_id, addon_version)

Update a version of an addon

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import addon_versions_api
from gmodstore-sdk.model.error_response import ErrorResponse
from gmodstore-sdk.model.addon_version_response import AddonVersionResponse
from gmodstore-sdk.model.addon_version import AddonVersion
from pprint import pprint
# Defining the host is optional and defaults to https://api.gmodstore.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = gmodstore-sdk.Configuration(
    host = "https://api.gmodstore.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = addon_versions_api.AddonVersionsApi(api_client)
    addon_id = 1 # int | Id of the addon
    version_id = 1 # int | Id of the version
    addon_version = AddonVersion(
        name="name_example",
        changelog="changelog_example",
        release_type=AddonVersionReleaseType("stable"),
    ) # AddonVersion | 
    _with = [
        "addon",
    ] # [str] | The relations you want to fetch with the `AddonVersion` (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a version of an addon
        api_response = api_instance.update_addon_version(addon_id, version_id, addon_version)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonVersionsApi->update_addon_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a version of an addon
        api_response = api_instance.update_addon_version(addon_id, version_id, addon_version, _with=_with)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonVersionsApi->update_addon_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon |
 **version_id** | **int**| Id of the version |
 **addon_version** | [**AddonVersion**](AddonVersion.md)|  |
 **_with** | **[str]**| The relations you want to fetch with the &#x60;AddonVersion&#x60; | [optional]

### Return type

[**AddonVersionResponse**](AddonVersionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully processed the request. |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |
**429** | Too many requests |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset - The UNIX timestamp at which your rate limit quota will reset. <br>  |
**0** | Something went wrong |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

