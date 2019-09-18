# coding: utf-8

# flake8: noqa

"""
    TextMagic API Documentation

    # Overview ## Introduction 123 <img style=\"float: right; margin-left: 10px; width: 100px;\" src=\"images/phone.png\"> TextMagic SMS API is a platform for building your own messaging app using our messaging infrastructure. It allows you to send and receive SMS text messages, query information about inbound and outbound messages, manage contacts, create templates (i.e. message formats and static texts) and schedule recurrent SMS messages as well as process bulk SMS messages. <button name=\"button\" onclick=\"http://www.google.com\" class=\"btn\">Try TextMagic API for Free</button>  ### Two Ways to Use TextMagic API * [REST API](https://www.textmagic.com/docs/api/start/) – get full access to TextMagic’s messaging gateway features * [Email to SMS API](https://www.textmagic.com/docs/api/send-email-to-sms/) – set up two-way SMS communication without the need to write any additional code  ### Code Libraries We have created a set of client libraries for the most popular programming languages (such as REST API Java and REST API PHP). These libraries allow you to integrate our API into your code in minutes. Just choose your preferred language to get started:  ## Getting started Get Started with the TextMagic REST API To start sending text messages using the TextMagic REST API, just follow these steps: 1. Generate the API credentials 1. Connect to our API endpoint This page provides all the information you need to get started. Here, we explain the following steps:  How to obtain the API credentials The API endpoint How the REST API works The next step How to obtain the API credentials  ### How to obtain the API credentials To start sending text messages, you need to create an API key. API keys are similar to an account password; the difference is that an API key only provides access to the API: you cannot log in to TextMagic Online using the API key.  Your program sends the login credentials with each API request as HTTP headers: `X-TM-Username` is your TextMagic username, while `X-TM-Key` is your API key.  How to obtain an API key:  1. Log in to TextMagic (or start a free trial if you haven’t registered yet). 1. Go to the API settings page. 1. Click the Add new API key button. 1. Enter an app name for this key. Note, it’s just a label, so pick any name. 1. Click Generate new key. 1. You should now see your new API key in the green notification banner above the table:  ![alt text](images/credentials.png)  > Note for API v1 users > V1 keys are not compatible with the V2 version of the TextMagic REST API, so you will need to generate a new API key to use the V2 endpoint.  ### The API endpoint The TextMagic REST API endpoint is: ``` https://rest.textmagic.com/api/v2 ``` All the URLs referenced in this documentation should use this base URL.  ### How the REST API works REST APIs use the HTTP protocol to send and receive messages. REST messages are usually encoded as JSON documents and are an improvement over older methods such as the XML based SOAP protocol. REST APIs use the same set of methods that web browsers use: POST, GET, PUT or DELETE. These correspond to the CRUD operations: create, read, update and delete. Often, REST URIs provide direct CRUD access to entities or collections of entities, for example: http://api.foo.com/people. In this instance, to delete a person’s endpoint, you might simply call the endpoint DELETE http://api.foo.com/people/{id}. REST makes these types of operations simple.  > Example > > Let’s take the entity most often used in messaging: contacts. Imagine you want to perform operations on your contacts list: well, it’s only a matter of calling the following endpoints: > * GET /api/v2/contacts (get all of your contacts) > * GET /api/v2/contacts/{id} (get a specific contact) > * POST /api/v2/contacts (create a new contact) > * PUT /api/v2/contacts/{id} (update an existing contact) > * DELETE /api/v2/contacts/{id} (delete an existing contact) It’s that simple! In fact, that’s all you need to do to manage the contacts in your TextMagic account!  ## Sandbox Sandbox is a tool to test TextMagic REST API requests without the need to install any applications or write any code. Here, we explain the following details about Sandbox: * The credentials area * Command documentation * How it works  <a href=\"\">Go to TextMagic Sandbox</a>  ### The credentials area To make requests using your TextMagic account, you need to enter your account username and your API key into the corresponding fields. You may also Save them in your browser or press Clear to erase them.  ![alt text](images/sandbox.png)   # noqa: E501

    OpenAPI spec version: 2
    Contact: support@textmagi.biz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from TextMagic.api.text_magic_api import TextMagicApi

# import ApiClient
from TextMagic.api_client import ApiClient
from TextMagic.configuration import Configuration
# import models into sdk package
from TextMagic.models.assign_contacts_to_list_input_object import AssignContactsToListInputObject
from TextMagic.models.bad_request_response import BadRequestResponse
from TextMagic.models.bad_request_response_errors import BadRequestResponseErrors
from TextMagic.models.block_contact_input_object import BlockContactInputObject
from TextMagic.models.bulk_session import BulkSession
from TextMagic.models.buy_dedicated_number_input_object import BuyDedicatedNumberInputObject
from TextMagic.models.chat import Chat
from TextMagic.models.check_phone_verification_code_input_object import CheckPhoneVerificationCodeInputObject
from TextMagic.models.clear_and_assign_contacts_to_list_input_object import ClearAndAssignContactsToListInputObject
from TextMagic.models.close_chats_bulk_input_object import CloseChatsBulkInputObject
from TextMagic.models.contact import Contact
from TextMagic.models.contact_custom_field import ContactCustomField
from TextMagic.models.contact_image import ContactImage
from TextMagic.models.contact_note import ContactNote
from TextMagic.models.conversation import Conversation
from TextMagic.models.country import Country
from TextMagic.models.create_contact_input_object import CreateContactInputObject
from TextMagic.models.create_contact_note_input_object import CreateContactNoteInputObject
from TextMagic.models.create_custom_field_input_object import CreateCustomFieldInputObject
from TextMagic.models.create_list_input_object import CreateListInputObject
from TextMagic.models.create_push_token_input_object import CreatePushTokenInputObject
from TextMagic.models.create_survey_input_object import CreateSurveyInputObject
from TextMagic.models.create_survey_node_input_object import CreateSurveyNodeInputObject
from TextMagic.models.create_template_input_object import CreateTemplateInputObject
from TextMagic.models.currency import Currency
from TextMagic.models.delete_chat_messages_bulk_input_object import DeleteChatMessagesBulkInputObject
from TextMagic.models.delete_chats_bulk_input_object import DeleteChatsBulkInputObject
from TextMagic.models.delete_contacs_from_list_object import DeleteContacsFromListObject
from TextMagic.models.delete_contact_notes_bulk_input_object import DeleteContactNotesBulkInputObject
from TextMagic.models.delete_contacts_by_ids_input_object import DeleteContactsByIdsInputObject
from TextMagic.models.delete_inbound_messages_bulk_input_object import DeleteInboundMessagesBulkInputObject
from TextMagic.models.delete_list_contacts_bulk_input_object import DeleteListContactsBulkInputObject
from TextMagic.models.delete_lists_bulk_input_object import DeleteListsBulkInputObject
from TextMagic.models.delete_message_sessions_bulk_input_object import DeleteMessageSessionsBulkInputObject
from TextMagic.models.delete_outbound_messages_bulk_input_object import DeleteOutboundMessagesBulkInputObject
from TextMagic.models.delete_scheduled_messages_bulk_input_object import DeleteScheduledMessagesBulkInputObject
from TextMagic.models.delete_templates_bulk_input_object import DeleteTemplatesBulkInputObject
from TextMagic.models.do_auth_input_object import DoAuthInputObject
from TextMagic.models.do_auth_response import DoAuthResponse
from TextMagic.models.do_auth_response_min_versions import DoAuthResponseMinVersions
from TextMagic.models.do_carrier_lookup_response import DoCarrierLookupResponse
from TextMagic.models.do_email_lookup_response import DoEmailLookupResponse
from TextMagic.models.favorite_contact import FavoriteContact
from TextMagic.models.forwarded_call import ForwardedCall
from TextMagic.models.get_all_bulk_sessions_response import GetAllBulkSessionsResponse
from TextMagic.models.get_all_chats_response import GetAllChatsResponse
from TextMagic.models.get_all_inbound_messages_response import GetAllInboundMessagesResponse
from TextMagic.models.get_all_message_sessions_response import GetAllMessageSessionsResponse
from TextMagic.models.get_all_outbound_messages_response import GetAllOutboundMessagesResponse
from TextMagic.models.get_all_scheduled_messages_response import GetAllScheduledMessagesResponse
from TextMagic.models.get_all_templates_response import GetAllTemplatesResponse
from TextMagic.models.get_available_dedicated_numbers_response import GetAvailableDedicatedNumbersResponse
from TextMagic.models.get_available_sender_setting_options_response import GetAvailableSenderSettingOptionsResponse
from TextMagic.models.get_balance_notification_options_response import GetBalanceNotificationOptionsResponse
from TextMagic.models.get_balance_notification_settings_response import GetBalanceNotificationSettingsResponse
from TextMagic.models.get_blocked_contacts_response import GetBlockedContactsResponse
from TextMagic.models.get_callback_settings_response import GetCallbackSettingsResponse
from TextMagic.models.get_chat_messages_response import GetChatMessagesResponse
from TextMagic.models.get_contact_import_session_progress_response import GetContactImportSessionProgressResponse
from TextMagic.models.get_contact_notes_response import GetContactNotesResponse
from TextMagic.models.get_contacts_autocomplete_response import GetContactsAutocompleteResponse
from TextMagic.models.get_contacts_by_list_id_response import GetContactsByListIdResponse
from TextMagic.models.get_contacts_response import GetContactsResponse
from TextMagic.models.get_custom_fields_response import GetCustomFieldsResponse
from TextMagic.models.get_favourites_response import GetFavouritesResponse
from TextMagic.models.get_forwarded_calls_response import GetForwardedCallsResponse
from TextMagic.models.get_inbound_messages_notification_settings_response import GetInboundMessagesNotificationSettingsResponse
from TextMagic.models.get_invoices_response import GetInvoicesResponse
from TextMagic.models.get_list_contacts_ids_response import GetListContactsIdsResponse
from TextMagic.models.get_lists_of_contact_response import GetListsOfContactResponse
from TextMagic.models.get_message_preview_response import GetMessagePreviewResponse
from TextMagic.models.get_message_price_response import GetMessagePriceResponse
from TextMagic.models.get_message_prices_response import GetMessagePricesResponse
from TextMagic.models.get_message_session_stat_response import GetMessageSessionStatResponse
from TextMagic.models.get_messages_by_session_id_response import GetMessagesBySessionIdResponse
from TextMagic.models.get_messaging_counters_response import GetMessagingCountersResponse
from TextMagic.models.get_messaging_stat_response import GetMessagingStatResponse
from TextMagic.models.get_outbound_messages_history_response import GetOutboundMessagesHistoryResponse
from TextMagic.models.get_push_tokens_response import GetPushTokensResponse
from TextMagic.models.get_sender_ids_response import GetSenderIdsResponse
from TextMagic.models.get_sender_settings_response import GetSenderSettingsResponse
from TextMagic.models.get_spending_stat_response import GetSpendingStatResponse
from TextMagic.models.get_state_response import GetStateResponse
from TextMagic.models.get_subaccounts_with_tokens_input_object import GetSubaccountsWithTokensInputObject
from TextMagic.models.get_subaccounts_with_tokens_response import GetSubaccountsWithTokensResponse
from TextMagic.models.get_survey_nodes_response import GetSurveyNodesResponse
from TextMagic.models.get_surveys_response import GetSurveysResponse
from TextMagic.models.get_unread_messages_total_response import GetUnreadMessagesTotalResponse
from TextMagic.models.get_unsubscribers_response import GetUnsubscribersResponse
from TextMagic.models.get_user_dedicated_numbers_response import GetUserDedicatedNumbersResponse
from TextMagic.models.get_user_lists_response import GetUserListsResponse
from TextMagic.models.get_versions_response import GetVersionsResponse
from TextMagic.models.group import Group
from TextMagic.models.group_image import GroupImage
from TextMagic.models.invite_subaccount_input_object import InviteSubaccountInputObject
from TextMagic.models.invoice import Invoice
from TextMagic.models.mark_chats_read_bulk_input_object import MarkChatsReadBulkInputObject
from TextMagic.models.mark_chats_unread_bulk_input_object import MarkChatsUnreadBulkInputObject
from TextMagic.models.merge_survey_nodes_input_object import MergeSurveyNodesInputObject
from TextMagic.models.message_in import MessageIn
from TextMagic.models.message_out import MessageOut
from TextMagic.models.message_session import MessageSession
from TextMagic.models.message_template import MessageTemplate
from TextMagic.models.messages_ics import MessagesIcs
from TextMagic.models.messages_ics_parameters import MessagesIcsParameters
from TextMagic.models.messages_ics_parameters_recipients import MessagesIcsParametersRecipients
from TextMagic.models.messages_ics_text_parameters import MessagesIcsTextParameters
from TextMagic.models.messaging_stat_item import MessagingStatItem
from TextMagic.models.mute_chat_input_object import MuteChatInputObject
from TextMagic.models.mute_chats_bulk_input_object import MuteChatsBulkInputObject
from TextMagic.models.not_found_response import NotFoundResponse
from TextMagic.models.ping_response import PingResponse
from TextMagic.models.push_token import PushToken
from TextMagic.models.reopen_chats_bulk_input_object import ReopenChatsBulkInputObject
from TextMagic.models.request_new_subaccount_token_input_object import RequestNewSubaccountTokenInputObject
from TextMagic.models.request_sender_id_input_object import RequestSenderIdInputObject
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.models.search_chats_by_ids_response import SearchChatsByIdsResponse
from TextMagic.models.search_chats_by_receipent_response import SearchChatsByReceipentResponse
from TextMagic.models.search_chats_response import SearchChatsResponse
from TextMagic.models.search_contacts_response import SearchContactsResponse
from TextMagic.models.search_inbound_messages_response import SearchInboundMessagesResponse
from TextMagic.models.search_lists_response import SearchListsResponse
from TextMagic.models.search_outbound_messages_response import SearchOutboundMessagesResponse
from TextMagic.models.search_scheduled_messages_response import SearchScheduledMessagesResponse
from TextMagic.models.search_templates_response import SearchTemplatesResponse
from TextMagic.models.send_message_input_object import SendMessageInputObject
from TextMagic.models.send_message_response import SendMessageResponse
from TextMagic.models.sender_id import SenderId
from TextMagic.models.set_chat_status_input_object import SetChatStatusInputObject
from TextMagic.models.subaccount_with_token import SubaccountWithToken
from TextMagic.models.successful_response import SuccessfulResponse
from TextMagic.models.survey import Survey
from TextMagic.models.survey_node import SurveyNode
from TextMagic.models.survey_recipient import SurveyRecipient
from TextMagic.models.survey_sender_countries import SurveySenderCountries
from TextMagic.models.timezone import Timezone
from TextMagic.models.unauthorized_response import UnauthorizedResponse
from TextMagic.models.unblock_contact_input_object import UnblockContactInputObject
from TextMagic.models.unblock_contacts_bulk_input_object import UnblockContactsBulkInputObject
from TextMagic.models.unmute_chats_bulk_input_object import UnmuteChatsBulkInputObject
from TextMagic.models.unsubscribe_contact_input_object import UnsubscribeContactInputObject
from TextMagic.models.unsubscribed_contact import UnsubscribedContact
from TextMagic.models.update_balance_notification_settings_input_object import UpdateBalanceNotificationSettingsInputObject
from TextMagic.models.update_callback_settings_input_object import UpdateCallbackSettingsInputObject
from TextMagic.models.update_chat_desktop_notification_settings_input_object import UpdateChatDesktopNotificationSettingsInputObject
from TextMagic.models.update_contact_input_object import UpdateContactInputObject
from TextMagic.models.update_contact_note_input_object import UpdateContactNoteInputObject
from TextMagic.models.update_current_user_input_object import UpdateCurrentUserInputObject
from TextMagic.models.update_current_user_response import UpdateCurrentUserResponse
from TextMagic.models.update_custom_field_input_object import UpdateCustomFieldInputObject
from TextMagic.models.update_custom_field_value_input_object import UpdateCustomFieldValueInputObject
from TextMagic.models.update_inbound_messages_notification_settings_input_object import UpdateInboundMessagesNotificationSettingsInputObject
from TextMagic.models.update_list_object import UpdateListObject
from TextMagic.models.update_password_input_object import UpdatePasswordInputObject
from TextMagic.models.update_sender_setting_input_object import UpdateSenderSettingInputObject
from TextMagic.models.update_survey_input_object import UpdateSurveyInputObject
from TextMagic.models.update_survey_node_input_object import UpdateSurveyNodeInputObject
from TextMagic.models.update_template_input_object import UpdateTemplateInputObject
from TextMagic.models.upload_message_attachment_response import UploadMessageAttachmentResponse
from TextMagic.models.user import User
from TextMagic.models.user_custom_field import UserCustomField
from TextMagic.models.user_image import UserImage
from TextMagic.models.user_statement import UserStatement
from TextMagic.models.users_inbound import UsersInbound
