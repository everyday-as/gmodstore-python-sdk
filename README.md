# GmodStore SDK
Welcome to the GmodStore API! You can use our API to access GmodStore API endpoints, which can be used interact with GmodStore programmatically.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.1.0
- Package version: 1.1.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://docs.gmodstore.com](https://docs.gmodstore.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/everyday-as/gmodstore-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/everyday-as/gmodstore-python-sdk.git`)

Then import the package:
```python
import gmodstore-sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gmodstore-sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import gmodstore-sdk
from gmodstore-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gmodstore.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = gmodstore-sdk.Configuration(
    host = "https://api.gmodstore.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = gmodstore-sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)


# Enter a context with an instance of the API client
with gmodstore-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gmodstore-sdk.AddonCouponsApi(api_client)
    addon_id = 56 # int | Id of the addon
addon_coupon = gmodstore-sdk.AddonCoupon() # AddonCoupon | 
_with = ['_with_example'] # list[str] | The relations you want to fetch with the `AddonCoupon` (optional)

    try:
        # Create an addon coupon
        api_response = api_instance.create_addon_coupon(addon_id, addon_coupon, _with=_with)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddonCouponsApi->create_addon_coupon: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://api.gmodstore.com/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AddonCouponsApi* | [**create_addon_coupon**](docs/AddonCouponsApi.md#create_addon_coupon) | **POST** /addons/{addon_id}/coupons | Create an addon coupon
*AddonCouponsApi* | [**delete_addon_coupon**](docs/AddonCouponsApi.md#delete_addon_coupon) | **DELETE** /addons/{addon_id}/coupons/{coupon_id} | Destroy an addon&#39;s coupon
*AddonCouponsApi* | [**get_addon_coupon**](docs/AddonCouponsApi.md#get_addon_coupon) | **GET** /addons/{addon_id}/coupons/{coupon_id} | Fetch an addon&#39;s coupon
*AddonCouponsApi* | [**list_addon_coupons**](docs/AddonCouponsApi.md#list_addon_coupons) | **GET** /addons/{addon_id}/coupons | Fetch all the coupons for an addon
*AddonCouponsApi* | [**update_addon_coupon**](docs/AddonCouponsApi.md#update_addon_coupon) | **PUT** /addons/{addon_id}/coupons/{coupon_id} | Update an addon&#39;s coupon
*AddonPurchasesApi* | [**create_addon_purchase**](docs/AddonPurchasesApi.md#create_addon_purchase) | **POST** /addons/{addon_id}/purchases | Create a purchase for an addon
*AddonPurchasesApi* | [**get_addon_purchase**](docs/AddonPurchasesApi.md#get_addon_purchase) | **GET** /addons/{addon_id}/purchases/{user_id} | Get a purchase of an addon by user
*AddonPurchasesApi* | [**list_addon_purchases**](docs/AddonPurchasesApi.md#list_addon_purchases) | **GET** /addons/{addon_id}/purchases | Fetch all purchases of an addon
*AddonPurchasesApi* | [**update_addon_purchase**](docs/AddonPurchasesApi.md#update_addon_purchase) | **PUT** /addons/{addon_id}/purchases/{user_id} | Update a purchase for an addon
*AddonReviewsApi* | [**get_addon_review**](docs/AddonReviewsApi.md#get_addon_review) | **GET** /addons/{addon_id}/reviews/{review_id} | Fetch a review of an addon
*AddonReviewsApi* | [**list_addon_reviews**](docs/AddonReviewsApi.md#list_addon_reviews) | **GET** /addons/{addon_id}/reviews | Fetch all the reviews of an addon
*AddonStatsApi* | [**get_addon_stats**](docs/AddonStatsApi.md#get_addon_stats) | **GET** /addons/{addon_id}/stats | Fetch all the stats for an addon
*AddonVersionsApi* | [**create_addon_version**](docs/AddonVersionsApi.md#create_addon_version) | **POST** /addons/{addon_id}/versions | Create a new version for an addon
*AddonVersionsApi* | [**download_addon_version**](docs/AddonVersionsApi.md#download_addon_version) | **GET** /addons/{addon_id}/versions/{version_id}/download | Generate a download token for a specific version of an addon
*AddonVersionsApi* | [**get_addon_version**](docs/AddonVersionsApi.md#get_addon_version) | **GET** /addons/{addon_id}/versions/{version_id} | Fetch a specific version of an addon
*AddonVersionsApi* | [**list_addon_versions**](docs/AddonVersionsApi.md#list_addon_versions) | **GET** /addons/{addon_id}/versions | Fetch all the versions of an addon
*AddonVersionsApi* | [**update_addon_version**](docs/AddonVersionsApi.md#update_addon_version) | **PUT** /addons/{addon_id}/versions/{version_id} | Update a version of an addon
*AddonsApi* | [**get_addon**](docs/AddonsApi.md#get_addon) | **GET** /addons/{addon_id} | Fetch a single addon
*AddonsApi* | [**list_self_addons**](docs/AddonsApi.md#list_self_addons) | **GET** /addons | Fetch all the addons that you have access to
*AdventCalendarApi* | [**get_advent_calendar_stats**](docs/AdventCalendarApi.md#get_advent_calendar_stats) | **GET** /events/advent-calendar/stats | Fetch statistics relating to the advent calendar event
*PermissionGroupsApi* | [**list_permission_groups**](docs/PermissionGroupsApi.md#list_permission_groups) | **GET** /permission-groups | Fetches all available permission groups
*TeamAddonsApi* | [**list_team_addons**](docs/TeamAddonsApi.md#list_team_addons) | **GET** /teams/{team_id}/addons | Fetch all the addons in the given team
*TeamUsersApi* | [**list_team_users**](docs/TeamUsersApi.md#list_team_users) | **GET** /teams/{team_id}/users | Fetch all the users in the given team
*TeamsApi* | [**get_team**](docs/TeamsApi.md#get_team) | **GET** /teams/{team_id} | Fetch a single team
*UserAddonsApi* | [**list_user_addons**](docs/UserAddonsApi.md#list_user_addons) | **GET** /users/{user_id}/addons | Fetch all the addons authored / co-authored by a user
*UserBadgesApi* | [**create_user_badge**](docs/UserBadgesApi.md#create_user_badge) | **POST** /users/{user_id}/badges | Give a user a badge
*UserBadgesApi* | [**delete_user_badge**](docs/UserBadgesApi.md#delete_user_badge) | **DELETE** /users/{user_id}/badges/{badge_id} | Destroy a users&#39;s badge
*UserBadgesApi* | [**list_user_badges**](docs/UserBadgesApi.md#list_user_badges) | **GET** /users/{user_id}/badges | Fetch all the badges a user has
*UserBansApi* | [**list_user_bans**](docs/UserBansApi.md#list_user_bans) | **GET** /users/{user_id}/bans | Fetch all active bans associated with this user
*UserPurchasesApi* | [**list_user_purchases**](docs/UserPurchasesApi.md#list_user_purchases) | **GET** /users/{user_id}/purchases | Fetch all purchases a user has made
*UserTeamsApi* | [**list_user_teams**](docs/UserTeamsApi.md#list_user_teams) | **GET** /users/{user_id}/teams | Fetch all the teams of a user
*UsersApi* | [**get_self_user**](docs/UsersApi.md#get_self_user) | **GET** /users/me | Fetches the current user (API Key Owner)
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /users/{user_id} | Fetch a single user


## Documentation For Models

 - [Addon](docs/Addon.md)
 - [AddonCoupon](docs/AddonCoupon.md)
 - [AddonCouponListResponse](docs/AddonCouponListResponse.md)
 - [AddonCouponResponse](docs/AddonCouponResponse.md)
 - [AddonDownload](docs/AddonDownload.md)
 - [AddonDownloadResponse](docs/AddonDownloadResponse.md)
 - [AddonImages](docs/AddonImages.md)
 - [AddonListResponse](docs/AddonListResponse.md)
 - [AddonPrice](docs/AddonPrice.md)
 - [AddonPurchase](docs/AddonPurchase.md)
 - [AddonPurchaseListResponse](docs/AddonPurchaseListResponse.md)
 - [AddonPurchaseResponse](docs/AddonPurchaseResponse.md)
 - [AddonResponse](docs/AddonResponse.md)
 - [AddonReview](docs/AddonReview.md)
 - [AddonReviewListResponse](docs/AddonReviewListResponse.md)
 - [AddonReviewResponse](docs/AddonReviewResponse.md)
 - [AddonStats](docs/AddonStats.md)
 - [AddonStatsListResponse](docs/AddonStatsListResponse.md)
 - [AddonStatsRevenue](docs/AddonStatsRevenue.md)
 - [AddonStatsRevenueCurrent](docs/AddonStatsRevenueCurrent.md)
 - [AddonStatsSales](docs/AddonStatsSales.md)
 - [AddonStatsSalesCurrent](docs/AddonStatsSalesCurrent.md)
 - [AddonStatsViews](docs/AddonStatsViews.md)
 - [AddonStatsViewsCurrent](docs/AddonStatsViewsCurrent.md)
 - [AddonVersion](docs/AddonVersion.md)
 - [AddonVersionListResponse](docs/AddonVersionListResponse.md)
 - [AddonVersionReleaseType](docs/AddonVersionReleaseType.md)
 - [AddonVersionResponse](docs/AddonVersionResponse.md)
 - [AdventCalendarStats](docs/AdventCalendarStats.md)
 - [AdventCalendarStatsResponse](docs/AdventCalendarStatsResponse.md)
 - [BadgeListResponse](docs/BadgeListResponse.md)
 - [BadgeResponse](docs/BadgeResponse.md)
 - [Error](docs/Error.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Money](docs/Money.md)
 - [NewAddonPurchase](docs/NewAddonPurchase.md)
 - [NewAddonVersion](docs/NewAddonVersion.md)
 - [OrderItem](docs/OrderItem.md)
 - [PermissionGroup](docs/PermissionGroup.md)
 - [PermissionGroupListResponse](docs/PermissionGroupListResponse.md)
 - [Team](docs/Team.md)
 - [TeamListResponse](docs/TeamListResponse.md)
 - [TeamResponse](docs/TeamResponse.md)
 - [TeamUser](docs/TeamUser.md)
 - [TeamUserListResponse](docs/TeamUserListResponse.md)
 - [User](docs/User.md)
 - [UserBadge](docs/UserBadge.md)
 - [UserBadgeLegend](docs/UserBadgeLegend.md)
 - [UserBan](docs/UserBan.md)
 - [UserBanListResponse](docs/UserBanListResponse.md)
 - [UserResponse](docs/UserResponse.md)


## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication (API Key)


## Author




