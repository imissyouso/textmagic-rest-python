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


class UpdateSurveyCountryItem(object):
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
        'country': 'str',
        'user_inbound_id': 'int'
    }

    attribute_map = {
        'country': 'country',
        'user_inbound_id': 'user_inbound_id'
    }

    def __init__(self, country=None, user_inbound_id=None):  # noqa: E501
        """UpdateSurveyCountryItem - a model defined in Swagger"""  # noqa: E501

        self._country = None
        self._user_inbound_id = None
        self.discriminator = None

        self.country = country
        self.user_inbound_id = user_inbound_id

    @property
    def country(self):
        """Gets the country of this UpdateSurveyCountryItem.  # noqa: E501

        Two-letter ISO country code  # noqa: E501

        :return: The country of this UpdateSurveyCountryItem.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this UpdateSurveyCountryItem.

        Two-letter ISO country code  # noqa: E501

        :param country: The country of this UpdateSurveyCountryItem.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def user_inbound_id(self):
        """Gets the user_inbound_id of this UpdateSurveyCountryItem.  # noqa: E501

        User inbound phone ID  # noqa: E501

        :return: The user_inbound_id of this UpdateSurveyCountryItem.  # noqa: E501
        :rtype: int
        """
        return self._user_inbound_id

    @user_inbound_id.setter
    def user_inbound_id(self, user_inbound_id):
        """Sets the user_inbound_id of this UpdateSurveyCountryItem.

        User inbound phone ID  # noqa: E501

        :param user_inbound_id: The user_inbound_id of this UpdateSurveyCountryItem.  # noqa: E501
        :type: int
        """

        self._user_inbound_id = user_inbound_id

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
        if issubclass(UpdateSurveyCountryItem, dict):
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
        if not isinstance(other, UpdateSurveyCountryItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other