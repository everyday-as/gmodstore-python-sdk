# coding: utf-8

"""
    GmodStore API

    Welcome to the GmodStore API! You can use our API to access GmodStore API endpoints, which can be used interact with GmodStore programmatically.  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gmodstore-sdk.configuration import Configuration


class User(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'name': 'str',
        'avatar': 'str',
        'country_code': 'str',
        'slug': 'str',
        'reputation': 'int',
        'team_reputation': 'int',
        'ban_properties': 'list[str]',
        'group': 'PermissionGroup'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'avatar': 'avatar',
        'country_code': 'country_code',
        'slug': 'slug',
        'reputation': 'reputation',
        'team_reputation': 'team_reputation',
        'ban_properties': 'ban_properties',
        'group': 'group'
    }

    def __init__(self, id=None, name=None, avatar=None, country_code=None, slug=None, reputation=None, team_reputation=None, ban_properties=None, group=None, local_vars_configuration=None):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._avatar = None
        self._country_code = None
        self._slug = None
        self._reputation = None
        self._team_reputation = None
        self._ban_properties = None
        self._group = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if avatar is not None:
            self.avatar = avatar
        if country_code is not None:
            self.country_code = country_code
        if slug is not None:
            self.slug = slug
        if reputation is not None:
            self.reputation = reputation
        if team_reputation is not None:
            self.team_reputation = team_reputation
        if ban_properties is not None:
            self.ban_properties = ban_properties
        if group is not None:
            self.group = group

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501


        :return: The name of this User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.


        :param name: The name of this User.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def avatar(self):
        """Gets the avatar of this User.  # noqa: E501


        :return: The avatar of this User.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this User.


        :param avatar: The avatar of this User.  # noqa: E501
        :type avatar: str
        """

        self._avatar = avatar

    @property
    def country_code(self):
        """Gets the country_code of this User.  # noqa: E501


        :return: The country_code of this User.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this User.


        :param country_code: The country_code of this User.  # noqa: E501
        :type country_code: str
        """

        self._country_code = country_code

    @property
    def slug(self):
        """Gets the slug of this User.  # noqa: E501


        :return: The slug of this User.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this User.


        :param slug: The slug of this User.  # noqa: E501
        :type slug: str
        """

        self._slug = slug

    @property
    def reputation(self):
        """Gets the reputation of this User.  # noqa: E501


        :return: The reputation of this User.  # noqa: E501
        :rtype: int
        """
        return self._reputation

    @reputation.setter
    def reputation(self, reputation):
        """Sets the reputation of this User.


        :param reputation: The reputation of this User.  # noqa: E501
        :type reputation: int
        """

        self._reputation = reputation

    @property
    def team_reputation(self):
        """Gets the team_reputation of this User.  # noqa: E501


        :return: The team_reputation of this User.  # noqa: E501
        :rtype: int
        """
        return self._team_reputation

    @team_reputation.setter
    def team_reputation(self, team_reputation):
        """Sets the team_reputation of this User.


        :param team_reputation: The team_reputation of this User.  # noqa: E501
        :type team_reputation: int
        """

        self._team_reputation = team_reputation

    @property
    def ban_properties(self):
        """Gets the ban_properties of this User.  # noqa: E501


        :return: The ban_properties of this User.  # noqa: E501
        :rtype: list[str]
        """
        return self._ban_properties

    @ban_properties.setter
    def ban_properties(self, ban_properties):
        """Sets the ban_properties of this User.


        :param ban_properties: The ban_properties of this User.  # noqa: E501
        :type ban_properties: list[str]
        """
        allowed_values = ["everything", "addon.create", "addon.purchase", "addon.download", "addon.review", "addon.comment", "job.create", "job.apply", "job.review", "job.comment", "ban.appeal"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(ban_properties).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `ban_properties` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(ban_properties) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._ban_properties = ban_properties

    @property
    def group(self):
        """Gets the group of this User.  # noqa: E501


        :return: The group of this User.  # noqa: E501
        :rtype: PermissionGroup
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this User.


        :param group: The group of this User.  # noqa: E501
        :type group: PermissionGroup
        """

        self._group = group

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()
