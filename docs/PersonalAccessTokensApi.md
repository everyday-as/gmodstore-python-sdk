# gmodstore-sdk.PersonalAccessTokensApi

All URIs are relative to *https://www.gmodstore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_personal_access_token**](PersonalAccessTokensApi.md#create_personal_access_token) | **POST** /api/v3/me/personal-access-tokens | Create a new personal access token for the current user
[**delete_personal_access_token**](PersonalAccessTokensApi.md#delete_personal_access_token) | **DELETE** /api/v3/me/personal-access-tokens/{personal_access_token} | Delete the specified personal access token
[**get_personal_access_token**](PersonalAccessTokensApi.md#get_personal_access_token) | **GET** /api/v3/me/personal-access-tokens/{personal_access_token} | Get a personal access token belonging to the current user
[**list_personal_access_tokens**](PersonalAccessTokensApi.md#list_personal_access_tokens) | **GET** /api/v3/me/personal-access-tokens | List all the current user&#39;s personal access tokens
[**update_personal_access_token**](PersonalAccessTokensApi.md#update_personal_access_token) | **PUT** /api/v3/me/personal-access-tokens/{personal_access_token} | Update a personal access token


# **create_personal_access_token**
> InlineResponse201 create_personal_access_token()

Create a new personal access token for the current user

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import personal_access_tokens_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.new_personal_access_token_payload import NewPersonalAccessTokenPayload
from gmodstore-sdk.model.inline_response201 import InlineResponse201
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
    api_instance = personal_access_tokens_api.PersonalAccessTokensApi(api_client)
    new_personal_access_token_payload = NewPersonalAccessTokenPayload(
        name="name_example",
        expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        abilities=[
            "permission-groups:read",
        ],
    ) # NewPersonalAccessTokenPayload |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new personal access token for the current user
        api_response = api_instance.create_personal_access_token(new_personal_access_token_payload=new_personal_access_token_payload)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling PersonalAccessTokensApi->create_personal_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_personal_access_token_payload** | [**NewPersonalAccessTokenPayload**](NewPersonalAccessTokenPayload.md)|  | [optional]

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response containing the newly created personal access token, along with the plain text token |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_personal_access_token**
> DeleteTeamResponse delete_personal_access_token(personal_access_token)

Delete the specified personal access token

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import personal_access_tokens_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.delete_team_response import DeleteTeamResponse
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
    api_instance = personal_access_tokens_api.PersonalAccessTokensApi(api_client)
    personal_access_token = "personal_access_token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the specified personal access token
        api_response = api_instance.delete_personal_access_token(personal_access_token)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling PersonalAccessTokensApi->delete_personal_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personal_access_token** | **str**|  |

### Return type

[**DeleteTeamResponse**](DeleteTeamResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing the team that was just deleted |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_personal_access_token**
> GetPersonalAccessTokenResponse get_personal_access_token(personal_access_token)

Get a personal access token belonging to the current user

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import personal_access_tokens_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.get_personal_access_token_response import GetPersonalAccessTokenResponse
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
    api_instance = personal_access_tokens_api.PersonalAccessTokensApi(api_client)
    personal_access_token = "personal_access_token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a personal access token belonging to the current user
        api_response = api_instance.get_personal_access_token(personal_access_token)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling PersonalAccessTokensApi->get_personal_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personal_access_token** | **str**|  |

### Return type

[**GetPersonalAccessTokenResponse**](GetPersonalAccessTokenResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing a single personal access token |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_personal_access_tokens**
> bool, date, datetime, dict, float, int, list, str, none_type list_personal_access_tokens()

List all the current user's personal access tokens

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import personal_access_tokens_api
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
    api_instance = personal_access_tokens_api.PersonalAccessTokensApi(api_client)
    per_page = 24 # int, none_type |  (optional) if omitted the server will use the default value of 24
    cursor = "cursor_example" # str | The cursor from which to return paginated results starting after (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all the current user's personal access tokens
        api_response = api_instance.list_personal_access_tokens(per_page=per_page, cursor=cursor)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling PersonalAccessTokensApi->list_personal_access_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int, none_type**|  | [optional] if omitted the server will use the default value of 24
 **cursor** | **str**| The cursor from which to return paginated results starting after | [optional]

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
**200** | Successful response containing a list of personal access tokens |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_personal_access_token**
> UpdatePersonalAccessTokenResponse update_personal_access_token(personal_access_token)

Update a personal access token

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import gmodstore-sdk
from gmodstore-sdk.api import personal_access_tokens_api
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.update_personal_access_token_response import UpdatePersonalAccessTokenResponse
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
    api_instance = personal_access_tokens_api.PersonalAccessTokensApi(api_client)
    personal_access_token = "personal_access_token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Update a personal access token
        api_response = api_instance.update_personal_access_token(personal_access_token)
        pprint(api_response)
    except gmodstore-sdk.ApiException as e:
        print("Exception when calling PersonalAccessTokensApi->update_personal_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personal_access_token** | **str**|  |

### Return type

[**UpdatePersonalAccessTokenResponse**](UpdatePersonalAccessTokenResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response containing the personal access token with changes applied |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**404** | The requested resource does not exist |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Improperly formatted request passed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | The passed bearer token is missing or invalid |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The passed bearer token does not have the right scopes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

