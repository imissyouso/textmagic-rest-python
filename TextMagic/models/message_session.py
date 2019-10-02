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


class MessageSession(object):
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
        'start_time': 'str',
        'text': 'str',
        'source': 'str',
        'reference_id': 'str',
        'price': 'float',
        'numbers_count': 'int',
        'destination': 'str'
    }

    attribute_map = {
        'id': 'id',
        'start_time': 'startTime',
        'text': 'text',
        'source': 'source',
        'reference_id': 'referenceId',
        'price': 'price',
        'numbers_count': 'numbersCount',
        'destination': 'destination'
    }

    def __init__(self, id=None, start_time=None, text=None, source=None, reference_id=None, price=None, numbers_count=None, destination=None):  # noqa: E501
        """MessageSession - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._start_time = None
        self._text = None
        self._source = None
        self._reference_id = None
        self._price = None
        self._numbers_count = None
        self._destination = None
        self.discriminator = None

        self.id = id
        self.start_time = start_time
        self.text = text
        self.source = source
        self.reference_id = reference_id
        self.price = price
        self.numbers_count = numbers_count
        self.destination = destination

    @property
    def id(self):
        """Gets the id of this MessageSession.  # noqa: E501

        Session ID.  # noqa: E501

        :return: The id of this MessageSession.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MessageSession.

        Session ID.  # noqa: E501

        :param id: The id of this MessageSession.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def start_time(self):
        """Gets the start_time of this MessageSession.  # noqa: E501

        Session creation time.  # noqa: E501

        :return: The start_time of this MessageSession.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this MessageSession.

        Session creation time.  # noqa: E501

        :param start_time: The start_time of this MessageSession.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def text(self):
        """Gets the text of this MessageSession.  # noqa: E501

        Session text. If a template was used for the session text (see [Messages: Send](#tag/Outbound-Messages) for details), it may contain template tags.   # noqa: E501

        :return: The text of this MessageSession.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this MessageSession.

        Session text. If a template was used for the session text (see [Messages: Send](#tag/Outbound-Messages) for details), it may contain template tags.   # noqa: E501

        :param text: The text of this MessageSession.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def source(self):
        """Gets the source of this MessageSession.  # noqa: E501

        *   **O** for TextMagic Online *   **A** for API *   **M** for TextMagic Messenger *   **E** for [Email to SMS](/docs/api/send-email-to-sms/) *   **X** for [Distribution lists](/docs/api/distribution-lists/)   # noqa: E501

        :return: The source of this MessageSession.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this MessageSession.

        *   **O** for TextMagic Online *   **A** for API *   **M** for TextMagic Messenger *   **E** for [Email to SMS](/docs/api/send-email-to-sms/) *   **X** for [Distribution lists](/docs/api/distribution-lists/)   # noqa: E501

        :param source: The source of this MessageSession.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def reference_id(self):
        """Gets the reference_id of this MessageSession.  # noqa: E501

        Custom reference ID (see [Messages: Send](/docs/api/send-sms/) for details).   # noqa: E501

        :return: The reference_id of this MessageSession.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this MessageSession.

        Custom reference ID (see [Messages: Send](/docs/api/send-sms/) for details).   # noqa: E501

        :param reference_id: The reference_id of this MessageSession.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

    @property
    def price(self):
        """Gets the price of this MessageSession.  # noqa: E501

        Session cost (in account currency).  # noqa: E501

        :return: The price of this MessageSession.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this MessageSession.

        Session cost (in account currency).  # noqa: E501

        :param price: The price of this MessageSession.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def numbers_count(self):
        """Gets the numbers_count of this MessageSession.  # noqa: E501

        Session recipient count.  # noqa: E501

        :return: The numbers_count of this MessageSession.  # noqa: E501
        :rtype: int
        """
        return self._numbers_count

    @numbers_count.setter
    def numbers_count(self, numbers_count):
        """Sets the numbers_count of this MessageSession.

        Session recipient count.  # noqa: E501

        :param numbers_count: The numbers_count of this MessageSession.  # noqa: E501
        :type: int
        """

        self._numbers_count = numbers_count

    @property
    def destination(self):
        """Gets the destination of this MessageSession.  # noqa: E501


        :return: The destination of this MessageSession.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this MessageSession.


        :param destination: The destination of this MessageSession.  # noqa: E501
        :type: str
        """

        self._destination = destination

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
        if issubclass(MessageSession, dict):
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
        if not isinstance(other, MessageSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
