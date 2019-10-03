# coding: utf-8

"""
    TextMagic API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    Contact: support@textmagi.biz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateListInputObject(object):
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
        'name': 'str',
        'shared': 'bool',
        'favorited': 'bool',
        'is_default': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'shared': 'shared',
        'favorited': 'favorited',
        'is_default': 'isDefault'
    }

    def __init__(self, name=None, shared=False, favorited=False, is_default=False):  # noqa: E501
        """CreateListInputObject - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._shared = None
        self._favorited = None
        self._is_default = None
        self.discriminator = None

        self.name = name
        if shared is not None:
            self.shared = shared
        if favorited is not None:
            self.favorited = favorited
        if is_default is not None:
            self.is_default = is_default

    @property
    def name(self):
        """Gets the name of this CreateListInputObject.  # noqa: E501

        List name.  # noqa: E501

        :return: The name of this CreateListInputObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateListInputObject.

        List name.  # noqa: E501

        :param name: The name of this CreateListInputObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def shared(self):
        """Gets the shared of this CreateListInputObject.  # noqa: E501

        Should new list be shared among all the sub-accounts? The default is 0 (false).  # noqa: E501

        :return: The shared of this CreateListInputObject.  # noqa: E501
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this CreateListInputObject.

        Should new list be shared among all the sub-accounts? The default is 0 (false).  # noqa: E501

        :param shared: The shared of this CreateListInputObject.  # noqa: E501
        :type: bool
        """

        self._shared = shared

    @property
    def favorited(self):
        """Gets the favorited of this CreateListInputObject.  # noqa: E501

        Is list favorited. Default is false.  # noqa: E501

        :return: The favorited of this CreateListInputObject.  # noqa: E501
        :rtype: bool
        """
        return self._favorited

    @favorited.setter
    def favorited(self, favorited):
        """Sets the favorited of this CreateListInputObject.

        Is list favorited. Default is false.  # noqa: E501

        :param favorited: The favorited of this CreateListInputObject.  # noqa: E501
        :type: bool
        """

        self._favorited = favorited

    @property
    def is_default(self):
        """Gets the is_default of this CreateListInputObject.  # noqa: E501

        Is list default for new contacts (web only). Default is false.  # noqa: E501

        :return: The is_default of this CreateListInputObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this CreateListInputObject.

        Is list default for new contacts (web only). Default is false.  # noqa: E501

        :param is_default: The is_default of this CreateListInputObject.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

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
        if issubclass(CreateListInputObject, dict):
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
        if not isinstance(other, CreateListInputObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
