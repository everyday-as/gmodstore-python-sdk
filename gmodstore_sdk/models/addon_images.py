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


class AddonImages(object):
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
        'bigspot': 'str',
        'listing': 'str',
        'listing_small': 'str'
    }

    attribute_map = {
        'bigspot': 'bigspot',
        'listing': 'listing',
        'listing_small': 'listing_small'
    }

    def __init__(self, bigspot=None, listing=None, listing_small=None):  # noqa: E501
        """AddonImages - a model defined in Swagger"""  # noqa: E501
        self._bigspot = None
        self._listing = None
        self._listing_small = None
        self.discriminator = None
        if bigspot is not None:
            self.bigspot = bigspot
        if listing is not None:
            self.listing = listing
        if listing_small is not None:
            self.listing_small = listing_small

    @property
    def bigspot(self):
        """Gets the bigspot of this AddonImages.  # noqa: E501


        :return: The bigspot of this AddonImages.  # noqa: E501
        :rtype: str
        """
        return self._bigspot

    @bigspot.setter
    def bigspot(self, bigspot):
        """Sets the bigspot of this AddonImages.


        :param bigspot: The bigspot of this AddonImages.  # noqa: E501
        :type: str
        """

        self._bigspot = bigspot

    @property
    def listing(self):
        """Gets the listing of this AddonImages.  # noqa: E501


        :return: The listing of this AddonImages.  # noqa: E501
        :rtype: str
        """
        return self._listing

    @listing.setter
    def listing(self, listing):
        """Sets the listing of this AddonImages.


        :param listing: The listing of this AddonImages.  # noqa: E501
        :type: str
        """

        self._listing = listing

    @property
    def listing_small(self):
        """Gets the listing_small of this AddonImages.  # noqa: E501


        :return: The listing_small of this AddonImages.  # noqa: E501
        :rtype: str
        """
        return self._listing_small

    @listing_small.setter
    def listing_small(self, listing_small):
        """Sets the listing_small of this AddonImages.


        :param listing_small: The listing_small of this AddonImages.  # noqa: E501
        :type: str
        """

        self._listing_small = listing_small

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
        if issubclass(AddonImages, dict):
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
        if not isinstance(other, AddonImages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
