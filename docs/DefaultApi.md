# gmodstore-sdk.DefaultApi

All URIs are relative to *https://www.gmodstore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_product_version**](DefaultApi.md#delete_product_version) | **DELETE** /api/v3/products/{product}/versions/{version} | Delete the specified version for a product


# **delete_product_version**
> DeleteProductVersionResponse delete_product_version(product, version)

Delete the specified version for a product

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import default_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.delete_product_version_response import DeleteProductVersionResponse
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
    api_instance = default_api.DefaultApi(api_client)
    product = "product_example" # str | 
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the specified version for a product
        api_response = api_instance.delete_product_version(product, version)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling DefaultApi->delete_product_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**|  |
 **version** | **str**|  |

### Return type

[**DeleteProductVersionResponse**](DeleteProductVersionResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing the product version that was just deleted |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

