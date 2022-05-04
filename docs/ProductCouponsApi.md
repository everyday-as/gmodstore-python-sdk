# gmodstore-sdk.ProductCouponsApi

All URIs are relative to *https://www.gmodstore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product_coupon**](ProductCouponsApi.md#create_product_coupon) | **POST** /api/v3/products/{product}/coupons | Create a coupon for a product
[**delete_product_coupon**](ProductCouponsApi.md#delete_product_coupon) | **DELETE** /api/v3/products/{product}/coupons/{coupon} | Delete the specified coupon for a product
[**get_product_coupon**](ProductCouponsApi.md#get_product_coupon) | **GET** /api/v3/products/{product}/coupons/{coupon} | Show the specified coupon for a product
[**list_product_coupons**](ProductCouponsApi.md#list_product_coupons) | **GET** /api/v3/products/{product}/coupons | List all coupons for a product
[**update_product_coupon**](ProductCouponsApi.md#update_product_coupon) | **PUT** /api/v3/products/{product}/coupons/{coupon} | Update the specified coupon for a product


# **create_product_coupon**
> CreateProductCouponResponse create_product_coupon(product)

Create a coupon for a product

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import product_coupons_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.create_product_coupon_response import CreateProductCouponResponse
from gmodstore-sdk.model.new_product_coupon_payload import NewProductCouponPayload
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
    api_instance = product_coupons_api.ProductCouponsApi(api_client)
    product = "product_example" # str | 
    new_product_coupon_payload = NewProductCouponPayload(
        percent=1,
        code="S",
        max_uses=1,
        expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        bound_user_id="bound_user_id_example",
    ) # NewProductCouponPayload |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a coupon for a product
        api_response = api_instance.create_product_coupon(product)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductCouponsApi->create_product_coupon: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a coupon for a product
        api_response = api_instance.create_product_coupon(product, new_product_coupon_payload=new_product_coupon_payload)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductCouponsApi->create_product_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**|  |
 **new_product_coupon_payload** | [**NewProductCouponPayload**](NewProductCouponPayload.md)|  | [optional]

### Return type

[**CreateProductCouponResponse**](CreateProductCouponResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response containing the newly created product coupon |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product_coupon**
> DeleteProductCouponResponse delete_product_coupon(product, coupon)

Delete the specified coupon for a product

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import product_coupons_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.delete_product_coupon_response import DeleteProductCouponResponse
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
    api_instance = product_coupons_api.ProductCouponsApi(api_client)
    product = "product_example" # str | 
    coupon = "coupon_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the specified coupon for a product
        api_response = api_instance.delete_product_coupon(product, coupon)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductCouponsApi->delete_product_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**|  |
 **coupon** | **str**|  |

### Return type

[**DeleteProductCouponResponse**](DeleteProductCouponResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing the product coupon that was just deleted |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_coupon**
> GetProductCouponResponse get_product_coupon(product, coupon)

Show the specified coupon for a product

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import product_coupons_api
from gmodstore-sdk.model.get_product_coupon_response import GetProductCouponResponse
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
    api_instance = product_coupons_api.ProductCouponsApi(api_client)
    product = "product_example" # str | 
    coupon = "coupon_example" # str | 
    filter = ProductPurchaseFilter(
        revoked=True,
        user_id="user_id_example",
        product_id="product_id_example",
    ) # ProductPurchaseFilter | Filter the results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Show the specified coupon for a product
        api_response = api_instance.get_product_coupon(product, coupon)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductCouponsApi->get_product_coupon: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Show the specified coupon for a product
        api_response = api_instance.get_product_coupon(product, coupon, filter=filter)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductCouponsApi->get_product_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**|  |
 **coupon** | **str**|  |
 **filter** | **ProductPurchaseFilter**| Filter the results | [optional]

### Return type

[**GetProductCouponResponse**](GetProductCouponResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing a single product coupon |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_product_coupons**
> bool, date, datetime, dict, float, int, list, str, none_type list_product_coupons(product)

List all coupons for a product

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import product_coupons_api
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
    api_instance = product_coupons_api.ProductCouponsApi(api_client)
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
        # List all coupons for a product
        api_response = api_instance.list_product_coupons(product)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductCouponsApi->list_product_coupons: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all coupons for a product
        api_response = api_instance.list_product_coupons(product, per_page=per_page, cursor=cursor, filter=filter)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductCouponsApi->list_product_coupons: %s\n" % e)
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
**200** | Successful response containing a list of product coupons |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product_coupon**
> UpdateProductCouponResponse update_product_coupon(product, coupon)

Update the specified coupon for a product

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import product_coupons_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.update_product_coupon_response import UpdateProductCouponResponse
from gmodstore-sdk.model.update_product_coupon_payload import UpdateProductCouponPayload
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
    api_instance = product_coupons_api.ProductCouponsApi(api_client)
    product = "product_example" # str | 
    coupon = "coupon_example" # str | 
    update_product_coupon_payload = UpdateProductCouponPayload(
        percent=1,
        code="S",
        max_uses=1,
        expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        bound_user_id="bound_user_id_example",
    ) # UpdateProductCouponPayload |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the specified coupon for a product
        api_response = api_instance.update_product_coupon(product, coupon)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductCouponsApi->update_product_coupon: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the specified coupon for a product
        api_response = api_instance.update_product_coupon(product, coupon, update_product_coupon_payload=update_product_coupon_payload)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductCouponsApi->update_product_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**|  |
 **coupon** | **str**|  |
 **update_product_coupon_payload** | [**UpdateProductCouponPayload**](UpdateProductCouponPayload.md)|  | [optional]

### Return type

[**UpdateProductCouponResponse**](UpdateProductCouponResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing the product coupon with changes applied |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

