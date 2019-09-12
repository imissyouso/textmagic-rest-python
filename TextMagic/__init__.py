# coding: utf-8

# flake8: noqa

"""
    TextMagic API Documentation

    # Overview ## Introduction test <img style=\"float: right; margin-left: 10px; width: 100px;\" src=\"images/phone.png\"> TextMagic SMS API is a platform for building your own messaging app using our messaging infrastructure. It allows you to send and receive SMS text messages, query information about inbound and outbound messages, manage contacts, create templates (i.e. message formats and static texts) and schedule recurrent SMS messages as well as process bulk SMS messages. <button name=\"button\" onclick=\"http://www.google.com\" class=\"btn\">Try TextMagic API for Free</button>  ### Two Ways to Use TextMagic API * [REST API](https://www.textmagic.com/docs/api/start/) – get full access to TextMagic’s messaging gateway features * [Email to SMS API](https://www.textmagic.com/docs/api/send-email-to-sms/) – set up two-way SMS communication without the need to write any additional code  ### Code Libraries We have created a set of client libraries for the most popular programming languages (such as REST API Java and REST API PHP). These libraries allow you to integrate our API into your code in minutes. Just choose your preferred language to get started:  ## Getting started Get Started with the TextMagic REST API To start sending text messages using the TextMagic REST API, just follow these steps: 1. Generate the API credentials 1. Connect to our API endpoint This page provides all the information you need to get started. Here, we explain the following steps:  How to obtain the API credentials The API endpoint How the REST API works The next step How to obtain the API credentials  ### How to obtain the API credentials To start sending text messages, you need to create an API key. API keys are similar to an account password; the difference is that an API key only provides access to the API: you cannot log in to TextMagic Online using the API key.  Your program sends the login credentials with each API request as HTTP headers: `X-TM-Username` is your TextMagic username, while `X-TM-Key` is your API key.  How to obtain an API key:  1. Log in to TextMagic (or start a free trial if you haven’t registered yet). 1. Go to the API settings page. 1. Click the Add new API key button. 1. Enter an app name for this key. Note, it’s just a label, so pick any name. 1. Click Generate new key. 1. You should now see your new API key in the green notification banner above the table:  ![alt text](images/credentials.png)  > Note for API v1 users > V1 keys are not compatible with the V2 version of the TextMagic REST API, so you will need to generate a new API key to use the V2 endpoint.  ### The API endpoint The TextMagic REST API endpoint is: ``` https://rest.textmagic.com/api/v2 ``` All the URLs referenced in this documentation should use this base URL.  ### How the REST API works REST APIs use the HTTP protocol to send and receive messages. REST messages are usually encoded as JSON documents and are an improvement over older methods such as the XML based SOAP protocol. REST APIs use the same set of methods that web browsers use: POST, GET, PUT or DELETE. These correspond to the CRUD operations: create, read, update and delete. Often, REST URIs provide direct CRUD access to entities or collections of entities, for example: http://api.foo.com/people. In this instance, to delete a person’s endpoint, you might simply call the endpoint DELETE http://api.foo.com/people/{id}. REST makes these types of operations simple.  > Example > > Let’s take the entity most often used in messaging: contacts. Imagine you want to perform operations on your contacts list: well, it’s only a matter of calling the following endpoints: > * GET /api/v2/contacts (get all of your contacts) > * GET /api/v2/contacts/{id} (get a specific contact) > * POST /api/v2/contacts (create a new contact) > * PUT /api/v2/contacts/{id} (update an existing contact) > * DELETE /api/v2/contacts/{id} (delete an existing contact) It’s that simple! In fact, that’s all you need to do to manage the contacts in your TextMagic account!  ## Sandbox Sandbox is a tool to test TextMagic REST API requests without the need to install any applications or write any code. Here, we explain the following details about Sandbox: * The credentials area * Command documentation * How it works  <a href=\"\">Go to TextMagic Sandbox</a>  ### The credentials area To make requests using your TextMagic account, you need to enter your account username and your API key into the corresponding fields. You may also Save them in your browser or press Clear to erase them.  ![alt text](images/sandbox.png)   # noqa: E501

    OpenAPI spec version: 2
    Contact: support@textmagi.biz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from Api.authentication_api import AuthenticationApi
from Api.billing_api import BillingApi
from Api.bulk_message_sessions_api import BulkMessageSessionsApi
from Api.calls_api import CallsApi
from Api.chats_api import ChatsApi
from Api.common_api import CommonApi
from Api.contact_lists_api import ContactListsApi
from Api.contact_notes_api import ContactNotesApi
from Api.contacts_api import ContactsApi
from Api.contacts_import_api import ContactsImportApi
from Api.custom_fields_api import CustomFieldsApi
from Api.inbound_messages_api import InboundMessagesApi
from Api.integration_api import IntegrationApi
from Api.numbers_api import NumbersApi
from Api.outbound_message_sessions_api import OutboundMessageSessionsApi
from Api.outbound_messages_api import OutboundMessagesApi
from Api.scheduled_messages_api import ScheduledMessagesApi
from Api.statistic_api import StatisticApi
from Api.surveys_api import SurveysApi
from Api.templates_api import TemplatesApi
from Api.tools_api import ToolsApi
from Api.user_api import UserApi
from Api.user_settings_api import UserSettingsApi
from Api.user_subaccounts_api import UserSubaccountsApi

# import ApiClient
from TextMagic.api_client import ApiClient
from TextMagic.configuration import Configuration
# import models into sdk package
from TextMagic.Model.assign_contacts_to_list_input_object import AssignContactsToListInputObject
from TextMagic.Model.bad_request_response import BadRequestResponse
from TextMagic.Model.bad_request_response_errors import BadRequestResponseErrors
from TextMagic.Model.block_contact_input_object import BlockContactInputObject
from TextMagic.Model.bulk_session import BulkSession
from TextMagic.Model.buy_dedicated_number_input_object import BuyDedicatedNumberInputObject
from TextMagic.Model.chat import Chat
from TextMagic.Model.check_phone_verification_code_input_object import CheckPhoneVerificationCodeInputObject
from TextMagic.Model.clear_and_assign_contacts_to_list_input_object import ClearAndAssignContactsToListInputObject
from TextMagic.Model.close_chats_bulk_input_object import CloseChatsBulkInputObject
from TextMagic.Model.contact import Contact
from TextMagic.Model.contact_custom_field import ContactCustomField
from TextMagic.Model.contact_image import ContactImage
from TextMagic.Model.contact_note import ContactNote
from TextMagic.Model.conversation import Conversation
from TextMagic.Model.country import Country
from TextMagic.Model.create_contact_input_object import CreateContactInputObject
from TextMagic.Model.create_contact_note_input_object import CreateContactNoteInputObject
from TextMagic.Model.create_custom_field_input_object import CreateCustomFieldInputObject
from TextMagic.Model.create_list_input_object import CreateListInputObject
from TextMagic.Model.create_push_token_input_object import CreatePushTokenInputObject
from TextMagic.Model.create_survey_input_object import CreateSurveyInputObject
from TextMagic.Model.create_survey_node_input_object import CreateSurveyNodeInputObject
from TextMagic.Model.create_template_input_object import CreateTemplateInputObject
from TextMagic.Model.currency import Currency
from TextMagic.Model.delete_chat_messages_bulk_input_object import DeleteChatMessagesBulkInputObject
from TextMagic.Model.delete_chats_bulk_input_object import DeleteChatsBulkInputObject
from TextMagic.Model.delete_contacs_from_list_object import DeleteContacsFromListObject
from TextMagic.Model.delete_contact_notes_bulk_input_object import DeleteContactNotesBulkInputObject
from TextMagic.Model.delete_contacts_by_ids_input_object import DeleteContactsByIdsInputObject
from TextMagic.Model.delete_inbound_messages_bulk_input_object import DeleteInboundMessagesBulkInputObject
from TextMagic.Model.delete_list_contacts_bulk_input_object import DeleteListContactsBulkInputObject
from TextMagic.Model.delete_lists_bulk_input_object import DeleteListsBulkInputObject
from TextMagic.Model.delete_message_sessions_bulk_input_object import DeleteMessageSessionsBulkInputObject
from TextMagic.Model.delete_outbound_messages_bulk_input_object import DeleteOutboundMessagesBulkInputObject
from TextMagic.Model.delete_scheduled_messages_bulk_input_object import DeleteScheduledMessagesBulkInputObject
from TextMagic.Model.delete_templates_bulk_input_object import DeleteTemplatesBulkInputObject
from TextMagic.Model.do_auth_input_object import DoAuthInputObject
from TextMagic.Model.do_auth_response import DoAuthResponse
from TextMagic.Model.do_auth_response_min_versions import DoAuthResponseMinVersions
from TextMagic.Model.do_carrier_lookup_response import DoCarrierLookupResponse
from TextMagic.Model.do_email_lookup_response import DoEmailLookupResponse
from TextMagic.Model.favorite_contact import FavoriteContact
from TextMagic.Model.forwarded_call import ForwardedCall
from TextMagic.Model.get_available_dedicated_numbers_response import GetAvailableDedicatedNumbersResponse
from TextMagic.Model.get_available_sender_setting_options_response import GetAvailableSenderSettingOptionsResponse
from TextMagic.Model.get_balance_notification_options_response import GetBalanceNotificationOptionsResponse
from TextMagic.Model.get_balance_notification_settings_response import GetBalanceNotificationSettingsResponse
from TextMagic.Model.get_callback_settings_response import GetCallbackSettingsResponse
from TextMagic.Model.get_contact_import_session_progress_response import GetContactImportSessionProgressResponse
from TextMagic.Model.get_contacts_autocomplete_response import GetContactsAutocompleteResponse
from TextMagic.Model.get_inbound_messages_notification_settings_response import GetInboundMessagesNotificationSettingsResponse
from TextMagic.Model.get_list_contacts_ids_response import GetListContactsIdsResponse
from TextMagic.Model.get_message_preview_response import GetMessagePreviewResponse
from TextMagic.Model.get_message_price_response import GetMessagePriceResponse
from TextMagic.Model.get_message_prices_response import GetMessagePricesResponse
from TextMagic.Model.get_message_session_stat_response import GetMessageSessionStatResponse
from TextMagic.Model.get_messaging_counters_response import GetMessagingCountersResponse
from TextMagic.Model.get_messaging_stat_response import GetMessagingStatResponse
from TextMagic.Model.get_push_tokens_response import GetPushTokensResponse
from TextMagic.Model.get_sender_settings_response import GetSenderSettingsResponse
from TextMagic.Model.get_state_response import GetStateResponse
from TextMagic.Model.get_subaccounts_with_tokens_input_object import GetSubaccountsWithTokensInputObject
from TextMagic.Model.get_subaccounts_with_tokens_response import GetSubaccountsWithTokensResponse
from TextMagic.Model.get_survey_nodes_response import GetSurveyNodesResponse
from TextMagic.Model.get_unread_messages_total_response import GetUnreadMessagesTotalResponse
from TextMagic.Model.get_versions_response import GetVersionsResponse
from TextMagic.Model.group import Group
from TextMagic.Model.group_image import GroupImage
from TextMagic.Model.invite_subaccount_input_object import InviteSubaccountInputObject
from TextMagic.Model.invoice import Invoice
from TextMagic.Model.mark_chats_read_bulk_input_object import MarkChatsReadBulkInputObject
from TextMagic.Model.mark_chats_unread_bulk_input_object import MarkChatsUnreadBulkInputObject
from TextMagic.Model.merge_survey_nodes_input_object import MergeSurveyNodesInputObject
from TextMagic.Model.message_in import MessageIn
from TextMagic.Model.message_out import MessageOut
from TextMagic.Model.message_session import MessageSession
from TextMagic.Model.message_template import MessageTemplate
from TextMagic.Model.messages_ics import MessagesIcs
from TextMagic.Model.messages_ics_parameters import MessagesIcsParameters
from TextMagic.Model.messages_ics_parameters_recipients import MessagesIcsParametersRecipients
from TextMagic.Model.messages_ics_text_parameters import MessagesIcsTextParameters
from TextMagic.Model.messaging_stat_item import MessagingStatItem
from TextMagic.Model.mute_chat_input_object import MuteChatInputObject
from TextMagic.Model.mute_chats_bulk_input_object import MuteChatsBulkInputObject
from TextMagic.Model.not_found_response import NotFoundResponse
from TextMagic.Model.ping_response import PingResponse
from TextMagic.Model.push_token import PushToken
from TextMagic.Model.reopen_chats_bulk_input_object import ReopenChatsBulkInputObject
from TextMagic.Model.request_new_subaccount_token_input_object import RequestNewSubaccountTokenInputObject
from TextMagic.Model.request_sender_id_input_object import RequestSenderIdInputObject
from TextMagic.Model.resource_link_response import ResourceLinkResponse
from TextMagic.Model.send_message_input_object import SendMessageInputObject
from TextMagic.Model.send_message_response import SendMessageResponse
from TextMagic.Model.sender_id import SenderId
from TextMagic.Model.set_chat_status_input_object import SetChatStatusInputObject
from TextMagic.Model.subaccount_with_token import SubaccountWithToken
from TextMagic.Model.successful_response import SuccessfulResponse
from TextMagic.Model.survey import Survey
from TextMagic.Model.survey_node import SurveyNode
from TextMagic.Model.survey_recipient import SurveyRecipient
from TextMagic.Model.survey_sender_countries import SurveySenderCountries
from TextMagic.Model.timezone import Timezone
from TextMagic.Model.unauthorized_response import UnauthorizedResponse
from TextMagic.Model.unblock_contact_input_object import UnblockContactInputObject
from TextMagic.Model.unblock_contacts_bulk_input_object import UnblockContactsBulkInputObject
from TextMagic.Model.unmute_chats_bulk_input_object import UnmuteChatsBulkInputObject
from TextMagic.Model.unsubscribe_contact_input_object import UnsubscribeContactInputObject
from TextMagic.Model.unsubscribed_contact import UnsubscribedContact
from TextMagic.Model.update_balance_notification_settings_input_object import UpdateBalanceNotificationSettingsInputObject
from TextMagic.Model.update_callback_settings_input_object import UpdateCallbackSettingsInputObject
from TextMagic.Model.update_chat_desktop_notification_settings_input_object import UpdateChatDesktopNotificationSettingsInputObject
from TextMagic.Model.update_contact_input_object import UpdateContactInputObject
from TextMagic.Model.update_contact_note_input_object import UpdateContactNoteInputObject
from TextMagic.Model.update_current_user_input_object import UpdateCurrentUserInputObject
from TextMagic.Model.update_current_user_response import UpdateCurrentUserResponse
from TextMagic.Model.update_custom_field_input_object import UpdateCustomFieldInputObject
from TextMagic.Model.update_custom_field_value_input_object import UpdateCustomFieldValueInputObject
from TextMagic.Model.update_inbound_messages_notification_settings_input_object import UpdateInboundMessagesNotificationSettingsInputObject
from TextMagic.Model.update_list_object import UpdateListObject
from TextMagic.Model.update_password_input_object import UpdatePasswordInputObject
from TextMagic.Model.update_sender_setting_input_object import UpdateSenderSettingInputObject
from TextMagic.Model.update_survey_input_object import UpdateSurveyInputObject
from TextMagic.Model.update_survey_node_input_object import UpdateSurveyNodeInputObject
from TextMagic.Model.update_template_input_object import UpdateTemplateInputObject
from TextMagic.Model.upload_message_attachment_response import UploadMessageAttachmentResponse
from TextMagic.Model.user import User
from TextMagic.Model.user_custom_field import UserCustomField
from TextMagic.Model.user_image import UserImage
from TextMagic.Model.user_statement import UserStatement
from TextMagic.Model.users_inbound import UsersInbound
