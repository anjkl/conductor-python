from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from conductor.client.http.api_client import ApiClient


class MigrationResourceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def migrate_index(self, **kwargs):  # noqa: E501
        """Migrate Workflow Index t o the sharded table  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.migrate_index(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.migrate_index_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.migrate_index_with_http_info(**kwargs)  # noqa: E501
            return data

    def migrate_index_with_http_info(self, **kwargs):  # noqa: E501
        """Migrate Workflow Index t o the sharded table  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.migrate_index_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method migrate_index" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/admin/migrate_index', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def migrate_metadata(self, **kwargs):  # noqa: E501
        """Migrate Workflow and Task Definitions to Postgres  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.migrate_metadata(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.migrate_metadata_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.migrate_metadata_with_http_info(**kwargs)  # noqa: E501
            return data

    def migrate_metadata_with_http_info(self, **kwargs):  # noqa: E501
        """Migrate Workflow and Task Definitions to Postgres  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.migrate_metadata_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method migrate_metadata" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/admin/migrate_metadata', 'GET',
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

    def migrate_workflows(self, batch_size, start_from_timestamp, **kwargs):  # noqa: E501
        """Migrate workflows from Redis to Postgres  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.migrate_workflows(batch_size, start_from_timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int batch_size: (required)
        :param int start_from_timestamp: (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.migrate_workflows_with_http_info(batch_size, start_from_timestamp, **kwargs)  # noqa: E501
        else:
            (data) = self.migrate_workflows_with_http_info(batch_size, start_from_timestamp, **kwargs)  # noqa: E501
            return data

    def migrate_workflows_with_http_info(self, batch_size, start_from_timestamp, **kwargs):  # noqa: E501
        """Migrate workflows from Redis to Postgres  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.migrate_workflows_with_http_info(batch_size, start_from_timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int batch_size: (required)
        :param int start_from_timestamp: (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['batch_size', 'start_from_timestamp']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method migrate_workflows" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'batch_size' is set
        if ('batch_size' not in params or
                params['batch_size'] is None):
            raise ValueError("Missing the required parameter `batch_size` when calling `migrate_workflows`")  # noqa: E501
        # verify the required parameter 'start_from_timestamp' is set
        if ('start_from_timestamp' not in params or
                params['start_from_timestamp'] is None):
            raise ValueError("Missing the required parameter `start_from_timestamp` when calling `migrate_workflows`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'batch_size' in params:
            query_params.append(('batchSize', params['batch_size']))  # noqa: E501
        if 'start_from_timestamp' in params:
            query_params.append(('startFromTimestamp', params['start_from_timestamp']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/admin/migrate_workflow', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, object)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
