# gmodstore_sdk.UserBadgesApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_user_id_badges_badge_id_delete**](UserBadgesApi.md#users_user_id_badges_badge_id_delete) | **DELETE** /users/{user_id}/badges/{badge_id} | Destroy a users&#x27;s badge
[**users_user_id_badges_get**](UserBadgesApi.md#users_user_id_badges_get) | **GET** /users/{user_id}/badges | Fetch all the badges a user has
[**users_user_id_badges_post**](UserBadgesApi.md#users_user_id_badges_post) | **POST** /users/{user_id}/badges | Give a user a badge

# **users_user_id_badges_badge_id_delete**
> users_user_id_badges_badge_id_delete(user_id, badge_id)

Destroy a users's badge

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
api_instance = gmodstore_sdk.UserBadgesApi(gmodstore_sdk.ApiClient(configuration))
user_id = 'user_id_example' # str | Id of the user
badge_id = 789 # int | Id of the badge

try:
    # Destroy a users's badge
    api_instance.users_user_id_badges_badge_id_delete(user_id, badge_id)
except ApiException as e:
    print("Exception when calling UserBadgesApi->users_user_id_badges_badge_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Id of the user | 
 **badge_id** | **int**| Id of the badge | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_badges_get**
> InlineResponse20013 users_user_id_badges_get(user_id)

Fetch all the badges a user has

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
api_instance = gmodstore_sdk.UserBadgesApi(gmodstore_sdk.ApiClient(configuration))
user_id = 'user_id_example' # str | Id of the user

try:
    # Fetch all the badges a user has
    api_response = api_instance.users_user_id_badges_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserBadgesApi->users_user_id_badges_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Id of the user | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_badges_post**
> InlineResponse2013 users_user_id_badges_post(body, user_id)

Give a user a badge

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
api_instance = gmodstore_sdk.UserBadgesApi(gmodstore_sdk.ApiClient(configuration))
body = NULL # object | 
user_id = 'user_id_example' # str | Id of the user

try:
    # Give a user a badge
    api_response = api_instance.users_user_id_badges_post(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserBadgesApi->users_user_id_badges_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **user_id** | **str**| Id of the user | 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

