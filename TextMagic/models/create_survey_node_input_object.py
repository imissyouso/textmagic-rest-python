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


class CreateSurveyNodeInputObject(object):
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
        'node_type': 'str',
        'label': 'str',
        'body': 'str',
        'start_node': 'int',
        'send_delay': 'int'
    }

    attribute_map = {
        'node_type': 'nodeType',
        'label': 'label',
        'body': 'body',
        'start_node': 'startNode',
        'send_delay': 'sendDelay'
    }

    def __init__(self, node_type=None, label=None, body=None, start_node=None, send_delay=None):  # noqa: E501
        """CreateSurveyNodeInputObject - a model defined in Swagger"""  # noqa: E501

        self._node_type = None
        self._label = None
        self._body = None
        self._start_node = None
        self._send_delay = None
        self.discriminator = None

        if node_type is not None:
            self.node_type = node_type
        if label is not None:
            self.label = label
        if body is not None:
            self.body = body
        if start_node is not None:
            self.start_node = start_node
        if send_delay is not None:
            self.send_delay = send_delay

    @property
    def node_type(self):
        """Gets the node_type of this CreateSurveyNodeInputObject.  # noqa: E501

        Node type. \\'a\\' answer; \\'q\\' - question  # noqa: E501

        :return: The node_type of this CreateSurveyNodeInputObject.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this CreateSurveyNodeInputObject.

        Node type. \\'a\\' answer; \\'q\\' - question  # noqa: E501

        :param node_type: The node_type of this CreateSurveyNodeInputObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["a", "q"]  # noqa: E501
        if node_type not in allowed_values:
            raise ValueError(
                "Invalid value for `node_type` ({0}), must be one of {1}"  # noqa: E501
                .format(node_type, allowed_values)
            )

        self._node_type = node_type

    @property
    def label(self):
        """Gets the label of this CreateSurveyNodeInputObject.  # noqa: E501

        Node label  # noqa: E501

        :return: The label of this CreateSurveyNodeInputObject.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CreateSurveyNodeInputObject.

        Node label  # noqa: E501

        :param label: The label of this CreateSurveyNodeInputObject.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def body(self):
        """Gets the body of this CreateSurveyNodeInputObject.  # noqa: E501

        Node body  # noqa: E501

        :return: The body of this CreateSurveyNodeInputObject.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateSurveyNodeInputObject.

        Node body  # noqa: E501

        :param body: The body of this CreateSurveyNodeInputObject.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def start_node(self):
        """Gets the start_node of this CreateSurveyNodeInputObject.  # noqa: E501

        Start node id  # noqa: E501

        :return: The start_node of this CreateSurveyNodeInputObject.  # noqa: E501
        :rtype: int
        """
        return self._start_node

    @start_node.setter
    def start_node(self, start_node):
        """Sets the start_node of this CreateSurveyNodeInputObject.

        Start node id  # noqa: E501

        :param start_node: The start_node of this CreateSurveyNodeInputObject.  # noqa: E501
        :type: int
        """

        self._start_node = start_node

    @property
    def send_delay(self):
        """Gets the send_delay of this CreateSurveyNodeInputObject.  # noqa: E501

        Define delay for sending question to recipients after previous answer.  # noqa: E501

        :return: The send_delay of this CreateSurveyNodeInputObject.  # noqa: E501
        :rtype: int
        """
        return self._send_delay

    @send_delay.setter
    def send_delay(self, send_delay):
        """Sets the send_delay of this CreateSurveyNodeInputObject.

        Define delay for sending question to recipients after previous answer.  # noqa: E501

        :param send_delay: The send_delay of this CreateSurveyNodeInputObject.  # noqa: E501
        :type: int
        """

        self._send_delay = send_delay

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
        if issubclass(CreateSurveyNodeInputObject, dict):
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
        if not isinstance(other, CreateSurveyNodeInputObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
