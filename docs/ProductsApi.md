# gmodstore-sdk.ProductsApi

All URIs are relative to *https://www.gmodstore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_product**](ProductsApi.md#get_product) | **GET** /api/v3/products/{product} | Get the specified product
[**get_products**](ProductsApi.md#get_products) | **GET** /api/v3/products/batch | Get a batch of products by id
[**list_products**](ProductsApi.md#list_products) | **GET** /api/v3/teams/{team}/products | List all products for a team
[**update_product**](ProductsApi.md#update_product) | **PUT** /api/v3/products/{product} | Update the specified product


# **get_product**
> GetProductResponse get_product(product)

Get the specified product

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import products_api
from gmodstore-sdk.model.get_product_response import GetProductResponse
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
    api_instance = products_api.ProductsApi(api_client)
    product = "product_example" # str | 
    filter = ProductFilter(
        slug="slug_example",
    ) # ProductFilter | Filter the results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the specified product
        api_response = api_instance.get_product(product)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductsApi->get_product: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the specified product
        api_response = api_instance.get_product(product, filter=filter)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductsApi->get_product: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**|  |
 **filter** | **ProductFilter**| Filter the results | [optional]

### Return type

[**GetProductResponse**](GetProductResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing a single product |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products**
> GetProductsResponse get_products(ids)

Get a batch of products by id

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import products_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.product_filter import ProductFilter
from gmodstore-sdk.model.get_products_response import GetProductsResponse
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
    api_instance = products_api.ProductsApi(api_client)
    ids = [
        "ids[]_example",
    ] # [str] | 
    filter = ProductFilter(
        slug="slug_example",
    ) # ProductFilter | Filter the results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a batch of products by id
        api_response = api_instance.get_products(ids)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductsApi->get_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a batch of products by id
        api_response = api_instance.get_products(ids, filter=filter)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductsApi->get_products: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**|  |
 **filter** | **ProductFilter**| Filter the results | [optional]

### Return type

[**GetProductsResponse**](GetProductsResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing the requested batch of products |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_products**
> bool, date, datetime, dict, float, int, list, str, none_type list_products(team)

List all products for a team

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import products_api
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
    api_instance = products_api.ProductsApi(api_client)
    team = "team_example" # str | 
    per_page = 24 # int, none_type |  (optional) if omitted the server will use the default value of 24
    cursor = "cursor_example" # str | The cursor from which to return paginated results starting after (optional)
    filter = ProductFilter(
        slug="slug_example",
    ) # ProductFilter | Filter the results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all products for a team
        api_response = api_instance.list_products(team)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductsApi->list_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all products for a team
        api_response = api_instance.list_products(team, per_page=per_page, cursor=cursor, filter=filter)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductsApi->list_products: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team** | **str**|  |
 **per_page** | **int, none_type**|  | [optional] if omitted the server will use the default value of 24
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product**
> update_product(product)

Update the specified product

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import products_api
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
    api_instance = products_api.ProductsApi(api_client)
    product = "product_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Update the specified product
        api_instance.update_product(product)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductsApi->update_product: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**|  |

### Return type

void (empty response body)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

