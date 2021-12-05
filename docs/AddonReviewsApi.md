# gmodstore-sdk.AddonReviewsApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_addon_review**](AddonReviewsApi.md#get_addon_review) | **GET** /addons/{addon_id}/reviews/{review_id} | Fetch a review of an addon
[**list_addon_reviews**](AddonReviewsApi.md#list_addon_reviews) | **GET** /addons/{addon_id}/reviews | Fetch all the reviews of an addon


# **get_addon_review**
> AddonReviewResponse get_addon_review(addon_id, review_id)

Fetch a review of an addon

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import addon_reviews_api
from gmodstore-sdk.model.addon_review_response import AddonReviewResponse
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
    api_instance = addon_reviews_api.AddonReviewsApi(api_client)
    addon_id = 1 # int | Id of the addon
    review_id = 1 # int | Id of the review
    _with = [
        "addon",
    ] # [str] | The relations you want to fetch with the `AddonReview` (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch a review of an addon
        api_response = api_instance.get_addon_review(addon_id, review_id)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonReviewsApi->get_addon_review: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch a review of an addon
        api_response = api_instance.get_addon_review(addon_id, review_id, _with=_with)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonReviewsApi->get_addon_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon |
 **review_id** | **int**| Id of the review |
 **_with** | **[str]**| The relations you want to fetch with the &#x60;AddonReview&#x60; | [optional]

### Return type

[**AddonReviewResponse**](AddonReviewResponse.md)

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

# **list_addon_reviews**
> AddonReviewListResponse list_addon_reviews(addon_id)

Fetch all the reviews of an addon

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import addon_reviews_api
from gmodstore-sdk.model.error_response import ErrorResponse
from gmodstore-sdk.model.addon_review_list_response import AddonReviewListResponse
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
    api_instance = addon_reviews_api.AddonReviewsApi(api_client)
    addon_id = 1 # int | Id of the addon
    _with = [
        "addon",
    ] # [str] | The relations you want to fetch with the `AddonReview` (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch all the reviews of an addon
        api_response = api_instance.list_addon_reviews(addon_id)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonReviewsApi->list_addon_reviews: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all the reviews of an addon
        api_response = api_instance.list_addon_reviews(addon_id, _with=_with)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling AddonReviewsApi->list_addon_reviews: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon |
 **_with** | **[str]**| The relations you want to fetch with the &#x60;AddonReview&#x60; | [optional]

### Return type

[**AddonReviewListResponse**](AddonReviewListResponse.md)

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

