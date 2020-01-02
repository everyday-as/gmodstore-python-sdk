# coding: utf-8

"""
    GmodStore

    Welcome to the Gmodstore API! You can use our API to access Gmodstore API endpoints, which can be used interact with Gmodstore programmatically.  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AddonStatsSalesCurrent(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'day': 'str',
        'week': 'str',
        'month': 'str'
    }

    attribute_map = {
        'day': 'day',
        'week': 'week',
        'month': 'month'
    }

    def __init__(self, day=None, week=None, month=None):  # noqa: E501
        """AddonStatsSalesCurrent - a model defined in Swagger"""  # noqa: E501
        self._day = None
        self._week = None
        self._month = None
        self.discriminator = None
        if day is not None:
            self.day = day
        if week is not None:
            self.week = week
        if month is not None:
            self.month = month

    @property
    def day(self):
        """Gets the day of this AddonStatsSalesCurrent.  # noqa: E501


        :return: The day of this AddonStatsSalesCurrent.  # noqa: E501
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this AddonStatsSalesCurrent.


        :param day: The day of this AddonStatsSalesCurrent.  # noqa: E501
        :type: str
        """

        self._day = day

    @property
    def week(self):
        """Gets the week of this AddonStatsSalesCurrent.  # noqa: E501


        :return: The week of this AddonStatsSalesCurrent.  # noqa: E501
        :rtype: str
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this AddonStatsSalesCurrent.


        :param week: The week of this AddonStatsSalesCurrent.  # noqa: E501
        :type: str
        """

        self._week = week

    @property
    def month(self):
        """Gets the month of this AddonStatsSalesCurrent.  # noqa: E501


        :return: The month of this AddonStatsSalesCurrent.  # noqa: E501
        :rtype: str
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this AddonStatsSalesCurrent.


        :param month: The month of this AddonStatsSalesCurrent.  # noqa: E501
        :type: str
        """

        self._month = month

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(AddonStatsSalesCurrent, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddonStatsSalesCurrent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other