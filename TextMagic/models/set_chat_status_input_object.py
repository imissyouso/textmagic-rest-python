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


class SetChatStatusInputObject(object):
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
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status'
    }

    def __init__(self, id=None, status=None):  # noqa: E501
        """SetChatStatusInputObject - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.status = status

    @property
    def id(self):
        """Gets the id of this SetChatStatusInputObject.  # noqa: E501

        Chat ID  # noqa: E501

        :return: The id of this SetChatStatusInputObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SetChatStatusInputObject.

        Chat ID  # noqa: E501

        :param id: The id of this SetChatStatusInputObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this SetChatStatusInputObject.  # noqa: E501

        Status  # noqa: E501

        :return: The status of this SetChatStatusInputObject.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SetChatStatusInputObject.

        Status  # noqa: E501

        :param status: The status of this SetChatStatusInputObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["a", "c", "d"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(SetChatStatusInputObject, dict):
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
        if not isinstance(other, SetChatStatusInputObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
