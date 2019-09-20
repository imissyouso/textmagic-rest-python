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


class SurveyNode(object):
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
        'label': 'str',
        'body': 'str',
        'node_type': 'str',
        'is_end_node': 'bool',
        'send_delay': 'int',
        'start_nodes': 'list[str]',
        'end_nodes': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'label': 'label',
        'body': 'body',
        'node_type': 'nodeType',
        'is_end_node': 'isEndNode',
        'send_delay': 'sendDelay',
        'start_nodes': 'startNodes',
        'end_nodes': 'endNodes'
    }

    def __init__(self, id=None, label=None, body=None, node_type=None, is_end_node=None, send_delay=None, start_nodes=None, end_nodes=None):  # noqa: E501
        """SurveyNode - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._label = None
        self._body = None
        self._node_type = None
        self._is_end_node = None
        self._send_delay = None
        self._start_nodes = None
        self._end_nodes = None
        self.discriminator = None

        self.id = id
        self.label = label
        self.body = body
        self.node_type = node_type
        self.is_end_node = is_end_node
        self.send_delay = send_delay
        self.start_nodes = start_nodes
        self.end_nodes = end_nodes

    @property
    def id(self):
        """Gets the id of this SurveyNode.  # noqa: E501


        :return: The id of this SurveyNode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SurveyNode.


        :param id: The id of this SurveyNode.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this SurveyNode.  # noqa: E501


        :return: The label of this SurveyNode.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SurveyNode.


        :param label: The label of this SurveyNode.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def body(self):
        """Gets the body of this SurveyNode.  # noqa: E501


        :return: The body of this SurveyNode.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SurveyNode.


        :param body: The body of this SurveyNode.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def node_type(self):
        """Gets the node_type of this SurveyNode.  # noqa: E501


        :return: The node_type of this SurveyNode.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this SurveyNode.


        :param node_type: The node_type of this SurveyNode.  # noqa: E501
        :type: str
        """

        self._node_type = node_type

    @property
    def is_end_node(self):
        """Gets the is_end_node of this SurveyNode.  # noqa: E501


        :return: The is_end_node of this SurveyNode.  # noqa: E501
        :rtype: bool
        """
        return self._is_end_node

    @is_end_node.setter
    def is_end_node(self, is_end_node):
        """Sets the is_end_node of this SurveyNode.


        :param is_end_node: The is_end_node of this SurveyNode.  # noqa: E501
        :type: bool
        """

        self._is_end_node = is_end_node

    @property
    def send_delay(self):
        """Gets the send_delay of this SurveyNode.  # noqa: E501


        :return: The send_delay of this SurveyNode.  # noqa: E501
        :rtype: int
        """
        return self._send_delay

    @send_delay.setter
    def send_delay(self, send_delay):
        """Sets the send_delay of this SurveyNode.


        :param send_delay: The send_delay of this SurveyNode.  # noqa: E501
        :type: int
        """

        self._send_delay = send_delay

    @property
    def start_nodes(self):
        """Gets the start_nodes of this SurveyNode.  # noqa: E501


        :return: The start_nodes of this SurveyNode.  # noqa: E501
        :rtype: list[str]
        """
        return self._start_nodes

    @start_nodes.setter
    def start_nodes(self, start_nodes):
        """Sets the start_nodes of this SurveyNode.


        :param start_nodes: The start_nodes of this SurveyNode.  # noqa: E501
        :type: list[str]
        """

        self._start_nodes = start_nodes

    @property
    def end_nodes(self):
        """Gets the end_nodes of this SurveyNode.  # noqa: E501


        :return: The end_nodes of this SurveyNode.  # noqa: E501
        :rtype: list[str]
        """
        return self._end_nodes

    @end_nodes.setter
    def end_nodes(self, end_nodes):
        """Sets the end_nodes of this SurveyNode.


        :param end_nodes: The end_nodes of this SurveyNode.  # noqa: E501
        :type: list[str]
        """

        self._end_nodes = end_nodes

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
        if issubclass(SurveyNode, dict):
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
        if not isinstance(other, SurveyNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
