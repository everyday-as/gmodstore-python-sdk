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
from api.addons_api import AddonsApi  # noqa: E501
from gmodstore_sdk.rest import ApiException


class TestAddonsApi(unittest.TestCase):
    """AddonsApi unit test stubs"""

    def setUp(self):
        self.api = api.addons_api.AddonsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_addon(self):
        """Test case for get_addon

        Fetch a single addon  # noqa: E501
        """
        pass

    def test_list_self_addons(self):
        """Test case for list_self_addons

        Fetch all the addons that you have access to  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
