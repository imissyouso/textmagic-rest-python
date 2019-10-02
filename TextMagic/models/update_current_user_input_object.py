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


class UpdateCurrentUserInputObject(object):
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
        'username': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'phone': 'str',
        'company': 'str',
        'timezone': 'int'
    }

    attribute_map = {
        'username': 'username',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email': 'email',
        'phone': 'phone',
        'company': 'company',
        'timezone': 'timezone'
    }

    def __init__(self, username=None, first_name=None, last_name=None, email=None, phone=None, company=None, timezone=None):  # noqa: E501
        """UpdateCurrentUserInputObject - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._phone = None
        self._company = None
        self._timezone = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if company is not None:
            self.company = company
        if timezone is not None:
            self.timezone = timezone

    @property
    def username(self):
        """Gets the username of this UpdateCurrentUserInputObject.  # noqa: E501


        :return: The username of this UpdateCurrentUserInputObject.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UpdateCurrentUserInputObject.


        :param username: The username of this UpdateCurrentUserInputObject.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def first_name(self):
        """Gets the first_name of this UpdateCurrentUserInputObject.  # noqa: E501

        Account first name.  # noqa: E501

        :return: The first_name of this UpdateCurrentUserInputObject.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UpdateCurrentUserInputObject.

        Account first name.  # noqa: E501

        :param first_name: The first_name of this UpdateCurrentUserInputObject.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UpdateCurrentUserInputObject.  # noqa: E501

        Account last name.  # noqa: E501

        :return: The last_name of this UpdateCurrentUserInputObject.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UpdateCurrentUserInputObject.

        Account last name.  # noqa: E501

        :param last_name: The last_name of this UpdateCurrentUserInputObject.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this UpdateCurrentUserInputObject.  # noqa: E501


        :return: The email of this UpdateCurrentUserInputObject.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UpdateCurrentUserInputObject.


        :param email: The email of this UpdateCurrentUserInputObject.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this UpdateCurrentUserInputObject.  # noqa: E501


        :return: The phone of this UpdateCurrentUserInputObject.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UpdateCurrentUserInputObject.


        :param phone: The phone of this UpdateCurrentUserInputObject.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def company(self):
        """Gets the company of this UpdateCurrentUserInputObject.  # noqa: E501

        Account company name.  # noqa: E501

        :return: The company of this UpdateCurrentUserInputObject.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this UpdateCurrentUserInputObject.

        Account company name.  # noqa: E501

        :param company: The company of this UpdateCurrentUserInputObject.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def timezone(self):
        """Gets the timezone of this UpdateCurrentUserInputObject.  # noqa: E501

        The timezome internal id  # noqa: E501

        :return: The timezone of this UpdateCurrentUserInputObject.  # noqa: E501
        :rtype: int
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this UpdateCurrentUserInputObject.

        The timezome internal id  # noqa: E501

        :param timezone: The timezone of this UpdateCurrentUserInputObject.  # noqa: E501
        :type: int
        """

        self._timezone = timezone

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
        if issubclass(UpdateCurrentUserInputObject, dict):
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
        if not isinstance(other, UpdateCurrentUserInputObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
