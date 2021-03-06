# coding: utf-8

"""
    GmodStore

    Welcome to the Gmodstore API! You can use our API to access Gmodstore API endpoints, which can be used interact with Gmodstore programmatically.  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gmodstore_sdk
from api.user_addons_api import UserAddonsApi  # noqa: E501
from gmodstore_sdk.rest import ApiException


class TestUserAddonsApi(unittest.TestCase):
    """UserAddonsApi unit test stubs"""

    def setUp(self):
        self.api = api.user_addons_api.UserAddonsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_user_addons(self):
        """Test case for list_user_addons

        Fetch all the addons authored / co-authored by a user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
