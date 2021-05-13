"""
    GmodStore API

    Welcome to the GmodStore API! You can use our API to access GmodStore API endpoints, which can be used interact with GmodStore programmatically.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gmodstore-sdk.api_client import ApiClient, Endpoint as _Endpoint
from gmodstore-sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from gmodstore-sdk.model.api_key_response import ApiKeyResponse
from gmodstore-sdk.model.error_response import ErrorResponse


class CurrentAPIKeyApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_current_api_key(
            self,
            **kwargs
        ):
            """Get meta information about the current API key  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_current_api_key(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                _with ([str]): The relations you want to fetch with the `ApiKey`. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ApiKeyResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_current_api_key = _Endpoint(
            settings={
                'response_type': (ApiKeyResponse,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/me',
                'operation_id': 'get_current_api_key',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    '_with',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    '_with',
                ],
                'validation': [
                    '_with',
                ]
            },
            root_map={
                'validations': {
                    ('_with',): {

                    },
                },
                'allowed_values': {
                    ('_with',): {

                        "USER": "user"
                    },
                },
                'openapi_types': {
                    '_with':
                        ([str],),
                },
                'attribute_map': {
                    '_with': 'with',
                },
                'location_map': {
                    '_with': 'query',
                },
                'collection_format_map': {
                    '_with': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_current_api_key
        )
