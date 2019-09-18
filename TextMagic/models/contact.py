# coding: utf-8

"""
    TextMagic API Documentation

    # Overview ## Introduction 22 <img style=\"float: right; margin-left: 10px; width: 100px;\" src=\"images/phone.png\"> TextMagic SMS API is a platform for building your own messaging app using our messaging infrastructure. It allows you to send and receive SMS text messages, query information about inbound and outbound messages, manage contacts, create templates (i.e. message formats and static texts) and schedule recurrent SMS messages as well as process bulk SMS messages. <button name=\"button\" onclick=\"http://www.google.com\" class=\"btn\">Try TextMagic API for Free</button>  ### Two Ways to Use TextMagic API * [REST API](https://www.textmagic.com/docs/api/start/) – get full access to TextMagic’s messaging gateway features * [Email to SMS API](https://www.textmagic.com/docs/api/send-email-to-sms/) – set up two-way SMS communication without the need to write any additional code  ### Code Libraries We have created a set of client libraries for the most popular programming languages (such as REST API Java and REST API PHP). These libraries allow you to integrate our API into your code in minutes. Just choose your preferred language to get started:  ## Getting started Get Started with the TextMagic REST API To start sending text messages using the TextMagic REST API, just follow these steps: 1. Generate the API credentials 1. Connect to our API endpoint This page provides all the information you need to get started. Here, we explain the following steps:  How to obtain the API credentials The API endpoint How the REST API works The next step How to obtain the API credentials  ### How to obtain the API credentials To start sending text messages, you need to create an API key. API keys are similar to an account password; the difference is that an API key only provides access to the API: you cannot log in to TextMagic Online using the API key.  Your program sends the login credentials with each API request as HTTP headers: `X-TM-Username` is your TextMagic username, while `X-TM-Key` is your API key.  How to obtain an API key:  1. Log in to TextMagic (or start a free trial if you haven’t registered yet). 1. Go to the API settings page. 1. Click the Add new API key button. 1. Enter an app name for this key. Note, it’s just a label, so pick any name. 1. Click Generate new key. 1. You should now see your new API key in the green notification banner above the table:  ![alt text](images/credentials.png)  > Note for API v1 users > V1 keys are not compatible with the V2 version of the TextMagic REST API, so you will need to generate a new API key to use the V2 endpoint.  ### The API endpoint The TextMagic REST API endpoint is: ``` https://rest.textmagic.com/api/v2 ``` All the URLs referenced in this documentation should use this base URL.  ### How the REST API works REST APIs use the HTTP protocol to send and receive messages. REST messages are usually encoded as JSON documents and are an improvement over older methods such as the XML based SOAP protocol. REST APIs use the same set of methods that web browsers use: POST, GET, PUT or DELETE. These correspond to the CRUD operations: create, read, update and delete. Often, REST URIs provide direct CRUD access to entities or collections of entities, for example: http://api.foo.com/people. In this instance, to delete a person’s endpoint, you might simply call the endpoint DELETE http://api.foo.com/people/{id}. REST makes these types of operations simple.  > Example > > Let’s take the entity most often used in messaging: contacts. Imagine you want to perform operations on your contacts list: well, it’s only a matter of calling the following endpoints: > * GET /api/v2/contacts (get all of your contacts) > * GET /api/v2/contacts/{id} (get a specific contact) > * POST /api/v2/contacts (create a new contact) > * PUT /api/v2/contacts/{id} (update an existing contact) > * DELETE /api/v2/contacts/{id} (delete an existing contact) It’s that simple! In fact, that’s all you need to do to manage the contacts in your TextMagic account!  ## Sandbox Sandbox is a tool to test TextMagic REST API requests without the need to install any applications or write any code. Here, we explain the following details about Sandbox: * The credentials area * Command documentation * How it works  <a href=\"\">Go to TextMagic Sandbox</a>  ### The credentials area To make requests using your TextMagic account, you need to enter your account username and your API key into the corresponding fields. You may also Save them in your browser or press Clear to erase them.  ![alt text](images/sandbox.png)   # noqa: E501

    OpenAPI spec version: 2
    Contact: support@textmagi.biz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Contact(object):
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
        'favorited': 'bool',
        'blocked': 'bool',
        'first_name': 'str',
        'last_name': 'str',
        'company_name': 'str',
        'phone': 'str',
        'email': 'str',
        'country': 'Country',
        'custom_fields': 'list[ContactCustomField]',
        'user': 'User',
        'lists': 'list[Group]',
        'phone_type': 'str',
        'avatar': 'ContactImage',
        'notes': 'list[ContactNote]'
    }

    attribute_map = {
        'id': 'id',
        'favorited': 'favorited',
        'blocked': 'blocked',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'company_name': 'companyName',
        'phone': 'phone',
        'email': 'email',
        'country': 'country',
        'custom_fields': 'customFields',
        'user': 'user',
        'lists': 'lists',
        'phone_type': 'phoneType',
        'avatar': 'avatar',
        'notes': 'notes'
    }

    def __init__(self, id=None, favorited=None, blocked=None, first_name=None, last_name=None, company_name=None, phone=None, email=None, country=None, custom_fields=None, user=None, lists=None, phone_type=None, avatar=None, notes=None):  # noqa: E501
        """Contact - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._favorited = None
        self._blocked = None
        self._first_name = None
        self._last_name = None
        self._company_name = None
        self._phone = None
        self._email = None
        self._country = None
        self._custom_fields = None
        self._user = None
        self._lists = None
        self._phone_type = None
        self._avatar = None
        self._notes = None
        self.discriminator = None

        self.id = id
        self.favorited = favorited
        self.blocked = blocked
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.phone = phone
        self.email = email
        self.country = country
        self.custom_fields = custom_fields
        self.user = user
        self.lists = lists
        self.phone_type = phone_type
        self.avatar = avatar
        self.notes = notes

    @property
    def id(self):
        """Gets the id of this Contact.  # noqa: E501


        :return: The id of this Contact.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Contact.


        :param id: The id of this Contact.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def favorited(self):
        """Gets the favorited of this Contact.  # noqa: E501


        :return: The favorited of this Contact.  # noqa: E501
        :rtype: bool
        """
        return self._favorited

    @favorited.setter
    def favorited(self, favorited):
        """Sets the favorited of this Contact.


        :param favorited: The favorited of this Contact.  # noqa: E501
        :type: bool
        """

        self._favorited = favorited

    @property
    def blocked(self):
        """Gets the blocked of this Contact.  # noqa: E501


        :return: The blocked of this Contact.  # noqa: E501
        :rtype: bool
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """Sets the blocked of this Contact.


        :param blocked: The blocked of this Contact.  # noqa: E501
        :type: bool
        """

        self._blocked = blocked

    @property
    def first_name(self):
        """Gets the first_name of this Contact.  # noqa: E501


        :return: The first_name of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Contact.


        :param first_name: The first_name of this Contact.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Contact.  # noqa: E501


        :return: The last_name of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Contact.


        :param last_name: The last_name of this Contact.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def company_name(self):
        """Gets the company_name of this Contact.  # noqa: E501


        :return: The company_name of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this Contact.


        :param company_name: The company_name of this Contact.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def phone(self):
        """Gets the phone of this Contact.  # noqa: E501


        :return: The phone of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Contact.


        :param phone: The phone of this Contact.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this Contact.  # noqa: E501


        :return: The email of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Contact.


        :param email: The email of this Contact.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def country(self):
        """Gets the country of this Contact.  # noqa: E501


        :return: The country of this Contact.  # noqa: E501
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Contact.


        :param country: The country of this Contact.  # noqa: E501
        :type: Country
        """

        self._country = country

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Contact.  # noqa: E501


        :return: The custom_fields of this Contact.  # noqa: E501
        :rtype: list[ContactCustomField]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Contact.


        :param custom_fields: The custom_fields of this Contact.  # noqa: E501
        :type: list[ContactCustomField]
        """

        self._custom_fields = custom_fields

    @property
    def user(self):
        """Gets the user of this Contact.  # noqa: E501


        :return: The user of this Contact.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Contact.


        :param user: The user of this Contact.  # noqa: E501
        :type: User
        """

        self._user = user

    @property
    def lists(self):
        """Gets the lists of this Contact.  # noqa: E501


        :return: The lists of this Contact.  # noqa: E501
        :rtype: list[Group]
        """
        return self._lists

    @lists.setter
    def lists(self, lists):
        """Sets the lists of this Contact.


        :param lists: The lists of this Contact.  # noqa: E501
        :type: list[Group]
        """

        self._lists = lists

    @property
    def phone_type(self):
        """Gets the phone_type of this Contact.  # noqa: E501


        :return: The phone_type of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._phone_type

    @phone_type.setter
    def phone_type(self, phone_type):
        """Sets the phone_type of this Contact.


        :param phone_type: The phone_type of this Contact.  # noqa: E501
        :type: str
        """

        self._phone_type = phone_type

    @property
    def avatar(self):
        """Gets the avatar of this Contact.  # noqa: E501


        :return: The avatar of this Contact.  # noqa: E501
        :rtype: ContactImage
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this Contact.


        :param avatar: The avatar of this Contact.  # noqa: E501
        :type: ContactImage
        """

        self._avatar = avatar

    @property
    def notes(self):
        """Gets the notes of this Contact.  # noqa: E501


        :return: The notes of this Contact.  # noqa: E501
        :rtype: list[ContactNote]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Contact.


        :param notes: The notes of this Contact.  # noqa: E501
        :type: list[ContactNote]
        """

        self._notes = notes

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
        if issubclass(Contact, dict):
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
        if not isinstance(other, Contact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
