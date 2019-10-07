# coding: utf-8

"""
    TextMagic API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MuteChatInputObject(object):
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
        'mute': 'bool',
        '_for': 'int'
    }

    attribute_map = {
        'id': 'id',
        'mute': 'mute',
        '_for': 'for'
    }

    def __init__(self, id=None, mute=None, _for=None):  # noqa: E501
        """MuteChatInputObject - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._mute = None
        self.__for = None
        self.discriminator = None

        self.id = id
        self.mute = mute
        if _for is not None:
            self._for = _for

    @property
    def id(self):
        """Gets the id of this MuteChatInputObject.  # noqa: E501

        Chat ID  # noqa: E501

        :return: The id of this MuteChatInputObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MuteChatInputObject.

        Chat ID  # noqa: E501

        :param id: The id of this MuteChatInputObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def mute(self):
        """Gets the mute of this MuteChatInputObject.  # noqa: E501

        Mute value  # noqa: E501

        :return: The mute of this MuteChatInputObject.  # noqa: E501
        :rtype: bool
        """
        return self._mute

    @mute.setter
    def mute(self, mute):
        """Sets the mute of this MuteChatInputObject.

        Mute value  # noqa: E501

        :param mute: The mute of this MuteChatInputObject.  # noqa: E501
        :type: bool
        """

        self._mute = mute

    @property
    def _for(self):
        """Gets the _for of this MuteChatInputObject.  # noqa: E501

        Mute for N hours  # noqa: E501

        :return: The _for of this MuteChatInputObject.  # noqa: E501
        :rtype: int
        """
        return self.__for

    @_for.setter
    def _for(self, _for):
        """Sets the _for of this MuteChatInputObject.

        Mute for N hours  # noqa: E501

        :param _for: The _for of this MuteChatInputObject.  # noqa: E501
        :type: int
        """

        self.__for = _for

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
        if issubclass(MuteChatInputObject, dict):
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
        if not isinstance(other, MuteChatInputObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
