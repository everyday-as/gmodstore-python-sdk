# gmodstore-sdk.ProductVersionsApi

All URIs are relative to *https://www.gmodstore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product_version**](ProductVersionsApi.md#create_product_version) | **POST** /api/v3/products/{product}/versions | Create a version for a product
[**get_product_download_token**](ProductVersionsApi.md#get_product_download_token) | **POST** /api/v3/products/{product}/versions/{version}/download | Get a one time use url for downloading a product
[**get_product_version**](ProductVersionsApi.md#get_product_version) | **GET** /api/v3/products/{product}/versions/{version} | Show the specified version for a product
[**list_product_versions**](ProductVersionsApi.md#list_product_versions) | **GET** /api/v3/products/{product}/versions | List all versions for a product
[**update_product_version**](ProductVersionsApi.md#update_product_version) | **PUT** /api/v3/products/{product}/versions/{version} | Update the specified version for a product


# **create_product_version**
> CreateProductVersionResponse create_product_version(product, name, changelog, file, release_type)

Create a version for a product

### Example

* Bearer (Personal Access Token) Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import product_versions_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.create_product_version_response import CreateProductVersionResponse
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

# Configure Bearer authorization (Personal Access Token): PersonalAccessToken
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product_versions_api.ProductVersionsApi(api_client)
    product = "product_example" # str | 
    name = "name_example" # str | 
    changelog = "changelog_example" # str | 
    file = open('/path/to/file', 'rb') # file_type | 
    release_type = "stable" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Create a version for a product
        api_response = api_instance.create_product_version(product, name, changelog, file, release_type)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductVersionsApi->create_product_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**|  |
 **name** | **str**|  |
 **changelog** | **str**|  |
 **file** | **file_type**|  |
 **release_type** | **str**|  |

### Return type

[**CreateProductVersionResponse**](CreateProductVersionResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response containing the newly created product version |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_download_token**
> DownloadProductVersionResponse get_product_download_token(product, version)

Get a one time use url for downloading a product

### Example

* Bearer (Personal Access Token) Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import product_versions_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.download_product_version_response import DownloadProductVersionResponse
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

# Configure Bearer authorization (Personal Access Token): PersonalAccessToken
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product_versions_api.ProductVersionsApi(api_client)
    product = "product_example" # str | 
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a one time use url for downloading a product
        api_response = api_instance.get_product_download_token(product, version)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductVersionsApi->get_product_download_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**|  |
 **version** | **str**|  |

### Return type

[**DownloadProductVersionResponse**](DownloadProductVersionResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing a download url |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_version**
> GetProductVersionResponse get_product_version(product, version)

Show the specified version for a product

### Example

* Bearer (Personal Access Token) Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import product_versions_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.get_product_version_response import GetProductVersionResponse
from gmodstore-sdk.model.product_version_filter import ProductVersionFilter
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

# Configure Bearer authorization (Personal Access Token): PersonalAccessToken
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product_versions_api.ProductVersionsApi(api_client)
    product = "product_example" # str | 
    version = "version_example" # str | 
    filter = ProductVersionFilter(
        release_type="stable",
    ) # ProductVersionFilter | Filter the results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Show the specified version for a product
        api_response = api_instance.get_product_version(product, version)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductVersionsApi->get_product_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Show the specified version for a product
        api_response = api_instance.get_product_version(product, version, filter=filter)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductVersionsApi->get_product_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**|  |
 **version** | **str**|  |
 **filter** | **ProductVersionFilter**| Filter the results | [optional]

### Return type

[**GetProductVersionResponse**](GetProductVersionResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing a single product version |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_product_versions**
> bool, date, datetime, dict, float, int, list, str, none_type list_product_versions(product)

List all versions for a product

### Example

* Bearer (Personal Access Token) Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import product_versions_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.product_version_filter import ProductVersionFilter
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

# Configure Bearer authorization (Personal Access Token): PersonalAccessToken
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product_versions_api.ProductVersionsApi(api_client)
    product = "product_example" # str | 
    per_page = 24 # int, none_type |  (optional) if omitted the server will use the default value of 24
    cursor = "cursor_example" # str | The cursor from which to return paginated results starting after (optional)
    filter = ProductVersionFilter(
        release_type="stable",
    ) # ProductVersionFilter | Filter the results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all versions for a product
        api_response = api_instance.list_product_versions(product)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductVersionsApi->list_product_versions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all versions for a product
        api_response = api_instance.list_product_versions(product, per_page=per_page, cursor=cursor, filter=filter)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductVersionsApi->list_product_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**|  |
 **per_page** | **int, none_type**|  | [optional] if omitted the server will use the default value of 24
 **cursor** | **str**| The cursor from which to return paginated results starting after | [optional]
 **filter** | **ProductVersionFilter**| Filter the results | [optional]

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
**200** | Successful response containing a list of product versions |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product_version**
> UpdateProductVersionResponse update_product_version(product, version)

Update the specified version for a product

### Example

* Bearer (Personal Access Token) Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import product_versions_api
from gmodstore-sdk.model.update_product_version_response import UpdateProductVersionResponse
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.update_product_version_payload import UpdateProductVersionPayload
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

# Configure Bearer authorization (Personal Access Token): PersonalAccessToken
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product_versions_api.ProductVersionsApi(api_client)
    product = "product_example" # str | 
    version = "version_example" # str | 
    update_product_version_payload = UpdateProductVersionPayload(
        name="name_example",
        changelog="changelog_example",
        release_type="stable",
    ) # UpdateProductVersionPayload |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the specified version for a product
        api_response = api_instance.update_product_version(product, version)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductVersionsApi->update_product_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the specified version for a product
        api_response = api_instance.update_product_version(product, version, update_product_version_payload=update_product_version_payload)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling ProductVersionsApi->update_product_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**|  |
 **version** | **str**|  |
 **update_product_version_payload** | [**UpdateProductVersionPayload**](UpdateProductVersionPayload.md)|  | [optional]

### Return type

[**UpdateProductVersionResponse**](UpdateProductVersionResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing the product version with changes applied |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

