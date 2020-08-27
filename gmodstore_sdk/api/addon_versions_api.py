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


class AddonVersionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_addon_version(self, name, changelog, file, release_type, addon_id, **kwargs):  # noqa: E501
        """Create a new version for an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_addon_version(name, changelog, file, release_type, addon_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param str changelog: (required)
        :param str file: (required)
        :param AddonVersionReleaseType release_type: (required)
        :param int addon_id: Id of the addon (required)
        :param list[str] _with: The relations you want to fetch with the `AddonVersion`
        :return: AddonVersionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_addon_version_with_http_info(name, changelog, file, release_type, addon_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_addon_version_with_http_info(name, changelog, file, release_type, addon_id, **kwargs)  # noqa: E501
            return data

    def create_addon_version_with_http_info(self, name, changelog, file, release_type, addon_id, **kwargs):  # noqa: E501
        """Create a new version for an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_addon_version_with_http_info(name, changelog, file, release_type, addon_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param str changelog: (required)
        :param str file: (required)
        :param AddonVersionReleaseType release_type: (required)
        :param int addon_id: Id of the addon (required)
        :param list[str] _with: The relations you want to fetch with the `AddonVersion`
        :return: AddonVersionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'changelog', 'file', 'release_type', 'addon_id', '_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_addon_version" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `create_addon_version`")  # noqa: E501
        # verify the required parameter 'changelog' is set
        if ('changelog' not in params or
                params['changelog'] is None):
            raise ValueError("Missing the required parameter `changelog` when calling `create_addon_version`")  # noqa: E501
        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `create_addon_version`")  # noqa: E501
        # verify the required parameter 'release_type' is set
        if ('release_type' not in params or
                params['release_type'] is None):
            raise ValueError("Missing the required parameter `release_type` when calling `create_addon_version`")  # noqa: E501
        # verify the required parameter 'addon_id' is set
        if ('addon_id' not in params or
                params['addon_id'] is None):
            raise ValueError("Missing the required parameter `addon_id` when calling `create_addon_version`")  # noqa: E501

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
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'changelog' in params:
            form_params.append(('changelog', params['changelog']))  # noqa: E501
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501
        if 'release_type' in params:
            form_params.append(('release_type', params['release_type']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/addons/{addon_id}/versions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddonVersionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def download_addon_version(self, addon_id, version_id, **kwargs):  # noqa: E501
        """Generate a download token for a specific version of an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_addon_version(addon_id, version_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int addon_id: Id of the addon (required)
        :param int version_id: Id of the version (required)
        :return: AddonDownloadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_addon_version_with_http_info(addon_id, version_id, **kwargs)  # noqa: E501
        else:
            (data) = self.download_addon_version_with_http_info(addon_id, version_id, **kwargs)  # noqa: E501
            return data

    def download_addon_version_with_http_info(self, addon_id, version_id, **kwargs):  # noqa: E501
        """Generate a download token for a specific version of an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_addon_version_with_http_info(addon_id, version_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int addon_id: Id of the addon (required)
        :param int version_id: Id of the version (required)
        :return: AddonDownloadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['addon_id', 'version_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_addon_version" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'addon_id' is set
        if ('addon_id' not in params or
                params['addon_id'] is None):
            raise ValueError("Missing the required parameter `addon_id` when calling `download_addon_version`")  # noqa: E501
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `download_addon_version`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_id' in params:
            path_params['addon_id'] = params['addon_id']  # noqa: E501
        if 'version_id' in params:
            path_params['version_id'] = params['version_id']  # noqa: E501

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
            '/addons/{addon_id}/versions/{version_id}/download', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddonDownloadResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_addon_version(self, addon_id, version_id, **kwargs):  # noqa: E501
        """Fetch a specific version of an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_addon_version(addon_id, version_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int addon_id: Id of the addon (required)
        :param int version_id: Id of the version (required)
        :param list[str] _with: The relations you want to fetch with the `AddonVersion`
        :return: AddonVersionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_addon_version_with_http_info(addon_id, version_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_addon_version_with_http_info(addon_id, version_id, **kwargs)  # noqa: E501
            return data

    def get_addon_version_with_http_info(self, addon_id, version_id, **kwargs):  # noqa: E501
        """Fetch a specific version of an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_addon_version_with_http_info(addon_id, version_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int addon_id: Id of the addon (required)
        :param int version_id: Id of the version (required)
        :param list[str] _with: The relations you want to fetch with the `AddonVersion`
        :return: AddonVersionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['addon_id', 'version_id', '_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_addon_version" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'addon_id' is set
        if ('addon_id' not in params or
                params['addon_id'] is None):
            raise ValueError("Missing the required parameter `addon_id` when calling `get_addon_version`")  # noqa: E501
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `get_addon_version`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_id' in params:
            path_params['addon_id'] = params['addon_id']  # noqa: E501
        if 'version_id' in params:
            path_params['version_id'] = params['version_id']  # noqa: E501

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
            '/addons/{addon_id}/versions/{version_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddonVersionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_addon_versions(self, addon_id, **kwargs):  # noqa: E501
        """Fetch all the versions of an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_addon_versions(addon_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int addon_id: Id of the addon (required)
        :param list[str] _with: The relations you want to fetch with the `AddonVersion`
        :return: AddonVersionListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_addon_versions_with_http_info(addon_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_addon_versions_with_http_info(addon_id, **kwargs)  # noqa: E501
            return data

    def list_addon_versions_with_http_info(self, addon_id, **kwargs):  # noqa: E501
        """Fetch all the versions of an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_addon_versions_with_http_info(addon_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int addon_id: Id of the addon (required)
        :param list[str] _with: The relations you want to fetch with the `AddonVersion`
        :return: AddonVersionListResponse
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
                    " to method list_addon_versions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'addon_id' is set
        if ('addon_id' not in params or
                params['addon_id'] is None):
            raise ValueError("Missing the required parameter `addon_id` when calling `list_addon_versions`")  # noqa: E501

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
            '/addons/{addon_id}/versions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddonVersionListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_addon_version(self, id, name, changelog, file_hash, file_size, release_type, created_at, updated_at, addon, addon_id, version_id, **kwargs):  # noqa: E501
        """Update a version of an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_addon_version(id, name, changelog, file_hash, file_size, release_type, created_at, updated_at, addon, addon_id, version_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param str name: (required)
        :param str changelog: (required)
        :param str file_hash: (required)
        :param int file_size: (required)
        :param AddonVersionReleaseType release_type: (required)
        :param datetime created_at: (required)
        :param datetime updated_at: (required)
        :param Addon addon: (required)
        :param int addon_id: Id of the addon (required)
        :param int version_id: Id of the version (required)
        :param list[str] _with: The relations you want to fetch with the `AddonVersion`
        :return: AddonVersionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_addon_version_with_http_info(id, name, changelog, file_hash, file_size, release_type, created_at, updated_at, addon, addon_id, version_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_addon_version_with_http_info(id, name, changelog, file_hash, file_size, release_type, created_at, updated_at, addon, addon_id, version_id, **kwargs)  # noqa: E501
            return data

    def update_addon_version_with_http_info(self, id, name, changelog, file_hash, file_size, release_type, created_at, updated_at, addon, addon_id, version_id, **kwargs):  # noqa: E501
        """Update a version of an addon  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_addon_version_with_http_info(id, name, changelog, file_hash, file_size, release_type, created_at, updated_at, addon, addon_id, version_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param str name: (required)
        :param str changelog: (required)
        :param str file_hash: (required)
        :param int file_size: (required)
        :param AddonVersionReleaseType release_type: (required)
        :param datetime created_at: (required)
        :param datetime updated_at: (required)
        :param Addon addon: (required)
        :param int addon_id: Id of the addon (required)
        :param int version_id: Id of the version (required)
        :param list[str] _with: The relations you want to fetch with the `AddonVersion`
        :return: AddonVersionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'name', 'changelog', 'file_hash', 'file_size', 'release_type', 'created_at', 'updated_at', 'addon', 'addon_id', 'version_id', '_with']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_addon_version" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_addon_version`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `update_addon_version`")  # noqa: E501
        # verify the required parameter 'changelog' is set
        if ('changelog' not in params or
                params['changelog'] is None):
            raise ValueError("Missing the required parameter `changelog` when calling `update_addon_version`")  # noqa: E501
        # verify the required parameter 'file_hash' is set
        if ('file_hash' not in params or
                params['file_hash'] is None):
            raise ValueError("Missing the required parameter `file_hash` when calling `update_addon_version`")  # noqa: E501
        # verify the required parameter 'file_size' is set
        if ('file_size' not in params or
                params['file_size'] is None):
            raise ValueError("Missing the required parameter `file_size` when calling `update_addon_version`")  # noqa: E501
        # verify the required parameter 'release_type' is set
        if ('release_type' not in params or
                params['release_type'] is None):
            raise ValueError("Missing the required parameter `release_type` when calling `update_addon_version`")  # noqa: E501
        # verify the required parameter 'created_at' is set
        if ('created_at' not in params or
                params['created_at'] is None):
            raise ValueError("Missing the required parameter `created_at` when calling `update_addon_version`")  # noqa: E501
        # verify the required parameter 'updated_at' is set
        if ('updated_at' not in params or
                params['updated_at'] is None):
            raise ValueError("Missing the required parameter `updated_at` when calling `update_addon_version`")  # noqa: E501
        # verify the required parameter 'addon' is set
        if ('addon' not in params or
                params['addon'] is None):
            raise ValueError("Missing the required parameter `addon` when calling `update_addon_version`")  # noqa: E501
        # verify the required parameter 'addon_id' is set
        if ('addon_id' not in params or
                params['addon_id'] is None):
            raise ValueError("Missing the required parameter `addon_id` when calling `update_addon_version`")  # noqa: E501
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `update_addon_version`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'addon_id' in params:
            path_params['addon_id'] = params['addon_id']  # noqa: E501
        if 'version_id' in params:
            path_params['version_id'] = params['version_id']  # noqa: E501

        query_params = []
        if '_with' in params:
            query_params.append(('with', params['_with']))  # noqa: E501
            collection_formats['with'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'id' in params:
            form_params.append(('id', params['id']))  # noqa: E501
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'changelog' in params:
            form_params.append(('changelog', params['changelog']))  # noqa: E501
        if 'file_hash' in params:
            form_params.append(('file_hash', params['file_hash']))  # noqa: E501
        if 'file_size' in params:
            form_params.append(('file_size', params['file_size']))  # noqa: E501
        if 'release_type' in params:
            form_params.append(('release_type', params['release_type']))  # noqa: E501
        if 'created_at' in params:
            form_params.append(('created_at', params['created_at']))  # noqa: E501
        if 'updated_at' in params:
            form_params.append(('updated_at', params['updated_at']))  # noqa: E501
        if 'addon' in params:
            form_params.append(('addon', params['addon']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/addons/{addon_id}/versions/{version_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddonVersionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
