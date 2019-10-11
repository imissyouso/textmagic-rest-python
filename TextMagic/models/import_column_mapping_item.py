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


class ImportColumnMappingItem(object):
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
        'column_position_in_file': 'str',
        'field_or_custom_field_id': 'str'
    }

    attribute_map = {
        'column_position_in_file': 'column_position_in_file',
        'field_or_custom_field_id': 'field_or_custom_field_id'
    }

    def __init__(self, column_position_in_file=None, field_or_custom_field_id=None):  # noqa: E501
        """ImportColumnMappingItem - a model defined in Swagger"""  # noqa: E501

        self._column_position_in_file = None
        self._field_or_custom_field_id = None
        self.discriminator = None

        if column_position_in_file is not None:
            self.column_position_in_file = column_position_in_file
        if field_or_custom_field_id is not None:
            self.field_or_custom_field_id = field_or_custom_field_id

    @property
    def column_position_in_file(self):
        """Gets the column_position_in_file of this ImportColumnMappingItem.  # noqa: E501

        Column position in file (indexed from 0)  # noqa: E501

        :return: The column_position_in_file of this ImportColumnMappingItem.  # noqa: E501
        :rtype: str
        """
        return self._column_position_in_file

    @column_position_in_file.setter
    def column_position_in_file(self, column_position_in_file):
        """Sets the column_position_in_file of this ImportColumnMappingItem.

        Column position in file (indexed from 0)  # noqa: E501

        :param column_position_in_file: The column_position_in_file of this ImportColumnMappingItem.  # noqa: E501
        :type: str
        """

        self._column_position_in_file = column_position_in_file

    @property
    def field_or_custom_field_id(self):
        """Gets the field_or_custom_field_id of this ImportColumnMappingItem.  # noqa: E501

        Field or custom field id  # noqa: E501

        :return: The field_or_custom_field_id of this ImportColumnMappingItem.  # noqa: E501
        :rtype: str
        """
        return self._field_or_custom_field_id

    @field_or_custom_field_id.setter
    def field_or_custom_field_id(self, field_or_custom_field_id):
        """Sets the field_or_custom_field_id of this ImportColumnMappingItem.

        Field or custom field id  # noqa: E501

        :param field_or_custom_field_id: The field_or_custom_field_id of this ImportColumnMappingItem.  # noqa: E501
        :type: str
        """

        self._field_or_custom_field_id = field_or_custom_field_id

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
        if issubclass(ImportColumnMappingItem, dict):
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
        if not isinstance(other, ImportColumnMappingItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
