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


class DoEmailLookupResponse(object):
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
        'address': 'str',
        'address_type': 'str',
        'email_role': 'str',
        'reason': 'str',
        'status': 'str',
        'deliverability': 'str',
        'is_disposable_address': 'bool',
        'local_part': 'str',
        'domain_part': 'str',
        'exchange': 'str',
        'is_in_white_list': 'bool',
        'is_in_black_list': 'bool',
        'has_mx': 'bool',
        'has_aa': 'bool',
        'has_aaaa': 'bool',
        'risk': 'str',
        'preference': 'int',
        'suggestion': 'str'
    }

    attribute_map = {
        'address': 'address',
        'address_type': 'addressType',
        'email_role': 'emailRole',
        'reason': 'reason',
        'status': 'status',
        'deliverability': 'deliverability',
        'is_disposable_address': 'isDisposableAddress',
        'local_part': 'localPart',
        'domain_part': 'domainPart',
        'exchange': 'exchange',
        'is_in_white_list': 'isInWhiteList',
        'is_in_black_list': 'isInBlackList',
        'has_mx': 'hasMx',
        'has_aa': 'hasAa',
        'has_aaaa': 'hasAaaa',
        'risk': 'risk',
        'preference': 'preference',
        'suggestion': 'suggestion'
    }

    def __init__(self, address=None, address_type=None, email_role=None, reason=None, status=None, deliverability=None, is_disposable_address=None, local_part=None, domain_part=None, exchange=None, is_in_white_list=None, is_in_black_list=None, has_mx=None, has_aa=None, has_aaaa=None, risk=None, preference=None, suggestion=None):  # noqa: E501
        """DoEmailLookupResponse - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._address_type = None
        self._email_role = None
        self._reason = None
        self._status = None
        self._deliverability = None
        self._is_disposable_address = None
        self._local_part = None
        self._domain_part = None
        self._exchange = None
        self._is_in_white_list = None
        self._is_in_black_list = None
        self._has_mx = None
        self._has_aa = None
        self._has_aaaa = None
        self._risk = None
        self._preference = None
        self._suggestion = None
        self.discriminator = None

        self.address = address
        self.address_type = address_type
        self.email_role = email_role
        self.reason = reason
        self.status = status
        self.deliverability = deliverability
        self.is_disposable_address = is_disposable_address
        self.local_part = local_part
        self.domain_part = domain_part
        self.exchange = exchange
        self.is_in_white_list = is_in_white_list
        self.is_in_black_list = is_in_black_list
        self.has_mx = has_mx
        self.has_aa = has_aa
        self.has_aaaa = has_aaaa
        self.risk = risk
        self.preference = preference
        self.suggestion = suggestion

    @property
    def address(self):
        """Gets the address of this DoEmailLookupResponse.  # noqa: E501


        :return: The address of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this DoEmailLookupResponse.


        :param address: The address of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def address_type(self):
        """Gets the address_type of this DoEmailLookupResponse.  # noqa: E501


        :return: The address_type of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this DoEmailLookupResponse.


        :param address_type: The address_type of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """

        self._address_type = address_type

    @property
    def email_role(self):
        """Gets the email_role of this DoEmailLookupResponse.  # noqa: E501


        :return: The email_role of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._email_role

    @email_role.setter
    def email_role(self, email_role):
        """Sets the email_role of this DoEmailLookupResponse.


        :param email_role: The email_role of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """

        self._email_role = email_role

    @property
    def reason(self):
        """Gets the reason of this DoEmailLookupResponse.  # noqa: E501


        :return: The reason of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this DoEmailLookupResponse.


        :param reason: The reason of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def status(self):
        """Gets the status of this DoEmailLookupResponse.  # noqa: E501


        :return: The status of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DoEmailLookupResponse.


        :param status: The status of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["valid", "invalid"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def deliverability(self):
        """Gets the deliverability of this DoEmailLookupResponse.  # noqa: E501


        :return: The deliverability of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._deliverability

    @deliverability.setter
    def deliverability(self, deliverability):
        """Sets the deliverability of this DoEmailLookupResponse.


        :param deliverability: The deliverability of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """

        self._deliverability = deliverability

    @property
    def is_disposable_address(self):
        """Gets the is_disposable_address of this DoEmailLookupResponse.  # noqa: E501


        :return: The is_disposable_address of this DoEmailLookupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_disposable_address

    @is_disposable_address.setter
    def is_disposable_address(self, is_disposable_address):
        """Sets the is_disposable_address of this DoEmailLookupResponse.


        :param is_disposable_address: The is_disposable_address of this DoEmailLookupResponse.  # noqa: E501
        :type: bool
        """

        self._is_disposable_address = is_disposable_address

    @property
    def local_part(self):
        """Gets the local_part of this DoEmailLookupResponse.  # noqa: E501


        :return: The local_part of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._local_part

    @local_part.setter
    def local_part(self, local_part):
        """Sets the local_part of this DoEmailLookupResponse.


        :param local_part: The local_part of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """

        self._local_part = local_part

    @property
    def domain_part(self):
        """Gets the domain_part of this DoEmailLookupResponse.  # noqa: E501


        :return: The domain_part of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._domain_part

    @domain_part.setter
    def domain_part(self, domain_part):
        """Sets the domain_part of this DoEmailLookupResponse.


        :param domain_part: The domain_part of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """

        self._domain_part = domain_part

    @property
    def exchange(self):
        """Gets the exchange of this DoEmailLookupResponse.  # noqa: E501


        :return: The exchange of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this DoEmailLookupResponse.


        :param exchange: The exchange of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """

        self._exchange = exchange

    @property
    def is_in_white_list(self):
        """Gets the is_in_white_list of this DoEmailLookupResponse.  # noqa: E501


        :return: The is_in_white_list of this DoEmailLookupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_in_white_list

    @is_in_white_list.setter
    def is_in_white_list(self, is_in_white_list):
        """Sets the is_in_white_list of this DoEmailLookupResponse.


        :param is_in_white_list: The is_in_white_list of this DoEmailLookupResponse.  # noqa: E501
        :type: bool
        """

        self._is_in_white_list = is_in_white_list

    @property
    def is_in_black_list(self):
        """Gets the is_in_black_list of this DoEmailLookupResponse.  # noqa: E501


        :return: The is_in_black_list of this DoEmailLookupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_in_black_list

    @is_in_black_list.setter
    def is_in_black_list(self, is_in_black_list):
        """Sets the is_in_black_list of this DoEmailLookupResponse.


        :param is_in_black_list: The is_in_black_list of this DoEmailLookupResponse.  # noqa: E501
        :type: bool
        """

        self._is_in_black_list = is_in_black_list

    @property
    def has_mx(self):
        """Gets the has_mx of this DoEmailLookupResponse.  # noqa: E501


        :return: The has_mx of this DoEmailLookupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_mx

    @has_mx.setter
    def has_mx(self, has_mx):
        """Sets the has_mx of this DoEmailLookupResponse.


        :param has_mx: The has_mx of this DoEmailLookupResponse.  # noqa: E501
        :type: bool
        """

        self._has_mx = has_mx

    @property
    def has_aa(self):
        """Gets the has_aa of this DoEmailLookupResponse.  # noqa: E501


        :return: The has_aa of this DoEmailLookupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_aa

    @has_aa.setter
    def has_aa(self, has_aa):
        """Sets the has_aa of this DoEmailLookupResponse.


        :param has_aa: The has_aa of this DoEmailLookupResponse.  # noqa: E501
        :type: bool
        """

        self._has_aa = has_aa

    @property
    def has_aaaa(self):
        """Gets the has_aaaa of this DoEmailLookupResponse.  # noqa: E501


        :return: The has_aaaa of this DoEmailLookupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_aaaa

    @has_aaaa.setter
    def has_aaaa(self, has_aaaa):
        """Sets the has_aaaa of this DoEmailLookupResponse.


        :param has_aaaa: The has_aaaa of this DoEmailLookupResponse.  # noqa: E501
        :type: bool
        """

        self._has_aaaa = has_aaaa

    @property
    def risk(self):
        """Gets the risk of this DoEmailLookupResponse.  # noqa: E501


        :return: The risk of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._risk

    @risk.setter
    def risk(self, risk):
        """Sets the risk of this DoEmailLookupResponse.


        :param risk: The risk of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """

        self._risk = risk

    @property
    def preference(self):
        """Gets the preference of this DoEmailLookupResponse.  # noqa: E501


        :return: The preference of this DoEmailLookupResponse.  # noqa: E501
        :rtype: int
        """
        return self._preference

    @preference.setter
    def preference(self, preference):
        """Sets the preference of this DoEmailLookupResponse.


        :param preference: The preference of this DoEmailLookupResponse.  # noqa: E501
        :type: int
        """

        self._preference = preference

    @property
    def suggestion(self):
        """Gets the suggestion of this DoEmailLookupResponse.  # noqa: E501


        :return: The suggestion of this DoEmailLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this DoEmailLookupResponse.


        :param suggestion: The suggestion of this DoEmailLookupResponse.  # noqa: E501
        :type: str
        """

        self._suggestion = suggestion

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
        if issubclass(DoEmailLookupResponse, dict):
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
        if not isinstance(other, DoEmailLookupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
