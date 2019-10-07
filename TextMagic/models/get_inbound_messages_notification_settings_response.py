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


class GetInboundMessagesNotificationSettingsResponse(object):
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
        'inbound_message_notification': 'bool',
        'forwarded_call_notification': 'bool',
        'include_sms_history': 'bool',
        'send_in_html_format': 'bool',
        'alert_email1': 'str',
        'alert_email2': 'str',
        'alert_email3': 'str'
    }

    attribute_map = {
        'inbound_message_notification': 'inboundMessageNotification',
        'forwarded_call_notification': 'forwardedCallNotification',
        'include_sms_history': 'includeSmsHistory',
        'send_in_html_format': 'sendInHtmlFormat',
        'alert_email1': 'alertEmail1',
        'alert_email2': 'alertEmail2',
        'alert_email3': 'alertEmail3'
    }

    def __init__(self, inbound_message_notification=None, forwarded_call_notification=None, include_sms_history=None, send_in_html_format=None, alert_email1=None, alert_email2=None, alert_email3=None):  # noqa: E501
        """GetInboundMessagesNotificationSettingsResponse - a model defined in Swagger"""  # noqa: E501

        self._inbound_message_notification = None
        self._forwarded_call_notification = None
        self._include_sms_history = None
        self._send_in_html_format = None
        self._alert_email1 = None
        self._alert_email2 = None
        self._alert_email3 = None
        self.discriminator = None

        self.inbound_message_notification = inbound_message_notification
        self.forwarded_call_notification = forwarded_call_notification
        self.include_sms_history = include_sms_history
        self.send_in_html_format = send_in_html_format
        self.alert_email1 = alert_email1
        self.alert_email2 = alert_email2
        self.alert_email3 = alert_email3

    @property
    def inbound_message_notification(self):
        """Gets the inbound_message_notification of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501

        Should user receive notification about new incoming messages  # noqa: E501

        :return: The inbound_message_notification of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._inbound_message_notification

    @inbound_message_notification.setter
    def inbound_message_notification(self, inbound_message_notification):
        """Sets the inbound_message_notification of this GetInboundMessagesNotificationSettingsResponse.

        Should user receive notification about new incoming messages  # noqa: E501

        :param inbound_message_notification: The inbound_message_notification of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501
        :type: bool
        """

        self._inbound_message_notification = inbound_message_notification

    @property
    def forwarded_call_notification(self):
        """Gets the forwarded_call_notification of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501

        Should user receive notification about new forwarded calls  # noqa: E501

        :return: The forwarded_call_notification of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._forwarded_call_notification

    @forwarded_call_notification.setter
    def forwarded_call_notification(self, forwarded_call_notification):
        """Sets the forwarded_call_notification of this GetInboundMessagesNotificationSettingsResponse.

        Should user receive notification about new forwarded calls  # noqa: E501

        :param forwarded_call_notification: The forwarded_call_notification of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501
        :type: bool
        """

        self._forwarded_call_notification = forwarded_call_notification

    @property
    def include_sms_history(self):
        """Gets the include_sms_history of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501

        Include SMS history into notification Email  # noqa: E501

        :return: The include_sms_history of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._include_sms_history

    @include_sms_history.setter
    def include_sms_history(self, include_sms_history):
        """Sets the include_sms_history of this GetInboundMessagesNotificationSettingsResponse.

        Include SMS history into notification Email  # noqa: E501

        :param include_sms_history: The include_sms_history of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501
        :type: bool
        """

        self._include_sms_history = include_sms_history

    @property
    def send_in_html_format(self):
        """Gets the send_in_html_format of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501

        Send Email notification in HTML format  # noqa: E501

        :return: The send_in_html_format of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._send_in_html_format

    @send_in_html_format.setter
    def send_in_html_format(self, send_in_html_format):
        """Sets the send_in_html_format of this GetInboundMessagesNotificationSettingsResponse.

        Send Email notification in HTML format  # noqa: E501

        :param send_in_html_format: The send_in_html_format of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501
        :type: bool
        """

        self._send_in_html_format = send_in_html_format

    @property
    def alert_email1(self):
        """Gets the alert_email1 of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501

        New message notification email 2  # noqa: E501

        :return: The alert_email1 of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501
        :rtype: str
        """
        return self._alert_email1

    @alert_email1.setter
    def alert_email1(self, alert_email1):
        """Sets the alert_email1 of this GetInboundMessagesNotificationSettingsResponse.

        New message notification email 2  # noqa: E501

        :param alert_email1: The alert_email1 of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501
        :type: str
        """

        self._alert_email1 = alert_email1

    @property
    def alert_email2(self):
        """Gets the alert_email2 of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501

        New message notification email 2  # noqa: E501

        :return: The alert_email2 of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501
        :rtype: str
        """
        return self._alert_email2

    @alert_email2.setter
    def alert_email2(self, alert_email2):
        """Sets the alert_email2 of this GetInboundMessagesNotificationSettingsResponse.

        New message notification email 2  # noqa: E501

        :param alert_email2: The alert_email2 of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501
        :type: str
        """

        self._alert_email2 = alert_email2

    @property
    def alert_email3(self):
        """Gets the alert_email3 of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501

        New message notification email 3  # noqa: E501

        :return: The alert_email3 of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501
        :rtype: str
        """
        return self._alert_email3

    @alert_email3.setter
    def alert_email3(self, alert_email3):
        """Sets the alert_email3 of this GetInboundMessagesNotificationSettingsResponse.

        New message notification email 3  # noqa: E501

        :param alert_email3: The alert_email3 of this GetInboundMessagesNotificationSettingsResponse.  # noqa: E501
        :type: str
        """

        self._alert_email3 = alert_email3

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
        if issubclass(GetInboundMessagesNotificationSettingsResponse, dict):
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
        if not isinstance(other, GetInboundMessagesNotificationSettingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
