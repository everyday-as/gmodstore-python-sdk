# coding: utf-8

"""
    GmodStore

    Welcome to the Gmodstore API! You can use our API to access Gmodstore API endpoints, which can be used interact with Gmodstore programmatically.  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from gmodstore_sdk.api_client import ApiClient


class AddonCouponsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_addon_coupon(self, body, addon_id, **kwargs):  # noqa: E501
        """Create an addon coupon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_addon_coupon(body, addon_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddonCoupon body: (required)
        :param int addon_id: Id of the addon (required)
        :param list[str] _with: The relations you want to fetch with the `AddonCoupon`
        :return: AddonCouponResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_addon_coupon_with_http_info(body, addon_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_addon_coupon_with_http_info(body, addon_id, **kwargs)  # noqa: E501
            return data

    def create_addon_coupon_with_http_info(self, body, addon_id, **kwargs):  # noqa: E501
        """Create an addon coupon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_addon_coupon_with_http_info(body, addon_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddonCoupon body: (required)
        :param int addon_id: Id of the addon (required)
        :param list[str] _with: The relations you want to fetch with the `AddonCoupon`
        :return: AddonCouponResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'addon_id', '_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_addon_coupon" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_addon_coupon`")  # noqa: E501
        # verify the required parameter 'addon_id' is set
        if ('addon_id' not in params or
                params['addon_id'] is None):
            raise ValueError("Missing the required parameter `addon_id` when calling `create_addon_coupon`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_id' in params:
            path_params['addon_id'] = params['addon_id']  # noqa: E501

        query_params = []
        if '_with' in params:
            query_params.append(('with', params['_with']))  # noqa: E501
            collection_formats['with'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
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
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_addon_coupon(self, addon_id, coupon_id, **kwargs):  # noqa: E501
        """Destroy an addon's coupon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_addon_coupon(addon_id, coupon_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int addon_id: Id of the addon (required)
        :param int coupon_id: Id of the coupon (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_addon_coupon_with_http_info(addon_id, coupon_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_addon_coupon_with_http_info(addon_id, coupon_id, **kwargs)  # noqa: E501
            return data

    def delete_addon_coupon_with_http_info(self, addon_id, coupon_id, **kwargs):  # noqa: E501
        """Destroy an addon's coupon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_addon_coupon_with_http_info(addon_id, coupon_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int addon_id: Id of the addon (required)
        :param int coupon_id: Id of the coupon (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['addon_id', 'coupon_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_addon_coupon" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'addon_id' is set
        if ('addon_id' not in params or
                params['addon_id'] is None):
            raise ValueError("Missing the required parameter `addon_id` when calling `delete_addon_coupon`")  # noqa: E501
        # verify the required parameter 'coupon_id' is set
        if ('coupon_id' not in params or
                params['coupon_id'] is None):
            raise ValueError("Missing the required parameter `coupon_id` when calling `delete_addon_coupon`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_id' in params:
            path_params['addon_id'] = params['addon_id']  # noqa: E501
        if 'coupon_id' in params:
            path_params['coupon_id'] = params['coupon_id']  # noqa: E501

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
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_addon_coupon(self, addon_id, coupon_id, **kwargs):  # noqa: E501
        """Fetch an addon's coupon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_addon_coupon(addon_id, coupon_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int addon_id: Id of the addon (required)
        :param int coupon_id: Id of the coupon (required)
        :param list[str] _with: The relations you want to fetch with the `AddonCoupon`
        :return: AddonCouponResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_addon_coupon_with_http_info(addon_id, coupon_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_addon_coupon_with_http_info(addon_id, coupon_id, **kwargs)  # noqa: E501
            return data

    def get_addon_coupon_with_http_info(self, addon_id, coupon_id, **kwargs):  # noqa: E501
        """Fetch an addon's coupon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_addon_coupon_with_http_info(addon_id, coupon_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int addon_id: Id of the addon (required)
        :param int coupon_id: Id of the coupon (required)
        :param list[str] _with: The relations you want to fetch with the `AddonCoupon`
        :return: AddonCouponResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['addon_id', 'coupon_id', '_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_addon_coupon" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'addon_id' is set
        if ('addon_id' not in params or
                params['addon_id'] is None):
            raise ValueError("Missing the required parameter `addon_id` when calling `get_addon_coupon`")  # noqa: E501
        # verify the required parameter 'coupon_id' is set
        if ('coupon_id' not in params or
                params['coupon_id'] is None):
            raise ValueError("Missing the required parameter `coupon_id` when calling `get_addon_coupon`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_id' in params:
            path_params['addon_id'] = params['addon_id']  # noqa: E501
        if 'coupon_id' in params:
            path_params['coupon_id'] = params['coupon_id']  # noqa: E501

        query_params = []
        if '_with' in params:
            query_params.append(('with', params['_with']))  # noqa: E501
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
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_addon_coupons(self, addon_id, **kwargs):  # noqa: E501
        """Fetch all the coupons for an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_addon_coupons(addon_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int addon_id: Id of the addon (required)
        :param list[str] _with: The relations you want to fetch with the `AddonCoupon`
        :return: AddonCouponListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_addon_coupons_with_http_info(addon_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_addon_coupons_with_http_info(addon_id, **kwargs)  # noqa: E501
            return data

    def list_addon_coupons_with_http_info(self, addon_id, **kwargs):  # noqa: E501
        """Fetch all the coupons for an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_addon_coupons_with_http_info(addon_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int addon_id: Id of the addon (required)
        :param list[str] _with: The relations you want to fetch with the `AddonCoupon`
        :return: AddonCouponListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['addon_id', '_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_addon_coupons" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'addon_id' is set
        if ('addon_id' not in params or
                params['addon_id'] is None):
            raise ValueError("Missing the required parameter `addon_id` when calling `list_addon_coupons`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_id' in params:
            path_params['addon_id'] = params['addon_id']  # noqa: E501

        query_params = []
        if '_with' in params:
            query_params.append(('with', params['_with']))  # noqa: E501
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
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_addon_coupon(self, body, addon_id, coupon_id, **kwargs):  # noqa: E501
        """Update an addon's coupon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_addon_coupon(body, addon_id, coupon_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddonCoupon body: (required)
        :param int addon_id: Id of the addon (required)
        :param int coupon_id: Id of the coupon (required)
        :param list[str] _with: The relations you want to fetch with the `AddonCoupon`
        :return: AddonCouponResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_addon_coupon_with_http_info(body, addon_id, coupon_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_addon_coupon_with_http_info(body, addon_id, coupon_id, **kwargs)  # noqa: E501
            return data

    def update_addon_coupon_with_http_info(self, body, addon_id, coupon_id, **kwargs):  # noqa: E501
        """Update an addon's coupon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_addon_coupon_with_http_info(body, addon_id, coupon_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddonCoupon body: (required)
        :param int addon_id: Id of the addon (required)
        :param int coupon_id: Id of the coupon (required)
        :param list[str] _with: The relations you want to fetch with the `AddonCoupon`
        :return: AddonCouponResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'addon_id', 'coupon_id', '_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_addon_coupon" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_addon_coupon`")  # noqa: E501
        # verify the required parameter 'addon_id' is set
        if ('addon_id' not in params or
                params['addon_id'] is None):
            raise ValueError("Missing the required parameter `addon_id` when calling `update_addon_coupon`")  # noqa: E501
        # verify the required parameter 'coupon_id' is set
        if ('coupon_id' not in params or
                params['coupon_id'] is None):
            raise ValueError("Missing the required parameter `coupon_id` when calling `update_addon_coupon`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_id' in params:
            path_params['addon_id'] = params['addon_id']  # noqa: E501
        if 'coupon_id' in params:
            path_params['coupon_id'] = params['coupon_id']  # noqa: E501

        query_params = []
        if '_with' in params:
            query_params.append(('with', params['_with']))  # noqa: E501
            collection_formats['with'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
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
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
