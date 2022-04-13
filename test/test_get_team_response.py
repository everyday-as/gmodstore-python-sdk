"""
    gmodstore

    Welcome to the GmodStore API! You can use our API to access GmodStore API endpoints, which can be used interact with GmodStore programmatically.  # Rate limits Every request you make to the GmodStore API will count against your rate limit, which at the time of writing this, is 60 requests / minute. An up-to-date value will always provided in the `X-RateLimit-Limit` header The number of requests you have remaining before you must wait is provided in the `X-RateLimit-Remaining` header.  # API SDKs For a list of available API SDKs check the README here: https://github.com/everyday-as/gmodstore-api-docs#client-libraries  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import gmodstore-sdk
from gmodstore-sdk.model.team import Team
globals()['Team'] = Team
from gmodstore-sdk.model.get_team_response import GetTeamResponse


class TestGetTeamResponse(unittest.TestCase):
    """GetTeamResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetTeamResponse(self):
        """Test GetTeamResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GetTeamResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
