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


class GetAvailableSenderSettingOptionsResponse(object):
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
        'dedicated': 'list[str]',
        'user': 'list[str]',
        'shared': 'list[str]',
        'sender_ids': 'list[str]'
    }

    attribute_map = {
        'dedicated': 'dedicated',
        'user': 'user',
        'shared': 'shared',
        'sender_ids': 'senderIds'
    }

    def __init__(self, dedicated=None, user=None, shared=None, sender_ids=None):  # noqa: E501
        """GetAvailableSenderSettingOptionsResponse - a model defined in Swagger"""  # noqa: E501

        self._dedicated = None
        self._user = None
        self._shared = None
        self._sender_ids = None
        self.discriminator = None

        self.dedicated = dedicated
        self.user = user
        self.shared = shared
        self.sender_ids = sender_ids

    @property
    def dedicated(self):
        """Gets the dedicated of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501


        :return: The dedicated of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._dedicated

    @dedicated.setter
    def dedicated(self, dedicated):
        """Sets the dedicated of this GetAvailableSenderSettingOptionsResponse.


        :param dedicated: The dedicated of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :type: list[str]
        """
        if dedicated is None:
            raise ValueError("Invalid value for `dedicated`, must not be `None`")  # noqa: E501

        self._dedicated = dedicated

    @property
    def user(self):
        """Gets the user of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501


        :return: The user of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this GetAvailableSenderSettingOptionsResponse.


        :param user: The user of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :type: list[str]
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def shared(self):
        """Gets the shared of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501


        :return: The shared of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this GetAvailableSenderSettingOptionsResponse.


        :param shared: The shared of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :type: list[str]
        """
        if shared is None:
            raise ValueError("Invalid value for `shared`, must not be `None`")  # noqa: E501

        self._shared = shared

    @property
    def sender_ids(self):
        """Gets the sender_ids of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501


        :return: The sender_ids of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._sender_ids

    @sender_ids.setter
    def sender_ids(self, sender_ids):
        """Sets the sender_ids of this GetAvailableSenderSettingOptionsResponse.


        :param sender_ids: The sender_ids of this GetAvailableSenderSettingOptionsResponse.  # noqa: E501
        :type: list[str]
        """
        if sender_ids is None:
            raise ValueError("Invalid value for `sender_ids`, must not be `None`")  # noqa: E501

        self._sender_ids = sender_ids

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
        if issubclass(GetAvailableSenderSettingOptionsResponse, dict):
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
        if not isinstance(other, GetAvailableSenderSettingOptionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
