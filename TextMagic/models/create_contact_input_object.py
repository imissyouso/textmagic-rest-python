# coding: utf-8

"""
    TextMagic API Documentation

    # Overview ## Introduction <img style=\"float: right; margin-left: 10px; width: 100px;\" src=\"images/phone.png\"> TextMagic SMS API is a platform for building your own messaging app using our messaging infrastructure. It allows you to send and receive SMS text messages, query information about inbound and outbound messages, manage contacts, create templates (i.e. message formats and static texts) and schedule recurrent SMS messages as well as process bulk SMS messages. <button name=\"button\" onclick=\"http://www.google.com\" class=\"btn\">Try TextMagic API for Free</button>  ### Two Ways to Use TextMagic API * [REST API](https://www.textmagic.com/docs/api/start/) – get full access to TextMagic’s messaging gateway features * [Email to SMS API](https://www.textmagic.com/docs/api/send-email-to-sms/) – set up two-way SMS communication without the need to write any additional code  ### Code Libraries We have created a set of client libraries for the most popular programming languages (such as REST API Java and REST API PHP). These libraries allow you to integrate our API into your code in minutes. Just choose your preferred language to get started:  ## Getting started Get Started with the TextMagic REST API To start sending text messages using the TextMagic REST API, just follow these steps: 1. Generate the API credentials 1. Connect to our API endpoint This page provides all the information you need to get started. Here, we explain the following steps:  How to obtain the API credentials The API endpoint How the REST API works The next step How to obtain the API credentials  ### How to obtain the API credentials To start sending text messages, you need to create an API key. API keys are similar to an account password; the difference is that an API key only provides access to the API: you cannot log in to TextMagic Online using the API key.  Your program sends the login credentials with each API request as HTTP headers: `X-TM-Username` is your TextMagic username, while `X-TM-Key` is your API key.  How to obtain an API key:  1. Log in to TextMagic (or start a free trial if you haven’t registered yet). 1. Go to the API settings page. 1. Click the Add new API key button. 1. Enter an app name for this key. Note, it’s just a label, so pick any name. 1. Click Generate new key. 1. You should now see your new API key in the green notification banner above the table:  ![alt text](images/credentials.png)  > Note for API v1 users > V1 keys are not compatible with the V2 version of the TextMagic REST API, so you will need to generate a new API key to use the V2 endpoint.  ### The API endpoint The TextMagic REST API endpoint is: ``` https://rest.textmagic.com/api/v2 ``` All the URLs referenced in this documentation should use this base URL.  ### How the REST API works REST APIs use the HTTP protocol to send and receive messages. REST messages are usually encoded as JSON documents and are an improvement over older methods such as the XML based SOAP protocol. REST APIs use the same set of methods that web browsers use: POST, GET, PUT or DELETE. These correspond to the CRUD operations: create, read, update and delete. Often, REST URIs provide direct CRUD access to entities or collections of entities, for example: http://api.foo.com/people. In this instance, to delete a person’s endpoint, you might simply call the endpoint DELETE http://api.foo.com/people/{id}. REST makes these types of operations simple.  > Example > > Let’s take the entity most often used in messaging: contacts. Imagine you want to perform operations on your contacts list: well, it’s only a matter of calling the following endpoints: > * GET /api/v2/contacts (get all of your contacts) > * GET /api/v2/contacts/{id} (get a specific contact) > * POST /api/v2/contacts (create a new contact) > * PUT /api/v2/contacts/{id} (update an existing contact) > * DELETE /api/v2/contacts/{id} (delete an existing contact) It’s that simple! In fact, that’s all you need to do to manage the contacts in your TextMagic account!  ## Sandbox Sandbox is a tool to test TextMagic REST API requests without the need to install any applications or write any code. Here, we explain the following details about Sandbox: * The credentials area * Command documentation * How it works  <a href=\"\">Go to TextMagic Sandbox</a>  ### The credentials area To make requests using your TextMagic account, you need to enter your account username and your API key into the corresponding fields. You may also Save them in your browser or press Clear to erase them.  ![alt text](images/sandbox.png)   # noqa: E501

    OpenAPI spec version: 2
    Contact: support@textmagi.biz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateContactInputObject(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'phone': 'str',
        'email': 'str',
        'company_name': 'str',
        'lists': 'str',
        'favorited': 'bool',
        'blocked': 'bool',
        'type': 'int',
        'custom_field_values': 'object',
        'local': 'int',
        'country': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'phone': 'phone',
        'email': 'email',
        'company_name': 'companyName',
        'lists': 'lists',
        'favorited': 'favorited',
        'blocked': 'blocked',
        'type': 'type',
        'custom_field_values': 'customFieldValues',
        'local': 'local',
        'country': 'country'
    }

    def __init__(self, first_name=None, last_name=None, phone=None, email=None, company_name=None, lists=None, favorited=None, blocked=None, type=None, custom_field_values=None, local=None, country=None):  # noqa: E501
        """CreateContactInputObject - a model defined in Swagger"""  # noqa: E501

        self._first_name = None
        self._last_name = None
        self._phone = None
        self._email = None
        self._company_name = None
        self._lists = None
        self._favorited = None
        self._blocked = None
        self._type = None
        self._custom_field_values = None
        self._local = None
        self._country = None
        self.discriminator = None

        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        self.phone = phone
        if email is not None:
            self.email = email
        if company_name is not None:
            self.company_name = company_name
        self.lists = lists
        if favorited is not None:
            self.favorited = favorited
        if blocked is not None:
            self.blocked = blocked
        if type is not None:
            self.type = type
        if custom_field_values is not None:
            self.custom_field_values = custom_field_values
        if local is not None:
            self.local = local
        if country is not None:
            self.country = country

    @property
    def first_name(self):
        """Gets the first_name of this CreateContactInputObject.  # noqa: E501

        Contact first name  # noqa: E501

        :return: The first_name of this CreateContactInputObject.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CreateContactInputObject.

        Contact first name  # noqa: E501

        :param first_name: The first_name of this CreateContactInputObject.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this CreateContactInputObject.  # noqa: E501

        Contact last name  # noqa: E501

        :return: The last_name of this CreateContactInputObject.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CreateContactInputObject.

        Contact last name  # noqa: E501

        :param last_name: The last_name of this CreateContactInputObject.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def phone(self):
        """Gets the phone of this CreateContactInputObject.  # noqa: E501

        Contact phone number in E.164 (international) format without leading + or zeroes  # noqa: E501

        :return: The phone of this CreateContactInputObject.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CreateContactInputObject.

        Contact phone number in E.164 (international) format without leading + or zeroes  # noqa: E501

        :param phone: The phone of this CreateContactInputObject.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this CreateContactInputObject.  # noqa: E501

        Contact email  # noqa: E501

        :return: The email of this CreateContactInputObject.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateContactInputObject.

        Contact email  # noqa: E501

        :param email: The email of this CreateContactInputObject.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def company_name(self):
        """Gets the company_name of this CreateContactInputObject.  # noqa: E501

        Contact company name  # noqa: E501

        :return: The company_name of this CreateContactInputObject.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this CreateContactInputObject.

        Contact company name  # noqa: E501

        :param company_name: The company_name of this CreateContactInputObject.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def lists(self):
        """Gets the lists of this CreateContactInputObject.  # noqa: E501

        Array of list resources id contact will be assigned to  # noqa: E501

        :return: The lists of this CreateContactInputObject.  # noqa: E501
        :rtype: str
        """
        return self._lists

    @lists.setter
    def lists(self, lists):
        """Sets the lists of this CreateContactInputObject.

        Array of list resources id contact will be assigned to  # noqa: E501

        :param lists: The lists of this CreateContactInputObject.  # noqa: E501
        :type: str
        """

        self._lists = lists

    @property
    def favorited(self):
        """Gets the favorited of this CreateContactInputObject.  # noqa: E501

        Is contact favorited  # noqa: E501

        :return: The favorited of this CreateContactInputObject.  # noqa: E501
        :rtype: bool
        """
        return self._favorited

    @favorited.setter
    def favorited(self, favorited):
        """Sets the favorited of this CreateContactInputObject.

        Is contact favorited  # noqa: E501

        :param favorited: The favorited of this CreateContactInputObject.  # noqa: E501
        :type: bool
        """

        self._favorited = favorited

    @property
    def blocked(self):
        """Gets the blocked of this CreateContactInputObject.  # noqa: E501

        Is contact blocked for outgoing and incoming messaging  # noqa: E501

        :return: The blocked of this CreateContactInputObject.  # noqa: E501
        :rtype: bool
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """Sets the blocked of this CreateContactInputObject.

        Is contact blocked for outgoing and incoming messaging  # noqa: E501

        :param blocked: The blocked of this CreateContactInputObject.  # noqa: E501
        :type: bool
        """

        self._blocked = blocked

    @property
    def type(self):
        """Gets the type of this CreateContactInputObject.  # noqa: E501

        Force type of phone. Possible values: 0 - landline, 1 - mobile. Default is -1 (auto detection)  # noqa: E501

        :return: The type of this CreateContactInputObject.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateContactInputObject.

        Force type of phone. Possible values: 0 - landline, 1 - mobile. Default is -1 (auto detection)  # noqa: E501

        :param type: The type of this CreateContactInputObject.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def custom_field_values(self):
        """Gets the custom_field_values of this CreateContactInputObject.  # noqa: E501


        :return: The custom_field_values of this CreateContactInputObject.  # noqa: E501
        :rtype: object
        """
        return self._custom_field_values

    @custom_field_values.setter
    def custom_field_values(self, custom_field_values):
        """Sets the custom_field_values of this CreateContactInputObject.


        :param custom_field_values: The custom_field_values of this CreateContactInputObject.  # noqa: E501
        :type: object
        """

        self._custom_field_values = custom_field_values

    @property
    def local(self):
        """Gets the local of this CreateContactInputObject.  # noqa: E501

        Treat phone number passed in request body as local  # noqa: E501

        :return: The local of this CreateContactInputObject.  # noqa: E501
        :rtype: int
        """
        return self._local

    @local.setter
    def local(self, local):
        """Sets the local of this CreateContactInputObject.

        Treat phone number passed in request body as local  # noqa: E501

        :param local: The local of this CreateContactInputObject.  # noqa: E501
        :type: int
        """

        self._local = local

    @property
    def country(self):
        """Gets the country of this CreateContactInputObject.  # noqa: E501

        2-letter ISO country code for local phone numbers, used when local is  set to true. Default is account country  # noqa: E501

        :return: The country of this CreateContactInputObject.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CreateContactInputObject.

        2-letter ISO country code for local phone numbers, used when local is  set to true. Default is account country  # noqa: E501

        :param country: The country of this CreateContactInputObject.  # noqa: E501
        :type: str
        """

        self._country = country

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
        if issubclass(CreateContactInputObject, dict):
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
        if not isinstance(other, CreateContactInputObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
