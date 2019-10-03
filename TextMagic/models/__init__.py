# coding: utf-8

# flake8: noqa
"""
    TextMagic API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    Contact: support@textmagi.biz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from TextMagic.models.assign_contacts_to_list_input_object import AssignContactsToListInputObject
from TextMagic.models.bad_request_response import BadRequestResponse
from TextMagic.models.bad_request_response_errors import BadRequestResponseErrors
from TextMagic.models.block_contact_input_object import BlockContactInputObject
from TextMagic.models.bulk_session import BulkSession
from TextMagic.models.buy_dedicated_number_input_object import BuyDedicatedNumberInputObject
from TextMagic.models.chat import Chat
from TextMagic.models.check_phone_verification_code_input_object import CheckPhoneVerificationCodeInputObject
from TextMagic.models.check_phone_verification_code_input_object1 import CheckPhoneVerificationCodeInputObject1
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
from TextMagic.models.get_all_bulk_sessions_paginated_response import GetAllBulkSessionsPaginatedResponse
from TextMagic.models.get_all_chats_paginated_response import GetAllChatsPaginatedResponse
from TextMagic.models.get_all_inbound_messages_paginated_response import GetAllInboundMessagesPaginatedResponse
from TextMagic.models.get_all_message_sessions_paginated_response import GetAllMessageSessionsPaginatedResponse
from TextMagic.models.get_all_outbound_messages_paginated_response import GetAllOutboundMessagesPaginatedResponse
from TextMagic.models.get_all_scheduled_messages_paginated_response import GetAllScheduledMessagesPaginatedResponse
from TextMagic.models.get_all_templates_paginated_response import GetAllTemplatesPaginatedResponse
from TextMagic.models.get_available_dedicated_numbers_response import GetAvailableDedicatedNumbersResponse
from TextMagic.models.get_available_sender_setting_options_response import GetAvailableSenderSettingOptionsResponse
from TextMagic.models.get_balance_notification_options_response import GetBalanceNotificationOptionsResponse
from TextMagic.models.get_balance_notification_settings_response import GetBalanceNotificationSettingsResponse
from TextMagic.models.get_blocked_contacts_paginated_response import GetBlockedContactsPaginatedResponse
from TextMagic.models.get_callback_settings_response import GetCallbackSettingsResponse
from TextMagic.models.get_calls_prices_response import GetCallsPricesResponse
from TextMagic.models.get_chat_messages_paginated_response import GetChatMessagesPaginatedResponse
from TextMagic.models.get_contact_import_session_progress_response import GetContactImportSessionProgressResponse
from TextMagic.models.get_contact_notes_paginated_response import GetContactNotesPaginatedResponse
from TextMagic.models.get_contacts_autocomplete_response import GetContactsAutocompleteResponse
from TextMagic.models.get_contacts_by_list_id_paginated_response import GetContactsByListIdPaginatedResponse
from TextMagic.models.get_contacts_paginated_response import GetContactsPaginatedResponse
from TextMagic.models.get_countries_response import GetCountriesResponse
from TextMagic.models.get_custom_fields_paginated_response import GetCustomFieldsPaginatedResponse
from TextMagic.models.get_disallowed_rules_response import GetDisallowedRulesResponse
from TextMagic.models.get_favourites_paginated_response import GetFavouritesPaginatedResponse
from TextMagic.models.get_inbound_messages_notification_settings_response import GetInboundMessagesNotificationSettingsResponse
from TextMagic.models.get_invoices_paginated_response import GetInvoicesPaginatedResponse
from TextMagic.models.get_list_contacts_ids_response import GetListContactsIdsResponse
from TextMagic.models.get_lists_of_contact_paginated_response import GetListsOfContactPaginatedResponse
from TextMagic.models.get_lists_paginated_response import GetListsPaginatedResponse
from TextMagic.models.get_message_preview_response import GetMessagePreviewResponse
from TextMagic.models.get_message_price_response import GetMessagePriceResponse
from TextMagic.models.get_message_prices_response import GetMessagePricesResponse
from TextMagic.models.get_message_session_stat_response import GetMessageSessionStatResponse
from TextMagic.models.get_messages_by_session_id_paginated_response import GetMessagesBySessionIdPaginatedResponse
from TextMagic.models.get_messaging_counters_response import GetMessagingCountersResponse
from TextMagic.models.get_messaging_stat_response import GetMessagingStatResponse
from TextMagic.models.get_outbound_messages_history_paginated_response import GetOutboundMessagesHistoryPaginatedResponse
from TextMagic.models.get_push_tokens_response import GetPushTokensResponse
from TextMagic.models.get_sender_ids_paginated_response import GetSenderIdsPaginatedResponse
from TextMagic.models.get_sender_settings_response import GetSenderSettingsResponse
from TextMagic.models.get_spending_stat_paginated_response import GetSpendingStatPaginatedResponse
from TextMagic.models.get_state_response import GetStateResponse
from TextMagic.models.get_subaccounts_with_tokens_input_object import GetSubaccountsWithTokensInputObject
from TextMagic.models.get_subaccounts_with_tokens_response import GetSubaccountsWithTokensResponse
from TextMagic.models.get_survey_nodes_response import GetSurveyNodesResponse
from TextMagic.models.get_surveys_paginated_response import GetSurveysPaginatedResponse
from TextMagic.models.get_timezones_response import GetTimezonesResponse
from TextMagic.models.get_unread_messages_total_response import GetUnreadMessagesTotalResponse
from TextMagic.models.get_unsubscribers_paginated_response import GetUnsubscribersPaginatedResponse
from TextMagic.models.get_user_dedicated_numbers_paginated_response import GetUserDedicatedNumbersPaginatedResponse
from TextMagic.models.get_versions_response import GetVersionsResponse
from TextMagic.models.invite_subaccount_input_object import InviteSubaccountInputObject
from TextMagic.models.invoice import Invoice
from TextMagic.models.list import List
from TextMagic.models.list_image import ListImage
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
from TextMagic.models.search_chats_by_ids_paginated_response import SearchChatsByIdsPaginatedResponse
from TextMagic.models.search_chats_by_receipent_paginated_response import SearchChatsByReceipentPaginatedResponse
from TextMagic.models.search_chats_paginated_response import SearchChatsPaginatedResponse
from TextMagic.models.search_contacts_paginated_response import SearchContactsPaginatedResponse
from TextMagic.models.search_inbound_messages_paginated_response import SearchInboundMessagesPaginatedResponse
from TextMagic.models.search_lists_paginated_response import SearchListsPaginatedResponse
from TextMagic.models.search_outbound_messages_paginated_response import SearchOutboundMessagesPaginatedResponse
from TextMagic.models.search_scheduled_messages_paginated_response import SearchScheduledMessagesPaginatedResponse
from TextMagic.models.search_templates_paginated_response import SearchTemplatesPaginatedResponse
from TextMagic.models.send_message_input_object import SendMessageInputObject
from TextMagic.models.send_message_response import SendMessageResponse
from TextMagic.models.send_phone_verification_code_input_object import SendPhoneVerificationCodeInputObject
from TextMagic.models.send_phone_verification_code_response import SendPhoneVerificationCodeResponse
from TextMagic.models.sender_id import SenderId
from TextMagic.models.set_chat_status_input_object import SetChatStatusInputObject
from TextMagic.models.subaccount_with_token import SubaccountWithToken
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
