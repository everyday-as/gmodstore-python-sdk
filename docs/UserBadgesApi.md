# gmodstore_sdk.UserBadgesApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_badge**](UserBadgesApi.md#create_user_badge) | **POST** /users/{user_id}/badges | Give a user a badge
[**delete_user_badge**](UserBadgesApi.md#delete_user_badge) | **DELETE** /users/{user_id}/badges/{badge_id} | Destroy a users&#x27;s badge
[**list_user_badges**](UserBadgesApi.md#list_user_badges) | **GET** /users/{user_id}/badges | Fetch all the badges a user has

# **create_user_badge**
> InlineResponse2013 create_user_badge(body, user_id)

Give a user a badge

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.UserBadgesApi(gmodstore_sdk.ApiClient(configuration))
body = gmodstore_sdk.BadgeCreateBody() # BadgeCreateBody | 
user_id = 'user_id_example' # str | Id of the user

try:
    # Give a user a badge
    api_response = api_instance.create_user_badge(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserBadgesApi->create_user_badge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BadgeCreateBody**](BadgeCreateBody.md)|  | 
 **user_id** | **str**| Id of the user | 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_badge**
> delete_user_badge(user_id, badge_id)

Destroy a users's badge

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.UserBadgesApi(gmodstore_sdk.ApiClient(configuration))
user_id = 'user_id_example' # str | Id of the user
badge_id = 789 # int | Id of the badge

try:
    # Destroy a users's badge
    api_instance.delete_user_badge(user_id, badge_id)
except ApiException as e:
    print("Exception when calling UserBadgesApi->delete_user_badge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Id of the user | 
 **badge_id** | **int**| Id of the badge | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_badges**
> InlineResponse20014 list_user_badges(user_id)

Fetch all the badges a user has

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.UserBadgesApi(gmodstore_sdk.ApiClient(configuration))
user_id = 'user_id_example' # str | Id of the user

try:
    # Fetch all the badges a user has
    api_response = api_instance.list_user_badges(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserBadgesApi->list_user_badges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Id of the user | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

