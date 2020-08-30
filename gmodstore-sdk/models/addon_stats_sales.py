# coding: utf-8

"""
    GmodStore API

    Welcome to the GmodStore API! You can use our API to access GmodStore API endpoints, which can be used interact with GmodStore programmatically.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gmodstore-sdk.configuration import Configuration


class AddonStatsSales(object):
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
        'current': 'AddonStatsSalesCurrent'
    }

    attribute_map = {
        'current': 'current'
    }

    def __init__(self, current=None, local_vars_configuration=None):  # noqa: E501
        """AddonStatsSales - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._current = None
        self.discriminator = None

        if current is not None:
            self.current = current

    @property
    def current(self):
        """Gets the current of this AddonStatsSales.  # noqa: E501


        :return: The current of this AddonStatsSales.  # noqa: E501
        :rtype: AddonStatsSalesCurrent
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this AddonStatsSales.


        :param current: The current of this AddonStatsSales.  # noqa: E501
        :type current: AddonStatsSalesCurrent
        """

        self._current = current

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
        if not isinstance(other, AddonStatsSales):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddonStatsSales):
            return True

        return self.to_dict() != other.to_dict()
