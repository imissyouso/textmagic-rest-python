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


class MessagingStatItem(object):
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
        'reply_rate': 'float',
        '_date': 'datetime',
        'delivery_rate': 'float',
        'costs': 'float',
        'messages_received': 'int',
        'messages_sent_delivered': 'int',
        'messages_sent_accepted': 'int',
        'messages_sent_buffered': 'int',
        'messages_sent_failed': 'int',
        'messages_sent_rejected': 'int',
        'messages_sent_parts': 'int'
    }

    attribute_map = {
        'reply_rate': 'replyRate',
        '_date': 'date',
        'delivery_rate': 'deliveryRate',
        'costs': 'costs',
        'messages_received': 'messagesReceived',
        'messages_sent_delivered': 'messagesSentDelivered',
        'messages_sent_accepted': 'messagesSentAccepted',
        'messages_sent_buffered': 'messagesSentBuffered',
        'messages_sent_failed': 'messagesSentFailed',
        'messages_sent_rejected': 'messagesSentRejected',
        'messages_sent_parts': 'messagesSentParts'
    }

    def __init__(self, reply_rate=None, _date=None, delivery_rate=None, costs=None, messages_received=None, messages_sent_delivered=None, messages_sent_accepted=None, messages_sent_buffered=None, messages_sent_failed=None, messages_sent_rejected=None, messages_sent_parts=None):  # noqa: E501
        """MessagingStatItem - a model defined in Swagger"""  # noqa: E501

        self._reply_rate = None
        self.__date = None
        self._delivery_rate = None
        self._costs = None
        self._messages_received = None
        self._messages_sent_delivered = None
        self._messages_sent_accepted = None
        self._messages_sent_buffered = None
        self._messages_sent_failed = None
        self._messages_sent_rejected = None
        self._messages_sent_parts = None
        self.discriminator = None

        self.reply_rate = reply_rate
        self._date = _date
        self.delivery_rate = delivery_rate
        self.costs = costs
        self.messages_received = messages_received
        self.messages_sent_delivered = messages_sent_delivered
        self.messages_sent_accepted = messages_sent_accepted
        self.messages_sent_buffered = messages_sent_buffered
        self.messages_sent_failed = messages_sent_failed
        self.messages_sent_rejected = messages_sent_rejected
        self.messages_sent_parts = messages_sent_parts

    @property
    def reply_rate(self):
        """Gets the reply_rate of this MessagingStatItem.  # noqa: E501


        :return: The reply_rate of this MessagingStatItem.  # noqa: E501
        :rtype: float
        """
        return self._reply_rate

    @reply_rate.setter
    def reply_rate(self, reply_rate):
        """Sets the reply_rate of this MessagingStatItem.


        :param reply_rate: The reply_rate of this MessagingStatItem.  # noqa: E501
        :type: float
        """

        self._reply_rate = reply_rate

    @property
    def _date(self):
        """Gets the _date of this MessagingStatItem.  # noqa: E501


        :return: The _date of this MessagingStatItem.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this MessagingStatItem.


        :param _date: The _date of this MessagingStatItem.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def delivery_rate(self):
        """Gets the delivery_rate of this MessagingStatItem.  # noqa: E501


        :return: The delivery_rate of this MessagingStatItem.  # noqa: E501
        :rtype: float
        """
        return self._delivery_rate

    @delivery_rate.setter
    def delivery_rate(self, delivery_rate):
        """Sets the delivery_rate of this MessagingStatItem.


        :param delivery_rate: The delivery_rate of this MessagingStatItem.  # noqa: E501
        :type: float
        """

        self._delivery_rate = delivery_rate

    @property
    def costs(self):
        """Gets the costs of this MessagingStatItem.  # noqa: E501


        :return: The costs of this MessagingStatItem.  # noqa: E501
        :rtype: float
        """
        return self._costs

    @costs.setter
    def costs(self, costs):
        """Sets the costs of this MessagingStatItem.


        :param costs: The costs of this MessagingStatItem.  # noqa: E501
        :type: float
        """

        self._costs = costs

    @property
    def messages_received(self):
        """Gets the messages_received of this MessagingStatItem.  # noqa: E501


        :return: The messages_received of this MessagingStatItem.  # noqa: E501
        :rtype: int
        """
        return self._messages_received

    @messages_received.setter
    def messages_received(self, messages_received):
        """Sets the messages_received of this MessagingStatItem.


        :param messages_received: The messages_received of this MessagingStatItem.  # noqa: E501
        :type: int
        """

        self._messages_received = messages_received

    @property
    def messages_sent_delivered(self):
        """Gets the messages_sent_delivered of this MessagingStatItem.  # noqa: E501


        :return: The messages_sent_delivered of this MessagingStatItem.  # noqa: E501
        :rtype: int
        """
        return self._messages_sent_delivered

    @messages_sent_delivered.setter
    def messages_sent_delivered(self, messages_sent_delivered):
        """Sets the messages_sent_delivered of this MessagingStatItem.


        :param messages_sent_delivered: The messages_sent_delivered of this MessagingStatItem.  # noqa: E501
        :type: int
        """

        self._messages_sent_delivered = messages_sent_delivered

    @property
    def messages_sent_accepted(self):
        """Gets the messages_sent_accepted of this MessagingStatItem.  # noqa: E501


        :return: The messages_sent_accepted of this MessagingStatItem.  # noqa: E501
        :rtype: int
        """
        return self._messages_sent_accepted

    @messages_sent_accepted.setter
    def messages_sent_accepted(self, messages_sent_accepted):
        """Sets the messages_sent_accepted of this MessagingStatItem.


        :param messages_sent_accepted: The messages_sent_accepted of this MessagingStatItem.  # noqa: E501
        :type: int
        """

        self._messages_sent_accepted = messages_sent_accepted

    @property
    def messages_sent_buffered(self):
        """Gets the messages_sent_buffered of this MessagingStatItem.  # noqa: E501


        :return: The messages_sent_buffered of this MessagingStatItem.  # noqa: E501
        :rtype: int
        """
        return self._messages_sent_buffered

    @messages_sent_buffered.setter
    def messages_sent_buffered(self, messages_sent_buffered):
        """Sets the messages_sent_buffered of this MessagingStatItem.


        :param messages_sent_buffered: The messages_sent_buffered of this MessagingStatItem.  # noqa: E501
        :type: int
        """

        self._messages_sent_buffered = messages_sent_buffered

    @property
    def messages_sent_failed(self):
        """Gets the messages_sent_failed of this MessagingStatItem.  # noqa: E501


        :return: The messages_sent_failed of this MessagingStatItem.  # noqa: E501
        :rtype: int
        """
        return self._messages_sent_failed

    @messages_sent_failed.setter
    def messages_sent_failed(self, messages_sent_failed):
        """Sets the messages_sent_failed of this MessagingStatItem.


        :param messages_sent_failed: The messages_sent_failed of this MessagingStatItem.  # noqa: E501
        :type: int
        """

        self._messages_sent_failed = messages_sent_failed

    @property
    def messages_sent_rejected(self):
        """Gets the messages_sent_rejected of this MessagingStatItem.  # noqa: E501


        :return: The messages_sent_rejected of this MessagingStatItem.  # noqa: E501
        :rtype: int
        """
        return self._messages_sent_rejected

    @messages_sent_rejected.setter
    def messages_sent_rejected(self, messages_sent_rejected):
        """Sets the messages_sent_rejected of this MessagingStatItem.


        :param messages_sent_rejected: The messages_sent_rejected of this MessagingStatItem.  # noqa: E501
        :type: int
        """

        self._messages_sent_rejected = messages_sent_rejected

    @property
    def messages_sent_parts(self):
        """Gets the messages_sent_parts of this MessagingStatItem.  # noqa: E501


        :return: The messages_sent_parts of this MessagingStatItem.  # noqa: E501
        :rtype: int
        """
        return self._messages_sent_parts

    @messages_sent_parts.setter
    def messages_sent_parts(self, messages_sent_parts):
        """Sets the messages_sent_parts of this MessagingStatItem.


        :param messages_sent_parts: The messages_sent_parts of this MessagingStatItem.  # noqa: E501
        :type: int
        """

        self._messages_sent_parts = messages_sent_parts

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
        if issubclass(MessagingStatItem, dict):
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
        if not isinstance(other, MessagingStatItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
