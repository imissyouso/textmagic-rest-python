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


class GetStateResponse(object):
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
        'system_cache_clear': 'int',
        'system_exit': 'int',
        'system_alert': 'int',
        'system_account_state_changed': 'int',
        'message_deleted': 'int',
        'message_incoming': 'int',
        'message_incoming_deleted': 'int',
        'message_state_changed': 'int',
        'message_bulk_end': 'int',
        'message_wipe_end': 'int',
        'message_sent': 'int',
        'message_session_deleted': 'int',
        'message_cache_clear': 'int',
        'message_incoming_cache_clear': 'int',
        'message_schedule_added': 'int',
        'message_schedule_state_changed': 'int',
        'message_schedule_deleted': 'int',
        'message_schedule_cache_clear': 'int',
        'message_template_cache_clear': 'int',
        'call_finished': 'int',
        'chat_created': 'int',
        'chat_marked_as_read': 'int',
        'chat_muted': 'int',
        'chat_unmuted': 'int',
        'chat_deleted': 'int',
        'chat_closed': 'int',
        'chat_reopened': 'int',
        'chat_cache_clear': 'int',
        'contact_added': 'int',
        'contact_deleted': 'int',
        'contact_state_changed': 'int',
        'list_added': 'int',
        'list_deleted': 'int',
        'list_state_changed': 'int',
        'contact_wipe_end': 'int',
        'contact_import_end': 'int',
        'contact_cache_clear': 'int',
        'list_cache_clear': 'int',
        'custom_fields_cache_clear': 'int'
    }

    attribute_map = {
        'system_cache_clear': 'systemCacheClear',
        'system_exit': 'systemExit',
        'system_alert': 'systemAlert',
        'system_account_state_changed': 'systemAccountStateChanged',
        'message_deleted': 'messageDeleted',
        'message_incoming': 'messageIncoming',
        'message_incoming_deleted': 'messageIncomingDeleted',
        'message_state_changed': 'messageStateChanged',
        'message_bulk_end': 'messageBulkEnd',
        'message_wipe_end': 'messageWipeEnd',
        'message_sent': 'messageSent',
        'message_session_deleted': 'messageSessionDeleted',
        'message_cache_clear': 'messageCacheClear',
        'message_incoming_cache_clear': 'messageIncomingCacheClear',
        'message_schedule_added': 'messageScheduleAdded',
        'message_schedule_state_changed': 'messageScheduleStateChanged',
        'message_schedule_deleted': 'messageScheduleDeleted',
        'message_schedule_cache_clear': 'messageScheduleCacheClear',
        'message_template_cache_clear': 'messageTemplateCacheClear',
        'call_finished': 'callFinished',
        'chat_created': 'chatCreated',
        'chat_marked_as_read': 'chatMarkedAsRead',
        'chat_muted': 'chatMuted',
        'chat_unmuted': 'chatUnmuted',
        'chat_deleted': 'chatDeleted',
        'chat_closed': 'chatClosed',
        'chat_reopened': 'chatReopened',
        'chat_cache_clear': 'chatCacheClear',
        'contact_added': 'contactAdded',
        'contact_deleted': 'contactDeleted',
        'contact_state_changed': 'contactStateChanged',
        'list_added': 'listAdded',
        'list_deleted': 'listDeleted',
        'list_state_changed': 'listStateChanged',
        'contact_wipe_end': 'contactWipeEnd',
        'contact_import_end': 'contactImportEnd',
        'contact_cache_clear': 'contactCacheClear',
        'list_cache_clear': 'listCacheClear',
        'custom_fields_cache_clear': 'customFieldsCacheClear'
    }

    def __init__(self, system_cache_clear=None, system_exit=None, system_alert=None, system_account_state_changed=None, message_deleted=None, message_incoming=None, message_incoming_deleted=None, message_state_changed=None, message_bulk_end=None, message_wipe_end=None, message_sent=None, message_session_deleted=None, message_cache_clear=None, message_incoming_cache_clear=None, message_schedule_added=None, message_schedule_state_changed=None, message_schedule_deleted=None, message_schedule_cache_clear=None, message_template_cache_clear=None, call_finished=None, chat_created=None, chat_marked_as_read=None, chat_muted=None, chat_unmuted=None, chat_deleted=None, chat_closed=None, chat_reopened=None, chat_cache_clear=None, contact_added=None, contact_deleted=None, contact_state_changed=None, list_added=None, list_deleted=None, list_state_changed=None, contact_wipe_end=None, contact_import_end=None, contact_cache_clear=None, list_cache_clear=None, custom_fields_cache_clear=None):  # noqa: E501
        """GetStateResponse - a model defined in Swagger"""  # noqa: E501

        self._system_cache_clear = None
        self._system_exit = None
        self._system_alert = None
        self._system_account_state_changed = None
        self._message_deleted = None
        self._message_incoming = None
        self._message_incoming_deleted = None
        self._message_state_changed = None
        self._message_bulk_end = None
        self._message_wipe_end = None
        self._message_sent = None
        self._message_session_deleted = None
        self._message_cache_clear = None
        self._message_incoming_cache_clear = None
        self._message_schedule_added = None
        self._message_schedule_state_changed = None
        self._message_schedule_deleted = None
        self._message_schedule_cache_clear = None
        self._message_template_cache_clear = None
        self._call_finished = None
        self._chat_created = None
        self._chat_marked_as_read = None
        self._chat_muted = None
        self._chat_unmuted = None
        self._chat_deleted = None
        self._chat_closed = None
        self._chat_reopened = None
        self._chat_cache_clear = None
        self._contact_added = None
        self._contact_deleted = None
        self._contact_state_changed = None
        self._list_added = None
        self._list_deleted = None
        self._list_state_changed = None
        self._contact_wipe_end = None
        self._contact_import_end = None
        self._contact_cache_clear = None
        self._list_cache_clear = None
        self._custom_fields_cache_clear = None
        self.discriminator = None

        self.system_cache_clear = system_cache_clear
        self.system_exit = system_exit
        self.system_alert = system_alert
        self.system_account_state_changed = system_account_state_changed
        self.message_deleted = message_deleted
        self.message_incoming = message_incoming
        self.message_incoming_deleted = message_incoming_deleted
        self.message_state_changed = message_state_changed
        self.message_bulk_end = message_bulk_end
        self.message_wipe_end = message_wipe_end
        self.message_sent = message_sent
        self.message_session_deleted = message_session_deleted
        self.message_cache_clear = message_cache_clear
        self.message_incoming_cache_clear = message_incoming_cache_clear
        self.message_schedule_added = message_schedule_added
        self.message_schedule_state_changed = message_schedule_state_changed
        self.message_schedule_deleted = message_schedule_deleted
        self.message_schedule_cache_clear = message_schedule_cache_clear
        self.message_template_cache_clear = message_template_cache_clear
        self.call_finished = call_finished
        self.chat_created = chat_created
        self.chat_marked_as_read = chat_marked_as_read
        self.chat_muted = chat_muted
        self.chat_unmuted = chat_unmuted
        self.chat_deleted = chat_deleted
        self.chat_closed = chat_closed
        self.chat_reopened = chat_reopened
        self.chat_cache_clear = chat_cache_clear
        self.contact_added = contact_added
        self.contact_deleted = contact_deleted
        self.contact_state_changed = contact_state_changed
        self.list_added = list_added
        self.list_deleted = list_deleted
        self.list_state_changed = list_state_changed
        self.contact_wipe_end = contact_wipe_end
        self.contact_import_end = contact_import_end
        self.contact_cache_clear = contact_cache_clear
        self.list_cache_clear = list_cache_clear
        self.custom_fields_cache_clear = custom_fields_cache_clear

    @property
    def system_cache_clear(self):
        """Gets the system_cache_clear of this GetStateResponse.  # noqa: E501


        :return: The system_cache_clear of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._system_cache_clear

    @system_cache_clear.setter
    def system_cache_clear(self, system_cache_clear):
        """Sets the system_cache_clear of this GetStateResponse.


        :param system_cache_clear: The system_cache_clear of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._system_cache_clear = system_cache_clear

    @property
    def system_exit(self):
        """Gets the system_exit of this GetStateResponse.  # noqa: E501


        :return: The system_exit of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._system_exit

    @system_exit.setter
    def system_exit(self, system_exit):
        """Sets the system_exit of this GetStateResponse.


        :param system_exit: The system_exit of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._system_exit = system_exit

    @property
    def system_alert(self):
        """Gets the system_alert of this GetStateResponse.  # noqa: E501


        :return: The system_alert of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._system_alert

    @system_alert.setter
    def system_alert(self, system_alert):
        """Sets the system_alert of this GetStateResponse.


        :param system_alert: The system_alert of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._system_alert = system_alert

    @property
    def system_account_state_changed(self):
        """Gets the system_account_state_changed of this GetStateResponse.  # noqa: E501


        :return: The system_account_state_changed of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._system_account_state_changed

    @system_account_state_changed.setter
    def system_account_state_changed(self, system_account_state_changed):
        """Sets the system_account_state_changed of this GetStateResponse.


        :param system_account_state_changed: The system_account_state_changed of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._system_account_state_changed = system_account_state_changed

    @property
    def message_deleted(self):
        """Gets the message_deleted of this GetStateResponse.  # noqa: E501


        :return: The message_deleted of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._message_deleted

    @message_deleted.setter
    def message_deleted(self, message_deleted):
        """Sets the message_deleted of this GetStateResponse.


        :param message_deleted: The message_deleted of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._message_deleted = message_deleted

    @property
    def message_incoming(self):
        """Gets the message_incoming of this GetStateResponse.  # noqa: E501


        :return: The message_incoming of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._message_incoming

    @message_incoming.setter
    def message_incoming(self, message_incoming):
        """Sets the message_incoming of this GetStateResponse.


        :param message_incoming: The message_incoming of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._message_incoming = message_incoming

    @property
    def message_incoming_deleted(self):
        """Gets the message_incoming_deleted of this GetStateResponse.  # noqa: E501


        :return: The message_incoming_deleted of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._message_incoming_deleted

    @message_incoming_deleted.setter
    def message_incoming_deleted(self, message_incoming_deleted):
        """Sets the message_incoming_deleted of this GetStateResponse.


        :param message_incoming_deleted: The message_incoming_deleted of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._message_incoming_deleted = message_incoming_deleted

    @property
    def message_state_changed(self):
        """Gets the message_state_changed of this GetStateResponse.  # noqa: E501


        :return: The message_state_changed of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._message_state_changed

    @message_state_changed.setter
    def message_state_changed(self, message_state_changed):
        """Sets the message_state_changed of this GetStateResponse.


        :param message_state_changed: The message_state_changed of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._message_state_changed = message_state_changed

    @property
    def message_bulk_end(self):
        """Gets the message_bulk_end of this GetStateResponse.  # noqa: E501


        :return: The message_bulk_end of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._message_bulk_end

    @message_bulk_end.setter
    def message_bulk_end(self, message_bulk_end):
        """Sets the message_bulk_end of this GetStateResponse.


        :param message_bulk_end: The message_bulk_end of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._message_bulk_end = message_bulk_end

    @property
    def message_wipe_end(self):
        """Gets the message_wipe_end of this GetStateResponse.  # noqa: E501


        :return: The message_wipe_end of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._message_wipe_end

    @message_wipe_end.setter
    def message_wipe_end(self, message_wipe_end):
        """Sets the message_wipe_end of this GetStateResponse.


        :param message_wipe_end: The message_wipe_end of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._message_wipe_end = message_wipe_end

    @property
    def message_sent(self):
        """Gets the message_sent of this GetStateResponse.  # noqa: E501


        :return: The message_sent of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._message_sent

    @message_sent.setter
    def message_sent(self, message_sent):
        """Sets the message_sent of this GetStateResponse.


        :param message_sent: The message_sent of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._message_sent = message_sent

    @property
    def message_session_deleted(self):
        """Gets the message_session_deleted of this GetStateResponse.  # noqa: E501


        :return: The message_session_deleted of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._message_session_deleted

    @message_session_deleted.setter
    def message_session_deleted(self, message_session_deleted):
        """Sets the message_session_deleted of this GetStateResponse.


        :param message_session_deleted: The message_session_deleted of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._message_session_deleted = message_session_deleted

    @property
    def message_cache_clear(self):
        """Gets the message_cache_clear of this GetStateResponse.  # noqa: E501


        :return: The message_cache_clear of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._message_cache_clear

    @message_cache_clear.setter
    def message_cache_clear(self, message_cache_clear):
        """Sets the message_cache_clear of this GetStateResponse.


        :param message_cache_clear: The message_cache_clear of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._message_cache_clear = message_cache_clear

    @property
    def message_incoming_cache_clear(self):
        """Gets the message_incoming_cache_clear of this GetStateResponse.  # noqa: E501


        :return: The message_incoming_cache_clear of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._message_incoming_cache_clear

    @message_incoming_cache_clear.setter
    def message_incoming_cache_clear(self, message_incoming_cache_clear):
        """Sets the message_incoming_cache_clear of this GetStateResponse.


        :param message_incoming_cache_clear: The message_incoming_cache_clear of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._message_incoming_cache_clear = message_incoming_cache_clear

    @property
    def message_schedule_added(self):
        """Gets the message_schedule_added of this GetStateResponse.  # noqa: E501


        :return: The message_schedule_added of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._message_schedule_added

    @message_schedule_added.setter
    def message_schedule_added(self, message_schedule_added):
        """Sets the message_schedule_added of this GetStateResponse.


        :param message_schedule_added: The message_schedule_added of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._message_schedule_added = message_schedule_added

    @property
    def message_schedule_state_changed(self):
        """Gets the message_schedule_state_changed of this GetStateResponse.  # noqa: E501


        :return: The message_schedule_state_changed of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._message_schedule_state_changed

    @message_schedule_state_changed.setter
    def message_schedule_state_changed(self, message_schedule_state_changed):
        """Sets the message_schedule_state_changed of this GetStateResponse.


        :param message_schedule_state_changed: The message_schedule_state_changed of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._message_schedule_state_changed = message_schedule_state_changed

    @property
    def message_schedule_deleted(self):
        """Gets the message_schedule_deleted of this GetStateResponse.  # noqa: E501


        :return: The message_schedule_deleted of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._message_schedule_deleted

    @message_schedule_deleted.setter
    def message_schedule_deleted(self, message_schedule_deleted):
        """Sets the message_schedule_deleted of this GetStateResponse.


        :param message_schedule_deleted: The message_schedule_deleted of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._message_schedule_deleted = message_schedule_deleted

    @property
    def message_schedule_cache_clear(self):
        """Gets the message_schedule_cache_clear of this GetStateResponse.  # noqa: E501


        :return: The message_schedule_cache_clear of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._message_schedule_cache_clear

    @message_schedule_cache_clear.setter
    def message_schedule_cache_clear(self, message_schedule_cache_clear):
        """Sets the message_schedule_cache_clear of this GetStateResponse.


        :param message_schedule_cache_clear: The message_schedule_cache_clear of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._message_schedule_cache_clear = message_schedule_cache_clear

    @property
    def message_template_cache_clear(self):
        """Gets the message_template_cache_clear of this GetStateResponse.  # noqa: E501


        :return: The message_template_cache_clear of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._message_template_cache_clear

    @message_template_cache_clear.setter
    def message_template_cache_clear(self, message_template_cache_clear):
        """Sets the message_template_cache_clear of this GetStateResponse.


        :param message_template_cache_clear: The message_template_cache_clear of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._message_template_cache_clear = message_template_cache_clear

    @property
    def call_finished(self):
        """Gets the call_finished of this GetStateResponse.  # noqa: E501


        :return: The call_finished of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._call_finished

    @call_finished.setter
    def call_finished(self, call_finished):
        """Sets the call_finished of this GetStateResponse.


        :param call_finished: The call_finished of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._call_finished = call_finished

    @property
    def chat_created(self):
        """Gets the chat_created of this GetStateResponse.  # noqa: E501


        :return: The chat_created of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._chat_created

    @chat_created.setter
    def chat_created(self, chat_created):
        """Sets the chat_created of this GetStateResponse.


        :param chat_created: The chat_created of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._chat_created = chat_created

    @property
    def chat_marked_as_read(self):
        """Gets the chat_marked_as_read of this GetStateResponse.  # noqa: E501


        :return: The chat_marked_as_read of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._chat_marked_as_read

    @chat_marked_as_read.setter
    def chat_marked_as_read(self, chat_marked_as_read):
        """Sets the chat_marked_as_read of this GetStateResponse.


        :param chat_marked_as_read: The chat_marked_as_read of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._chat_marked_as_read = chat_marked_as_read

    @property
    def chat_muted(self):
        """Gets the chat_muted of this GetStateResponse.  # noqa: E501


        :return: The chat_muted of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._chat_muted

    @chat_muted.setter
    def chat_muted(self, chat_muted):
        """Sets the chat_muted of this GetStateResponse.


        :param chat_muted: The chat_muted of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._chat_muted = chat_muted

    @property
    def chat_unmuted(self):
        """Gets the chat_unmuted of this GetStateResponse.  # noqa: E501


        :return: The chat_unmuted of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._chat_unmuted

    @chat_unmuted.setter
    def chat_unmuted(self, chat_unmuted):
        """Sets the chat_unmuted of this GetStateResponse.


        :param chat_unmuted: The chat_unmuted of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._chat_unmuted = chat_unmuted

    @property
    def chat_deleted(self):
        """Gets the chat_deleted of this GetStateResponse.  # noqa: E501


        :return: The chat_deleted of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._chat_deleted

    @chat_deleted.setter
    def chat_deleted(self, chat_deleted):
        """Sets the chat_deleted of this GetStateResponse.


        :param chat_deleted: The chat_deleted of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._chat_deleted = chat_deleted

    @property
    def chat_closed(self):
        """Gets the chat_closed of this GetStateResponse.  # noqa: E501


        :return: The chat_closed of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._chat_closed

    @chat_closed.setter
    def chat_closed(self, chat_closed):
        """Sets the chat_closed of this GetStateResponse.


        :param chat_closed: The chat_closed of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._chat_closed = chat_closed

    @property
    def chat_reopened(self):
        """Gets the chat_reopened of this GetStateResponse.  # noqa: E501


        :return: The chat_reopened of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._chat_reopened

    @chat_reopened.setter
    def chat_reopened(self, chat_reopened):
        """Sets the chat_reopened of this GetStateResponse.


        :param chat_reopened: The chat_reopened of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._chat_reopened = chat_reopened

    @property
    def chat_cache_clear(self):
        """Gets the chat_cache_clear of this GetStateResponse.  # noqa: E501


        :return: The chat_cache_clear of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._chat_cache_clear

    @chat_cache_clear.setter
    def chat_cache_clear(self, chat_cache_clear):
        """Sets the chat_cache_clear of this GetStateResponse.


        :param chat_cache_clear: The chat_cache_clear of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._chat_cache_clear = chat_cache_clear

    @property
    def contact_added(self):
        """Gets the contact_added of this GetStateResponse.  # noqa: E501


        :return: The contact_added of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._contact_added

    @contact_added.setter
    def contact_added(self, contact_added):
        """Sets the contact_added of this GetStateResponse.


        :param contact_added: The contact_added of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._contact_added = contact_added

    @property
    def contact_deleted(self):
        """Gets the contact_deleted of this GetStateResponse.  # noqa: E501


        :return: The contact_deleted of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._contact_deleted

    @contact_deleted.setter
    def contact_deleted(self, contact_deleted):
        """Sets the contact_deleted of this GetStateResponse.


        :param contact_deleted: The contact_deleted of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._contact_deleted = contact_deleted

    @property
    def contact_state_changed(self):
        """Gets the contact_state_changed of this GetStateResponse.  # noqa: E501


        :return: The contact_state_changed of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._contact_state_changed

    @contact_state_changed.setter
    def contact_state_changed(self, contact_state_changed):
        """Sets the contact_state_changed of this GetStateResponse.


        :param contact_state_changed: The contact_state_changed of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._contact_state_changed = contact_state_changed

    @property
    def list_added(self):
        """Gets the list_added of this GetStateResponse.  # noqa: E501


        :return: The list_added of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._list_added

    @list_added.setter
    def list_added(self, list_added):
        """Sets the list_added of this GetStateResponse.


        :param list_added: The list_added of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._list_added = list_added

    @property
    def list_deleted(self):
        """Gets the list_deleted of this GetStateResponse.  # noqa: E501


        :return: The list_deleted of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._list_deleted

    @list_deleted.setter
    def list_deleted(self, list_deleted):
        """Sets the list_deleted of this GetStateResponse.


        :param list_deleted: The list_deleted of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._list_deleted = list_deleted

    @property
    def list_state_changed(self):
        """Gets the list_state_changed of this GetStateResponse.  # noqa: E501


        :return: The list_state_changed of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._list_state_changed

    @list_state_changed.setter
    def list_state_changed(self, list_state_changed):
        """Sets the list_state_changed of this GetStateResponse.


        :param list_state_changed: The list_state_changed of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._list_state_changed = list_state_changed

    @property
    def contact_wipe_end(self):
        """Gets the contact_wipe_end of this GetStateResponse.  # noqa: E501


        :return: The contact_wipe_end of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._contact_wipe_end

    @contact_wipe_end.setter
    def contact_wipe_end(self, contact_wipe_end):
        """Sets the contact_wipe_end of this GetStateResponse.


        :param contact_wipe_end: The contact_wipe_end of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._contact_wipe_end = contact_wipe_end

    @property
    def contact_import_end(self):
        """Gets the contact_import_end of this GetStateResponse.  # noqa: E501


        :return: The contact_import_end of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._contact_import_end

    @contact_import_end.setter
    def contact_import_end(self, contact_import_end):
        """Sets the contact_import_end of this GetStateResponse.


        :param contact_import_end: The contact_import_end of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._contact_import_end = contact_import_end

    @property
    def contact_cache_clear(self):
        """Gets the contact_cache_clear of this GetStateResponse.  # noqa: E501


        :return: The contact_cache_clear of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._contact_cache_clear

    @contact_cache_clear.setter
    def contact_cache_clear(self, contact_cache_clear):
        """Sets the contact_cache_clear of this GetStateResponse.


        :param contact_cache_clear: The contact_cache_clear of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._contact_cache_clear = contact_cache_clear

    @property
    def list_cache_clear(self):
        """Gets the list_cache_clear of this GetStateResponse.  # noqa: E501


        :return: The list_cache_clear of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._list_cache_clear

    @list_cache_clear.setter
    def list_cache_clear(self, list_cache_clear):
        """Sets the list_cache_clear of this GetStateResponse.


        :param list_cache_clear: The list_cache_clear of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._list_cache_clear = list_cache_clear

    @property
    def custom_fields_cache_clear(self):
        """Gets the custom_fields_cache_clear of this GetStateResponse.  # noqa: E501


        :return: The custom_fields_cache_clear of this GetStateResponse.  # noqa: E501
        :rtype: int
        """
        return self._custom_fields_cache_clear

    @custom_fields_cache_clear.setter
    def custom_fields_cache_clear(self, custom_fields_cache_clear):
        """Sets the custom_fields_cache_clear of this GetStateResponse.


        :param custom_fields_cache_clear: The custom_fields_cache_clear of this GetStateResponse.  # noqa: E501
        :type: int
        """

        self._custom_fields_cache_clear = custom_fields_cache_clear

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
        if issubclass(GetStateResponse, dict):
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
        if not isinstance(other, GetStateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
