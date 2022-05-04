# gmodstore-sdk.ProductPurchasesApi

All URIs are relative to *https://www.gmodstore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product_purchase**](ProductPurchasesApi.md#create_product_purchase) | **POST** /api/v3/products/{product}/purchases | Create a purchase for a product
[**get_product_purchase**](ProductPurchasesApi.md#get_product_purchase) | **GET** /api/v3/products/{product}/purchases/{purchase} | Show the specified purchase for a product
[**list_product_purchases**](ProductPurchasesApi.md#list_product_purchases) | **GET** /api/v3/products/{product}/purchases | List all purchases for a product
[**update_product_purchase**](ProductPurchasesApi.md#update_product_purchase) | **PUT** /api/v3/products/{product}/purchases/{purchase} | Update the specified purchase for a product


# **create_product_purchase**
> CreateProductPurchaseResponse create_product_purchase(product)

Create a purchase for a product

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import product_purchases_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.new_product_purchase_payload import NewProductPurchasePayload
from gmodstore-sdk.model.create_product_purchase_response import CreateProductPurchaseResponse
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
    api_instance = product_purchases_api.ProductPurchasesApi(api_client)
    product = "product_example" # str | 
    new_product_purchase_payload = NewProductPurchasePayload(
        user_id="user_id_example",
    ) # NewProductPurchasePayload |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a purchase for a product
        api_response = api_instance.create_product_purchase(product)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductPurchasesApi->create_product_purchase: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a purchase for a product
        api_response = api_instance.create_product_purchase(product, new_product_purchase_payload=new_product_purchase_payload)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductPurchasesApi->create_product_purchase: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**|  |
 **new_product_purchase_payload** | [**NewProductPurchasePayload**](NewProductPurchasePayload.md)|  | [optional]

### Return type

[**CreateProductPurchaseResponse**](CreateProductPurchaseResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response containing the newly created product purchase |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_purchase**
> GetProductPurchaseResponse get_product_purchase(product, purchase)

Show the specified purchase for a product

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import product_purchases_api
from gmodstore-sdk.model.product_purchase_filter import ProductPurchaseFilter
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.get_product_purchase_response import GetProductPurchaseResponse
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
    api_instance = product_purchases_api.ProductPurchasesApi(api_client)
    product = "product_example" # str | 
    purchase = "purchase_example" # str | 
    filter = ProductPurchaseFilter(
        revoked=True,
        user_id="user_id_example",
        product_id="product_id_example",
    ) # ProductPurchaseFilter | Filter the results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Show the specified purchase for a product
        api_response = api_instance.get_product_purchase(product, purchase)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductPurchasesApi->get_product_purchase: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Show the specified purchase for a product
        api_response = api_instance.get_product_purchase(product, purchase, filter=filter)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductPurchasesApi->get_product_purchase: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**|  |
 **purchase** | **str**|  |
 **filter** | **ProductPurchaseFilter**| Filter the results | [optional]

### Return type

[**GetProductPurchaseResponse**](GetProductPurchaseResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing a single product purchase |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_product_purchases**
> bool, date, datetime, dict, float, int, list, str, none_type list_product_purchases(product)

List all purchases for a product

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import product_purchases_api
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
    api_instance = product_purchases_api.ProductPurchasesApi(api_client)
    product = "product_example" # str | 
    per_page = 24 # int, none_type |  (optional) if omitted the server will use the default value of 24
    cursor = "cursor_example" # str | The cursor from which to return paginated results starting after (optional)
    filter = ProductPurchaseFilter(
        revoked=True,
        user_id="user_id_example",
        product_id="product_id_example",
    ) # ProductPurchaseFilter | Filter the results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all purchases for a product
        api_response = api_instance.list_product_purchases(product)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductPurchasesApi->list_product_purchases: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all purchases for a product
        api_response = api_instance.list_product_purchases(product, per_page=per_page, cursor=cursor, filter=filter)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductPurchasesApi->list_product_purchases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**|  |
 **per_page** | **int, none_type**|  | [optional] if omitted the server will use the default value of 24
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product_purchase**
> UpdateProductPurchaseResponse update_product_purchase(product, purchase)

Update the specified purchase for a product

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import product_purchases_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.update_product_purchase_response import UpdateProductPurchaseResponse
from gmodstore-sdk.model.update_product_purchase_payload import UpdateProductPurchasePayload
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
    api_instance = product_purchases_api.ProductPurchasesApi(api_client)
    product = "product_example" # str | 
    purchase = "purchase_example" # str | 
    update_product_purchase_payload = UpdateProductPurchasePayload(
        revoked=True,
    ) # UpdateProductPurchasePayload |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the specified purchase for a product
        api_response = api_instance.update_product_purchase(product, purchase)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductPurchasesApi->update_product_purchase: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the specified purchase for a product
        api_response = api_instance.update_product_purchase(product, purchase, update_product_purchase_payload=update_product_purchase_payload)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductPurchasesApi->update_product_purchase: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**|  |
 **purchase** | **str**|  |
 **update_product_purchase_payload** | [**UpdateProductPurchasePayload**](UpdateProductPurchasePayload.md)|  | [optional]

### Return type

[**UpdateProductPurchaseResponse**](UpdateProductPurchaseResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing the product purchase with changes applied |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

