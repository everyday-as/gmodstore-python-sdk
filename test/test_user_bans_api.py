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
from api.user_bans_api import UserBansApi  # noqa: E501
from gmodstore_sdk.rest import ApiException


class TestUserBansApi(unittest.TestCase):
    """UserBansApi unit test stubs"""

    def setUp(self):
        self.api = api.user_bans_api.UserBansApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_user_bans(self):
        """Test case for list_user_bans

        Fetch all active bans associated with this user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
