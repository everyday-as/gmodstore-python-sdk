# coding: utf-8

"""
    GmodStore API

    Welcome to the GmodStore API! You can use our API to access GmodStore API endpoints, which can be used interact with GmodStore programmatically.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import gmodstore-sdk
from gmodstore-sdk.models.api_key import ApiKey  # noqa: E501
from gmodstore-sdk.rest import ApiException

class TestApiKey(unittest.TestCase):
    """ApiKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiKey
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = gmodstore-sdk.models.api_key.ApiKey()  # noqa: E501
        if include_optional :
            return ApiKey(
                permissions = [
                    'addons.read'
                    ], 
                user = gmodstore-sdk.models.user.User(
                    id = 56, 
                    name = '0', 
                    avatar = '0', 
                    country_code = '0', 
                    slug = '0', 
                    reputation = 56, 
                    team_reputation = 56, 
                    ban_properties = [
                        'everything'
                        ], 
                    group = gmodstore-sdk.models.permission_group.PermissionGroup(
                        id = 56, 
                        title = '0', 
                        display_order = 56, ), )
            )
        else :
            return ApiKey(
        )

    def testApiKey(self):
        """Test ApiKey"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
