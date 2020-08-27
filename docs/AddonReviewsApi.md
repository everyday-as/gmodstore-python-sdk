# gmodstore_sdk.AddonReviewsApi

All URIs are relative to *https://api.gmodstore.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_addon_review**](AddonReviewsApi.md#get_addon_review) | **GET** /addons/{addon_id}/reviews/{review_id} | Fetch a review of an addon
[**list_addon_reviews**](AddonReviewsApi.md#list_addon_reviews) | **GET** /addons/{addon_id}/reviews | Fetch all the reviews of an addon

# **get_addon_review**
> AddonReviewResponse get_addon_review(addon_id, review_id, _with=_with)

Fetch a review of an addon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.AddonReviewsApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
review_id = 789 # int | Id of the review
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonReview schema (optional)

try:
    # Fetch a review of an addon
    api_response = api_instance.get_addon_review(addon_id, review_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonReviewsApi->get_addon_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **review_id** | **int**| Id of the review | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonReview schema | [optional] 

### Return type

[**AddonReviewResponse**](AddonReviewResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_addon_reviews**
> AddonReviewListResponse list_addon_reviews(addon_id, _with=_with)

Fetch all the reviews of an addon

### Example
```python
from __future__ import print_function
import time
import gmodstore_sdk
from gmodstore_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = gmodstore_sdk.AddonReviewsApi(gmodstore_sdk.ApiClient(configuration))
addon_id = 789 # int | Id of the addon
_with = ['_with_example'] # list[str] | The relations you want to fetch with the AddonReview schema (optional)

try:
    # Fetch all the reviews of an addon
    api_response = api_instance.list_addon_reviews(addon_id, _with=_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonReviewsApi->list_addon_reviews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **int**| Id of the addon | 
 **_with** | [**list[str]**](str.md)| The relations you want to fetch with the AddonReview schema | [optional] 

### Return type

[**AddonReviewListResponse**](AddonReviewListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

