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


class AddonReview(object):
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
        'id': 'int',
        'title': 'str',
        'version': 'str',
        'body': 'str',
        'rating': 'float',
        'addon': 'Addon',
        'author': 'User'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'version': 'version',
        'body': 'body',
        'rating': 'rating',
        'addon': 'addon',
        'author': 'author'
    }

    def __init__(self, id=None, title=None, version=None, body=None, rating=None, addon=None, author=None):  # noqa: E501
        """AddonReview - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._title = None
        self._version = None
        self._body = None
        self._rating = None
        self._addon = None
        self._author = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if version is not None:
            self.version = version
        if body is not None:
            self.body = body
        if rating is not None:
            self.rating = rating
        if addon is not None:
            self.addon = addon
        if author is not None:
            self.author = author

    @property
    def id(self):
        """Gets the id of this AddonReview.  # noqa: E501


        :return: The id of this AddonReview.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AddonReview.


        :param id: The id of this AddonReview.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this AddonReview.  # noqa: E501


        :return: The title of this AddonReview.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AddonReview.


        :param title: The title of this AddonReview.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def version(self):
        """Gets the version of this AddonReview.  # noqa: E501


        :return: The version of this AddonReview.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AddonReview.


        :param version: The version of this AddonReview.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def body(self):
        """Gets the body of this AddonReview.  # noqa: E501


        :return: The body of this AddonReview.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this AddonReview.


        :param body: The body of this AddonReview.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def rating(self):
        """Gets the rating of this AddonReview.  # noqa: E501


        :return: The rating of this AddonReview.  # noqa: E501
        :rtype: float
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this AddonReview.


        :param rating: The rating of this AddonReview.  # noqa: E501
        :type: float
        """

        self._rating = rating

    @property
    def addon(self):
        """Gets the addon of this AddonReview.  # noqa: E501


        :return: The addon of this AddonReview.  # noqa: E501
        :rtype: Addon
        """
        return self._addon

    @addon.setter
    def addon(self, addon):
        """Sets the addon of this AddonReview.


        :param addon: The addon of this AddonReview.  # noqa: E501
        :type: Addon
        """

        self._addon = addon

    @property
    def author(self):
        """Gets the author of this AddonReview.  # noqa: E501


        :return: The author of this AddonReview.  # noqa: E501
        :rtype: User
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this AddonReview.


        :param author: The author of this AddonReview.  # noqa: E501
        :type: User
        """

        self._author = author

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
        if issubclass(AddonReview, dict):
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
        if not isinstance(other, AddonReview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
