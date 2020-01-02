# gmodstore_sdk.AddonReviewsApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addons_addon_id_reviews_get**](AddonReviewsApi.md#addons_addon_id_reviews_get) | **GET** /addons/{addon_id}/reviews | Fetch all the reviews of an addon
[**addons_addon_id_reviews_review_id_get**](AddonReviewsApi.md#addons_addon_id_reviews_review_id_get) | **GET** /addons/{addon_id}/reviews/{review_id} | Fetch a review of an addon

# **addons_addon_id_reviews_get**
> InlineResponse2005 addons_addon_id_reviews_get(addon_id, _with=_with)

Fetch all the reviews of an addon

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
api_instance = gmodstore_sdk.AddonReviewsApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonReview schema (optional)

try:
    # Fetch all the reviews of an addon
    api_response = api_instance.addons_addon_id_reviews_get(addon_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonReviewsApi->addons_addon_id_reviews_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonReview schema | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_addon_id_reviews_review_id_get**
> InlineResponse2006 addons_addon_id_reviews_review_id_get(addon_id, review_id, _with=_with)

Fetch a review of an addon

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
api_instance = gmodstore_sdk.AddonReviewsApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
review_id = 789 # int | Id of the review
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonReview schema (optional)

try:
    # Fetch a review of an addon
    api_response = api_instance.addons_addon_id_reviews_review_id_get(addon_id, review_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonReviewsApi->addons_addon_id_reviews_review_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **review_id** | **int**| Id of the review | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonReview schema | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

