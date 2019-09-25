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


class MessagesIcsTextParameters(object):
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
        'cost': 'float',
        'parts': 'int',
        'chars': 'int',
        'encoding': 'str',
        'countries': 'list[str]',
        'charset_label': 'str'
    }

    attribute_map = {
        'cost': 'cost',
        'parts': 'parts',
        'chars': 'chars',
        'encoding': 'encoding',
        'countries': 'countries',
        'charset_label': 'charsetLabel'
    }

    def __init__(self, cost=None, parts=None, chars=None, encoding=None, countries=None, charset_label=None):  # noqa: E501
        """MessagesIcsTextParameters - a model defined in Swagger"""  # noqa: E501

        self._cost = None
        self._parts = None
        self._chars = None
        self._encoding = None
        self._countries = None
        self._charset_label = None
        self.discriminator = None

        self.cost = cost
        self.parts = parts
        self.chars = chars
        self.encoding = encoding
        self.countries = countries
        self.charset_label = charset_label

    @property
    def cost(self):
        """Gets the cost of this MessagesIcsTextParameters.  # noqa: E501


        :return: The cost of this MessagesIcsTextParameters.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this MessagesIcsTextParameters.


        :param cost: The cost of this MessagesIcsTextParameters.  # noqa: E501
        :type: float
        """

        self._cost = cost

    @property
    def parts(self):
        """Gets the parts of this MessagesIcsTextParameters.  # noqa: E501


        :return: The parts of this MessagesIcsTextParameters.  # noqa: E501
        :rtype: int
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this MessagesIcsTextParameters.


        :param parts: The parts of this MessagesIcsTextParameters.  # noqa: E501
        :type: int
        """

        self._parts = parts

    @property
    def chars(self):
        """Gets the chars of this MessagesIcsTextParameters.  # noqa: E501


        :return: The chars of this MessagesIcsTextParameters.  # noqa: E501
        :rtype: int
        """
        return self._chars

    @chars.setter
    def chars(self, chars):
        """Sets the chars of this MessagesIcsTextParameters.


        :param chars: The chars of this MessagesIcsTextParameters.  # noqa: E501
        :type: int
        """

        self._chars = chars

    @property
    def encoding(self):
        """Gets the encoding of this MessagesIcsTextParameters.  # noqa: E501


        :return: The encoding of this MessagesIcsTextParameters.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this MessagesIcsTextParameters.


        :param encoding: The encoding of this MessagesIcsTextParameters.  # noqa: E501
        :type: str
        """

        self._encoding = encoding

    @property
    def countries(self):
        """Gets the countries of this MessagesIcsTextParameters.  # noqa: E501


        :return: The countries of this MessagesIcsTextParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this MessagesIcsTextParameters.


        :param countries: The countries of this MessagesIcsTextParameters.  # noqa: E501
        :type: list[str]
        """

        self._countries = countries

    @property
    def charset_label(self):
        """Gets the charset_label of this MessagesIcsTextParameters.  # noqa: E501


        :return: The charset_label of this MessagesIcsTextParameters.  # noqa: E501
        :rtype: str
        """
        return self._charset_label

    @charset_label.setter
    def charset_label(self, charset_label):
        """Sets the charset_label of this MessagesIcsTextParameters.


        :param charset_label: The charset_label of this MessagesIcsTextParameters.  # noqa: E501
        :type: str
        """

        self._charset_label = charset_label

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
        if issubclass(MessagesIcsTextParameters, dict):
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
        if not isinstance(other, MessagesIcsTextParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
