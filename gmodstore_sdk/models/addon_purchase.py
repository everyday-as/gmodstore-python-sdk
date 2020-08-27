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


class AddonPurchase(object):
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
        'revoked': 'bool',
        'created_at': 'datetime',
        'updated_at': 'int',
        'addon': 'Addon',
        'order_item': 'OrderItem',
        'user': 'User'
    }

    attribute_map = {
        'revoked': 'revoked',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'addon': 'addon',
        'order_item': 'order_item',
        'user': 'user'
    }

    def __init__(self, revoked=None, created_at=None, updated_at=None, addon=None, order_item=None, user=None):  # noqa: E501
        """AddonPurchase - a model defined in Swagger"""  # noqa: E501
        self._revoked = None
        self._created_at = None
        self._updated_at = None
        self._addon = None
        self._order_item = None
        self._user = None
        self.discriminator = None
        self.revoked = revoked
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if addon is not None:
            self.addon = addon
        if order_item is not None:
            self.order_item = order_item
        if user is not None:
            self.user = user

    @property
    def revoked(self):
        """Gets the revoked of this AddonPurchase.  # noqa: E501


        :return: The revoked of this AddonPurchase.  # noqa: E501
        :rtype: bool
        """
        return self._revoked

    @revoked.setter
    def revoked(self, revoked):
        """Sets the revoked of this AddonPurchase.


        :param revoked: The revoked of this AddonPurchase.  # noqa: E501
        :type: bool
        """
        if revoked is None:
            raise ValueError("Invalid value for `revoked`, must not be `None`")  # noqa: E501

        self._revoked = revoked

    @property
    def created_at(self):
        """Gets the created_at of this AddonPurchase.  # noqa: E501


        :return: The created_at of this AddonPurchase.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AddonPurchase.


        :param created_at: The created_at of this AddonPurchase.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AddonPurchase.  # noqa: E501


        :return: The updated_at of this AddonPurchase.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AddonPurchase.


        :param updated_at: The updated_at of this AddonPurchase.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

    @property
    def addon(self):
        """Gets the addon of this AddonPurchase.  # noqa: E501


        :return: The addon of this AddonPurchase.  # noqa: E501
        :rtype: Addon
        """
        return self._addon

    @addon.setter
    def addon(self, addon):
        """Sets the addon of this AddonPurchase.


        :param addon: The addon of this AddonPurchase.  # noqa: E501
        :type: Addon
        """

        self._addon = addon

    @property
    def order_item(self):
        """Gets the order_item of this AddonPurchase.  # noqa: E501


        :return: The order_item of this AddonPurchase.  # noqa: E501
        :rtype: OrderItem
        """
        return self._order_item

    @order_item.setter
    def order_item(self, order_item):
        """Sets the order_item of this AddonPurchase.


        :param order_item: The order_item of this AddonPurchase.  # noqa: E501
        :type: OrderItem
        """

        self._order_item = order_item

    @property
    def user(self):
        """Gets the user of this AddonPurchase.  # noqa: E501


        :return: The user of this AddonPurchase.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AddonPurchase.


        :param user: The user of this AddonPurchase.  # noqa: E501
        :type: User
        """

        self._user = user

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
        if issubclass(AddonPurchase, dict):
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
        if not isinstance(other, AddonPurchase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
