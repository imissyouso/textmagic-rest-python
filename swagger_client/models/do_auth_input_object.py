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


        class DoAuthInputObject(object):
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
            'username': 'str',
            'password': 'str',
            'app_name': 'str',
            'app_version': 'str',
            'device_id': 'str',
            'push_service_type': 'str',
            'tfa_code': 'str',
            'tfa_id': 'str'
        }

        attribute_map = {
            'username': 'username',
            'password': 'password',
            'app_name': 'appName',
            'app_version': 'appVersion',
            'device_id': 'deviceId',
            'push_service_type': 'pushServiceType',
            'tfa_code': 'tfaCode',
            'tfa_id': 'tfaId'
        }

        def __init__(self, username=None, password=None, app_name=None, app_version=None, device_id=None, push_service_type=None, tfa_code=None, tfa_id=None):  # noqa: E501
        """DoAuthInputObject - a model defined in Swagger"""  # noqa: E501
        
        self._username = None
        self._password = None
        self._app_name = None
        self._app_version = None
        self._device_id = None
        self._push_service_type = None
        self._tfa_code = None
        self._tfa_id = None
        self.discriminator = None
        
            self.username = username
            self.password = password
            if app_name is not None:
            self.app_name = app_name
            if app_version is not None:
            self.app_version = app_version
            if device_id is not None:
            self.device_id = device_id
            if push_service_type is not None:
            self.push_service_type = push_service_type
            if tfa_code is not None:
            self.tfa_code = tfa_code
            if tfa_id is not None:
            self.tfa_id = tfa_id

            @property
            def username(self):
            """Gets the username of this DoAuthInputObject.  # noqa: E501

                Account username or email  # noqa: E501

            :return: The username of this DoAuthInputObject.  # noqa: E501
            :rtype: str
            """
            return self._username

            @username.setter
            def username(self, username):
            """Sets the username of this DoAuthInputObject.

                Account username or email  # noqa: E501

            :param username: The username of this DoAuthInputObject.  # noqa: E501
            :type: str
            """

            self._username = username

            @property
            def password(self):
            """Gets the password of this DoAuthInputObject.  # noqa: E501

                Account password  # noqa: E501

            :return: The password of this DoAuthInputObject.  # noqa: E501
            :rtype: str
            """
            return self._password

            @password.setter
            def password(self, password):
            """Sets the password of this DoAuthInputObject.

                Account password  # noqa: E501

            :param password: The password of this DoAuthInputObject.  # noqa: E501
            :type: str
            """

            self._password = password

            @property
            def app_name(self):
            """Gets the app_name of this DoAuthInputObject.  # noqa: E501

                Application name  # noqa: E501

            :return: The app_name of this DoAuthInputObject.  # noqa: E501
            :rtype: str
            """
            return self._app_name

            @app_name.setter
            def app_name(self, app_name):
            """Sets the app_name of this DoAuthInputObject.

                Application name  # noqa: E501

            :param app_name: The app_name of this DoAuthInputObject.  # noqa: E501
            :type: str
            """

            self._app_name = app_name

            @property
            def app_version(self):
            """Gets the app_version of this DoAuthInputObject.  # noqa: E501

                Application version  # noqa: E501

            :return: The app_version of this DoAuthInputObject.  # noqa: E501
            :rtype: str
            """
            return self._app_version

            @app_version.setter
            def app_version(self, app_version):
            """Sets the app_version of this DoAuthInputObject.

                Application version  # noqa: E501

            :param app_version: The app_version of this DoAuthInputObject.  # noqa: E501
            :type: str
            """

            self._app_version = app_version

            @property
            def device_id(self):
            """Gets the device_id of this DoAuthInputObject.  # noqa: E501

                Device ID for push notification service  # noqa: E501

            :return: The device_id of this DoAuthInputObject.  # noqa: E501
            :rtype: str
            """
            return self._device_id

            @device_id.setter
            def device_id(self, device_id):
            """Sets the device_id of this DoAuthInputObject.

                Device ID for push notification service  # noqa: E501

            :param device_id: The device_id of this DoAuthInputObject.  # noqa: E501
            :type: str
            """

            self._device_id = device_id

            @property
            def push_service_type(self):
            """Gets the push_service_type of this DoAuthInputObject.  # noqa: E501

                required when deviceId provided. Push notification service type: a for Apple Push Notifications, g for Google Cloud Messaging  # noqa: E501

            :return: The push_service_type of this DoAuthInputObject.  # noqa: E501
            :rtype: str
            """
            return self._push_service_type

            @push_service_type.setter
            def push_service_type(self, push_service_type):
            """Sets the push_service_type of this DoAuthInputObject.

                required when deviceId provided. Push notification service type: a for Apple Push Notifications, g for Google Cloud Messaging  # noqa: E501

            :param push_service_type: The push_service_type of this DoAuthInputObject.  # noqa: E501
            :type: str
            """

            self._push_service_type = push_service_type

            @property
            def tfa_code(self):
            """Gets the tfa_code of this DoAuthInputObject.  # noqa: E501

                required when 2FA enabled on account. 2FA challenge response (SMS code or security question answer)  # noqa: E501

            :return: The tfa_code of this DoAuthInputObject.  # noqa: E501
            :rtype: str
            """
            return self._tfa_code

            @tfa_code.setter
            def tfa_code(self, tfa_code):
            """Sets the tfa_code of this DoAuthInputObject.

                required when 2FA enabled on account. 2FA challenge response (SMS code or security question answer)  # noqa: E501

            :param tfa_code: The tfa_code of this DoAuthInputObject.  # noqa: E501
            :type: str
            """

            self._tfa_code = tfa_code

            @property
            def tfa_id(self):
            """Gets the tfa_id of this DoAuthInputObject.  # noqa: E501

                required when 2FA enabled on account. 2FA challenge response (SMS code or security question answer)  # noqa: E501

            :return: The tfa_id of this DoAuthInputObject.  # noqa: E501
            :rtype: str
            """
            return self._tfa_id

            @tfa_id.setter
            def tfa_id(self, tfa_id):
            """Sets the tfa_id of this DoAuthInputObject.

                required when 2FA enabled on account. 2FA challenge response (SMS code or security question answer)  # noqa: E501

            :param tfa_id: The tfa_id of this DoAuthInputObject.  # noqa: E501
            :type: str
            """

            self._tfa_id = tfa_id

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
        if issubclass(DoAuthInputObject, dict):
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
        if not isinstance(other, DoAuthInputObject):
        return False

        return self.__dict__ == other.__dict__

        def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
