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


class MessagesIcs(object):
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
        'next_send': 'datetime',
        'rrule': 'str',
        'session': 'MessageSession',
        'last_sent': 'datetime',
        'contact_name': 'str',
        'parameters': 'MessagesIcsParameters',
        'type': 'str',
        'summary': 'str',
        'text_parameters': 'MessagesIcsTextParameters',
        'first_occurrence': 'datetime',
        'last_occurrence': 'datetime',
        'recipients_count': 'int',
        'timezone': 'str',
        'completed': 'bool',
        'avatar': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'next_send': 'nextSend',
        'rrule': 'rrule',
        'session': 'session',
        'last_sent': 'lastSent',
        'contact_name': 'contactName',
        'parameters': 'parameters',
        'type': 'type',
        'summary': 'summary',
        'text_parameters': 'textParameters',
        'first_occurrence': 'firstOccurrence',
        'last_occurrence': 'lastOccurrence',
        'recipients_count': 'recipientsCount',
        'timezone': 'timezone',
        'completed': 'completed',
        'avatar': 'avatar',
        'created_at': 'createdAt'
    }

    def __init__(self, id=None, next_send=None, rrule=None, session=None, last_sent=None, contact_name=None, parameters=None, type=None, summary=None, text_parameters=None, first_occurrence=None, last_occurrence=None, recipients_count=None, timezone=None, completed=None, avatar=None, created_at=None):  # noqa: E501
        """MessagesIcs - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._next_send = None
        self._rrule = None
        self._session = None
        self._last_sent = None
        self._contact_name = None
        self._parameters = None
        self._type = None
        self._summary = None
        self._text_parameters = None
        self._first_occurrence = None
        self._last_occurrence = None
        self._recipients_count = None
        self._timezone = None
        self._completed = None
        self._avatar = None
        self._created_at = None
        self.discriminator = None

        self.id = id
        self.next_send = next_send
        self.rrule = rrule
        self.session = session
        self.last_sent = last_sent
        self.contact_name = contact_name
        self.parameters = parameters
        self.type = type
        self.summary = summary
        self.text_parameters = text_parameters
        self.first_occurrence = first_occurrence
        self.last_occurrence = last_occurrence
        self.recipients_count = recipients_count
        self.timezone = timezone
        self.completed = completed
        self.avatar = avatar
        self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this MessagesIcs.  # noqa: E501


        :return: The id of this MessagesIcs.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MessagesIcs.


        :param id: The id of this MessagesIcs.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def next_send(self):
        """Gets the next_send of this MessagesIcs.  # noqa: E501


        :return: The next_send of this MessagesIcs.  # noqa: E501
        :rtype: datetime
        """
        return self._next_send

    @next_send.setter
    def next_send(self, next_send):
        """Sets the next_send of this MessagesIcs.


        :param next_send: The next_send of this MessagesIcs.  # noqa: E501
        :type: datetime
        """

        self._next_send = next_send

    @property
    def rrule(self):
        """Gets the rrule of this MessagesIcs.  # noqa: E501


        :return: The rrule of this MessagesIcs.  # noqa: E501
        :rtype: str
        """
        return self._rrule

    @rrule.setter
    def rrule(self, rrule):
        """Sets the rrule of this MessagesIcs.


        :param rrule: The rrule of this MessagesIcs.  # noqa: E501
        :type: str
        """

        self._rrule = rrule

    @property
    def session(self):
        """Gets the session of this MessagesIcs.  # noqa: E501


        :return: The session of this MessagesIcs.  # noqa: E501
        :rtype: MessageSession
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this MessagesIcs.


        :param session: The session of this MessagesIcs.  # noqa: E501
        :type: MessageSession
        """

        self._session = session

    @property
    def last_sent(self):
        """Gets the last_sent of this MessagesIcs.  # noqa: E501


        :return: The last_sent of this MessagesIcs.  # noqa: E501
        :rtype: datetime
        """
        return self._last_sent

    @last_sent.setter
    def last_sent(self, last_sent):
        """Sets the last_sent of this MessagesIcs.


        :param last_sent: The last_sent of this MessagesIcs.  # noqa: E501
        :type: datetime
        """

        self._last_sent = last_sent

    @property
    def contact_name(self):
        """Gets the contact_name of this MessagesIcs.  # noqa: E501


        :return: The contact_name of this MessagesIcs.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this MessagesIcs.


        :param contact_name: The contact_name of this MessagesIcs.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def parameters(self):
        """Gets the parameters of this MessagesIcs.  # noqa: E501


        :return: The parameters of this MessagesIcs.  # noqa: E501
        :rtype: MessagesIcsParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this MessagesIcs.


        :param parameters: The parameters of this MessagesIcs.  # noqa: E501
        :type: MessagesIcsParameters
        """

        self._parameters = parameters

    @property
    def type(self):
        """Gets the type of this MessagesIcs.  # noqa: E501


        :return: The type of this MessagesIcs.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MessagesIcs.


        :param type: The type of this MessagesIcs.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def summary(self):
        """Gets the summary of this MessagesIcs.  # noqa: E501


        :return: The summary of this MessagesIcs.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this MessagesIcs.


        :param summary: The summary of this MessagesIcs.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def text_parameters(self):
        """Gets the text_parameters of this MessagesIcs.  # noqa: E501


        :return: The text_parameters of this MessagesIcs.  # noqa: E501
        :rtype: MessagesIcsTextParameters
        """
        return self._text_parameters

    @text_parameters.setter
    def text_parameters(self, text_parameters):
        """Sets the text_parameters of this MessagesIcs.


        :param text_parameters: The text_parameters of this MessagesIcs.  # noqa: E501
        :type: MessagesIcsTextParameters
        """

        self._text_parameters = text_parameters

    @property
    def first_occurrence(self):
        """Gets the first_occurrence of this MessagesIcs.  # noqa: E501


        :return: The first_occurrence of this MessagesIcs.  # noqa: E501
        :rtype: datetime
        """
        return self._first_occurrence

    @first_occurrence.setter
    def first_occurrence(self, first_occurrence):
        """Sets the first_occurrence of this MessagesIcs.


        :param first_occurrence: The first_occurrence of this MessagesIcs.  # noqa: E501
        :type: datetime
        """

        self._first_occurrence = first_occurrence

    @property
    def last_occurrence(self):
        """Gets the last_occurrence of this MessagesIcs.  # noqa: E501


        :return: The last_occurrence of this MessagesIcs.  # noqa: E501
        :rtype: datetime
        """
        return self._last_occurrence

    @last_occurrence.setter
    def last_occurrence(self, last_occurrence):
        """Sets the last_occurrence of this MessagesIcs.


        :param last_occurrence: The last_occurrence of this MessagesIcs.  # noqa: E501
        :type: datetime
        """

        self._last_occurrence = last_occurrence

    @property
    def recipients_count(self):
        """Gets the recipients_count of this MessagesIcs.  # noqa: E501


        :return: The recipients_count of this MessagesIcs.  # noqa: E501
        :rtype: int
        """
        return self._recipients_count

    @recipients_count.setter
    def recipients_count(self, recipients_count):
        """Sets the recipients_count of this MessagesIcs.


        :param recipients_count: The recipients_count of this MessagesIcs.  # noqa: E501
        :type: int
        """

        self._recipients_count = recipients_count

    @property
    def timezone(self):
        """Gets the timezone of this MessagesIcs.  # noqa: E501


        :return: The timezone of this MessagesIcs.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this MessagesIcs.


        :param timezone: The timezone of this MessagesIcs.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def completed(self):
        """Gets the completed of this MessagesIcs.  # noqa: E501


        :return: The completed of this MessagesIcs.  # noqa: E501
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this MessagesIcs.


        :param completed: The completed of this MessagesIcs.  # noqa: E501
        :type: bool
        """

        self._completed = completed

    @property
    def avatar(self):
        """Gets the avatar of this MessagesIcs.  # noqa: E501


        :return: The avatar of this MessagesIcs.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this MessagesIcs.


        :param avatar: The avatar of this MessagesIcs.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def created_at(self):
        """Gets the created_at of this MessagesIcs.  # noqa: E501


        :return: The created_at of this MessagesIcs.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MessagesIcs.


        :param created_at: The created_at of this MessagesIcs.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

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
        if issubclass(MessagesIcs, dict):
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
        if not isinstance(other, MessagesIcs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
