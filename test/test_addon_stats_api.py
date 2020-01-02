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
from api.addon_stats_api import AddonStatsApi  # noqa: E501
from gmodstore_sdk.rest import ApiException


class TestAddonStatsApi(unittest.TestCase):
    """AddonStatsApi unit test stubs"""

    def setUp(self):
        self.api = api.addon_stats_api.AddonStatsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_addons_addon_id_stats_get(self):
        """Test case for addons_addon_id_stats_get

        Fetch all the stats for an addon  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
