# gmodstore-sdk.UsersApi

All URIs are relative to *https://www.gmodstore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_me**](UsersApi.md#get_me) | **GET** /api/v3/me | Fetch the current authenticated user and their access token
[**get_user**](UsersApi.md#get_user) | **GET** /api/v3/users/{user} | Fetch the specified user
[**get_users**](UsersApi.md#get_users) | **GET** /api/v3/users/batch | Fetch a batch of users by id
[**list_users**](UsersApi.md#list_users) | **GET** /api/v3/users | List all users


# **get_me**
> GetMeResponse get_me()

Fetch the current authenticated user and their access token

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import users_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.get_me_response import GetMeResponse
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

# Configure Bearer authorization: PersonalAccessToken
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch the current authenticated user and their access token
        api_response = api_instance.get_me()
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling UsersApi->get_me: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMeResponse**](GetMeResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing the authenticated user and their access token |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> GetUserResponse get_user(user)

Fetch the specified user

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import users_api
from gmodstore-sdk.model.user_filter import UserFilter
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.get_user_response import GetUserResponse
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

# Configure Bearer authorization: PersonalAccessToken
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user = "user_example" # str | 
    filter = UserFilter(
        steam_id=1,
    ) # UserFilter | Filter the results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch the specified user
        api_response = api_instance.get_user(user)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch the specified user
        api_response = api_instance.get_user(user, filter=filter)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**|  |
 **filter** | **UserFilter**| Filter the results | [optional]

### Return type

[**GetUserResponse**](GetUserResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing a single user |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> GetUsersResponse get_users(ids)

Fetch a batch of users by id

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import users_api
from gmodstore-sdk.model.user_filter import UserFilter
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.get_users_response import GetUsersResponse
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

# Configure Bearer authorization: PersonalAccessToken
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    ids = [
        "ids[]_example",
    ] # [str] | 
    filter = UserFilter(
        steam_id=1,
    ) # UserFilter | Filter the results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch a batch of users by id
        api_response = api_instance.get_users(ids)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling UsersApi->get_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch a batch of users by id
        api_response = api_instance.get_users(ids, filter=filter)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling UsersApi->get_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**|  |
 **filter** | **UserFilter**| Filter the results | [optional]

### Return type

[**GetUsersResponse**](GetUsersResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing the requested batch of users |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> bool, date, datetime, dict, float, int, list, str, none_type list_users()

List all users

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import users_api
from gmodstore-sdk.model.user_filter import UserFilter
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

# Configure Bearer authorization: PersonalAccessToken
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    per_page = 24 # int, none_type |  (optional) if omitted the server will use the default value of 24
    cursor = "cursor_example" # str | The cursor from which to return paginated results starting after (optional)
    filter = UserFilter(
        steam_id=1,
    ) # UserFilter | Filter the results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all users
        api_response = api_instance.list_users(per_page=per_page, cursor=cursor, filter=filter)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling UsersApi->list_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int, none_type**|  | [optional] if omitted the server will use the default value of 24
 **cursor** | **str**| The cursor from which to return paginated results starting after | [optional]
 **filter** | **UserFilter**| Filter the results | [optional]

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
**200** | Successful response containing a list of users |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

