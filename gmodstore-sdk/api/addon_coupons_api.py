# coding: utf-8

"""
    GmodStore API

    Welcome to the GmodStore API! You can use our API to access GmodStore API endpoints, which can be used interact with GmodStore programmatically.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from gmodstore-sdk.api_client import ApiClient
from gmodstore-sdk.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AddonCouponsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_addon_coupon(self, addon_id, addon_coupon, **kwargs):  # noqa: E501
        """Create an addon coupon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_addon_coupon(addon_id, addon_coupon, async_req=True)
        >>> result = thread.get()

        :param addon_id: Id of the addon (required)
        :type addon_id: int
        :param addon_coupon: (required)
        :type addon_coupon: AddonCoupon
        :param _with: The relations you want to fetch with the `AddonCoupon`
        :type _with: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AddonCouponResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.create_addon_coupon_with_http_info(addon_id, addon_coupon, **kwargs)  # noqa: E501

    def create_addon_coupon_with_http_info(self, addon_id, addon_coupon, **kwargs):  # noqa: E501
        """Create an addon coupon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_addon_coupon_with_http_info(addon_id, addon_coupon, async_req=True)
        >>> result = thread.get()

        :param addon_id: Id of the addon (required)
        :type addon_id: int
        :param addon_coupon: (required)
        :type addon_coupon: AddonCoupon
        :param _with: The relations you want to fetch with the `AddonCoupon`
        :type _with: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AddonCouponResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'addon_id',
            'addon_coupon',
            '_with'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_addon_coupon" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'addon_id' is set
        if self.api_client.client_side_validation and ('addon_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['addon_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `addon_id` when calling `create_addon_coupon`")  # noqa: E501
        # verify the required parameter 'addon_coupon' is set
        if self.api_client.client_side_validation and ('addon_coupon' not in local_var_params or  # noqa: E501
                                                        local_var_params['addon_coupon'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `addon_coupon` when calling `create_addon_coupon`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_id' in local_var_params:
            path_params['addon_id'] = local_var_params['addon_id']  # noqa: E501

        query_params = []
        if '_with' in local_var_params and local_var_params['_with'] is not None:  # noqa: E501
            query_params.append(('with', local_var_params['_with']))  # noqa: E501
            collection_formats['with'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'addon_coupon' in local_var_params:
            body_params = local_var_params['addon_coupon']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/addons/{addon_id}/coupons', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddonCouponResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def delete_addon_coupon(self, addon_id, coupon_id, **kwargs):  # noqa: E501
        """Destroy an addon's coupon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_addon_coupon(addon_id, coupon_id, async_req=True)
        >>> result = thread.get()

        :param addon_id: Id of the addon (required)
        :type addon_id: int
        :param coupon_id: Id of the coupon (required)
        :type coupon_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_addon_coupon_with_http_info(addon_id, coupon_id, **kwargs)  # noqa: E501

    def delete_addon_coupon_with_http_info(self, addon_id, coupon_id, **kwargs):  # noqa: E501
        """Destroy an addon's coupon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_addon_coupon_with_http_info(addon_id, coupon_id, async_req=True)
        >>> result = thread.get()

        :param addon_id: Id of the addon (required)
        :type addon_id: int
        :param coupon_id: Id of the coupon (required)
        :type coupon_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'addon_id',
            'coupon_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_addon_coupon" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'addon_id' is set
        if self.api_client.client_side_validation and ('addon_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['addon_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `addon_id` when calling `delete_addon_coupon`")  # noqa: E501
        # verify the required parameter 'coupon_id' is set
        if self.api_client.client_side_validation and ('coupon_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['coupon_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `coupon_id` when calling `delete_addon_coupon`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_id' in local_var_params:
            path_params['addon_id'] = local_var_params['addon_id']  # noqa: E501
        if 'coupon_id' in local_var_params:
            path_params['coupon_id'] = local_var_params['coupon_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/addons/{addon_id}/coupons/{coupon_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_addon_coupon(self, addon_id, coupon_id, **kwargs):  # noqa: E501
        """Fetch an addon's coupon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_addon_coupon(addon_id, coupon_id, async_req=True)
        >>> result = thread.get()

        :param addon_id: Id of the addon (required)
        :type addon_id: int
        :param coupon_id: Id of the coupon (required)
        :type coupon_id: int
        :param _with: The relations you want to fetch with the `AddonCoupon`
        :type _with: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AddonCouponResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_addon_coupon_with_http_info(addon_id, coupon_id, **kwargs)  # noqa: E501

    def get_addon_coupon_with_http_info(self, addon_id, coupon_id, **kwargs):  # noqa: E501
        """Fetch an addon's coupon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_addon_coupon_with_http_info(addon_id, coupon_id, async_req=True)
        >>> result = thread.get()

        :param addon_id: Id of the addon (required)
        :type addon_id: int
        :param coupon_id: Id of the coupon (required)
        :type coupon_id: int
        :param _with: The relations you want to fetch with the `AddonCoupon`
        :type _with: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AddonCouponResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'addon_id',
            'coupon_id',
            '_with'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_addon_coupon" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'addon_id' is set
        if self.api_client.client_side_validation and ('addon_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['addon_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `addon_id` when calling `get_addon_coupon`")  # noqa: E501
        # verify the required parameter 'coupon_id' is set
        if self.api_client.client_side_validation and ('coupon_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['coupon_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `coupon_id` when calling `get_addon_coupon`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_id' in local_var_params:
            path_params['addon_id'] = local_var_params['addon_id']  # noqa: E501
        if 'coupon_id' in local_var_params:
            path_params['coupon_id'] = local_var_params['coupon_id']  # noqa: E501

        query_params = []
        if '_with' in local_var_params and local_var_params['_with'] is not None:  # noqa: E501
            query_params.append(('with', local_var_params['_with']))  # noqa: E501
            collection_formats['with'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/addons/{addon_id}/coupons/{coupon_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddonCouponResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def list_addon_coupons(self, addon_id, **kwargs):  # noqa: E501
        """Fetch all the coupons for an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_addon_coupons(addon_id, async_req=True)
        >>> result = thread.get()

        :param addon_id: Id of the addon (required)
        :type addon_id: int
        :param _with: The relations you want to fetch with the `AddonCoupon`
        :type _with: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AddonCouponListResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.list_addon_coupons_with_http_info(addon_id, **kwargs)  # noqa: E501

    def list_addon_coupons_with_http_info(self, addon_id, **kwargs):  # noqa: E501
        """Fetch all the coupons for an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_addon_coupons_with_http_info(addon_id, async_req=True)
        >>> result = thread.get()

        :param addon_id: Id of the addon (required)
        :type addon_id: int
        :param _with: The relations you want to fetch with the `AddonCoupon`
        :type _with: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AddonCouponListResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'addon_id',
            '_with'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_addon_coupons" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'addon_id' is set
        if self.api_client.client_side_validation and ('addon_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['addon_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `addon_id` when calling `list_addon_coupons`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_id' in local_var_params:
            path_params['addon_id'] = local_var_params['addon_id']  # noqa: E501

        query_params = []
        if '_with' in local_var_params and local_var_params['_with'] is not None:  # noqa: E501
            query_params.append(('with', local_var_params['_with']))  # noqa: E501
            collection_formats['with'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/addons/{addon_id}/coupons', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddonCouponListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def update_addon_coupon(self, addon_id, coupon_id, addon_coupon, **kwargs):  # noqa: E501
        """Update an addon's coupon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_addon_coupon(addon_id, coupon_id, addon_coupon, async_req=True)
        >>> result = thread.get()

        :param addon_id: Id of the addon (required)
        :type addon_id: int
        :param coupon_id: Id of the coupon (required)
        :type coupon_id: int
        :param addon_coupon: (required)
        :type addon_coupon: AddonCoupon
        :param _with: The relations you want to fetch with the `AddonCoupon`
        :type _with: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AddonCouponResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.update_addon_coupon_with_http_info(addon_id, coupon_id, addon_coupon, **kwargs)  # noqa: E501

    def update_addon_coupon_with_http_info(self, addon_id, coupon_id, addon_coupon, **kwargs):  # noqa: E501
        """Update an addon's coupon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_addon_coupon_with_http_info(addon_id, coupon_id, addon_coupon, async_req=True)
        >>> result = thread.get()

        :param addon_id: Id of the addon (required)
        :type addon_id: int
        :param coupon_id: Id of the coupon (required)
        :type coupon_id: int
        :param addon_coupon: (required)
        :type addon_coupon: AddonCoupon
        :param _with: The relations you want to fetch with the `AddonCoupon`
        :type _with: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AddonCouponResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'addon_id',
            'coupon_id',
            'addon_coupon',
            '_with'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_addon_coupon" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'addon_id' is set
        if self.api_client.client_side_validation and ('addon_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['addon_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `addon_id` when calling `update_addon_coupon`")  # noqa: E501
        # verify the required parameter 'coupon_id' is set
        if self.api_client.client_side_validation and ('coupon_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['coupon_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `coupon_id` when calling `update_addon_coupon`")  # noqa: E501
        # verify the required parameter 'addon_coupon' is set
        if self.api_client.client_side_validation and ('addon_coupon' not in local_var_params or  # noqa: E501
                                                        local_var_params['addon_coupon'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `addon_coupon` when calling `update_addon_coupon`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_id' in local_var_params:
            path_params['addon_id'] = local_var_params['addon_id']  # noqa: E501
        if 'coupon_id' in local_var_params:
            path_params['coupon_id'] = local_var_params['coupon_id']  # noqa: E501

        query_params = []
        if '_with' in local_var_params and local_var_params['_with'] is not None:  # noqa: E501
            query_params.append(('with', local_var_params['_with']))  # noqa: E501
            collection_formats['with'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'addon_coupon' in local_var_params:
            body_params = local_var_params['addon_coupon']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/addons/{addon_id}/coupons/{coupon_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddonCouponResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
