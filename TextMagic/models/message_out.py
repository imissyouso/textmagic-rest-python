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


class MessageOut(object):
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
        'contact_id': 'int',
        'session_id': 'int',
        'receiver': 'str',
        'message_time': 'datetime',
        'status': 'str',
        'avatar': 'str',
        'text': 'str',
        'deleted': 'bool',
        'charset': 'str',
        'charset_label': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'country': 'str',
        'sender': 'str',
        'phone': 'str',
        'price': 'float',
        'parts_count': 'int',
        'from_email': 'str',
        'from_number': 'str',
        'smsc_id': 'str',
        'contact': 'str',
        'source': 'str',
        'delivered_count': 'int',
        'numbers_count': 'int',
        'user_id': 'int',
        'credits_price': 'str',
        'chars': 'int'
    }

    attribute_map = {
        'id': 'id',
        'contact_id': 'contactId',
        'session_id': 'sessionId',
        'receiver': 'receiver',
        'message_time': 'messageTime',
        'status': 'status',
        'avatar': 'avatar',
        'text': 'text',
        'deleted': 'deleted',
        'charset': 'charset',
        'charset_label': 'charsetLabel',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'country': 'country',
        'sender': 'sender',
        'phone': 'phone',
        'price': 'price',
        'parts_count': 'partsCount',
        'from_email': 'fromEmail',
        'from_number': 'fromNumber',
        'smsc_id': 'smscId',
        'contact': 'contact',
        'source': 'source',
        'delivered_count': 'deliveredCount',
        'numbers_count': 'numbersCount',
        'user_id': 'userId',
        'credits_price': 'creditsPrice',
        'chars': 'chars'
    }

    def __init__(self, id=None, contact_id=None, session_id=None, receiver=None, message_time=None, status=None, avatar=None, text=None, deleted=None, charset=None, charset_label=None, first_name=None, last_name=None, country=None, sender=None, phone=None, price=None, parts_count=None, from_email=None, from_number=None, smsc_id=None, contact=None, source=None, delivered_count=None, numbers_count=None, user_id=None, credits_price=None, chars=None):  # noqa: E501
        """MessageOut - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._contact_id = None
        self._session_id = None
        self._receiver = None
        self._message_time = None
        self._status = None
        self._avatar = None
        self._text = None
        self._deleted = None
        self._charset = None
        self._charset_label = None
        self._first_name = None
        self._last_name = None
        self._country = None
        self._sender = None
        self._phone = None
        self._price = None
        self._parts_count = None
        self._from_email = None
        self._from_number = None
        self._smsc_id = None
        self._contact = None
        self._source = None
        self._delivered_count = None
        self._numbers_count = None
        self._user_id = None
        self._credits_price = None
        self._chars = None
        self.discriminator = None

        self.id = id
        self.contact_id = contact_id
        self.session_id = session_id
        if receiver is not None:
            self.receiver = receiver
        self.message_time = message_time
        self.status = status
        self.avatar = avatar
        self.text = text
        if deleted is not None:
            self.deleted = deleted
        self.charset = charset
        self.charset_label = charset_label
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        if sender is not None:
            self.sender = sender
        if phone is not None:
            self.phone = phone
        if price is not None:
            self.price = price
        self.parts_count = parts_count
        if from_email is not None:
            self.from_email = from_email
        if from_number is not None:
            self.from_number = from_number
        if smsc_id is not None:
            self.smsc_id = smsc_id
        if contact is not None:
            self.contact = contact
        if source is not None:
            self.source = source
        if delivered_count is not None:
            self.delivered_count = delivered_count
        if numbers_count is not None:
            self.numbers_count = numbers_count
        if user_id is not None:
            self.user_id = user_id
        if credits_price is not None:
            self.credits_price = credits_price
        if chars is not None:
            self.chars = chars

    @property
    def id(self):
        """Gets the id of this MessageOut.  # noqa: E501


        :return: The id of this MessageOut.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MessageOut.


        :param id: The id of this MessageOut.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def contact_id(self):
        """Gets the contact_id of this MessageOut.  # noqa: E501


        :return: The contact_id of this MessageOut.  # noqa: E501
        :rtype: int
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this MessageOut.


        :param contact_id: The contact_id of this MessageOut.  # noqa: E501
        :type: int
        """

        self._contact_id = contact_id

    @property
    def session_id(self):
        """Gets the session_id of this MessageOut.  # noqa: E501


        :return: The session_id of this MessageOut.  # noqa: E501
        :rtype: int
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this MessageOut.


        :param session_id: The session_id of this MessageOut.  # noqa: E501
        :type: int
        """

        self._session_id = session_id

    @property
    def receiver(self):
        """Gets the receiver of this MessageOut.  # noqa: E501


        :return: The receiver of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        """Sets the receiver of this MessageOut.


        :param receiver: The receiver of this MessageOut.  # noqa: E501
        :type: str
        """

        self._receiver = receiver

    @property
    def message_time(self):
        """Gets the message_time of this MessageOut.  # noqa: E501


        :return: The message_time of this MessageOut.  # noqa: E501
        :rtype: datetime
        """
        return self._message_time

    @message_time.setter
    def message_time(self, message_time):
        """Sets the message_time of this MessageOut.


        :param message_time: The message_time of this MessageOut.  # noqa: E501
        :type: datetime
        """

        self._message_time = message_time

    @property
    def status(self):
        """Gets the status of this MessageOut.  # noqa: E501

        q - queued s - scheduled queue e - sending error r - enroute a - acked d - delivered b - buffered f - failed u - unknown j - rejected i - bulk insert p - scheduled suspend h - queue suspend  # noqa: E501

        :return: The status of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MessageOut.

        q - queued s - scheduled queue e - sending error r - enroute a - acked d - delivered b - buffered f - failed u - unknown j - rejected i - bulk insert p - scheduled suspend h - queue suspend  # noqa: E501

        :param status: The status of this MessageOut.  # noqa: E501
        :type: str
        """
        allowed_values = ["q", "s", "e", "r", "a", "d", "b", "f", "u", "j", "i", "p", "h"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def avatar(self):
        """Gets the avatar of this MessageOut.  # noqa: E501


        :return: The avatar of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this MessageOut.


        :param avatar: The avatar of this MessageOut.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def text(self):
        """Gets the text of this MessageOut.  # noqa: E501


        :return: The text of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this MessageOut.


        :param text: The text of this MessageOut.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def deleted(self):
        """Gets the deleted of this MessageOut.  # noqa: E501


        :return: The deleted of this MessageOut.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this MessageOut.


        :param deleted: The deleted of this MessageOut.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def charset(self):
        """Gets the charset of this MessageOut.  # noqa: E501


        :return: The charset of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._charset

    @charset.setter
    def charset(self, charset):
        """Sets the charset of this MessageOut.


        :param charset: The charset of this MessageOut.  # noqa: E501
        :type: str
        """

        self._charset = charset

    @property
    def charset_label(self):
        """Gets the charset_label of this MessageOut.  # noqa: E501


        :return: The charset_label of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._charset_label

    @charset_label.setter
    def charset_label(self, charset_label):
        """Sets the charset_label of this MessageOut.


        :param charset_label: The charset_label of this MessageOut.  # noqa: E501
        :type: str
        """

        self._charset_label = charset_label

    @property
    def first_name(self):
        """Gets the first_name of this MessageOut.  # noqa: E501


        :return: The first_name of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this MessageOut.


        :param first_name: The first_name of this MessageOut.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this MessageOut.  # noqa: E501


        :return: The last_name of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this MessageOut.


        :param last_name: The last_name of this MessageOut.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def country(self):
        """Gets the country of this MessageOut.  # noqa: E501


        :return: The country of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this MessageOut.


        :param country: The country of this MessageOut.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def sender(self):
        """Gets the sender of this MessageOut.  # noqa: E501


        :return: The sender of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this MessageOut.


        :param sender: The sender of this MessageOut.  # noqa: E501
        :type: str
        """

        self._sender = sender

    @property
    def phone(self):
        """Gets the phone of this MessageOut.  # noqa: E501


        :return: The phone of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this MessageOut.


        :param phone: The phone of this MessageOut.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def price(self):
        """Gets the price of this MessageOut.  # noqa: E501


        :return: The price of this MessageOut.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this MessageOut.


        :param price: The price of this MessageOut.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def parts_count(self):
        """Gets the parts_count of this MessageOut.  # noqa: E501


        :return: The parts_count of this MessageOut.  # noqa: E501
        :rtype: int
        """
        return self._parts_count

    @parts_count.setter
    def parts_count(self, parts_count):
        """Sets the parts_count of this MessageOut.


        :param parts_count: The parts_count of this MessageOut.  # noqa: E501
        :type: int
        """

        self._parts_count = parts_count

    @property
    def from_email(self):
        """Gets the from_email of this MessageOut.  # noqa: E501


        :return: The from_email of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._from_email

    @from_email.setter
    def from_email(self, from_email):
        """Sets the from_email of this MessageOut.


        :param from_email: The from_email of this MessageOut.  # noqa: E501
        :type: str
        """

        self._from_email = from_email

    @property
    def from_number(self):
        """Gets the from_number of this MessageOut.  # noqa: E501


        :return: The from_number of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._from_number

    @from_number.setter
    def from_number(self, from_number):
        """Sets the from_number of this MessageOut.


        :param from_number: The from_number of this MessageOut.  # noqa: E501
        :type: str
        """

        self._from_number = from_number

    @property
    def smsc_id(self):
        """Gets the smsc_id of this MessageOut.  # noqa: E501


        :return: The smsc_id of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._smsc_id

    @smsc_id.setter
    def smsc_id(self, smsc_id):
        """Sets the smsc_id of this MessageOut.


        :param smsc_id: The smsc_id of this MessageOut.  # noqa: E501
        :type: str
        """

        self._smsc_id = smsc_id

    @property
    def contact(self):
        """Gets the contact of this MessageOut.  # noqa: E501


        :return: The contact of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this MessageOut.


        :param contact: The contact of this MessageOut.  # noqa: E501
        :type: str
        """

        self._contact = contact

    @property
    def source(self):
        """Gets the source of this MessageOut.  # noqa: E501


        :return: The source of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this MessageOut.


        :param source: The source of this MessageOut.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def delivered_count(self):
        """Gets the delivered_count of this MessageOut.  # noqa: E501


        :return: The delivered_count of this MessageOut.  # noqa: E501
        :rtype: int
        """
        return self._delivered_count

    @delivered_count.setter
    def delivered_count(self, delivered_count):
        """Sets the delivered_count of this MessageOut.


        :param delivered_count: The delivered_count of this MessageOut.  # noqa: E501
        :type: int
        """

        self._delivered_count = delivered_count

    @property
    def numbers_count(self):
        """Gets the numbers_count of this MessageOut.  # noqa: E501


        :return: The numbers_count of this MessageOut.  # noqa: E501
        :rtype: int
        """
        return self._numbers_count

    @numbers_count.setter
    def numbers_count(self, numbers_count):
        """Sets the numbers_count of this MessageOut.


        :param numbers_count: The numbers_count of this MessageOut.  # noqa: E501
        :type: int
        """

        self._numbers_count = numbers_count

    @property
    def user_id(self):
        """Gets the user_id of this MessageOut.  # noqa: E501


        :return: The user_id of this MessageOut.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this MessageOut.


        :param user_id: The user_id of this MessageOut.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def credits_price(self):
        """Gets the credits_price of this MessageOut.  # noqa: E501


        :return: The credits_price of this MessageOut.  # noqa: E501
        :rtype: str
        """
        return self._credits_price

    @credits_price.setter
    def credits_price(self, credits_price):
        """Sets the credits_price of this MessageOut.


        :param credits_price: The credits_price of this MessageOut.  # noqa: E501
        :type: str
        """

        self._credits_price = credits_price

    @property
    def chars(self):
        """Gets the chars of this MessageOut.  # noqa: E501


        :return: The chars of this MessageOut.  # noqa: E501
        :rtype: int
        """
        return self._chars

    @chars.setter
    def chars(self, chars):
        """Sets the chars of this MessageOut.


        :param chars: The chars of this MessageOut.  # noqa: E501
        :type: int
        """

        self._chars = chars

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
        if issubclass(MessageOut, dict):
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
        if not isinstance(other, MessageOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
