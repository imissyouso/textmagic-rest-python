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


class SubaccountWithToken(object):
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
        'username': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'status': 'str',
        'balance': 'float',
        'phone': 'str',
        'company': 'str',
        'currency': 'Currency',
        'country': 'Country',
        'timezone': 'Timezone',
        'subaccount_type': 'str',
        'email_accepted': 'bool',
        'phone_accepted': 'bool',
        'avatar': 'UserImage',
        'token': 'str'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email': 'email',
        'status': 'status',
        'balance': 'balance',
        'phone': 'phone',
        'company': 'company',
        'currency': 'currency',
        'country': 'country',
        'timezone': 'timezone',
        'subaccount_type': 'subaccountType',
        'email_accepted': 'emailAccepted',
        'phone_accepted': 'phoneAccepted',
        'avatar': 'avatar',
        'token': 'token'
    }

    def __init__(self, id=None, username=None, first_name=None, last_name=None, email=None, status=None, balance=None, phone=None, company=None, currency=None, country=None, timezone=None, subaccount_type=None, email_accepted=None, phone_accepted=None, avatar=None, token=None):  # noqa: E501
        """SubaccountWithToken - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._username = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._status = None
        self._balance = None
        self._phone = None
        self._company = None
        self._currency = None
        self._country = None
        self._timezone = None
        self._subaccount_type = None
        self._email_accepted = None
        self._phone_accepted = None
        self._avatar = None
        self._token = None
        self.discriminator = None

        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.status = status
        self.balance = balance
        self.phone = phone
        self.company = company
        self.currency = currency
        self.country = country
        self.timezone = timezone
        self.subaccount_type = subaccount_type
        self.email_accepted = email_accepted
        self.phone_accepted = phone_accepted
        self.avatar = avatar
        self.token = token

    @property
    def id(self):
        """Gets the id of this SubaccountWithToken.  # noqa: E501

        Sub-account ID.  # noqa: E501

        :return: The id of this SubaccountWithToken.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubaccountWithToken.

        Sub-account ID.  # noqa: E501

        :param id: The id of this SubaccountWithToken.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this SubaccountWithToken.  # noqa: E501

        Username.  # noqa: E501

        :return: The username of this SubaccountWithToken.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SubaccountWithToken.

        Username.  # noqa: E501

        :param username: The username of this SubaccountWithToken.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def first_name(self):
        """Gets the first_name of this SubaccountWithToken.  # noqa: E501

        Account first name.  # noqa: E501

        :return: The first_name of this SubaccountWithToken.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this SubaccountWithToken.

        Account first name.  # noqa: E501

        :param first_name: The first_name of this SubaccountWithToken.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this SubaccountWithToken.  # noqa: E501

        Account last name.  # noqa: E501

        :return: The last_name of this SubaccountWithToken.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this SubaccountWithToken.

        Account last name.  # noqa: E501

        :param last_name: The last_name of this SubaccountWithToken.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this SubaccountWithToken.  # noqa: E501


        :return: The email of this SubaccountWithToken.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SubaccountWithToken.


        :param email: The email of this SubaccountWithToken.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def status(self):
        """Gets the status of this SubaccountWithToken.  # noqa: E501

        Current account status: * **A** for Active * **T** for Trial.   # noqa: E501

        :return: The status of this SubaccountWithToken.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SubaccountWithToken.

        Current account status: * **A** for Active * **T** for Trial.   # noqa: E501

        :param status: The status of this SubaccountWithToken.  # noqa: E501
        :type: str
        """
        allowed_values = ["A", "T"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def balance(self):
        """Gets the balance of this SubaccountWithToken.  # noqa: E501

        Account balance (in account currency).  # noqa: E501

        :return: The balance of this SubaccountWithToken.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this SubaccountWithToken.

        Account balance (in account currency).  # noqa: E501

        :param balance: The balance of this SubaccountWithToken.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def phone(self):
        """Gets the phone of this SubaccountWithToken.  # noqa: E501

        Contact phone number.  # noqa: E501

        :return: The phone of this SubaccountWithToken.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this SubaccountWithToken.

        Contact phone number.  # noqa: E501

        :param phone: The phone of this SubaccountWithToken.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def company(self):
        """Gets the company of this SubaccountWithToken.  # noqa: E501

        Account company name.  # noqa: E501

        :return: The company of this SubaccountWithToken.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this SubaccountWithToken.

        Account company name.  # noqa: E501

        :param company: The company of this SubaccountWithToken.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def currency(self):
        """Gets the currency of this SubaccountWithToken.  # noqa: E501


        :return: The currency of this SubaccountWithToken.  # noqa: E501
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SubaccountWithToken.


        :param currency: The currency of this SubaccountWithToken.  # noqa: E501
        :type: Currency
        """

        self._currency = currency

    @property
    def country(self):
        """Gets the country of this SubaccountWithToken.  # noqa: E501


        :return: The country of this SubaccountWithToken.  # noqa: E501
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this SubaccountWithToken.


        :param country: The country of this SubaccountWithToken.  # noqa: E501
        :type: Country
        """

        self._country = country

    @property
    def timezone(self):
        """Gets the timezone of this SubaccountWithToken.  # noqa: E501


        :return: The timezone of this SubaccountWithToken.  # noqa: E501
        :rtype: Timezone
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this SubaccountWithToken.


        :param timezone: The timezone of this SubaccountWithToken.  # noqa: E501
        :type: Timezone
        """

        self._timezone = timezone

    @property
    def subaccount_type(self):
        """Gets the subaccount_type of this SubaccountWithToken.  # noqa: E501

        Type of account: *   **A** for Administrator sub-account *   **U** for Regular User   # noqa: E501

        :return: The subaccount_type of this SubaccountWithToken.  # noqa: E501
        :rtype: str
        """
        return self._subaccount_type

    @subaccount_type.setter
    def subaccount_type(self, subaccount_type):
        """Sets the subaccount_type of this SubaccountWithToken.

        Type of account: *   **A** for Administrator sub-account *   **U** for Regular User   # noqa: E501

        :param subaccount_type: The subaccount_type of this SubaccountWithToken.  # noqa: E501
        :type: str
        """
        allowed_values = ["A", "U"]  # noqa: E501
        if subaccount_type not in allowed_values:
            raise ValueError(
                "Invalid value for `subaccount_type` ({0}), must be one of {1}"  # noqa: E501
                .format(subaccount_type, allowed_values)
            )

        self._subaccount_type = subaccount_type

    @property
    def email_accepted(self):
        """Gets the email_accepted of this SubaccountWithToken.  # noqa: E501

        Is account has confirmed Email.  # noqa: E501

        :return: The email_accepted of this SubaccountWithToken.  # noqa: E501
        :rtype: bool
        """
        return self._email_accepted

    @email_accepted.setter
    def email_accepted(self, email_accepted):
        """Sets the email_accepted of this SubaccountWithToken.

        Is account has confirmed Email.  # noqa: E501

        :param email_accepted: The email_accepted of this SubaccountWithToken.  # noqa: E501
        :type: bool
        """

        self._email_accepted = email_accepted

    @property
    def phone_accepted(self):
        """Gets the phone_accepted of this SubaccountWithToken.  # noqa: E501

        Is account has confirmed Phone number.  # noqa: E501

        :return: The phone_accepted of this SubaccountWithToken.  # noqa: E501
        :rtype: bool
        """
        return self._phone_accepted

    @phone_accepted.setter
    def phone_accepted(self, phone_accepted):
        """Sets the phone_accepted of this SubaccountWithToken.

        Is account has confirmed Phone number.  # noqa: E501

        :param phone_accepted: The phone_accepted of this SubaccountWithToken.  # noqa: E501
        :type: bool
        """

        self._phone_accepted = phone_accepted

    @property
    def avatar(self):
        """Gets the avatar of this SubaccountWithToken.  # noqa: E501


        :return: The avatar of this SubaccountWithToken.  # noqa: E501
        :rtype: UserImage
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this SubaccountWithToken.


        :param avatar: The avatar of this SubaccountWithToken.  # noqa: E501
        :type: UserImage
        """

        self._avatar = avatar

    @property
    def token(self):
        """Gets the token of this SubaccountWithToken.  # noqa: E501

        Access token of account.  # noqa: E501

        :return: The token of this SubaccountWithToken.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this SubaccountWithToken.

        Access token of account.  # noqa: E501

        :param token: The token of this SubaccountWithToken.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if issubclass(SubaccountWithToken, dict):
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
        if not isinstance(other, SubaccountWithToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
