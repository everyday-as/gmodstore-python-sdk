# gmodstore-sdk.UserProductsApi

All URIs are relative to *https://www.gmodstore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_user_products**](UserProductsApi.md#list_user_products) | **GET** /api/v3/users/{user}/products | List all the specified user&#39;s products


# **list_user_products**
> bool, date, datetime, dict, float, int, list, str, none_type list_user_products(user)

List all the specified user's products

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import user_products_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.product_filter import ProductFilter
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
    api_instance = user_products_api.UserProductsApi(api_client)
    user = "user_example" # str | 
    cursor = "cursor_example" # str | The cursor from which to return paginated results starting after (optional)
    filter = ProductFilter(
        slug="slug_example",
    ) # ProductFilter | Filter the results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all the specified user's products
        api_response = api_instance.list_user_products(user)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling UserProductsApi->list_user_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all the specified user's products
        api_response = api_instance.list_user_products(user, cursor=cursor, filter=filter)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling UserProductsApi->list_user_products: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**|  |
 **cursor** | **str**| The cursor from which to return paginated results starting after | [optional]
 **filter** | **ProductFilter**| Filter the results | [optional]

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
**200** | Successful response containing a list of products |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

