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
from gmodstore-sdk.model.addon_purchase import AddonPurchase
from gmodstore-sdk.model.addon_purchase_list_response import AddonPurchaseListResponse
from gmodstore-sdk.model.addon_purchase_response import AddonPurchaseResponse
from gmodstore-sdk.model.error_response import ErrorResponse
from gmodstore-sdk.model.new_addon_purchase import NewAddonPurchase


class AddonPurchasesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_addon_purchase(
            self,
            addon_id,
            new_addon_purchase,
            **kwargs
        ):
            """Create a purchase for an addon  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_addon_purchase(addon_id, new_addon_purchase, async_req=True)
            >>> result = thread.get()

            Args:
                addon_id (int): Id of the addon
                new_addon_purchase (NewAddonPurchase):

            Keyword Args:
                _with ([str]): The relations you want to fetch with the `AddonPurchase`. [optional]
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
                AddonPurchaseResponse
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
            kwargs['addon_id'] = \
                addon_id
            kwargs['new_addon_purchase'] = \
                new_addon_purchase
            return self.call_with_http_info(**kwargs)

        self.create_addon_purchase = _Endpoint(
            settings={
                'response_type': (AddonPurchaseResponse,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/addons/{addon_id}/purchases',
                'operation_id': 'create_addon_purchase',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'addon_id',
                    'new_addon_purchase',
                    '_with',
                ],
                'required': [
                    'addon_id',
                    'new_addon_purchase',
                ],
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

                        "ADDON": "addon",
                        "ORDER_ITEM": "order_item",
                        "USER": "user"
                    },
                },
                'openapi_types': {
                    'addon_id':
                        (int,),
                    'new_addon_purchase':
                        (NewAddonPurchase,),
                    '_with':
                        ([str],),
                },
                'attribute_map': {
                    'addon_id': 'addon_id',
                    '_with': 'with',
                },
                'location_map': {
                    'addon_id': 'path',
                    'new_addon_purchase': 'body',
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
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_addon_purchase
        )

        def __get_addon_purchase(
            self,
            addon_id,
            user_id,
            **kwargs
        ):
            """Get a purchase of an addon by user  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_addon_purchase(addon_id, user_id, async_req=True)
            >>> result = thread.get()

            Args:
                addon_id (int): Id of the addon
                user_id (int): Id of the user

            Keyword Args:
                _with ([str]): The relations you want to fetch with the `AddonPurchase`. [optional]
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
                AddonPurchaseResponse
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
            kwargs['addon_id'] = \
                addon_id
            kwargs['user_id'] = \
                user_id
            return self.call_with_http_info(**kwargs)

        self.get_addon_purchase = _Endpoint(
            settings={
                'response_type': (AddonPurchaseResponse,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/addons/{addon_id}/purchases/{user_id}',
                'operation_id': 'get_addon_purchase',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'addon_id',
                    'user_id',
                    '_with',
                ],
                'required': [
                    'addon_id',
                    'user_id',
                ],
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

                        "ADDON": "addon",
                        "ORDER_ITEM": "order_item",
                        "USER": "user"
                    },
                },
                'openapi_types': {
                    'addon_id':
                        (int,),
                    'user_id':
                        (int,),
                    '_with':
                        ([str],),
                },
                'attribute_map': {
                    'addon_id': 'addon_id',
                    'user_id': 'user_id',
                    '_with': 'with',
                },
                'location_map': {
                    'addon_id': 'path',
                    'user_id': 'path',
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
            callable=__get_addon_purchase
        )

        def __list_addon_purchases(
            self,
            addon_id,
            **kwargs
        ):
            """Fetch all purchases of an addon  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_addon_purchases(addon_id, async_req=True)
            >>> result = thread.get()

            Args:
                addon_id (int): Id of the addon

            Keyword Args:
                _with ([str]): The relations you want to fetch with the `AddonPurchase`. [optional]
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
                AddonPurchaseListResponse
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
            kwargs['addon_id'] = \
                addon_id
            return self.call_with_http_info(**kwargs)

        self.list_addon_purchases = _Endpoint(
            settings={
                'response_type': (AddonPurchaseListResponse,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/addons/{addon_id}/purchases',
                'operation_id': 'list_addon_purchases',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'addon_id',
                    '_with',
                ],
                'required': [
                    'addon_id',
                ],
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

                        "ADDON": "addon",
                        "ORDER_ITEM": "order_item",
                        "USER": "user"
                    },
                },
                'openapi_types': {
                    'addon_id':
                        (int,),
                    '_with':
                        ([str],),
                },
                'attribute_map': {
                    'addon_id': 'addon_id',
                    '_with': 'with',
                },
                'location_map': {
                    'addon_id': 'path',
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
            callable=__list_addon_purchases
        )

        def __update_addon_purchase(
            self,
            addon_id,
            user_id,
            addon_purchase,
            **kwargs
        ):
            """Update a purchase for an addon  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_addon_purchase(addon_id, user_id, addon_purchase, async_req=True)
            >>> result = thread.get()

            Args:
                addon_id (int): Id of the addon
                user_id (int): Id of the user
                addon_purchase (AddonPurchase):

            Keyword Args:
                _with ([str]): The relations you want to fetch with the `AddonPurchase`. [optional]
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
                AddonPurchaseResponse
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
            kwargs['addon_id'] = \
                addon_id
            kwargs['user_id'] = \
                user_id
            kwargs['addon_purchase'] = \
                addon_purchase
            return self.call_with_http_info(**kwargs)

        self.update_addon_purchase = _Endpoint(
            settings={
                'response_type': (AddonPurchaseResponse,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/addons/{addon_id}/purchases/{user_id}',
                'operation_id': 'update_addon_purchase',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'addon_id',
                    'user_id',
                    'addon_purchase',
                    '_with',
                ],
                'required': [
                    'addon_id',
                    'user_id',
                    'addon_purchase',
                ],
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

                        "ADDON": "addon",
                        "ORDER_ITEM": "order_item",
                        "USER": "user"
                    },
                },
                'openapi_types': {
                    'addon_id':
                        (int,),
                    'user_id':
                        (int,),
                    'addon_purchase':
                        (AddonPurchase,),
                    '_with':
                        ([str],),
                },
                'attribute_map': {
                    'addon_id': 'addon_id',
                    'user_id': 'user_id',
                    '_with': 'with',
                },
                'location_map': {
                    'addon_id': 'path',
                    'user_id': 'path',
                    'addon_purchase': 'body',
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
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_addon_purchase
        )
