# coding: utf-8

"""
    GmodStore

    Welcome to the Gmodstore API! You can use our API to access Gmodstore API endpoints, which can be used interact with Gmodstore programmatically.  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gmodstore-sdk.configuration import Configuration


class UserBan(object):
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
        'user_id': 'int',
        'reason': 'str',
        'unban_reason': 'str',
        'properties': 'list[str]',
        'start': 'datetime',
        'end': 'datetime'
    }

    attribute_map = {
        'user_id': 'user_id',
        'reason': 'reason',
        'unban_reason': 'unban_reason',
        'properties': 'properties',
        'start': 'start',
        'end': 'end'
    }

    def __init__(self, user_id=None, reason=None, unban_reason=None, properties=None, start=None, end=None, local_vars_configuration=None):  # noqa: E501
        """UserBan - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._reason = None
        self._unban_reason = None
        self._properties = None
        self._start = None
        self._end = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if reason is not None:
            self.reason = reason
        if unban_reason is not None:
            self.unban_reason = unban_reason
        if properties is not None:
            self.properties = properties
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end

    @property
    def user_id(self):
        """Gets the user_id of this UserBan.  # noqa: E501


        :return: The user_id of this UserBan.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserBan.


        :param user_id: The user_id of this UserBan.  # noqa: E501
        :type user_id: int
        """

        self._user_id = user_id

    @property
    def reason(self):
        """Gets the reason of this UserBan.  # noqa: E501


        :return: The reason of this UserBan.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this UserBan.


        :param reason: The reason of this UserBan.  # noqa: E501
        :type reason: str
        """

        self._reason = reason

    @property
    def unban_reason(self):
        """Gets the unban_reason of this UserBan.  # noqa: E501


        :return: The unban_reason of this UserBan.  # noqa: E501
        :rtype: str
        """
        return self._unban_reason

    @unban_reason.setter
    def unban_reason(self, unban_reason):
        """Sets the unban_reason of this UserBan.


        :param unban_reason: The unban_reason of this UserBan.  # noqa: E501
        :type unban_reason: str
        """

        self._unban_reason = unban_reason

    @property
    def properties(self):
        """Gets the properties of this UserBan.  # noqa: E501


        :return: The properties of this UserBan.  # noqa: E501
        :rtype: list[str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UserBan.


        :param properties: The properties of this UserBan.  # noqa: E501
        :type properties: list[str]
        """
        allowed_values = ["everything", "addon.create", "addon.purchase", "addon.download", "addon.review", "addon.comment", "job.create", "job.apply", "job.review", "job.comment", "ban.appeal"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(properties).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `properties` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(properties) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._properties = properties

    @property
    def start(self):
        """Gets the start of this UserBan.  # noqa: E501


        :return: The start of this UserBan.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this UserBan.


        :param start: The start of this UserBan.  # noqa: E501
        :type start: datetime
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this UserBan.  # noqa: E501


        :return: The end of this UserBan.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this UserBan.


        :param end: The end of this UserBan.  # noqa: E501
        :type end: datetime
        """

        self._end = end

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
        if not isinstance(other, UserBan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserBan):
            return True

        return self.to_dict() != other.to_dict()
