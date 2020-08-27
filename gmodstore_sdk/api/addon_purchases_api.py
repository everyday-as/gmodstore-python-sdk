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


class AddonPurchasesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_addon_purchase(self, body, addon_id, **kwargs):  # noqa: E501
        """Create a purchase for an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_addon_purchase(body, addon_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewAddonPurchase body: (required)
        :param int addon_id: Id of the addon (required)
        :param list[str] _with: The relations you want to fetch with the `AddonPurchase`
        :return: AddonPurchaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_addon_purchase_with_http_info(body, addon_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_addon_purchase_with_http_info(body, addon_id, **kwargs)  # noqa: E501
            return data

    def create_addon_purchase_with_http_info(self, body, addon_id, **kwargs):  # noqa: E501
        """Create a purchase for an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_addon_purchase_with_http_info(body, addon_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewAddonPurchase body: (required)
        :param int addon_id: Id of the addon (required)
        :param list[str] _with: The relations you want to fetch with the `AddonPurchase`
        :return: AddonPurchaseResponse
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
                    " to method create_addon_purchase" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_addon_purchase`")  # noqa: E501
        # verify the required parameter 'addon_id' is set
        if ('addon_id' not in params or
                params['addon_id'] is None):
            raise ValueError("Missing the required parameter `addon_id` when calling `create_addon_purchase`")  # noqa: E501

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
            '/addons/{addon_id}/purchases', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddonPurchaseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_addon_purchase(self, addon_id, user_id, **kwargs):  # noqa: E501
        """Get a purchase of an addon by user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_addon_purchase(addon_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int addon_id: Id of the addon (required)
        :param int user_id: Id of the user (required)
        :param list[str] _with: The relations you want to fetch with the `AddonPurchase`
        :return: AddonPurchaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_addon_purchase_with_http_info(addon_id, user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_addon_purchase_with_http_info(addon_id, user_id, **kwargs)  # noqa: E501
            return data

    def get_addon_purchase_with_http_info(self, addon_id, user_id, **kwargs):  # noqa: E501
        """Get a purchase of an addon by user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_addon_purchase_with_http_info(addon_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int addon_id: Id of the addon (required)
        :param int user_id: Id of the user (required)
        :param list[str] _with: The relations you want to fetch with the `AddonPurchase`
        :return: AddonPurchaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['addon_id', 'user_id', '_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_addon_purchase" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'addon_id' is set
        if ('addon_id' not in params or
                params['addon_id'] is None):
            raise ValueError("Missing the required parameter `addon_id` when calling `get_addon_purchase`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_addon_purchase`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_id' in params:
            path_params['addon_id'] = params['addon_id']  # noqa: E501
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

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
            '/addons/{addon_id}/purchases/{user_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddonPurchaseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_addon_purchases(self, addon_id, **kwargs):  # noqa: E501
        """Fetch all purchases of an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_addon_purchases(addon_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int addon_id: Id of the addon (required)
        :param list[str] _with: The relations you want to fetch with the `AddonPurchase`
        :return: AddonPurchaseListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_addon_purchases_with_http_info(addon_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_addon_purchases_with_http_info(addon_id, **kwargs)  # noqa: E501
            return data

    def list_addon_purchases_with_http_info(self, addon_id, **kwargs):  # noqa: E501
        """Fetch all purchases of an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_addon_purchases_with_http_info(addon_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int addon_id: Id of the addon (required)
        :param list[str] _with: The relations you want to fetch with the `AddonPurchase`
        :return: AddonPurchaseListResponse
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
                    " to method list_addon_purchases" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'addon_id' is set
        if ('addon_id' not in params or
                params['addon_id'] is None):
            raise ValueError("Missing the required parameter `addon_id` when calling `list_addon_purchases`")  # noqa: E501

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
            '/addons/{addon_id}/purchases', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddonPurchaseListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_addon_purchase(self, body, addon_id, user_id, **kwargs):  # noqa: E501
        """Update a purchase for an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_addon_purchase(body, addon_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddonPurchase body: (required)
        :param int addon_id: Id of the addon (required)
        :param int user_id: Id of the user (required)
        :param list[str] _with: The relations you want to fetch with the `AddonPurchase`
        :return: AddonPurchaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_addon_purchase_with_http_info(body, addon_id, user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_addon_purchase_with_http_info(body, addon_id, user_id, **kwargs)  # noqa: E501
            return data

    def update_addon_purchase_with_http_info(self, body, addon_id, user_id, **kwargs):  # noqa: E501
        """Update a purchase for an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_addon_purchase_with_http_info(body, addon_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddonPurchase body: (required)
        :param int addon_id: Id of the addon (required)
        :param int user_id: Id of the user (required)
        :param list[str] _with: The relations you want to fetch with the `AddonPurchase`
        :return: AddonPurchaseResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'addon_id', 'user_id', '_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_addon_purchase" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_addon_purchase`")  # noqa: E501
        # verify the required parameter 'addon_id' is set
        if ('addon_id' not in params or
                params['addon_id'] is None):
            raise ValueError("Missing the required parameter `addon_id` when calling `update_addon_purchase`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `update_addon_purchase`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_id' in params:
            path_params['addon_id'] = params['addon_id']  # noqa: E501
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

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
            '/addons/{addon_id}/purchases/{user_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddonPurchaseResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
