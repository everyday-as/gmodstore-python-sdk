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
from api.addon_purchases_api import AddonPurchasesApi  # noqa: E501
from gmodstore_sdk.rest import ApiException


class TestAddonPurchasesApi(unittest.TestCase):
    """AddonPurchasesApi unit test stubs"""

    def setUp(self):
        self.api = api.addon_purchases_api.AddonPurchasesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_addons_addon_id_purchases_get(self):
        """Test case for addons_addon_id_purchases_get

        Fetch all purchases of an addon  # noqa: E501
        """
        pass

    def test_addons_addon_id_purchases_post(self):
        """Test case for addons_addon_id_purchases_post

        Create a purchase for an addon  # noqa: E501
        """
        pass

    def test_addons_addon_id_purchases_user_id_get(self):
        """Test case for addons_addon_id_purchases_user_id_get

        Get a purchase of an addon by user  # noqa: E501
        """
        pass

    def test_addons_addon_id_purchases_user_id_put(self):
        """Test case for addons_addon_id_purchases_user_id_put

        Update a purchase for an addon  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
