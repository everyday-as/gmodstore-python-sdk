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


class AddonStatsViewsCurrent(object):
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
        'day': 'int',
        'month': 'int'
    }

    attribute_map = {
        'day': 'day',
        'month': 'month'
    }

    def __init__(self, day=None, month=None, local_vars_configuration=None):  # noqa: E501
        """AddonStatsViewsCurrent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._day = None
        self._month = None
        self.discriminator = None

        if day is not None:
            self.day = day
        if month is not None:
            self.month = month

    @property
    def day(self):
        """Gets the day of this AddonStatsViewsCurrent.  # noqa: E501


        :return: The day of this AddonStatsViewsCurrent.  # noqa: E501
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this AddonStatsViewsCurrent.


        :param day: The day of this AddonStatsViewsCurrent.  # noqa: E501
        :type day: int
        """

        self._day = day

    @property
    def month(self):
        """Gets the month of this AddonStatsViewsCurrent.  # noqa: E501


        :return: The month of this AddonStatsViewsCurrent.  # noqa: E501
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this AddonStatsViewsCurrent.


        :param month: The month of this AddonStatsViewsCurrent.  # noqa: E501
        :type month: int
        """

        self._month = month

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
        if not isinstance(other, AddonStatsViewsCurrent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddonStatsViewsCurrent):
            return True

        return self.to_dict() != other.to_dict()
