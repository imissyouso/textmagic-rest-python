# coding: utf-8

"""
    TextMagic API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    Contact: support@textmagi.biz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import TextMagic
from TextMagic.api.text_magic_api import TextMagicApi  # noqa: E501
from TextMagic.rest import ApiException


class TestTextMagicApi(unittest.TestCase):
    """TextMagicApi unit test stubs"""

    def setUp(self):
        self.api = TextMagic.api.text_magic_api.TextMagicApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_assign_contacts_to_list(self):
        """Test case for assign_contacts_to_list

        Assign contacts to the specified list.  # noqa: E501
        """
        pass

    def test_block_contact(self):
        """Test case for block_contact

        Block contact from inbound and outbound communication by phone number.  # noqa: E501
        """
        pass

    def test_buy_dedicated_number(self):
        """Test case for buy_dedicated_number

        Buy a dedicated number  # noqa: E501
        """
        pass

    def test_cancel_survey(self):
        """Test case for cancel_survey

        Cancel a survey.  # noqa: E501
        """
        pass

    def test_cancel_verification(self):
        """Test case for cancel_verification

        Cancel verification process  # noqa: E501
        """
        pass

    def test_check_phone_verification_code(self):
        """Test case for check_phone_verification_code

        Check user phone verification code  # noqa: E501
        """
        pass

    def test_check_phone_verification_code_tfa(self):
        """Test case for check_phone_verification_code_tfa

        Step 2: Check the verification code   # noqa: E501
        """
        pass

    def test_clear_and_assign_contacts_to_list(self):
        """Test case for clear_and_assign_contacts_to_list

        Reset list members to the specified contacts.  # noqa: E501
        """
        pass

    def test_close_chats_bulk(self):
        """Test case for close_chats_bulk

        Close chats (bulk)  # noqa: E501
        """
        pass

    def test_close_read_chats(self):
        """Test case for close_read_chats

        Close read chats  # noqa: E501
        """
        pass

    def test_close_subaccount(self):
        """Test case for close_subaccount

        Close sub-account  # noqa: E501
        """
        pass

    def test_create_contact(self):
        """Test case for create_contact

        Create a new contact from the submitted data.  # noqa: E501
        """
        pass

    def test_create_contact_note(self):
        """Test case for create_contact_note

        Create a new contact note.  # noqa: E501
        """
        pass

    def test_create_custom_field(self):
        """Test case for create_custom_field

        Create a new custom field from the submitted data.  # noqa: E501
        """
        pass

    def test_create_list(self):
        """Test case for create_list

        Create a new list  # noqa: E501
        """
        pass

    def test_create_push_token(self):
        """Test case for create_push_token

        Add or update a device token.  # noqa: E501
        """
        pass

    def test_create_survey(self):
        """Test case for create_survey

        Create a new survey from the submitted data.  # noqa: E501
        """
        pass

    def test_create_survey_node(self):
        """Test case for create_survey_node

        Create a new node from the submitted data.  # noqa: E501
        """
        pass

    def test_create_template(self):
        """Test case for create_template

        Create a template  # noqa: E501
        """
        pass

    def test_delete_all_contacts(self):
        """Test case for delete_all_contacts

        Delete all contacts.  # noqa: E501
        """
        pass

    def test_delete_all_outbound_messages(self):
        """Test case for delete_all_outbound_messages

        Delete all messages  # noqa: E501
        """
        pass

    def test_delete_avatar(self):
        """Test case for delete_avatar

        Delete an avatar  # noqa: E501
        """
        pass

    def test_delete_chat_messages(self):
        """Test case for delete_chat_messages

        Delete chat messages by ID(s)  # noqa: E501
        """
        pass

    def test_delete_chats_bulk(self):
        """Test case for delete_chats_bulk

        Delete chats (bulk)  # noqa: E501
        """
        pass

    def test_delete_contact(self):
        """Test case for delete_contact

        Delete a single contact.  # noqa: E501
        """
        pass

    def test_delete_contact_avatar(self):
        """Test case for delete_contact_avatar

        Delete an avatar for the contact.  # noqa: E501
        """
        pass

    def test_delete_contact_note(self):
        """Test case for delete_contact_note

        Delete a single contact note.  # noqa: E501
        """
        pass

    def test_delete_contact_notes_bulk(self):
        """Test case for delete_contact_notes_bulk

        Delete contact note by given ID(s) or delete all contact notes.  # noqa: E501
        """
        pass

    def test_delete_contacts_by_ids(self):
        """Test case for delete_contacts_by_ids

        Delete contact by given ID(s) or delete all contacts.  # noqa: E501
        """
        pass

    def test_delete_contacts_from_list(self):
        """Test case for delete_contacts_from_list

        Unassign contacts from the specified list.  # noqa: E501
        """
        pass

    def test_delete_custom_field(self):
        """Test case for delete_custom_field

        Delete a single custom field.  # noqa: E501
        """
        pass

    def test_delete_dedicated_number(self):
        """Test case for delete_dedicated_number

        Cancel dedicated number subscription  # noqa: E501
        """
        pass

    def test_delete_inbound_message(self):
        """Test case for delete_inbound_message

        Delete a single inbound message  # noqa: E501
        """
        pass

    def test_delete_inbound_messages_bulk(self):
        """Test case for delete_inbound_messages_bulk

        Delete inbound messages (bulk)  # noqa: E501
        """
        pass

    def test_delete_list(self):
        """Test case for delete_list

        Delete a single list.  # noqa: E501
        """
        pass

    def test_delete_list_avatar(self):
        """Test case for delete_list_avatar

        Delete an avatar for the list.  # noqa: E501
        """
        pass

    def test_delete_list_contacts_bulk(self):
        """Test case for delete_list_contacts_bulk

        Delete contact from list by given ID(s) or all contacts from list.  # noqa: E501
        """
        pass

    def test_delete_lists_bulk(self):
        """Test case for delete_lists_bulk

        Delete list by given ID(s) or delete all lists.  # noqa: E501
        """
        pass

    def test_delete_message_session(self):
        """Test case for delete_message_session

        Delete a session  # noqa: E501
        """
        pass

    def test_delete_message_sessions_bulk(self):
        """Test case for delete_message_sessions_bulk

        Delete sessions (bulk)  # noqa: E501
        """
        pass

    def test_delete_outbound_message(self):
        """Test case for delete_outbound_message

        Delete message  # noqa: E501
        """
        pass

    def test_delete_outbound_messages_bulk(self):
        """Test case for delete_outbound_messages_bulk

        Delete messages (bulk)  # noqa: E501
        """
        pass

    def test_delete_push_token(self):
        """Test case for delete_push_token

        Delete a push notification device token.  # noqa: E501
        """
        pass

    def test_delete_scheduled_message(self):
        """Test case for delete_scheduled_message

        Delete a single scheduled message  # noqa: E501
        """
        pass

    def test_delete_scheduled_messages_bulk(self):
        """Test case for delete_scheduled_messages_bulk

        Delete scheduled messages (bulk)  # noqa: E501
        """
        pass

    def test_delete_sender_id(self):
        """Test case for delete_sender_id

        Delete a Sender ID  # noqa: E501
        """
        pass

    def test_delete_survey(self):
        """Test case for delete_survey

        Delete a survey.  # noqa: E501
        """
        pass

    def test_delete_survey_node(self):
        """Test case for delete_survey_node

        Delete a node.  # noqa: E501
        """
        pass

    def test_delete_template(self):
        """Test case for delete_template

        Delete a template  # noqa: E501
        """
        pass

    def test_delete_templates_bulk(self):
        """Test case for delete_templates_bulk

        Delete templates (bulk)  # noqa: E501
        """
        pass

    def test_do_auth(self):
        """Test case for do_auth

        Authenticate user by given username and password.  # noqa: E501
        """
        pass

    def test_do_carrier_lookup(self):
        """Test case for do_carrier_lookup

        Carrier Lookup  # noqa: E501
        """
        pass

    def test_do_email_lookup(self):
        """Test case for do_email_lookup

        Validate Email address using Email Lookup tool  # noqa: E501
        """
        pass

    def test_duplicate_survey(self):
        """Test case for duplicate_survey

        Duplicate a survey.  # noqa: E501
        """
        pass

    def test_get_all_bulk_sessions(self):
        """Test case for get_all_bulk_sessions

        Get all bulk sending sessions.  # noqa: E501
        """
        pass

    def test_get_all_chats(self):
        """Test case for get_all_chats

        Get all chats  # noqa: E501
        """
        pass

    def test_get_all_inbound_messages(self):
        """Test case for get_all_inbound_messages

        Get all inbound messages  # noqa: E501
        """
        pass

    def test_get_all_message_sessions(self):
        """Test case for get_all_message_sessions

        Get all sessions  # noqa: E501
        """
        pass

    def test_get_all_outbound_messages(self):
        """Test case for get_all_outbound_messages

        Get all messages  # noqa: E501
        """
        pass

    def test_get_all_scheduled_messages(self):
        """Test case for get_all_scheduled_messages

        Get all scheduled messages  # noqa: E501
        """
        pass

    def test_get_all_templates(self):
        """Test case for get_all_templates

        Get all templates  # noqa: E501
        """
        pass

    def test_get_available_dedicated_numbers(self):
        """Test case for get_available_dedicated_numbers

        Find dedicated numbers available for purchase  # noqa: E501
        """
        pass

    def test_get_available_sender_setting_options(self):
        """Test case for get_available_sender_setting_options

        Get available sender settings  # noqa: E501
        """
        pass

    def test_get_balance_notification_options(self):
        """Test case for get_balance_notification_options

        Returns the list of available balance options which can be used as a bound to determine when to send email to user with low balance notification. See https://my.textmagic.com/online/account/notifications/balance  # noqa: E501
        """
        pass

    def test_get_balance_notification_settings(self):
        """Test case for get_balance_notification_settings

        Get balance notification settings  # noqa: E501
        """
        pass

    def test_get_blocked_contacts(self):
        """Test case for get_blocked_contacts

        Get blocked contacts.  # noqa: E501
        """
        pass

    def test_get_bulk_session(self):
        """Test case for get_bulk_session

        Get bulk message session status.  # noqa: E501
        """
        pass

    def test_get_callback_settings(self):
        """Test case for get_callback_settings

        Fetch callback URL settings  # noqa: E501
        """
        pass

    def test_get_calls_prices(self):
        """Test case for get_calls_prices

        Check pricing for a inbound/outbound call.  # noqa: E501
        """
        pass

    def test_get_chat(self):
        """Test case for get_chat

        Get a single chat  # noqa: E501
        """
        pass

    def test_get_chat_by_phone(self):
        """Test case for get_chat_by_phone

        Find chats by phone  # noqa: E501
        """
        pass

    def test_get_chat_messages(self):
        """Test case for get_chat_messages

        Get chat messages  # noqa: E501
        """
        pass

    def test_get_contact(self):
        """Test case for get_contact

        Get a single contact.  # noqa: E501
        """
        pass

    def test_get_contact_by_phone(self):
        """Test case for get_contact_by_phone

        Get a single contact by phone number.  # noqa: E501
        """
        pass

    def test_get_contact_if_blocked(self):
        """Test case for get_contact_if_blocked

        Check is that phone number blocked  # noqa: E501
        """
        pass

    def test_get_contact_import_session_progress(self):
        """Test case for get_contact_import_session_progress

        Get contact import session progress.  # noqa: E501
        """
        pass

    def test_get_contact_note(self):
        """Test case for get_contact_note

        Get a single contact note.  # noqa: E501
        """
        pass

    def test_get_contact_notes(self):
        """Test case for get_contact_notes

        Fetch notes assigned to the given contact.  # noqa: E501
        """
        pass

    def test_get_contacts(self):
        """Test case for get_contacts

        Get all user contacts.  # noqa: E501
        """
        pass

    def test_get_contacts_autocomplete(self):
        """Test case for get_contacts_autocomplete

        Get contacts autocomplete suggestions by given search term.  # noqa: E501
        """
        pass

    def test_get_contacts_by_list_id(self):
        """Test case for get_contacts_by_list_id

        Fetch user contacts by given group id.  # noqa: E501
        """
        pass

    def test_get_countries(self):
        """Test case for get_countries

        Return list of countries.  # noqa: E501
        """
        pass

    def test_get_current_user(self):
        """Test case for get_current_user

        Get current account information  # noqa: E501
        """
        pass

    def test_get_custom_field(self):
        """Test case for get_custom_field

        Get a single custom field.  # noqa: E501
        """
        pass

    def test_get_custom_fields(self):
        """Test case for get_custom_fields

        Get all contact custom fields.  # noqa: E501
        """
        pass

    def test_get_dedicated_number(self):
        """Test case for get_dedicated_number

        Get the details of a specific dedicated number  # noqa: E501
        """
        pass

    def test_get_disallowed_rules(self):
        """Test case for get_disallowed_rules

        Get disallowed permissions  # noqa: E501
        """
        pass

    def test_get_favourites(self):
        """Test case for get_favourites

        Get favorite contacts and lists.  # noqa: E501
        """
        pass

    def test_get_inbound_message(self):
        """Test case for get_inbound_message

        Get a single inbound message  # noqa: E501
        """
        pass

    def test_get_inbound_messages_notification_settings(self):
        """Test case for get_inbound_messages_notification_settings

        Get inbound messages notification settings  # noqa: E501
        """
        pass

    def test_get_invoices(self):
        """Test case for get_invoices

        Get all invoices  # noqa: E501
        """
        pass

    def test_get_list(self):
        """Test case for get_list

        Get the details of a specific list  # noqa: E501
        """
        pass

    def test_get_list_contacts_ids(self):
        """Test case for get_list_contacts_ids

        Fetch all contacts IDs belonging to the list with ID.  # noqa: E501
        """
        pass

    def test_get_lists(self):
        """Test case for get_lists

        Get all lists  # noqa: E501
        """
        pass

    def test_get_lists_of_contact(self):
        """Test case for get_lists_of_contact

        Return lists which contact belongs to.  # noqa: E501
        """
        pass

    def test_get_message_preview(self):
        """Test case for get_message_preview

        Preview message  # noqa: E501
        """
        pass

    def test_get_message_price(self):
        """Test case for get_message_price

        Check price  # noqa: E501
        """
        pass

    def test_get_message_session(self):
        """Test case for get_message_session

        Get a session details  # noqa: E501
        """
        pass

    def test_get_message_session_stat(self):
        """Test case for get_message_session_stat

        Get a session statistics  # noqa: E501
        """
        pass

    def test_get_messages_by_session_id(self):
        """Test case for get_messages_by_session_id

        Get a session messages  # noqa: E501
        """
        pass

    def test_get_messaging_counters(self):
        """Test case for get_messaging_counters

        Get sent/received messages counters values  # noqa: E501
        """
        pass

    def test_get_messaging_stat(self):
        """Test case for get_messaging_stat

        Get messaging statistics  # noqa: E501
        """
        pass

    def test_get_outbound_message(self):
        """Test case for get_outbound_message

        Get a single message  # noqa: E501
        """
        pass

    def test_get_outbound_messages_history(self):
        """Test case for get_outbound_messages_history

        Get history  # noqa: E501
        """
        pass

    def test_get_push_tokens(self):
        """Test case for get_push_tokens

        Get all device tokens assigned to the current account  # noqa: E501
        """
        pass

    def test_get_scheduled_message(self):
        """Test case for get_scheduled_message

        Get a single scheduled message  # noqa: E501
        """
        pass

    def test_get_sender_id(self):
        """Test case for get_sender_id

        Get the details of a specific Sender ID  # noqa: E501
        """
        pass

    def test_get_sender_ids(self):
        """Test case for get_sender_ids

        Get all your approved Sender IDs  # noqa: E501
        """
        pass

    def test_get_sender_settings(self):
        """Test case for get_sender_settings

        Get current sender settings  # noqa: E501
        """
        pass

    def test_get_spending_stat(self):
        """Test case for get_spending_stat

        Get spending statistics  # noqa: E501
        """
        pass

    def test_get_state(self):
        """Test case for get_state

        Get current entities state  # noqa: E501
        """
        pass

    def test_get_subaccount(self):
        """Test case for get_subaccount

        Get sub-account information  # noqa: E501
        """
        pass

    def test_get_subaccounts(self):
        """Test case for get_subaccounts

        Get sub-accounts list  # noqa: E501
        """
        pass

    def test_get_subaccounts_with_tokens(self):
        """Test case for get_subaccounts_with_tokens

        Get all sub-accounts with their REST API tokens associated with app name  # noqa: E501
        """
        pass

    def test_get_survey(self):
        """Test case for get_survey

        Get a survey by id.  # noqa: E501
        """
        pass

    def test_get_survey_node(self):
        """Test case for get_survey_node

        Get a node by id.  # noqa: E501
        """
        pass

    def test_get_survey_nodes(self):
        """Test case for get_survey_nodes

        Fetch nodes by given survey id.  # noqa: E501
        """
        pass

    def test_get_surveys(self):
        """Test case for get_surveys

        Get all user surveys.  # noqa: E501
        """
        pass

    def test_get_template(self):
        """Test case for get_template

        Get a template details  # noqa: E501
        """
        pass

    def test_get_timezones(self):
        """Test case for get_timezones

        Return all available timezone IDs.  # noqa: E501
        """
        pass

    def test_get_unread_messages_total(self):
        """Test case for get_unread_messages_total

        Get unread messages number  # noqa: E501
        """
        pass

    def test_get_unsubscribed_contact(self):
        """Test case for get_unsubscribed_contact

        Get a single unsubscribed contact.  # noqa: E501
        """
        pass

    def test_get_unsubscribers(self):
        """Test case for get_unsubscribers

        Get all contact have unsubscribed from your communication.  # noqa: E501
        """
        pass

    def test_get_user_dedicated_numbers(self):
        """Test case for get_user_dedicated_numbers

        Get all your dedicated numbers  # noqa: E501
        """
        pass

    def test_get_versions(self):
        """Test case for get_versions

        Get minimal valid apps versions  # noqa: E501
        """
        pass

    def test_invite_subaccount(self):
        """Test case for invite_subaccount

        Invite a new sub-account  # noqa: E501
        """
        pass

    def test_mark_chats_read_bulk(self):
        """Test case for mark_chats_read_bulk

        Mark chats as read (bulk)  # noqa: E501
        """
        pass

    def test_mark_chats_unread_bulk(self):
        """Test case for mark_chats_unread_bulk

        Mark chats as unread (bulk)  # noqa: E501
        """
        pass

    def test_merge_survey_nodes(self):
        """Test case for merge_survey_nodes

        Merge two question nodes.  # noqa: E501
        """
        pass

    def test_mute_chat(self):
        """Test case for mute_chat

        Mute chat sounds  # noqa: E501
        """
        pass

    def test_mute_chats_bulk(self):
        """Test case for mute_chats_bulk

        Mute chats (bulk)  # noqa: E501
        """
        pass

    def test_ping(self):
        """Test case for ping

        Just does a pong.  # noqa: E501
        """
        pass

    def test_reopen_chats_bulk(self):
        """Test case for reopen_chats_bulk

        Reopen chats (bulk)  # noqa: E501
        """
        pass

    def test_request_new_subaccount_token(self):
        """Test case for request_new_subaccount_token

        Request a new REST API token for sub-account  # noqa: E501
        """
        pass

    def test_request_sender_id(self):
        """Test case for request_sender_id

        Apply for a new Sender ID  # noqa: E501
        """
        pass

    def test_reset_survey(self):
        """Test case for reset_survey

        Reset a survey flow.  # noqa: E501
        """
        pass

    def test_search_chats(self):
        """Test case for search_chats

        Find chats by message text  # noqa: E501
        """
        pass

    def test_search_chats_by_ids(self):
        """Test case for search_chats_by_ids

        Find chats (bulk)  # noqa: E501
        """
        pass

    def test_search_chats_by_receipent(self):
        """Test case for search_chats_by_receipent

        Find chats by recipient  # noqa: E501
        """
        pass

    def test_search_contacts(self):
        """Test case for search_contacts

        Find user contacts by given parameters.  # noqa: E501
        """
        pass

    def test_search_inbound_messages(self):
        """Test case for search_inbound_messages

        Find inbound messages  # noqa: E501
        """
        pass

    def test_search_lists(self):
        """Test case for search_lists

        Find contact lists by given parameters.  # noqa: E501
        """
        pass

    def test_search_outbound_messages(self):
        """Test case for search_outbound_messages

        Find messages  # noqa: E501
        """
        pass

    def test_search_scheduled_messages(self):
        """Test case for search_scheduled_messages

        Find scheduled messages  # noqa: E501
        """
        pass

    def test_search_templates(self):
        """Test case for search_templates

        Find templates by criteria  # noqa: E501
        """
        pass

    def test_send_email_verification_code(self):
        """Test case for send_email_verification_code

        Send user email verification  # noqa: E501
        """
        pass

    def test_send_message(self):
        """Test case for send_message

        Send message  # noqa: E501
        """
        pass

    def test_send_phone_verification_code(self):
        """Test case for send_phone_verification_code

        Send user phone verification  # noqa: E501
        """
        pass

    def test_send_phone_verification_code_tfa(self):
        """Test case for send_phone_verification_code_tfa

        Step 1: Send a verification code   # noqa: E501
        """
        pass

    def test_set_chat_status(self):
        """Test case for set_chat_status

        Change chat status  # noqa: E501
        """
        pass

    def test_start_survey(self):
        """Test case for start_survey

        Start a survey.  # noqa: E501
        """
        pass

    def test_unblock_contact(self):
        """Test case for unblock_contact

        Unblock contact by phone number.  # noqa: E501
        """
        pass

    def test_unblock_contacts_bulk(self):
        """Test case for unblock_contacts_bulk

        Unblock several contacts by blocked contact ids or unblock all contacts  # noqa: E501
        """
        pass

    def test_unmute_chats_bulk(self):
        """Test case for unmute_chats_bulk

        Unmute chats (bulk)  # noqa: E501
        """
        pass

    def test_unsubscribe_contact(self):
        """Test case for unsubscribe_contact

        Unsubscribe contact from your communication by phone number.  # noqa: E501
        """
        pass

    def test_update_balance_notification_settings(self):
        """Test case for update_balance_notification_settings

        Update balance notification settings  # noqa: E501
        """
        pass

    def test_update_callback_settings(self):
        """Test case for update_callback_settings

        Update callback URL settings  # noqa: E501
        """
        pass

    def test_update_chat_desktop_notification_settings(self):
        """Test case for update_chat_desktop_notification_settings

        Update chat desktop notification settings  # noqa: E501
        """
        pass

    def test_update_contact(self):
        """Test case for update_contact

        Update existing contact.  # noqa: E501
        """
        pass

    def test_update_contact_note(self):
        """Test case for update_contact_note

        Update existing contact note.  # noqa: E501
        """
        pass

    def test_update_current_user(self):
        """Test case for update_current_user

        Edit current account info  # noqa: E501
        """
        pass

    def test_update_custom_field(self):
        """Test case for update_custom_field

        Update existing custom field.  # noqa: E501
        """
        pass

    def test_update_custom_field_value(self):
        """Test case for update_custom_field_value

        Update contact's custom field value.  # noqa: E501
        """
        pass

    def test_update_inbound_messages_notification_settings(self):
        """Test case for update_inbound_messages_notification_settings

        Update inbound messages notification settings  # noqa: E501
        """
        pass

    def test_update_list(self):
        """Test case for update_list

        Update existing list.  # noqa: E501
        """
        pass

    def test_update_password(self):
        """Test case for update_password

        Change user password.  # noqa: E501
        """
        pass

    def test_update_sender_setting(self):
        """Test case for update_sender_setting

        Change sender settings  # noqa: E501
        """
        pass

    def test_update_survey(self):
        """Test case for update_survey

        Update existing survey.  # noqa: E501
        """
        pass

    def test_update_survey_node(self):
        """Test case for update_survey_node

        Update existing node.  # noqa: E501
        """
        pass

    def test_update_template(self):
        """Test case for update_template

        Update a template  # noqa: E501
        """
        pass

    def test_upload_avatar(self):
        """Test case for upload_avatar

        Upload an avatar  # noqa: E501
        """
        pass

    def test_upload_contact_avatar(self):
        """Test case for upload_contact_avatar

        Add an avatar for the contact.  # noqa: E501
        """
        pass

    def test_upload_list_avatar(self):
        """Test case for upload_list_avatar

        Add an avatar for the list.  # noqa: E501
        """
        pass

    def test_upload_message_attachment(self):
        """Test case for upload_message_attachment

        Upload message attachment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
