# coding: utf-8

"""
    TextMagic API Documentation

    # Overview ## Introduction test <img style=\"float: right; margin-left: 10px; width: 100px;\" src=\"images/phone.png\"> TextMagic SMS API is a platform for building your own messaging app using our messaging infrastructure. It allows you to send and receive SMS text messages, query information about inbound and outbound messages, manage contacts, create templates (i.e. message formats and static texts) and schedule recurrent SMS messages as well as process bulk SMS messages. <button name=\"button\" onclick=\"http://www.google.com\" class=\"btn\">Try TextMagic API for Free</button>  ### Two Ways to Use TextMagic API * [REST API](https://www.textmagic.com/docs/api/start/) – get full access to TextMagic’s messaging gateway features * [Email to SMS API](https://www.textmagic.com/docs/api/send-email-to-sms/) – set up two-way SMS communication without the need to write any additional code  ### Code Libraries We have created a set of client libraries for the most popular programming languages (such as REST API Java and REST API PHP). These libraries allow you to integrate our API into your code in minutes. Just choose your preferred language to get started:  ## Getting started Get Started with the TextMagic REST API To start sending text messages using the TextMagic REST API, just follow these steps: 1. Generate the API credentials 1. Connect to our API endpoint This page provides all the information you need to get started. Here, we explain the following steps:  How to obtain the API credentials The API endpoint How the REST API works The next step How to obtain the API credentials  ### How to obtain the API credentials To start sending text messages, you need to create an API key. API keys are similar to an account password; the difference is that an API key only provides access to the API: you cannot log in to TextMagic Online using the API key.  Your program sends the login credentials with each API request as HTTP headers: `X-TM-Username` is your TextMagic username, while `X-TM-Key` is your API key.  How to obtain an API key:  1. Log in to TextMagic (or start a free trial if you haven’t registered yet). 1. Go to the API settings page. 1. Click the Add new API key button. 1. Enter an app name for this key. Note, it’s just a label, so pick any name. 1. Click Generate new key. 1. You should now see your new API key in the green notification banner above the table:  ![alt text](images/credentials.png)  > Note for API v1 users > V1 keys are not compatible with the V2 version of the TextMagic REST API, so you will need to generate a new API key to use the V2 endpoint.  ### The API endpoint The TextMagic REST API endpoint is: ``` https://rest.textmagic.com/api/v2 ``` All the URLs referenced in this documentation should use this base URL.  ### How the REST API works REST APIs use the HTTP protocol to send and receive messages. REST messages are usually encoded as JSON documents and are an improvement over older methods such as the XML based SOAP protocol. REST APIs use the same set of methods that web browsers use: POST, GET, PUT or DELETE. These correspond to the CRUD operations: create, read, update and delete. Often, REST URIs provide direct CRUD access to entities or collections of entities, for example: http://api.foo.com/people. In this instance, to delete a person’s endpoint, you might simply call the endpoint DELETE http://api.foo.com/people/{id}. REST makes these types of operations simple.  > Example > > Let’s take the entity most often used in messaging: contacts. Imagine you want to perform operations on your contacts list: well, it’s only a matter of calling the following endpoints: > * GET /api/v2/contacts (get all of your contacts) > * GET /api/v2/contacts/{id} (get a specific contact) > * POST /api/v2/contacts (create a new contact) > * PUT /api/v2/contacts/{id} (update an existing contact) > * DELETE /api/v2/contacts/{id} (delete an existing contact) It’s that simple! In fact, that’s all you need to do to manage the contacts in your TextMagic account!  ## Sandbox Sandbox is a tool to test TextMagic REST API requests without the need to install any applications or write any code. Here, we explain the following details about Sandbox: * The credentials area * Command documentation * How it works  <a href=\"\">Go to TextMagic Sandbox</a>  ### The credentials area To make requests using your TextMagic account, you need to enter your account username and your API key into the corresponding fields. You may also Save them in your browser or press Clear to erase them.  ![alt text](images/sandbox.png)   # noqa: E501

    OpenAPI spec version: 2
    Contact: support@textmagi.biz
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


            :return: The id of this SubaccountWithToken.  # noqa: E501
            :rtype: int
            """
            return self._id

            @id.setter
            def id(self, id):
            """Sets the id of this SubaccountWithToken.


            :param id: The id of this SubaccountWithToken.  # noqa: E501
            :type: int
            """

            self._id = id

            @property
            def username(self):
            """Gets the username of this SubaccountWithToken.  # noqa: E501


            :return: The username of this SubaccountWithToken.  # noqa: E501
            :rtype: str
            """
            return self._username

            @username.setter
            def username(self, username):
            """Sets the username of this SubaccountWithToken.


            :param username: The username of this SubaccountWithToken.  # noqa: E501
            :type: str
            """

            self._username = username

            @property
            def first_name(self):
            """Gets the first_name of this SubaccountWithToken.  # noqa: E501


            :return: The first_name of this SubaccountWithToken.  # noqa: E501
            :rtype: str
            """
            return self._first_name

            @first_name.setter
            def first_name(self, first_name):
            """Sets the first_name of this SubaccountWithToken.


            :param first_name: The first_name of this SubaccountWithToken.  # noqa: E501
            :type: str
            """

            self._first_name = first_name

            @property
            def last_name(self):
            """Gets the last_name of this SubaccountWithToken.  # noqa: E501


            :return: The last_name of this SubaccountWithToken.  # noqa: E501
            :rtype: str
            """
            return self._last_name

            @last_name.setter
            def last_name(self, last_name):
            """Sets the last_name of this SubaccountWithToken.


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


            :return: The status of this SubaccountWithToken.  # noqa: E501
            :rtype: str
            """
            return self._status

            @status.setter
            def status(self, status):
            """Sets the status of this SubaccountWithToken.


            :param status: The status of this SubaccountWithToken.  # noqa: E501
            :type: str
            """

            self._status = status

            @property
            def balance(self):
            """Gets the balance of this SubaccountWithToken.  # noqa: E501


            :return: The balance of this SubaccountWithToken.  # noqa: E501
            :rtype: float
            """
            return self._balance

            @balance.setter
            def balance(self, balance):
            """Sets the balance of this SubaccountWithToken.


            :param balance: The balance of this SubaccountWithToken.  # noqa: E501
            :type: float
            """

            self._balance = balance

            @property
            def phone(self):
            """Gets the phone of this SubaccountWithToken.  # noqa: E501


            :return: The phone of this SubaccountWithToken.  # noqa: E501
            :rtype: str
            """
            return self._phone

            @phone.setter
            def phone(self, phone):
            """Sets the phone of this SubaccountWithToken.


            :param phone: The phone of this SubaccountWithToken.  # noqa: E501
            :type: str
            """

            self._phone = phone

            @property
            def company(self):
            """Gets the company of this SubaccountWithToken.  # noqa: E501


            :return: The company of this SubaccountWithToken.  # noqa: E501
            :rtype: str
            """
            return self._company

            @company.setter
            def company(self, company):
            """Sets the company of this SubaccountWithToken.


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


            :return: The subaccount_type of this SubaccountWithToken.  # noqa: E501
            :rtype: str
            """
            return self._subaccount_type

            @subaccount_type.setter
            def subaccount_type(self, subaccount_type):
            """Sets the subaccount_type of this SubaccountWithToken.


            :param subaccount_type: The subaccount_type of this SubaccountWithToken.  # noqa: E501
            :type: str
            """

            self._subaccount_type = subaccount_type

            @property
            def email_accepted(self):
            """Gets the email_accepted of this SubaccountWithToken.  # noqa: E501


            :return: The email_accepted of this SubaccountWithToken.  # noqa: E501
            :rtype: bool
            """
            return self._email_accepted

            @email_accepted.setter
            def email_accepted(self, email_accepted):
            """Sets the email_accepted of this SubaccountWithToken.


            :param email_accepted: The email_accepted of this SubaccountWithToken.  # noqa: E501
            :type: bool
            """

            self._email_accepted = email_accepted

            @property
            def phone_accepted(self):
            """Gets the phone_accepted of this SubaccountWithToken.  # noqa: E501


            :return: The phone_accepted of this SubaccountWithToken.  # noqa: E501
            :rtype: bool
            """
            return self._phone_accepted

            @phone_accepted.setter
            def phone_accepted(self, phone_accepted):
            """Sets the phone_accepted of this SubaccountWithToken.


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


            :return: The token of this SubaccountWithToken.  # noqa: E501
            :rtype: str
            """
            return self._token

            @token.setter
            def token(self, token):
            """Sets the token of this SubaccountWithToken.


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
