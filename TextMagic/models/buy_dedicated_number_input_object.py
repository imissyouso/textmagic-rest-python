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


class BuyDedicatedNumberInputObject(object):
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
        'phone': 'str',
        'country': 'str',
        'user_id': 'int'
    }

    attribute_map = {
        'phone': 'phone',
        'country': 'country',
        'user_id': 'userId'
    }

    def __init__(self, phone=None, country=None, user_id=None):  # noqa: E501
        """BuyDedicatedNumberInputObject - a model defined in Swagger"""  # noqa: E501

        self._phone = None
        self._country = None
        self._user_id = None
        self.discriminator = None

        self.phone = phone
        self.country = country
        self.user_id = user_id

    @property
    def phone(self):
        """Gets the phone of this BuyDedicatedNumberInputObject.  # noqa: E501

        Dedicated phone number.  # noqa: E501

        :return: The phone of this BuyDedicatedNumberInputObject.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this BuyDedicatedNumberInputObject.

        Dedicated phone number.  # noqa: E501

        :param phone: The phone of this BuyDedicatedNumberInputObject.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def country(self):
        """Gets the country of this BuyDedicatedNumberInputObject.  # noqa: E501

        Country code phone number.  # noqa: E501

        :return: The country of this BuyDedicatedNumberInputObject.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this BuyDedicatedNumberInputObject.

        Country code phone number.  # noqa: E501

        :param country: The country of this BuyDedicatedNumberInputObject.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def user_id(self):
        """Gets the user_id of this BuyDedicatedNumberInputObject.  # noqa: E501

        Assigned dedicated number. This number will be available for this account only. You cannot transfer numbers between sub-accounts.   # noqa: E501

        :return: The user_id of this BuyDedicatedNumberInputObject.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BuyDedicatedNumberInputObject.

        Assigned dedicated number. This number will be available for this account only. You cannot transfer numbers between sub-accounts.   # noqa: E501

        :param user_id: The user_id of this BuyDedicatedNumberInputObject.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if issubclass(BuyDedicatedNumberInputObject, dict):
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
        if not isinstance(other, BuyDedicatedNumberInputObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
