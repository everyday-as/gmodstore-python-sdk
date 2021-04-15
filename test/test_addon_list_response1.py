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
from gmodstore-sdk.models.addon_list_response1 import AddonListResponse1  # noqa: E501
from gmodstore-sdk.rest import ApiException

class TestAddonListResponse1(unittest.TestCase):
    """AddonListResponse1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddonListResponse1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = gmodstore-sdk.models.addon_list_response1.AddonListResponse1()  # noqa: E501
        if include_optional :
            return AddonListResponse1(
                data = [
                    gmodstore-sdk.models.addon.Addon(
                        id = 56, 
                        active = True, 
                        name = '0', 
                        short_description = '0', 
                        description = '0', 
                        requirements = [
                            '0'
                            ], 
                        price = gmodstore-sdk.models.addon_price.Addon_price(
                            original = gmodstore-sdk.models.money.Money(
                                amount = '0', 
                                currency = '0', ), 
                            purchase = gmodstore-sdk.models.money.Money(
                                amount = '0', 
                                currency = '0', ), ), 
                        images = gmodstore-sdk.models.addon_images.Addon_images(
                            bigspot = '0', 
                            listing = '0', 
                            listing_small = '0', ), 
                        slug = '0', 
                        route = '0', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        latest_version = gmodstore-sdk.models.addon_version.AddonVersion(
                            id = 56, 
                            name = '0', 
                            changelog = '0', 
                            file_hash = '0', 
                            file_size = 56, 
                            release_type = 'stable', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            addon = gmodstore-sdk.models.addon.Addon(
                                id = 56, 
                                active = True, 
                                name = '0', 
                                short_description = '0', 
                                description = '0', 
                                slug = '0', 
                                route = '0', 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                team = gmodstore-sdk.models.team.Team(
                                    id = 56, 
                                    name = '0', 
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    primary_author = gmodstore-sdk.models.team_user.TeamUser(
                                        team_id = 56, 
                                        primary = True, 
                                        percentage = 56, 
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
                                                display_order = 56, ), ), ), ), ), ), 
                        team = gmodstore-sdk.models.team.Team(
                            id = 56, 
                            name = '0', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
                    ]
            )
        else :
            return AddonListResponse1(
        )

    def testAddonListResponse1(self):
        """Test AddonListResponse1"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()