
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.addon_coupons_api import AddonCouponsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from gmodstore-sdk.api.addon_coupons_api import AddonCouponsApi
from gmodstore-sdk.api.addon_purchases_api import AddonPurchasesApi
from gmodstore-sdk.api.addon_reviews_api import AddonReviewsApi
from gmodstore-sdk.api.addon_stats_api import AddonStatsApi
from gmodstore-sdk.api.addon_versions_api import AddonVersionsApi
from gmodstore-sdk.api.addons_api import AddonsApi
from gmodstore-sdk.api.advent_calendar_api import AdventCalendarApi
from gmodstore-sdk.api.current_api_key_api import CurrentAPIKeyApi
from gmodstore-sdk.api.permission_groups_api import PermissionGroupsApi
from gmodstore-sdk.api.team_addons_api import TeamAddonsApi
from gmodstore-sdk.api.team_users_api import TeamUsersApi
from gmodstore-sdk.api.teams_api import TeamsApi
from gmodstore-sdk.api.user_addons_api import UserAddonsApi
from gmodstore-sdk.api.user_badges_api import UserBadgesApi
from gmodstore-sdk.api.user_bans_api import UserBansApi
from gmodstore-sdk.api.user_purchases_api import UserPurchasesApi
from gmodstore-sdk.api.user_teams_api import UserTeamsApi
from gmodstore-sdk.api.users_api import UsersApi
