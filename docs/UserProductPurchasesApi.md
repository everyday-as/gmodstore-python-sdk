# gmodstore-sdk.UserProductPurchasesApi

All URIs are relative to *https://www.gmodstore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_user_purchases**](UserProductPurchasesApi.md#list_user_purchases) | **GET** /api/v3/users/{user}/purchases | List all the specified user&#39;s purchases


# **list_user_purchases**
> bool, date, datetime, dict, float, int, list, str, none_type list_user_purchases(user)

List all the specified user's purchases

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import user_product_purchases_api
from gmodstore-sdk.model.product_purchase_filter import ProductPurchaseFilter
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
    api_instance = user_product_purchases_api.UserProductPurchasesApi(api_client)
    user = "user_example" # str | 
    cursor = "cursor_example" # str | The cursor from which to return paginated results starting after (optional)
    filter = ProductPurchaseFilter(
        revoked=True,
        user_id="user_id_example",
        product_id="product_id_example",
    ) # ProductPurchaseFilter | Filter the results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all the specified user's purchases
        api_response = api_instance.list_user_purchases(user)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling UserProductPurchasesApi->list_user_purchases: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all the specified user's purchases
        api_response = api_instance.list_user_purchases(user, cursor=cursor, filter=filter)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling UserProductPurchasesApi->list_user_purchases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**|  |
 **cursor** | **str**| The cursor from which to return paginated results starting after | [optional]
 **filter** | **ProductPurchaseFilter**| Filter the results | [optional]

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
**200** | Successful response containing a list of product purchases |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

