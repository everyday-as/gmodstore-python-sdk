# gmodstore-sdk.UsersApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_self_user**](UsersApi.md#get_self_user) | **GET** /users/me | Fetches the current user (API Key Owner)
[**get_user**](UsersApi.md#get_user) | **GET** /users/{user_id} | Fetch a single user


# **get_self_user**
> UserResponse get_self_user()

Fetches the current user (API Key Owner)

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import users_api
from gmodstore-sdk.model.error_response import ErrorResponse
from gmodstore-sdk.model.user_response import UserResponse
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
    api_instance = users_api.UsersApi(api_client)
    _with = [
        "group",
    ] # [str] | The relations you want to fetch with the `User` (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetches the current user (API Key Owner)
        api_response = api_instance.get_self_user(_with=_with)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling UsersApi->get_self_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_with** | **[str]**| The relations you want to fetch with the &#x60;User&#x60; | [optional]

### Return type

[**UserResponse**](UserResponse.md)

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

# **get_user**
> UserResponse get_user(user_id)

Fetch a single user

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import users_api
from gmodstore-sdk.model.error_response import ErrorResponse
from gmodstore-sdk.model.user_response import UserResponse
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
    api_instance = users_api.UsersApi(api_client)
    user_id = 1 # int | Id of the user
    _with = [
        "group",
    ] # [str] | The relations you want to fetch with the `User` (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch a single user
        api_response = api_instance.get_user(user_id)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch a single user
        api_response = api_instance.get_user(user_id, _with=_with)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of the user |
 **_with** | **[str]**| The relations you want to fetch with the &#x60;User&#x60; | [optional]

### Return type

[**UserResponse**](UserResponse.md)

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

