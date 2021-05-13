# gmodstore-sdk.UserBadgesApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_badge**](UserBadgesApi.md#create_user_badge) | **POST** /users/{user_id}/badges | Give a user a badge
[**delete_user_badge**](UserBadgesApi.md#delete_user_badge) | **DELETE** /users/{user_id}/badges/{badge_id} | Destroy a users&#39;s badge
[**list_user_badges**](UserBadgesApi.md#list_user_badges) | **GET** /users/{user_id}/badges | Fetch all the badges a user has


# **create_user_badge**
> BadgeResponse create_user_badge(user_id, user_badge)

Give a user a badge

### Example

* Bearer (API Key) Authentication (bearerAuth):
```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import user_badges_api
from gmodstore-sdk.model.badge_response import BadgeResponse
from gmodstore-sdk.model.user_badge import UserBadge
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
    api_instance = user_badges_api.UserBadgesApi(api_client)
    user_id = 1 # int | Id of the user
    user_badge = UserBadge(
        badge="badge_example",
    ) # UserBadge | 

    # example passing only required values which don't have defaults set
    try:
        # Give a user a badge
        api_response = api_instance.create_user_badge(user_id, user_badge)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling UserBadgesApi->create_user_badge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of the user |
 **user_badge** | [**UserBadge**](UserBadge.md)|  |

### Return type

[**BadgeResponse**](BadgeResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully processed the request. |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |
**429** | Too many requests |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset - The UNIX timestamp at which your rate limit quota will reset. <br>  |
**0** | Something went wrong |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_badge**
> delete_user_badge(user_id, badge_id)

Destroy a users's badge

### Example

* Bearer (API Key) Authentication (bearerAuth):
```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import user_badges_api
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
    api_instance = user_badges_api.UserBadgesApi(api_client)
    user_id = 1 # int | Id of the user
    badge_id = "badge_id_example" # str | Id of the badge

    # example passing only required values which don't have defaults set
    try:
        # Destroy a users's badge
        api_instance.delete_user_badge(user_id, badge_id)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling UserBadgesApi->delete_user_badge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of the user |
 **badge_id** | **str**| Id of the badge |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully processed the request. |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |
**0** | Something went wrong |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_badges**
> BadgeListResponse list_user_badges(user_id)

Fetch all the badges a user has

### Example

* Bearer (API Key) Authentication (bearerAuth):
```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import user_badges_api
from gmodstore-sdk.model.badge_list_response import BadgeListResponse
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
    api_instance = user_badges_api.UserBadgesApi(api_client)
    user_id = 1 # int | Id of the user

    # example passing only required values which don't have defaults set
    try:
        # Fetch all the badges a user has
        api_response = api_instance.list_user_badges(user_id)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling UserBadgesApi->list_user_badges: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of the user |

### Return type

[**BadgeListResponse**](BadgeListResponse.md)

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

