# gmodstore-sdk.PermissionGroupsApi

All URIs are relative to *https://www.gmodstore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_permission_group**](PermissionGroupsApi.md#create_permission_group) | **POST** /api/v3/permission-groups | Create a permission group
[**delete_permission_group**](PermissionGroupsApi.md#delete_permission_group) | **DELETE** /api/v3/permission-groups/{permission_group} | Delete the specified permission group
[**get_permission_group**](PermissionGroupsApi.md#get_permission_group) | **GET** /api/v3/permission-groups/{permission_group} | Show the specified permission group
[**list_permission_groups**](PermissionGroupsApi.md#list_permission_groups) | **GET** /api/v3/permission-groups | List all permission groups
[**update_permission_group**](PermissionGroupsApi.md#update_permission_group) | **PUT** /api/v3/permission-groups/{permission_group} | Update the specified permission group


# **create_permission_group**
> CreatePermissionGroupResponse create_permission_group()

Create a permission group

### Example

* Bearer (Personal Access Token) Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import permission_groups_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.new_permission_group_payload import NewPermissionGroupPayload
from gmodstore-sdk.model.create_permission_group_response import CreatePermissionGroupResponse
from pprint import pprint
# Defining the host is optional and defaults to https://www.gmodstore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = gmodstore-sdk.Configuration(
    host = "https://www.gmodstore.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Personal Access Token): PersonalAccessToken
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permission_groups_api.PermissionGroupsApi(api_client)
    new_permission_group_payload = NewPermissionGroupPayload(
        title="title_example",
        permissions="permissions_example",
    ) # NewPermissionGroupPayload |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a permission group
        api_response = api_instance.create_permission_group(new_permission_group_payload=new_permission_group_payload)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling PermissionGroupsApi->create_permission_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_permission_group_payload** | [**NewPermissionGroupPayload**](NewPermissionGroupPayload.md)|  | [optional]

### Return type

[**CreatePermissionGroupResponse**](CreatePermissionGroupResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response containing the newly created permission group |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_permission_group**
> DeletePermissionGroupResponse delete_permission_group(permission_group)

Delete the specified permission group

### Example

* Bearer (Personal Access Token) Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import permission_groups_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.delete_permission_group_response import DeletePermissionGroupResponse
from pprint import pprint
# Defining the host is optional and defaults to https://www.gmodstore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = gmodstore-sdk.Configuration(
    host = "https://www.gmodstore.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Personal Access Token): PersonalAccessToken
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permission_groups_api.PermissionGroupsApi(api_client)
    permission_group = "permission_group_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the specified permission group
        api_response = api_instance.delete_permission_group(permission_group)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling PermissionGroupsApi->delete_permission_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_group** | **str**|  |

### Return type

[**DeletePermissionGroupResponse**](DeletePermissionGroupResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing the permission group that was just deleted |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permission_group**
> GetPermissionGroupResponse get_permission_group(permission_group)

Show the specified permission group

### Example

* Bearer (Personal Access Token) Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import permission_groups_api
from gmodstore-sdk.model.get_permission_group_response import GetPermissionGroupResponse
from gmodstore-sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://www.gmodstore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = gmodstore-sdk.Configuration(
    host = "https://www.gmodstore.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Personal Access Token): PersonalAccessToken
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permission_groups_api.PermissionGroupsApi(api_client)
    permission_group = "permission_group_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Show the specified permission group
        api_response = api_instance.get_permission_group(permission_group)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling PermissionGroupsApi->get_permission_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_group** | **str**|  |

### Return type

[**GetPermissionGroupResponse**](GetPermissionGroupResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing a single permission group |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_permission_groups**
> bool, date, datetime, dict, float, int, list, str, none_type list_permission_groups()

List all permission groups

### Example

* Bearer (Personal Access Token) Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import permission_groups_api
from gmodstore-sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://www.gmodstore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = gmodstore-sdk.Configuration(
    host = "https://www.gmodstore.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Personal Access Token): PersonalAccessToken
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permission_groups_api.PermissionGroupsApi(api_client)
    per_page = 24 # int, none_type |  (optional) if omitted the server will use the default value of 24
    cursor = "cursor_example" # str | The cursor from which to return paginated results starting after (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all permission groups
        api_response = api_instance.list_permission_groups(per_page=per_page, cursor=cursor)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling PermissionGroupsApi->list_permission_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int, none_type**|  | [optional] if omitted the server will use the default value of 24
 **cursor** | **str**| The cursor from which to return paginated results starting after | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing a list of permission groups |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permission_group**
> UpdatePermissionGroupResponse update_permission_group(permission_group)

Update the specified permission group

### Example

* Bearer (Personal Access Token) Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import permission_groups_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.update_permission_group_payload import UpdatePermissionGroupPayload
from gmodstore-sdk.model.update_permission_group_response import UpdatePermissionGroupResponse
from pprint import pprint
# Defining the host is optional and defaults to https://www.gmodstore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = gmodstore-sdk.Configuration(
    host = "https://www.gmodstore.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Personal Access Token): PersonalAccessToken
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permission_groups_api.PermissionGroupsApi(api_client)
    permission_group = "permission_group_example" # str | 
    update_permission_group_payload = UpdatePermissionGroupPayload(
        title="title_example",
        permissions="permissions_example",
    ) # UpdatePermissionGroupPayload |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the specified permission group
        api_response = api_instance.update_permission_group(permission_group)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling PermissionGroupsApi->update_permission_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the specified permission group
        api_response = api_instance.update_permission_group(permission_group, update_permission_group_payload=update_permission_group_payload)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling PermissionGroupsApi->update_permission_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_group** | **str**|  |
 **update_permission_group_payload** | [**UpdatePermissionGroupPayload**](UpdatePermissionGroupPayload.md)|  | [optional]

### Return type

[**UpdatePermissionGroupResponse**](UpdatePermissionGroupResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing the permission group with changes applied |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

