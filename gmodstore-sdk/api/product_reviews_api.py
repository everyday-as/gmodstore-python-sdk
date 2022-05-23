"""
    gmodstore

    Welcome to the GmodStore API! You can use our API to access GmodStore API endpoints, which can be used interact with GmodStore programmatically.  # Rate limits Every request you make to the GmodStore API will count against your rate limit, which at the time of writing this, is 60 requests / minute. An up-to-date value will always provided in the `X-RateLimit-Limit` header The number of requests you have remaining before you must wait is provided in the `X-RateLimit-Remaining` header.  # API SDKs For a list of available API SDKs check the README here: https://github.com/everyday-as/gmodstore-api-docs#client-libraries  # noqa: E501

    The version of the OpenAPI document: 3.0.0
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
from gmodstore-sdk.model.error import Error
from gmodstore-sdk.model.get_product_review_response import GetProductReviewResponse
from gmodstore-sdk.model.product_review_filter import ProductReviewFilter


class ProductReviewsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_product_review_endpoint = _Endpoint(
            settings={
                'response_type': (GetProductReviewResponse,),
                'auth': [
                    'PersonalAccessToken'
                ],
                'endpoint_path': '/api/v3/products/{product}/reviews/{review}',
                'operation_id': 'get_product_review',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'product',
                    'review',
                    'filter',
                ],
                'required': [
                    'product',
                    'review',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'product':
                        (str,),
                    'review':
                        (str,),
                    'filter':
                        (ProductReviewFilter,),
                },
                'attribute_map': {
                    'product': 'product',
                    'review': 'review',
                    'filter': 'filter',
                },
                'location_map': {
                    'product': 'path',
                    'review': 'path',
                    'filter': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_product_reviews_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'PersonalAccessToken'
                ],
                'endpoint_path': '/api/v3/products/{product}/reviews',
                'operation_id': 'list_product_reviews',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'product',
                    'per_page',
                    'cursor',
                    'filter',
                ],
                'required': [
                    'product',
                ],
                'nullable': [
                    'per_page',
                ],
                'enum': [
                ],
                'validation': [
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'product':
                        (str,),
                    'per_page':
                        (int, none_type,),
                    'cursor':
                        (str,),
                    'filter':
                        (ProductReviewFilter,),
                },
                'attribute_map': {
                    'product': 'product',
                    'per_page': 'perPage',
                    'cursor': 'cursor',
                    'filter': 'filter',
                },
                'location_map': {
                    'product': 'path',
                    'per_page': 'query',
                    'cursor': 'query',
                    'filter': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_product_review(
        self,
        product,
        review,
        **kwargs
    ):
        """Show the specified review for a product  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_product_review(product, review, async_req=True)
        >>> result = thread.get()

        Args:
            product (str):
            review (str):

        Keyword Args:
            filter (ProductReviewFilter): Filter the results. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
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
            GetProductReviewResponse
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
        kwargs['product'] = \
            product
        kwargs['review'] = \
            review
        return self.get_product_review_endpoint.call_with_http_info(**kwargs)

    def list_product_reviews(
        self,
        product,
        **kwargs
    ):
        """List all reviews for a product  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_product_reviews(product, async_req=True)
        >>> result = thread.get()

        Args:
            product (str):

        Keyword Args:
            per_page (int, none_type): [optional] if omitted the server will use the default value of 24
            cursor (str): The cursor from which to return paginated results starting after. [optional]
            filter (ProductReviewFilter): Filter the results. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
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
            bool, date, datetime, dict, float, int, list, str, none_type
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
        kwargs['product'] = \
            product
        return self.list_product_reviews_endpoint.call_with_http_info(**kwargs)
