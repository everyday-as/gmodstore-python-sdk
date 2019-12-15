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
from api.team_users_api import TeamUsersApi  # noqa: E501
from gmodstore_sdk.rest import ApiException


class TestTeamUsersApi(unittest.TestCase):
    """TeamUsersApi unit test stubs"""

    def setUp(self):
        self.api = api.team_users_api.TeamUsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_teams_team_id_users_get(self):
        """Test case for teams_team_id_users_get

        Fetch all the users in the given team  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()