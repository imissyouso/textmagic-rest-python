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


class RequestSenderIdInputObject(object):
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
        'sender_id': 'str',
        'explanation': 'str'
    }

    attribute_map = {
        'sender_id': 'senderId',
        'explanation': 'explanation'
    }

    def __init__(self, sender_id=None, explanation=None):  # noqa: E501
        """RequestSenderIdInputObject - a model defined in Swagger"""  # noqa: E501

        self._sender_id = None
        self._explanation = None
        self.discriminator = None

        self.sender_id = sender_id
        self.explanation = explanation

    @property
    def sender_id(self):
        """Gets the sender_id of this RequestSenderIdInputObject.  # noqa: E501

        Sender ID that you are applying for. *   11 characters maximum *   Only Latin based characters and digits are allowed *   Should contain at least one letter   # noqa: E501

        :return: The sender_id of this RequestSenderIdInputObject.  # noqa: E501
        :rtype: str
        """
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        """Sets the sender_id of this RequestSenderIdInputObject.

        Sender ID that you are applying for. *   11 characters maximum *   Only Latin based characters and digits are allowed *   Should contain at least one letter   # noqa: E501

        :param sender_id: The sender_id of this RequestSenderIdInputObject.  # noqa: E501
        :type: str
        """

        self._sender_id = sender_id

    @property
    def explanation(self):
        """Gets the explanation of this RequestSenderIdInputObject.  # noqa: E501

        Explanation why do you need this Sender ID.  # noqa: E501

        :return: The explanation of this RequestSenderIdInputObject.  # noqa: E501
        :rtype: str
        """
        return self._explanation

    @explanation.setter
    def explanation(self, explanation):
        """Sets the explanation of this RequestSenderIdInputObject.

        Explanation why do you need this Sender ID.  # noqa: E501

        :param explanation: The explanation of this RequestSenderIdInputObject.  # noqa: E501
        :type: str
        """

        self._explanation = explanation

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
        if issubclass(RequestSenderIdInputObject, dict):
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
        if not isinstance(other, RequestSenderIdInputObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
