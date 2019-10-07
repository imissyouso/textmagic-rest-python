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


class Conversation(object):
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
        'direction': 'str',
        'sender': 'str',
        'message_time': 'datetime',
        'text': 'str',
        'receiver': 'str',
        'status': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'session_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'direction': 'direction',
        'sender': 'sender',
        'message_time': 'messageTime',
        'text': 'text',
        'receiver': 'receiver',
        'status': 'status',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'session_id': 'sessionId'
    }

    def __init__(self, id=None, direction=None, sender=None, message_time=None, text=None, receiver=None, status=None, first_name=None, last_name=None, session_id=None):  # noqa: E501
        """Conversation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._direction = None
        self._sender = None
        self._message_time = None
        self._text = None
        self._receiver = None
        self._status = None
        self._first_name = None
        self._last_name = None
        self._session_id = None
        self.discriminator = None

        self.id = id
        self.direction = direction
        self.sender = sender
        self.message_time = message_time
        self.text = text
        self.receiver = receiver
        self.status = status
        self.first_name = first_name
        self.last_name = last_name
        self.session_id = session_id

    @property
    def id(self):
        """Gets the id of this Conversation.  # noqa: E501


        :return: The id of this Conversation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Conversation.


        :param id: The id of this Conversation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def direction(self):
        """Gets the direction of this Conversation.  # noqa: E501

        Message type: inbound or outbound.   # noqa: E501

        :return: The direction of this Conversation.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this Conversation.

        Message type: inbound or outbound.   # noqa: E501

        :param direction: The direction of this Conversation.  # noqa: E501
        :type: str
        """
        allowed_values = ["in", "out", "o", "i"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def sender(self):
        """Gets the sender of this Conversation.  # noqa: E501

        Sender phone number.  # noqa: E501

        :return: The sender of this Conversation.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this Conversation.

        Sender phone number.  # noqa: E501

        :param sender: The sender of this Conversation.  # noqa: E501
        :type: str
        """

        self._sender = sender

    @property
    def message_time(self):
        """Gets the message_time of this Conversation.  # noqa: E501

        Time when message arrived at TextMagic.  # noqa: E501

        :return: The message_time of this Conversation.  # noqa: E501
        :rtype: datetime
        """
        return self._message_time

    @message_time.setter
    def message_time(self, message_time):
        """Sets the message_time of this Conversation.

        Time when message arrived at TextMagic.  # noqa: E501

        :param message_time: The message_time of this Conversation.  # noqa: E501
        :type: datetime
        """

        self._message_time = message_time

    @property
    def text(self):
        """Gets the text of this Conversation.  # noqa: E501

        Message text.  # noqa: E501

        :return: The text of this Conversation.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Conversation.

        Message text.  # noqa: E501

        :param text: The text of this Conversation.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def receiver(self):
        """Gets the receiver of this Conversation.  # noqa: E501

        Receiver phone number.  # noqa: E501

        :return: The receiver of this Conversation.  # noqa: E501
        :rtype: str
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        """Sets the receiver of this Conversation.

        Receiver phone number.  # noqa: E501

        :param receiver: The receiver of this Conversation.  # noqa: E501
        :type: str
        """

        self._receiver = receiver

    @property
    def status(self):
        """Gets the status of this Conversation.  # noqa: E501

        Message status (for chats outbound only). See [message delivery statuses](/docs/api/sms-sessions/#message-delivery-statuses) for details.  # noqa: E501

        :return: The status of this Conversation.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Conversation.

        Message status (for chats outbound only). See [message delivery statuses](/docs/api/sms-sessions/#message-delivery-statuses) for details.  # noqa: E501

        :param status: The status of this Conversation.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def first_name(self):
        """Gets the first_name of this Conversation.  # noqa: E501

        Contact first name.  # noqa: E501

        :return: The first_name of this Conversation.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Conversation.

        Contact first name.  # noqa: E501

        :param first_name: The first_name of this Conversation.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Conversation.  # noqa: E501

        Contact last name.  # noqa: E501

        :return: The last_name of this Conversation.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Conversation.

        Contact last name.  # noqa: E501

        :param last_name: The last_name of this Conversation.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def session_id(self):
        """Gets the session_id of this Conversation.  # noqa: E501


        :return: The session_id of this Conversation.  # noqa: E501
        :rtype: int
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this Conversation.


        :param session_id: The session_id of this Conversation.  # noqa: E501
        :type: int
        """

        self._session_id = session_id

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
        if issubclass(Conversation, dict):
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
        if not isinstance(other, Conversation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
