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


class AddonCoupon(object):
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
        'code': 'str',
        'percent': 'float',
        'max_uses': 'int',
        'expires_at': 'datetime',
        'bound_user_id': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'addon': 'Addon',
        'bound_user': 'User'
    }

    attribute_map = {
        'id': 'id',
        'code': 'code',
        'percent': 'percent',
        'max_uses': 'max_uses',
        'expires_at': 'expires_at',
        'bound_user_id': 'bound_user_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'addon': 'addon',
        'bound_user': 'bound_user'
    }

    def __init__(self, id=None, code=None, percent=None, max_uses=None, expires_at=None, bound_user_id=None, created_at=None, updated_at=None, addon=None, bound_user=None, local_vars_configuration=None):  # noqa: E501
        """AddonCoupon - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._code = None
        self._percent = None
        self._max_uses = None
        self._expires_at = None
        self._bound_user_id = None
        self._created_at = None
        self._updated_at = None
        self._addon = None
        self._bound_user = None
        self.discriminator = None

        self.id = id
        self.code = code
        self.percent = percent
        self.max_uses = max_uses
        self.expires_at = expires_at
        self.bound_user_id = bound_user_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if addon is not None:
            self.addon = addon
        if bound_user is not None:
            self.bound_user = bound_user

    @property
    def id(self):
        """Gets the id of this AddonCoupon.  # noqa: E501


        :return: The id of this AddonCoupon.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AddonCoupon.


        :param id: The id of this AddonCoupon.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and id < 1):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def code(self):
        """Gets the code of this AddonCoupon.  # noqa: E501


        :return: The code of this AddonCoupon.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AddonCoupon.


        :param code: The code of this AddonCoupon.  # noqa: E501
        :type code: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def percent(self):
        """Gets the percent of this AddonCoupon.  # noqa: E501


        :return: The percent of this AddonCoupon.  # noqa: E501
        :rtype: float
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        """Sets the percent of this AddonCoupon.


        :param percent: The percent of this AddonCoupon.  # noqa: E501
        :type percent: float
        """
        if self.local_vars_configuration.client_side_validation and percent is None:  # noqa: E501
            raise ValueError("Invalid value for `percent`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                percent is not None and percent > 99):  # noqa: E501
            raise ValueError("Invalid value for `percent`, must be a value less than or equal to `99`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                percent is not None and percent < 1):  # noqa: E501
            raise ValueError("Invalid value for `percent`, must be a value greater than or equal to `1`")  # noqa: E501

        self._percent = percent

    @property
    def max_uses(self):
        """Gets the max_uses of this AddonCoupon.  # noqa: E501


        :return: The max_uses of this AddonCoupon.  # noqa: E501
        :rtype: int
        """
        return self._max_uses

    @max_uses.setter
    def max_uses(self, max_uses):
        """Sets the max_uses of this AddonCoupon.


        :param max_uses: The max_uses of this AddonCoupon.  # noqa: E501
        :type max_uses: int
        """
        if self.local_vars_configuration.client_side_validation and max_uses is None:  # noqa: E501
            raise ValueError("Invalid value for `max_uses`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_uses is not None and max_uses < 1):  # noqa: E501
            raise ValueError("Invalid value for `max_uses`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_uses = max_uses

    @property
    def expires_at(self):
        """Gets the expires_at of this AddonCoupon.  # noqa: E501

        A future date less than 2 weeks from today  # noqa: E501

        :return: The expires_at of this AddonCoupon.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this AddonCoupon.

        A future date less than 2 weeks from today  # noqa: E501

        :param expires_at: The expires_at of this AddonCoupon.  # noqa: E501
        :type expires_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and expires_at is None:  # noqa: E501
            raise ValueError("Invalid value for `expires_at`, must not be `None`")  # noqa: E501

        self._expires_at = expires_at

    @property
    def bound_user_id(self):
        """Gets the bound_user_id of this AddonCoupon.  # noqa: E501


        :return: The bound_user_id of this AddonCoupon.  # noqa: E501
        :rtype: int
        """
        return self._bound_user_id

    @bound_user_id.setter
    def bound_user_id(self, bound_user_id):
        """Sets the bound_user_id of this AddonCoupon.


        :param bound_user_id: The bound_user_id of this AddonCoupon.  # noqa: E501
        :type bound_user_id: int
        """

        self._bound_user_id = bound_user_id

    @property
    def created_at(self):
        """Gets the created_at of this AddonCoupon.  # noqa: E501


        :return: The created_at of this AddonCoupon.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AddonCoupon.


        :param created_at: The created_at of this AddonCoupon.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AddonCoupon.  # noqa: E501


        :return: The updated_at of this AddonCoupon.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AddonCoupon.


        :param updated_at: The updated_at of this AddonCoupon.  # noqa: E501
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def addon(self):
        """Gets the addon of this AddonCoupon.  # noqa: E501


        :return: The addon of this AddonCoupon.  # noqa: E501
        :rtype: Addon
        """
        return self._addon

    @addon.setter
    def addon(self, addon):
        """Sets the addon of this AddonCoupon.


        :param addon: The addon of this AddonCoupon.  # noqa: E501
        :type addon: Addon
        """

        self._addon = addon

    @property
    def bound_user(self):
        """Gets the bound_user of this AddonCoupon.  # noqa: E501


        :return: The bound_user of this AddonCoupon.  # noqa: E501
        :rtype: User
        """
        return self._bound_user

    @bound_user.setter
    def bound_user(self, bound_user):
        """Sets the bound_user of this AddonCoupon.


        :param bound_user: The bound_user of this AddonCoupon.  # noqa: E501
        :type bound_user: User
        """

        self._bound_user = bound_user

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
        if not isinstance(other, AddonCoupon):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddonCoupon):
            return True

        return self.to_dict() != other.to_dict()
