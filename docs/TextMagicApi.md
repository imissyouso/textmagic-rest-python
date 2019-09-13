# TextMagic.TextMagicApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_contacts_to_list**](TextMagicApi.md#assign_contacts_to_list) | **PUT** /api/v2/lists/{id}/contacts | Assign contacts to the specified list.
[**block_contact**](TextMagicApi.md#block_contact) | **POST** /api/v2/contacts/block | Block contact from inbound and outbound communication by phone number.
[**buy_dedicated_number**](TextMagicApi.md#buy_dedicated_number) | **POST** /api/v2/numbers | Buy a dedicated number and assign it to the specified account.
[**cancel_survey**](TextMagicApi.md#cancel_survey) | **PUT** /api/v2/surveys/{id}/cancel | Cancel a survey.
[**check_phone_verification_code**](TextMagicApi.md#check_phone_verification_code) | **PUT** /api/v2/user/phone/verification | Check user phone verification code
[**clear_and_assign_contacts_to_list**](TextMagicApi.md#clear_and_assign_contacts_to_list) | **POST** /api/v2/lists/{id}/contacts | Reset list members to the specified contacts.
[**close_chats_bulk**](TextMagicApi.md#close_chats_bulk) | **POST** /api/v2/chats/close/bulk | Close chats by chat ids or close all chats
[**close_read_chats**](TextMagicApi.md#close_read_chats) | **POST** /api/v2/chats/close/read | Close all chats that have no unread messages.
[**close_subaccount**](TextMagicApi.md#close_subaccount) | **DELETE** /api/v2/subaccounts/{id} | Close subaccount.
[**create_contact**](TextMagicApi.md#create_contact) | **POST** /api/v2/contacts | Create a new contact from the submitted data.
[**create_contact_note**](TextMagicApi.md#create_contact_note) | **POST** /api/v2/contacts/{id}/notes | Create a new contact note.
[**create_custom_field**](TextMagicApi.md#create_custom_field) | **POST** /api/v2/customfields | Create a new custom field from the submitted data.
[**create_list**](TextMagicApi.md#create_list) | **POST** /api/v2/lists | Create a new list from the submitted data.
[**create_push_token**](TextMagicApi.md#create_push_token) | **POST** /api/v2/push/tokens | Add or update a device token.
[**create_survey**](TextMagicApi.md#create_survey) | **POST** /api/v2/surveys | Create a new survey from the submitted data.
[**create_survey_node**](TextMagicApi.md#create_survey_node) | **POST** /api/v2/surveys/{id}/nodes | Create a new node from the submitted data.
[**create_template**](TextMagicApi.md#create_template) | **POST** /api/v2/templates | Create a new template from the submitted data.
[**delete_all_contacts**](TextMagicApi.md#delete_all_contacts) | **DELETE** /api/v2/contact/all | Delete all contacts.
[**delete_all_outbound_messages**](TextMagicApi.md#delete_all_outbound_messages) | **DELETE** /api/v2/message/all | Delete all messages
[**delete_avatar**](TextMagicApi.md#delete_avatar) | **DELETE** /api/v2/user/avatar | Delete an avatar for the current user.\\
[**delete_chat_messages**](TextMagicApi.md#delete_chat_messages) | **POST** /api/v2/chats/{id}/messages/delete | Delete messages from chat by given messages ID(s).
[**delete_chats_bulk**](TextMagicApi.md#delete_chats_bulk) | **POST** /api/v2/chats/delete | Delete chats by given ID(s) or delete all chats.
[**delete_contact**](TextMagicApi.md#delete_contact) | **DELETE** /api/v2/contacts/{id} | Delete a single contact.
[**delete_contact_avatar**](TextMagicApi.md#delete_contact_avatar) | **DELETE** /api/v2/contacts/{id}/avatar | Delete an avatar for the contact.
[**delete_contact_note**](TextMagicApi.md#delete_contact_note) | **DELETE** /api/v2/notes/{id} | Delete a single contact note.
[**delete_contact_notes_bulk**](TextMagicApi.md#delete_contact_notes_bulk) | **POST** /api/v2/contacts/{id}/notes/delete | Delete contact note by given ID(s) or delete all contact notes.
[**delete_contacts_by_ids**](TextMagicApi.md#delete_contacts_by_ids) | **POST** /api/v2/contacts/delete | Delete contact by given ID(s) or delete all contacts.
[**delete_contacts_from_list**](TextMagicApi.md#delete_contacts_from_list) | **DELETE** /api/v2/lists/{id}/contacts | Unassign contacts from the specified list.
[**delete_custom_field**](TextMagicApi.md#delete_custom_field) | **DELETE** /api/v2/customfields/{id} | Delete a single custom field.
[**delete_dedicated_number**](TextMagicApi.md#delete_dedicated_number) | **DELETE** /api/v2/numbers/{id} | Cancel dedicated number subscription.
[**delete_inbound_message**](TextMagicApi.md#delete_inbound_message) | **DELETE** /api/v2/replies/{id} | Delete the incoming message.
[**delete_inbound_messages_bulk**](TextMagicApi.md#delete_inbound_messages_bulk) | **POST** /api/v2/replies/delete | Delete inbound messages by given ID(s) or delete all inbound messages.
[**delete_list**](TextMagicApi.md#delete_list) | **DELETE** /api/v2/lists/{id} | Delete a single list.
[**delete_list_avatar**](TextMagicApi.md#delete_list_avatar) | **DELETE** /api/v2/lists/{id}/avatar | Delete an avatar for the list.
[**delete_list_contacts_bulk**](TextMagicApi.md#delete_list_contacts_bulk) | **POST** /api/v2/lists/{id}/contacts/delete | Delete contact from list by given ID(s) or all contacts from list.
[**delete_lists_bulk**](TextMagicApi.md#delete_lists_bulk) | **POST** /api/v2/lists/delete | Delete list by given ID(s) or delete all lists.
[**delete_message_session**](TextMagicApi.md#delete_message_session) | **DELETE** /api/v2/sessions/{id} | Delete a message session, together with all nested messages.
[**delete_message_sessions_bulk**](TextMagicApi.md#delete_message_sessions_bulk) | **POST** /api/v2/sessions/delete | Delete messages sessions, together with all nested messages, by given ID(s) or delete all messages sessions.
[**delete_outbound_message**](TextMagicApi.md#delete_outbound_message) | **DELETE** /api/v2/messages/{id} | Delete message
[**delete_outbound_messages_bulk**](TextMagicApi.md#delete_outbound_messages_bulk) | **POST** /api/v2/messages/delete | Delete messages by IDs
[**delete_push_token**](TextMagicApi.md#delete_push_token) | **DELETE** /api/v2/push/tokens/{type}/{deviceId} | Delete a push notification device token.
[**delete_scheduled_message**](TextMagicApi.md#delete_scheduled_message) | **DELETE** /api/v2/schedules/{id} | Delete a message session, together with all nested messages.
[**delete_scheduled_messages_bulk**](TextMagicApi.md#delete_scheduled_messages_bulk) | **POST** /api/v2/schedules/delete | Delete scheduled messages by given ID(s) or delete all scheduled messages.
[**delete_sender_id**](TextMagicApi.md#delete_sender_id) | **DELETE** /api/v2/senderids/{id} | Delete a Sender ID.
[**delete_survey**](TextMagicApi.md#delete_survey) | **DELETE** /api/v2/surveys/{id} | Delete a survey.
[**delete_survey_node**](TextMagicApi.md#delete_survey_node) | **DELETE** /api/v2/surveys/nodes/{id} | Delete a node.
[**delete_template**](TextMagicApi.md#delete_template) | **DELETE** /api/v2/templates/{id} | Delete a single template.
[**delete_templates_bulk**](TextMagicApi.md#delete_templates_bulk) | **POST** /api/v2/templates/delete | Delete template by given ID(s) or delete all templates.
[**do_auth**](TextMagicApi.md#do_auth) | **POST** /api/v2/auth | Authenticate user by given username and password.
[**do_carrier_lookup**](TextMagicApi.md#do_carrier_lookup) | **GET** /api/v2/lookups/{phone} | Carrier Lookup
[**do_email_lookup**](TextMagicApi.md#do_email_lookup) | **GET** /api/v2/email-lookups/{email} | Validate Email address using Email Lookup tool
[**duplicate_survey**](TextMagicApi.md#duplicate_survey) | **PUT** /api/v2/surveys/{id}/duplicate | Duplicate a survey.
[**get_all_bulk_sessions**](TextMagicApi.md#get_all_bulk_sessions) | **GET** /api/v2/bulks | Get all bulk sending sessions.
[**get_all_chats**](TextMagicApi.md#get_all_chats) | **GET** /api/v2/chats | Get all user chats.
[**get_all_inbound_messages**](TextMagicApi.md#get_all_inbound_messages) | **GET** /api/v2/replies | Get all inbox messages.
[**get_all_message_sessions**](TextMagicApi.md#get_all_message_sessions) | **GET** /api/v2/sessions | Get all message sending sessions.
[**get_all_outbound_messages**](TextMagicApi.md#get_all_outbound_messages) | **GET** /api/v2/messages | Get all messages
[**get_all_scheduled_messages**](TextMagicApi.md#get_all_scheduled_messages) | **GET** /api/v2/schedules | Get all scheduled messages.
[**get_all_templates**](TextMagicApi.md#get_all_templates) | **GET** /api/v2/templates | Get all user templates.
[**get_available_dedicated_numbers**](TextMagicApi.md#get_available_dedicated_numbers) | **GET** /api/v2/numbers/available | Find available dedicated numbers to buy.
[**get_available_sender_setting_options**](TextMagicApi.md#get_available_sender_setting_options) | **GET** /api/v2/sources | Get all available sender setting options which could be used in \&quot;from\&quot; parameter of POST messages method.
[**get_balance_notification_options**](TextMagicApi.md#get_balance_notification_options) | **GET** /api/v2/user/notification/balance/bundles | Returns the list of available balance options which can be used as a bound to determine when to send email to user with low balance notification. See https://my.textmagic.com/online/account/notifications/balance
[**get_balance_notification_settings**](TextMagicApi.md#get_balance_notification_settings) | **GET** /api/v2/user/notification/balance | Get balance notification settings
[**get_blocked_contacts**](TextMagicApi.md#get_blocked_contacts) | **GET** /api/v2/contacts/block/list | Get blocked contacts.
[**get_bulk_session**](TextMagicApi.md#get_bulk_session) | **GET** /api/v2/bulks/{id} | Get bulk message session status.
[**get_callback_settings**](TextMagicApi.md#get_callback_settings) | **GET** /api/v2/callback/settings | Fetch callback URL settings
[**get_calls_prices**](TextMagicApi.md#get_calls_prices) | **GET** /api/v2/calls/price | Check pricing for a inbound/outbound call.
[**get_chat**](TextMagicApi.md#get_chat) | **GET** /api/v2/chats/{id} | Get a single chat.
[**get_chat_by_phone**](TextMagicApi.md#get_chat_by_phone) | **GET** /api/v2/chats/{phone}/by/phone | Find chats by phone.
[**get_chat_messages**](TextMagicApi.md#get_chat_messages) | **GET** /api/v2/chats/{id}/message | Fetch messages from chat with specified chat id.
[**get_contact**](TextMagicApi.md#get_contact) | **GET** /api/v2/contacts/{id} | Get a single contact.
[**get_contact_by_phone**](TextMagicApi.md#get_contact_by_phone) | **GET** /api/v2/contacts/phone/{phone} | Get a single contact by phone number.
[**get_contact_if_blocked**](TextMagicApi.md#get_contact_if_blocked) | **GET** /api/v2/contacts/block/phone | Check is that phone number blocked
[**get_contact_import_session_progress**](TextMagicApi.md#get_contact_import_session_progress) | **GET** /api/v2/contacts/import/progress/{id} | Get contact import session progress.
[**get_contact_note**](TextMagicApi.md#get_contact_note) | **GET** /api/v2/notes/{id} | Get a single contact note.
[**get_contact_notes**](TextMagicApi.md#get_contact_notes) | **GET** /api/v2/contacts/{id}/notes | Fetch notes assigned to the given contact.
[**get_contacts**](TextMagicApi.md#get_contacts) | **GET** /api/v2/contacts | Get all user contacts.
[**get_contacts_autocomplete**](TextMagicApi.md#get_contacts_autocomplete) | **GET** /api/v2/contacts/autocomplete | Get contacts autocomplete suggestions by given search term.
[**get_contacts_by_list_id**](TextMagicApi.md#get_contacts_by_list_id) | **GET** /api/v2/lists/{id}/contacts | Fetch user contacts by given group id.
[**get_countries**](TextMagicApi.md#get_countries) | **GET** /api/v2/countries | Return list of countries.
[**get_current_user**](TextMagicApi.md#get_current_user) | **GET** /api/v2/user | Get current user info.
[**get_custom_field**](TextMagicApi.md#get_custom_field) | **GET** /api/v2/customfields/{id} | Get a single custom field.
[**get_custom_fields**](TextMagicApi.md#get_custom_fields) | **GET** /api/v2/customfields | Get all contact custom fields.
[**get_dedicated_number**](TextMagicApi.md#get_dedicated_number) | **GET** /api/v2/numbers/{id} | Get a single dedicated number.
[**get_disallowed_rules**](TextMagicApi.md#get_disallowed_rules) | **GET** /api/v2/user/disallowed-rules | Get an array of all rules that are disallowed to the current account.
[**get_favourites**](TextMagicApi.md#get_favourites) | **GET** /api/v2/contacts/favorite | Get favorite contacts and lists.
[**get_forwarded_calls**](TextMagicApi.md#get_forwarded_calls) | **GET** /api/v2/calls | Get all forwarded calls.
[**get_inbound_message**](TextMagicApi.md#get_inbound_message) | **GET** /api/v2/replies/{id} | Get a single inbox message.
[**get_inbound_messages_notification_settings**](TextMagicApi.md#get_inbound_messages_notification_settings) | **GET** /api/v2/user/notification/inbound | Get inbound messages notification settings
[**get_invoices**](TextMagicApi.md#get_invoices) | **GET** /api/v2/invoices | Return account invoices.
[**get_list**](TextMagicApi.md#get_list) | **GET** /api/v2/lists/{id} | Get a single list.
[**get_list_contacts_ids**](TextMagicApi.md#get_list_contacts_ids) | **GET** /api/v2/lists/{id}/contacts/ids | Fetch all contacts IDs belonging to the list with ID.
[**get_lists_of_contact**](TextMagicApi.md#get_lists_of_contact) | **GET** /api/v2/contacts/{id}/lists | Return lists which contact belongs to.
[**get_message_preview**](TextMagicApi.md#get_message_preview) | **GET** /api/v2/messages/preview | Preview message
[**get_message_price**](TextMagicApi.md#get_message_price) | **GET** /api/v2/messages/price | Check price
[**get_message_prices**](TextMagicApi.md#get_message_prices) | **GET** /api/v2/messages/prices | Get pricing
[**get_message_session**](TextMagicApi.md#get_message_session) | **GET** /api/v2/sessions/{id} | Get a message session.
[**get_message_session_stat**](TextMagicApi.md#get_message_session_stat) | **GET** /api/v2/sessions/{id}/stat | Get sending session statistics.
[**get_messages_by_session_id**](TextMagicApi.md#get_messages_by_session_id) | **GET** /api/v2/sessions/{id}/messages | Fetch messages by given session id.
[**get_messaging_counters**](TextMagicApi.md#get_messaging_counters) | **GET** /api/v2/stats/messaging/data | Return counters for messaging data views.
[**get_messaging_stat**](TextMagicApi.md#get_messaging_stat) | **GET** /api/v2/stats/messaging | Return messaging statistics.
[**get_outbound_message**](TextMagicApi.md#get_outbound_message) | **GET** /api/v2/messages/{id} | Get a single message
[**get_outbound_messages_history**](TextMagicApi.md#get_outbound_messages_history) | **GET** /api/v2/history | Get history
[**get_push_tokens**](TextMagicApi.md#get_push_tokens) | **GET** /api/v2/push/tokens | Get all device tokens assigned to the current account
[**get_scheduled_message**](TextMagicApi.md#get_scheduled_message) | **GET** /api/v2/schedules/{id} | Get message schedule.
[**get_sender_id**](TextMagicApi.md#get_sender_id) | **GET** /api/v2/senderids/{id} | Get a single Sender ID.
[**get_sender_ids**](TextMagicApi.md#get_sender_ids) | **GET** /api/v2/senderids | Get all sender IDs of current user.
[**get_sender_settings**](TextMagicApi.md#get_sender_settings) | **GET** /api/v2/sender/settings | Get current user sender settings.
[**get_spending_stat**](TextMagicApi.md#get_spending_stat) | **GET** /api/v2/stats/spending | Return account spending statistics.
[**get_state**](TextMagicApi.md#get_state) | **GET** /api/v2/state | Get current entities state
[**get_subaccount**](TextMagicApi.md#get_subaccount) | **GET** /api/v2/subaccounts/{id} | Get a single subaccount.
[**get_subaccounts**](TextMagicApi.md#get_subaccounts) | **GET** /api/v2/subaccounts | Get all subaccounts of current user.
[**get_subaccounts_with_tokens**](TextMagicApi.md#get_subaccounts_with_tokens) | **POST** /api/v2/subaccounts/tokens/list | Get all subaccounts with their REST API tokens associated with specified app name.
[**get_survey**](TextMagicApi.md#get_survey) | **GET** /api/v2/surveys/{id} | Get a survey by id.
[**get_survey_node**](TextMagicApi.md#get_survey_node) | **GET** /api/v2/surveys/nodes/{id} | Get a node by id.
[**get_survey_nodes**](TextMagicApi.md#get_survey_nodes) | **GET** /api/v2/surveys/{id}/nodes | Fetch nodes by given survey id.
[**get_surveys**](TextMagicApi.md#get_surveys) | **GET** /api/v2/surveys | Get all user surveys.
[**get_template**](TextMagicApi.md#get_template) | **GET** /api/v2/templates/{id} | Get a single template.
[**get_timezones**](TextMagicApi.md#get_timezones) | **GET** /api/v2/timezones | Return all available timezone IDs.
[**get_unread_messages_total**](TextMagicApi.md#get_unread_messages_total) | **GET** /api/v2/chats/unread/count | Get total amount of unread messages in the current user chats.
[**get_unsubscribed_contact**](TextMagicApi.md#get_unsubscribed_contact) | **GET** /api/v2/unsubscribers/{id} | Get a single unsubscribed contact.
[**get_unsubscribers**](TextMagicApi.md#get_unsubscribers) | **GET** /api/v2/unsubscribers | Get all contact have unsubscribed from your communication.
[**get_user_dedicated_numbers**](TextMagicApi.md#get_user_dedicated_numbers) | **GET** /api/v2/numbers | Get user&#39;s dedicated numbers.
[**get_user_lists**](TextMagicApi.md#get_user_lists) | **GET** /api/v2/lists | Get all user lists.
[**get_versions**](TextMagicApi.md#get_versions) | **GET** /api/v2/versions | Get minimal valid apps versions
[**invite_subaccount**](TextMagicApi.md#invite_subaccount) | **POST** /api/v2/subaccounts | Invite new subaccount.
[**mark_chats_read_bulk**](TextMagicApi.md#mark_chats_read_bulk) | **POST** /api/v2/chats/read/bulk | Mark several chats as read by chat ids or mark all chats as read
[**mark_chats_unread_bulk**](TextMagicApi.md#mark_chats_unread_bulk) | **POST** /api/v2/chats/unread/bulk | Mark several chats as UNread by chat ids or mark all chats as UNread
[**merge_survey_nodes**](TextMagicApi.md#merge_survey_nodes) | **POST** /api/v2/surveys/nodes/merge | Merge two question nodes.
[**mute_chat**](TextMagicApi.md#mute_chat) | **POST** /api/v2/chats/mute | Set mute mode.
[**mute_chats_bulk**](TextMagicApi.md#mute_chats_bulk) | **POST** /api/v2/chats/mute/bulk | Mute several chats by chat ids or mute all chats
[**ping**](TextMagicApi.md#ping) | **GET** /api/v2/ping | Just does a pong.
[**reopen_chats_bulk**](TextMagicApi.md#reopen_chats_bulk) | **POST** /api/v2/chats/reopen/bulk | Reopen chats by chat ids or reopen all chats
[**request_new_subaccount_token**](TextMagicApi.md#request_new_subaccount_token) | **POST** /api/v2/subaccounts/tokens | Request a new REST API token for subaccount.
[**request_sender_id**](TextMagicApi.md#request_sender_id) | **POST** /api/v2/senderids | Request for a new Sender ID.
[**reset_survey**](TextMagicApi.md#reset_survey) | **PUT** /api/v2/surveys/{id}/reset | Reset a survey flow.
[**search_chats**](TextMagicApi.md#search_chats) | **GET** /api/v2/chats/search | Find chats by inbound or outbound messages text.
[**search_chats_by_ids**](TextMagicApi.md#search_chats_by_ids) | **GET** /api/v2/chats/search/ids | Find chats by IDs.
[**search_chats_by_receipent**](TextMagicApi.md#search_chats_by_receipent) | **GET** /api/v2/chats/search/recipients | Find chats by recipient (contact, list name or phone number).
[**search_contacts**](TextMagicApi.md#search_contacts) | **GET** /api/v2/contacts/search | Find user contacts by given parameters.
[**search_inbound_messages**](TextMagicApi.md#search_inbound_messages) | **GET** /api/v2/replies/search | Find inbound messages by given parameters.
[**search_lists**](TextMagicApi.md#search_lists) | **GET** /api/v2/lists/search | Find contact lists by given parameters.
[**search_outbound_messages**](TextMagicApi.md#search_outbound_messages) | **GET** /api/v2/messages/search | Find messages
[**search_scheduled_messages**](TextMagicApi.md#search_scheduled_messages) | **GET** /api/v2/schedules/search | Find scheduled messages by given parameters.
[**search_templates**](TextMagicApi.md#search_templates) | **GET** /api/v2/templates/search | Find user templates by given parameters.
[**send_email_verification_code**](TextMagicApi.md#send_email_verification_code) | **GET** /api/v2/user/email/verification | Send user email verification
[**send_message**](TextMagicApi.md#send_message) | **POST** /api/v2/messages | Send message
[**send_phone_verification_code**](TextMagicApi.md#send_phone_verification_code) | **GET** /api/v2/user/phone/verification | Send user phone verification
[**set_chat_status**](TextMagicApi.md#set_chat_status) | **POST** /api/v2/chats/status | Set status of the chat given by ID.
[**start_survey**](TextMagicApi.md#start_survey) | **PUT** /api/v2/surveys/{id}/start | Start a survey.
[**unblock_contact**](TextMagicApi.md#unblock_contact) | **POST** /api/v2/contacts/unblock | Unblock contact by phone number.
[**unblock_contacts_bulk**](TextMagicApi.md#unblock_contacts_bulk) | **POST** /api/v2/contacts/unblock/bulk | Unblock several contacts by blocked contact ids or unblock all contacts
[**unmute_chats_bulk**](TextMagicApi.md#unmute_chats_bulk) | **POST** /api/v2/chats/unmute/bulk | Unmute several chats by chat ids or unmute all chats
[**unsubscribe_contact**](TextMagicApi.md#unsubscribe_contact) | **POST** /api/v2/unsubscribers | Unsubscribe contact from your communication by phone number.
[**update_balance_notification_settings**](TextMagicApi.md#update_balance_notification_settings) | **PUT** /api/v2/user/notification/balance | Update balance notification settings
[**update_callback_settings**](TextMagicApi.md#update_callback_settings) | **PUT** /api/v2/callback/settings | Update callback URL settings
[**update_chat_desktop_notification_settings**](TextMagicApi.md#update_chat_desktop_notification_settings) | **PUT** /api/v2/user/desktop/notification | Update chat desktop notification settings
[**update_contact**](TextMagicApi.md#update_contact) | **PUT** /api/v2/contacts/{id} | Update existing contact.
[**update_contact_note**](TextMagicApi.md#update_contact_note) | **PUT** /api/v2/notes/{id} | Update existing contact note.
[**update_current_user**](TextMagicApi.md#update_current_user) | **PUT** /api/v2/user | Update current user info.
[**update_custom_field**](TextMagicApi.md#update_custom_field) | **PUT** /api/v2/customfields/{id} | Update existing custom field.
[**update_custom_field_value**](TextMagicApi.md#update_custom_field_value) | **PUT** /api/v2/customfields/{id}/update | Update contact&#39;s custom field value.
[**update_inbound_messages_notification_settings**](TextMagicApi.md#update_inbound_messages_notification_settings) | **PUT** /api/v2/user/notification/inbound | Update inbound messages notification settings
[**update_list**](TextMagicApi.md#update_list) | **PUT** /api/v2/lists/{id} | Update existing list.
[**update_password**](TextMagicApi.md#update_password) | **PUT** /api/v2/user/password/change | Change user password.
[**update_sender_setting**](TextMagicApi.md#update_sender_setting) | **PUT** /api/v2/sender/settings | Change sender settings for specified country.
[**update_survey**](TextMagicApi.md#update_survey) | **PUT** /api/v2/surveys/{id} | Update existing survey.
[**update_survey_node**](TextMagicApi.md#update_survey_node) | **PUT** /api/v2/surveys/nodes/{id} | Update existing node.
[**update_template**](TextMagicApi.md#update_template) | **PUT** /api/v2/templates/{id} | Update existing template.
[**upload_avatar**](TextMagicApi.md#upload_avatar) | **POST** /api/v2/user/avatar | Add an avatar for the current user.
[**upload_contact_avatar**](TextMagicApi.md#upload_contact_avatar) | **POST** /api/v2/contacts/{id}/avatar | Add an avatar for the contact.
[**upload_list_avatar**](TextMagicApi.md#upload_list_avatar) | **POST** /api/v2/lists/{id}/avatar | Add an avatar for the list.
[**upload_message_attachment**](TextMagicApi.md#upload_message_attachment) | **POST** /api/v2/messages/attachment | Upload message attachment


# **assign_contacts_to_list**
> ResourceLinkResponse assign_contacts_to_list(assign_contacts_to_list_input_object, id)

Assign contacts to the specified list.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
assign_contacts_to_list_input_object = TextMagic.AssignContactsToListInputObject() # AssignContactsToListInputObject | Contact ID(s), separated by comma or 'all' to add all contacts belonging to the current user
id = 1 # int | 

try:
    # Assign contacts to the specified list.
    api_response = api_instance.assign_contacts_to_list(assign_contacts_to_list_input_object, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->assign_contacts_to_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assign_contacts_to_list_input_object** | [**AssignContactsToListInputObject**](AssignContactsToListInputObject.md)| Contact ID(s), separated by comma or &#39;all&#39; to add all contacts belonging to the current user | 
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **block_contact**
> ResourceLinkResponse block_contact(block_contact_input_object, x_ignore_null_values=x_ignore_null_values)

Block contact from inbound and outbound communication by phone number.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
block_contact_input_object = TextMagic.BlockContactInputObject() # BlockContactInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Block contact from inbound and outbound communication by phone number.
    api_response = api_instance.block_contact(block_contact_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->block_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_contact_input_object** | [**BlockContactInputObject**](BlockContactInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buy_dedicated_number**
> buy_dedicated_number(buy_dedicated_number_input_object, x_ignore_null_values=x_ignore_null_values)

Buy a dedicated number and assign it to the specified account.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
buy_dedicated_number_input_object = TextMagic.BuyDedicatedNumberInputObject() # BuyDedicatedNumberInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Buy a dedicated number and assign it to the specified account.
    api_instance.buy_dedicated_number(buy_dedicated_number_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->buy_dedicated_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buy_dedicated_number_input_object** | [**BuyDedicatedNumberInputObject**](BuyDedicatedNumberInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_survey**
> ResourceLinkResponse cancel_survey(id)

Cancel a survey.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Cancel a survey.
    api_response = api_instance.cancel_survey(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->cancel_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_phone_verification_code**
> check_phone_verification_code(check_phone_verification_code_input_object, x_ignore_null_values=x_ignore_null_values)

Check user phone verification code

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
check_phone_verification_code_input_object = TextMagic.CheckPhoneVerificationCodeInputObject() # CheckPhoneVerificationCodeInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Check user phone verification code
    api_instance.check_phone_verification_code(check_phone_verification_code_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->check_phone_verification_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_phone_verification_code_input_object** | [**CheckPhoneVerificationCodeInputObject**](CheckPhoneVerificationCodeInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_and_assign_contacts_to_list**
> ResourceLinkResponse clear_and_assign_contacts_to_list(clear_and_assign_contacts_to_list_input_object, id)

Reset list members to the specified contacts.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
clear_and_assign_contacts_to_list_input_object = TextMagic.ClearAndAssignContactsToListInputObject() # ClearAndAssignContactsToListInputObject | Contact ID(s), separated by comma or 'all' to add all contacts belonging to the current user
id = 1 # int | 

try:
    # Reset list members to the specified contacts.
    api_response = api_instance.clear_and_assign_contacts_to_list(clear_and_assign_contacts_to_list_input_object, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->clear_and_assign_contacts_to_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clear_and_assign_contacts_to_list_input_object** | [**ClearAndAssignContactsToListInputObject**](ClearAndAssignContactsToListInputObject.md)| Contact ID(s), separated by comma or &#39;all&#39; to add all contacts belonging to the current user | 
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_chats_bulk**
> close_chats_bulk(close_chats_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Close chats by chat ids or close all chats

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
close_chats_bulk_input_object = TextMagic.CloseChatsBulkInputObject() # CloseChatsBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Close chats by chat ids or close all chats
    api_instance.close_chats_bulk(close_chats_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->close_chats_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **close_chats_bulk_input_object** | [**CloseChatsBulkInputObject**](CloseChatsBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_read_chats**
> close_read_chats()

Close all chats that have no unread messages.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Close all chats that have no unread messages.
    api_instance.close_read_chats()
except ApiException as e:
    print("Exception when calling TextMagicApi->close_read_chats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_subaccount**
> close_subaccount(id)

Close subaccount.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Close subaccount.
    api_instance.close_subaccount(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->close_subaccount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact**
> ResourceLinkResponse create_contact(create_contact_input_object, x_ignore_null_values=x_ignore_null_values)

Create a new contact from the submitted data.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
create_contact_input_object = TextMagic.CreateContactInputObject() # CreateContactInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Create a new contact from the submitted data.
    api_response = api_instance.create_contact(create_contact_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->create_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_contact_input_object** | [**CreateContactInputObject**](CreateContactInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact_note**
> ResourceLinkResponse create_contact_note(create_contact_note_input_object, id, x_ignore_null_values=x_ignore_null_values)

Create a new contact note.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
create_contact_note_input_object = TextMagic.CreateContactNoteInputObject() # CreateContactNoteInputObject | 
id = 56 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Create a new contact note.
    api_response = api_instance.create_contact_note(create_contact_note_input_object, id, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->create_contact_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_contact_note_input_object** | [**CreateContactNoteInputObject**](CreateContactNoteInputObject.md)|  | 
 **id** | **int**|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_field**
> ResourceLinkResponse create_custom_field(create_custom_field_input_object, x_ignore_null_values=x_ignore_null_values)

Create a new custom field from the submitted data.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
create_custom_field_input_object = TextMagic.CreateCustomFieldInputObject() # CreateCustomFieldInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Create a new custom field from the submitted data.
    api_response = api_instance.create_custom_field(create_custom_field_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->create_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_custom_field_input_object** | [**CreateCustomFieldInputObject**](CreateCustomFieldInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_list**
> ResourceLinkResponse create_list(create_list_input_object, x_ignore_null_values=x_ignore_null_values)

Create a new list from the submitted data.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
create_list_input_object = TextMagic.CreateListInputObject() # CreateListInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Create a new list from the submitted data.
    api_response = api_instance.create_list(create_list_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->create_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_list_input_object** | [**CreateListInputObject**](CreateListInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_push_token**
> create_push_token(create_push_token_input_object, x_ignore_null_values=x_ignore_null_values)

Add or update a device token.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
create_push_token_input_object = TextMagic.CreatePushTokenInputObject() # CreatePushTokenInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Add or update a device token.
    api_instance.create_push_token(create_push_token_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->create_push_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_push_token_input_object** | [**CreatePushTokenInputObject**](CreatePushTokenInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_survey**
> ResourceLinkResponse create_survey(create_survey_input_object, x_ignore_null_values=x_ignore_null_values)

Create a new survey from the submitted data.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
create_survey_input_object = TextMagic.CreateSurveyInputObject() # CreateSurveyInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Create a new survey from the submitted data.
    api_response = api_instance.create_survey(create_survey_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->create_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_survey_input_object** | [**CreateSurveyInputObject**](CreateSurveyInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_survey_node**
> ResourceLinkResponse create_survey_node(create_survey_node_input_object, id, x_ignore_null_values=x_ignore_null_values)

Create a new node from the submitted data.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
create_survey_node_input_object = TextMagic.CreateSurveyNodeInputObject() # CreateSurveyNodeInputObject | 
id = 1 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Create a new node from the submitted data.
    api_response = api_instance.create_survey_node(create_survey_node_input_object, id, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->create_survey_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_survey_node_input_object** | [**CreateSurveyNodeInputObject**](CreateSurveyNodeInputObject.md)|  | 
 **id** | **int**|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template**
> ResourceLinkResponse create_template(create_template_input_object, x_ignore_null_values=x_ignore_null_values)

Create a new template from the submitted data.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
create_template_input_object = TextMagic.CreateTemplateInputObject() # CreateTemplateInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Create a new template from the submitted data.
    api_response = api_instance.create_template(create_template_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->create_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_template_input_object** | [**CreateTemplateInputObject**](CreateTemplateInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_contacts**
> delete_all_contacts()

Delete all contacts.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Delete all contacts.
    api_instance.delete_all_contacts()
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_all_contacts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_outbound_messages**
> delete_all_outbound_messages()

Delete all messages

Delete all messages.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Delete all messages
    api_instance.delete_all_outbound_messages()
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_all_outbound_messages: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_avatar**
> delete_avatar()

Delete an avatar for the current user.\\

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Delete an avatar for the current user.\\
    api_instance.delete_avatar()
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_avatar: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chat_messages**
> delete_chat_messages(delete_chat_messages_bulk_input_object, id, x_ignore_null_values=x_ignore_null_values)

Delete messages from chat by given messages ID(s).

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_chat_messages_bulk_input_object = TextMagic.DeleteChatMessagesBulkInputObject() # DeleteChatMessagesBulkInputObject | 
id = 1 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete messages from chat by given messages ID(s).
    api_instance.delete_chat_messages(delete_chat_messages_bulk_input_object, id, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_chat_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_chat_messages_bulk_input_object** | [**DeleteChatMessagesBulkInputObject**](DeleteChatMessagesBulkInputObject.md)|  | 
 **id** | **int**|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chats_bulk**
> delete_chats_bulk(delete_chats_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Delete chats by given ID(s) or delete all chats.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_chats_bulk_input_object = TextMagic.DeleteChatsBulkInputObject() # DeleteChatsBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete chats by given ID(s) or delete all chats.
    api_instance.delete_chats_bulk(delete_chats_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_chats_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_chats_bulk_input_object** | [**DeleteChatsBulkInputObject**](DeleteChatsBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> delete_contact(id)

Delete a single contact.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a single contact.
    api_instance.delete_contact(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_avatar**
> delete_contact_avatar(id)

Delete an avatar for the contact.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete an avatar for the contact.
    api_instance.delete_contact_avatar(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_contact_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_note**
> delete_contact_note(id)

Delete a single contact note.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a single contact note.
    api_instance.delete_contact_note(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_contact_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_notes_bulk**
> delete_contact_notes_bulk(id, delete_contact_notes_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Delete contact note by given ID(s) or delete all contact notes.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
delete_contact_notes_bulk_input_object = TextMagic.DeleteContactNotesBulkInputObject() # DeleteContactNotesBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete contact note by given ID(s) or delete all contact notes.
    api_instance.delete_contact_notes_bulk(id, delete_contact_notes_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_contact_notes_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **delete_contact_notes_bulk_input_object** | [**DeleteContactNotesBulkInputObject**](DeleteContactNotesBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contacts_by_ids**
> delete_contacts_by_ids(delete_contacts_by_ids_input_object, x_ignore_null_values=x_ignore_null_values)

Delete contact by given ID(s) or delete all contacts.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_contacts_by_ids_input_object = TextMagic.DeleteContactsByIdsInputObject() # DeleteContactsByIdsInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete contact by given ID(s) or delete all contacts.
    api_instance.delete_contacts_by_ids(delete_contacts_by_ids_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_contacts_by_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_contacts_by_ids_input_object** | [**DeleteContactsByIdsInputObject**](DeleteContactsByIdsInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contacts_from_list**
> delete_contacts_from_list(delete_contacs_from_list_object, id)

Unassign contacts from the specified list.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_contacs_from_list_object = TextMagic.DeleteContacsFromListObject() # DeleteContacsFromListObject | Contact ID(s), separated by comma
id = 1 # int | 

try:
    # Unassign contacts from the specified list.
    api_instance.delete_contacts_from_list(delete_contacs_from_list_object, id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_contacts_from_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_contacs_from_list_object** | [**DeleteContacsFromListObject**](DeleteContacsFromListObject.md)| Contact ID(s), separated by comma | 
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_field**
> delete_custom_field(id)

Delete a single custom field.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a single custom field.
    api_instance.delete_custom_field(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dedicated_number**
> delete_dedicated_number(id)

Cancel dedicated number subscription.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Cancel dedicated number subscription.
    api_instance.delete_dedicated_number(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_dedicated_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inbound_message**
> delete_inbound_message(id)

Delete the incoming message.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete the incoming message.
    api_instance.delete_inbound_message(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_inbound_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inbound_messages_bulk**
> delete_inbound_messages_bulk(delete_inbound_messages_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Delete inbound messages by given ID(s) or delete all inbound messages.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_inbound_messages_bulk_input_object = TextMagic.DeleteInboundMessagesBulkInputObject() # DeleteInboundMessagesBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete inbound messages by given ID(s) or delete all inbound messages.
    api_instance.delete_inbound_messages_bulk(delete_inbound_messages_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_inbound_messages_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_inbound_messages_bulk_input_object** | [**DeleteInboundMessagesBulkInputObject**](DeleteInboundMessagesBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list**
> delete_list(id)

Delete a single list.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a single list.
    api_instance.delete_list(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list_avatar**
> delete_list_avatar(id)

Delete an avatar for the list.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete an avatar for the list.
    api_instance.delete_list_avatar(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_list_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list_contacts_bulk**
> delete_list_contacts_bulk(delete_list_contacts_bulk_input_object, id, x_ignore_null_values=x_ignore_null_values)

Delete contact from list by given ID(s) or all contacts from list.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_list_contacts_bulk_input_object = TextMagic.DeleteListContactsBulkInputObject() # DeleteListContactsBulkInputObject | 
id = 1 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete contact from list by given ID(s) or all contacts from list.
    api_instance.delete_list_contacts_bulk(delete_list_contacts_bulk_input_object, id, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_list_contacts_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_list_contacts_bulk_input_object** | [**DeleteListContactsBulkInputObject**](DeleteListContactsBulkInputObject.md)|  | 
 **id** | **int**|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lists_bulk**
> delete_lists_bulk(delete_lists_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Delete list by given ID(s) or delete all lists.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_lists_bulk_input_object = TextMagic.DeleteListsBulkInputObject() # DeleteListsBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete list by given ID(s) or delete all lists.
    api_instance.delete_lists_bulk(delete_lists_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_lists_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_lists_bulk_input_object** | [**DeleteListsBulkInputObject**](DeleteListsBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_message_session**
> delete_message_session(id)

Delete a message session, together with all nested messages.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a message session, together with all nested messages.
    api_instance.delete_message_session(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_message_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_message_sessions_bulk**
> delete_message_sessions_bulk(delete_message_sessions_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Delete messages sessions, together with all nested messages, by given ID(s) or delete all messages sessions.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_message_sessions_bulk_input_object = TextMagic.DeleteMessageSessionsBulkInputObject() # DeleteMessageSessionsBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete messages sessions, together with all nested messages, by given ID(s) or delete all messages sessions.
    api_instance.delete_message_sessions_bulk(delete_message_sessions_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_message_sessions_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_message_sessions_bulk_input_object** | [**DeleteMessageSessionsBulkInputObject**](DeleteMessageSessionsBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_outbound_message**
> delete_outbound_message(id)

Delete message

Delete a single message.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete message
    api_instance.delete_outbound_message(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_outbound_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_outbound_messages_bulk**
> delete_outbound_messages_bulk(delete_outbound_messages_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Delete messages by IDs

Delete outbound messages by given ID(s) or delete all outbound messages.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_outbound_messages_bulk_input_object = TextMagic.DeleteOutboundMessagesBulkInputObject() # DeleteOutboundMessagesBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete messages by IDs
    api_instance.delete_outbound_messages_bulk(delete_outbound_messages_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_outbound_messages_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_outbound_messages_bulk_input_object** | [**DeleteOutboundMessagesBulkInputObject**](DeleteOutboundMessagesBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_push_token**
> delete_push_token(type, device_id)

Delete a push notification device token.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
type = 'type_example' # str | 
device_id = 56 # int | 

try:
    # Delete a push notification device token.
    api_instance.delete_push_token(type, device_id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_push_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **device_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduled_message**
> delete_scheduled_message(id)

Delete a message session, together with all nested messages.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a message session, together with all nested messages.
    api_instance.delete_scheduled_message(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_scheduled_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduled_messages_bulk**
> delete_scheduled_messages_bulk(delete_scheduled_messages_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Delete scheduled messages by given ID(s) or delete all scheduled messages.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_scheduled_messages_bulk_input_object = TextMagic.DeleteScheduledMessagesBulkInputObject() # DeleteScheduledMessagesBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete scheduled messages by given ID(s) or delete all scheduled messages.
    api_instance.delete_scheduled_messages_bulk(delete_scheduled_messages_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_scheduled_messages_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_scheduled_messages_bulk_input_object** | [**DeleteScheduledMessagesBulkInputObject**](DeleteScheduledMessagesBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sender_id**
> delete_sender_id(id)

Delete a Sender ID.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a Sender ID.
    api_instance.delete_sender_id(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_sender_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_survey**
> delete_survey(id)

Delete a survey.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a survey.
    api_instance.delete_survey(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_survey_node**
> delete_survey_node(id)

Delete a node.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a node.
    api_instance.delete_survey_node(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_survey_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> delete_template(id)

Delete a single template.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a single template.
    api_instance.delete_template(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_templates_bulk**
> delete_templates_bulk(delete_templates_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Delete template by given ID(s) or delete all templates.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_templates_bulk_input_object = TextMagic.DeleteTemplatesBulkInputObject() # DeleteTemplatesBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete template by given ID(s) or delete all templates.
    api_instance.delete_templates_bulk(delete_templates_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_templates_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_templates_bulk_input_object** | [**DeleteTemplatesBulkInputObject**](DeleteTemplatesBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_auth**
> DoAuthResponse do_auth(do_auth_input_object, x_ignore_null_values=x_ignore_null_values)

Authenticate user by given username and password.

Returning a username and token that you should pass to the all requests (in X-TM-Username and X-TM-Key, respectively)

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TextMagic.TextMagicApi()
do_auth_input_object = TextMagic.DoAuthInputObject() # DoAuthInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Authenticate user by given username and password.
    api_response = api_instance.do_auth(do_auth_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->do_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **do_auth_input_object** | [**DoAuthInputObject**](DoAuthInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**DoAuthResponse**](DoAuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_carrier_lookup**
> DoCarrierLookupResponse do_carrier_lookup(phone, country=country)

Carrier Lookup

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
phone = '\"1-541-754-3010\"' # str | 
country = 'US' # str | Country code for local formatted numbers (optional) (default to US)

try:
    # Carrier Lookup
    api_response = api_instance.do_carrier_lookup(phone, country=country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->do_carrier_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**|  | 
 **country** | **str**| Country code for local formatted numbers | [optional] [default to US]

### Return type

[**DoCarrierLookupResponse**](DoCarrierLookupResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_email_lookup**
> DoEmailLookupResponse do_email_lookup(email)

Validate Email address using Email Lookup tool

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
email = '\"andrey.v@textmagic.biz\"' # str | 

try:
    # Validate Email address using Email Lookup tool
    api_response = api_instance.do_email_lookup(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->do_email_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**DoEmailLookupResponse**](DoEmailLookupResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_survey**
> ResourceLinkResponse duplicate_survey(id)

Duplicate a survey.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Duplicate a survey.
    api_response = api_instance.duplicate_survey(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->duplicate_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_bulk_sessions**
> GetAllBulkSessionsResponse get_all_bulk_sessions(page=page, limit=limit)

Get all bulk sending sessions.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Get all bulk sending sessions.
    api_response = api_instance.get_all_bulk_sessions(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_all_bulk_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]

### Return type

[**GetAllBulkSessionsResponse**](GetAllBulkSessionsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_chats**
> GetAllChatsResponse get_all_chats(status=status, page=page, limit=limit, order_by=order_by, voice=voice, flat=flat)

Get all user chats.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
status = 'status_example' # str | Fetch only (a)ctive, (c)losed or (d)eleted chats (optional)
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
voice = 0 # int | Fetch results with voice calls (optional) (default to 0)
flat = 0 # int | Should additional contact info be included (optional) (default to 0)

try:
    # Get all user chats.
    api_response = api_instance.get_all_chats(status=status, page=page, limit=limit, order_by=order_by, voice=voice, flat=flat)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_all_chats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Fetch only (a)ctive, (c)losed or (d)eleted chats | [optional] 
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **order_by** | **str**| Order results by some field. Default is id | [optional] [default to id]
 **voice** | **int**| Fetch results with voice calls | [optional] [default to 0]
 **flat** | **int**| Should additional contact info be included | [optional] [default to 0]

### Return type

[**GetAllChatsResponse**](GetAllChatsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_inbound_messages**
> GetAllInboundMessagesResponse get_all_inbound_messages(page=page, limit=limit, order_by=order_by, direction=direction)

Get all inbox messages.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)

try:
    # Get all inbox messages.
    api_response = api_instance.get_all_inbound_messages(page=page, limit=limit, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_all_inbound_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **order_by** | **str**| Order results by some field. Default is id | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc | [optional] [default to desc]

### Return type

[**GetAllInboundMessagesResponse**](GetAllInboundMessagesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_message_sessions**
> GetAllMessageSessionsResponse get_all_message_sessions(page=page, limit=limit)

Get all message sending sessions.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Get all message sending sessions.
    api_response = api_instance.get_all_message_sessions(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_all_message_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]

### Return type

[**GetAllMessageSessionsResponse**](GetAllMessageSessionsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_outbound_messages**
> GetAllOutboundMessagesResponse get_all_outbound_messages(page=page, limit=limit, last_id=last_id)

Get all messages

Get all user oubound messages.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
last_id = 56 # int | Filter results by ID, selecting all values lesser than the specified ID. Note that \\'page\\' parameter is ignored when \\'lastId\\' is specified (optional)

try:
    # Get all messages
    api_response = api_instance.get_all_outbound_messages(page=page, limit=limit, last_id=last_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_all_outbound_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **last_id** | **int**| Filter results by ID, selecting all values lesser than the specified ID. Note that \\&#39;page\\&#39; parameter is ignored when \\&#39;lastId\\&#39; is specified | [optional] 

### Return type

[**GetAllOutboundMessagesResponse**](GetAllOutboundMessagesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_scheduled_messages**
> GetAllScheduledMessagesResponse get_all_scheduled_messages(page=page, limit=limit, status=status, order_by=order_by, direction=direction)

Get all scheduled messages.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
status = 'x' # str | Fetch schedules with the specific status: a - actual, c - completed, x - all (optional) (default to x)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)

try:
    # Get all scheduled messages.
    api_response = api_instance.get_all_scheduled_messages(page=page, limit=limit, status=status, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_all_scheduled_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **status** | **str**| Fetch schedules with the specific status: a - actual, c - completed, x - all | [optional] [default to x]
 **order_by** | **str**| Order results by some field. Default is id | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc | [optional] [default to desc]

### Return type

[**GetAllScheduledMessagesResponse**](GetAllScheduledMessagesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_templates**
> GetAllTemplatesResponse get_all_templates(page=page, limit=limit)

Get all user templates.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional)
limit = 10 # int | How many results to return (optional)

try:
    # Get all user templates.
    api_response = api_instance.get_all_templates(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_all_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] 
 **limit** | **int**| How many results to return | [optional] 

### Return type

[**GetAllTemplatesResponse**](GetAllTemplatesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_dedicated_numbers**
> GetAvailableDedicatedNumbersResponse get_available_dedicated_numbers(country, prefix=prefix, tollfree=tollfree)

Find available dedicated numbers to buy.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
country = '\"GB\"' # str | Dedicated number country. Two letters in upper case
prefix = 1 # int | Desired number prefix. Should include country code (i.e. 447 for GB). In case provide tollfree = 1 parameter and there are available tollfree numbers, this parameter will be ignore. (optional) (default to 1)
tollfree = 0 # int | Should we show only tollfree numbers (tollfree available only for US). Default is false. (optional) (default to 0)

try:
    # Find available dedicated numbers to buy.
    api_response = api_instance.get_available_dedicated_numbers(country, prefix=prefix, tollfree=tollfree)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_available_dedicated_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Dedicated number country. Two letters in upper case | 
 **prefix** | **int**| Desired number prefix. Should include country code (i.e. 447 for GB). In case provide tollfree &#x3D; 1 parameter and there are available tollfree numbers, this parameter will be ignore. | [optional] [default to 1]
 **tollfree** | **int**| Should we show only tollfree numbers (tollfree available only for US). Default is false. | [optional] [default to 0]

### Return type

[**GetAvailableDedicatedNumbersResponse**](GetAvailableDedicatedNumbersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_sender_setting_options**
> GetAvailableSenderSettingOptionsResponse get_available_sender_setting_options(country=country)

Get all available sender setting options which could be used in \"from\" parameter of POST messages method.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
country = 'country_example' # str | Return sender setting options available in specific country only. Two upper case characters (optional)

try:
    # Get all available sender setting options which could be used in \"from\" parameter of POST messages method.
    api_response = api_instance.get_available_sender_setting_options(country=country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_available_sender_setting_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Return sender setting options available in specific country only. Two upper case characters | [optional] 

### Return type

[**GetAvailableSenderSettingOptionsResponse**](GetAvailableSenderSettingOptionsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_notification_options**
> GetBalanceNotificationOptionsResponse get_balance_notification_options()

Returns the list of available balance options which can be used as a bound to determine when to send email to user with low balance notification. See https://my.textmagic.com/online/account/notifications/balance

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Returns the list of available balance options which can be used as a bound to determine when to send email to user with low balance notification. See https://my.textmagic.com/online/account/notifications/balance
    api_response = api_instance.get_balance_notification_options()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_balance_notification_options: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBalanceNotificationOptionsResponse**](GetBalanceNotificationOptionsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_notification_settings**
> GetBalanceNotificationSettingsResponse get_balance_notification_settings()

Get balance notification settings

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Get balance notification settings
    api_response = api_instance.get_balance_notification_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_balance_notification_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBalanceNotificationSettingsResponse**](GetBalanceNotificationSettingsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blocked_contacts**
> GetBlockedContactsResponse get_blocked_contacts(page=page, limit=limit, query=query, order_by=order_by, direction=direction)

Get blocked contacts.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
query = 'query_example' # str | Find blocked contacts by specified search query (optional)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)

try:
    # Get blocked contacts.
    api_response = api_instance.get_blocked_contacts(page=page, limit=limit, query=query, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_blocked_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **query** | **str**| Find blocked contacts by specified search query | [optional] 
 **order_by** | **str**| Order results by some field. Default is id | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc | [optional] [default to desc]

### Return type

[**GetBlockedContactsResponse**](GetBlockedContactsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bulk_session**
> BulkSession get_bulk_session(id)

Get bulk message session status.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get bulk message session status.
    api_response = api_instance.get_bulk_session(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_bulk_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BulkSession**](BulkSession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_callback_settings**
> GetCallbackSettingsResponse get_callback_settings()

Fetch callback URL settings

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Fetch callback URL settings
    api_response = api_instance.get_callback_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_callback_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetCallbackSettingsResponse**](GetCallbackSettingsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calls_prices**
> dict(str, object) get_calls_prices()

Check pricing for a inbound/outbound call.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Check pricing for a inbound/outbound call.
    api_response = api_instance.get_calls_prices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_calls_prices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, object)**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat**
> Chat get_chat(id)

Get a single chat.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single chat.
    api_response = api_instance.get_chat(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Chat**](Chat.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_by_phone**
> Chat get_chat_by_phone(phone, upsert=upsert, reopen=reopen)

Find chats by phone.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
phone = 'phone_example' # str | 
upsert = 0 # int | Create a new chat if not found (optional) (default to 0)
reopen = 0 # int | Reopen chat if found or do not change status (optional) (default to 0)

try:
    # Find chats by phone.
    api_response = api_instance.get_chat_by_phone(phone, upsert=upsert, reopen=reopen)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_chat_by_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**|  | 
 **upsert** | **int**| Create a new chat if not found | [optional] [default to 0]
 **reopen** | **int**| Reopen chat if found or do not change status | [optional] [default to 0]

### Return type

[**Chat**](Chat.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_messages**
> GetChatMessagesResponse get_chat_messages(id, page=page, limit=limit, query=query, start=start, end=end, direction=direction, voice=voice)

Fetch messages from chat with specified chat id.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
query = 'query_example' # str | Find messages by specified search query (optional)
start = 56 # int | Return messages since specified timestamp only (optional)
end = 56 # int | Return messages up to specified timestamp only (optional)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)
voice = 0 # int | Fetch results with voice calls (optional) (default to 0)

try:
    # Fetch messages from chat with specified chat id.
    api_response = api_instance.get_chat_messages(id, page=page, limit=limit, query=query, start=start, end=end, direction=direction, voice=voice)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_chat_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **query** | **str**| Find messages by specified search query | [optional] 
 **start** | **int**| Return messages since specified timestamp only | [optional] 
 **end** | **int**| Return messages up to specified timestamp only | [optional] 
 **direction** | **str**| Order direction. Default is desc | [optional] [default to desc]
 **voice** | **int**| Fetch results with voice calls | [optional] [default to 0]

### Return type

[**GetChatMessagesResponse**](GetChatMessagesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact**
> Contact get_contact(id)

Get a single contact.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | The contact id

try:
    # Get a single contact.
    api_response = api_instance.get_contact(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The contact id | 

### Return type

[**Contact**](Contact.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_by_phone**
> Contact get_contact_by_phone(phone)

Get a single contact by phone number.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
phone = 'phone_example' # str | 

try:
    # Get a single contact by phone number.
    api_response = api_instance.get_contact_by_phone(phone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_contact_by_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_if_blocked**
> Contact get_contact_if_blocked(phone)

Check is that phone number blocked

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
phone = '9997339956475' # str | Phone number to check

try:
    # Check is that phone number blocked
    api_response = api_instance.get_contact_if_blocked(phone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_contact_if_blocked: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**| Phone number to check | 

### Return type

[**Contact**](Contact.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_import_session_progress**
> GetContactImportSessionProgressResponse get_contact_import_session_progress(id)

Get contact import session progress.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 56 # int | 

try:
    # Get contact import session progress.
    api_response = api_instance.get_contact_import_session_progress(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_contact_import_session_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetContactImportSessionProgressResponse**](GetContactImportSessionProgressResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_note**
> ContactNote get_contact_note(id)

Get a single contact note.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 56 # int | 

try:
    # Get a single contact note.
    api_response = api_instance.get_contact_note(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_contact_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ContactNote**](ContactNote.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_notes**
> GetContactNotesResponse get_contact_notes(id, page=page, limit=limit)

Fetch notes assigned to the given contact.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Fetch notes assigned to the given contact.
    api_response = api_instance.get_contact_notes(id, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_contact_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]

### Return type

[**GetContactNotesResponse**](GetContactNotesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts**
> GetContactsResponse get_contacts(page=page, limit=limit, shared=shared, order_by=order_by, direction=direction)

Get all user contacts.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
shared = 0 # int | Should shared contacts to be included (optional) (default to 0)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)

try:
    # Get all user contacts.
    api_response = api_instance.get_contacts(page=page, limit=limit, shared=shared, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **shared** | **int**| Should shared contacts to be included | [optional] [default to 0]
 **order_by** | **str**| Order results by some field. Default is id | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc | [optional] [default to desc]

### Return type

[**GetContactsResponse**](GetContactsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts_autocomplete**
> list[GetContactsAutocompleteResponse] get_contacts_autocomplete(query, limit=limit, lists=lists)

Get contacts autocomplete suggestions by given search term.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
query = '\"A\"' # str | Find recipients by specified search query
limit = 10 # int | How many results to return (optional) (default to 10)
lists = 0 # int | Should lists be returned or not (optional) (default to 0)

try:
    # Get contacts autocomplete suggestions by given search term.
    api_response = api_instance.get_contacts_autocomplete(query, limit=limit, lists=lists)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_contacts_autocomplete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Find recipients by specified search query | 
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **lists** | **int**| Should lists be returned or not | [optional] [default to 0]

### Return type

[**list[GetContactsAutocompleteResponse]**](GetContactsAutocompleteResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts_by_list_id**
> GetContactsByListIdResponse get_contacts_by_list_id(id, page=page, limit=limit, order_by=order_by, direction=direction)

Fetch user contacts by given group id.

A useful synonym for \"contacts/search\" command with provided \"listId\" parameter.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | Given group Id.
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)

try:
    # Fetch user contacts by given group id.
    api_response = api_instance.get_contacts_by_list_id(id, page=page, limit=limit, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_contacts_by_list_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Given group Id. | 
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **order_by** | **str**| Order results by some field. Default is id | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc | [optional] [default to desc]

### Return type

[**GetContactsByListIdResponse**](GetContactsByListIdResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_countries**
> list[Country] get_countries()

Return list of countries.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Return list of countries.
    api_response = api_instance.get_countries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_countries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Country]**](Country.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> User get_current_user()

Get current user info.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Get current user info.
    api_response = api_instance.get_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field**
> UserCustomField get_custom_field(id)

Get a single custom field.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single custom field.
    api_response = api_instance.get_custom_field(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UserCustomField**](UserCustomField.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_fields**
> GetCustomFieldsResponse get_custom_fields(page=page, limit=limit)

Get all contact custom fields.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Get all contact custom fields.
    api_response = api_instance.get_custom_fields(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]

### Return type

[**GetCustomFieldsResponse**](GetCustomFieldsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dedicated_number**
> UsersInbound get_dedicated_number(id)

Get a single dedicated number.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single dedicated number.
    api_response = api_instance.get_dedicated_number(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_dedicated_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UsersInbound**](UsersInbound.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disallowed_rules**
> list[str] get_disallowed_rules()

Get an array of all rules that are disallowed to the current account.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Get an array of all rules that are disallowed to the current account.
    api_response = api_instance.get_disallowed_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_disallowed_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favourites**
> GetFavouritesResponse get_favourites(page=page, limit=limit, query=query)

Get favorite contacts and lists.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
query = 'A' # str | Find contacts or lists by specified search query (optional) (default to A)

try:
    # Get favorite contacts and lists.
    api_response = api_instance.get_favourites(page=page, limit=limit, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_favourites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **query** | **str**| Find contacts or lists by specified search query | [optional] [default to A]

### Return type

[**GetFavouritesResponse**](GetFavouritesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forwarded_calls**
> GetForwardedCallsResponse get_forwarded_calls(page=page, limit=limit)

Get all forwarded calls.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Get all forwarded calls.
    api_response = api_instance.get_forwarded_calls(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_forwarded_calls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]

### Return type

[**GetForwardedCallsResponse**](GetForwardedCallsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound_message**
> MessageIn get_inbound_message(id)

Get a single inbox message.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single inbox message.
    api_response = api_instance.get_inbound_message(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_inbound_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MessageIn**](MessageIn.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound_messages_notification_settings**
> GetInboundMessagesNotificationSettingsResponse get_inbound_messages_notification_settings()

Get inbound messages notification settings

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Get inbound messages notification settings
    api_response = api_instance.get_inbound_messages_notification_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_inbound_messages_notification_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetInboundMessagesNotificationSettingsResponse**](GetInboundMessagesNotificationSettingsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices**
> GetInvoicesResponse get_invoices(page=page, limit=limit)

Return account invoices.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Return account invoices.
    api_response = api_instance.get_invoices(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]

### Return type

[**GetInvoicesResponse**](GetInvoicesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list**
> Group get_list(id)

Get a single list.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single list.
    api_response = api_instance.get_list(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Group**](Group.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_contacts_ids**
> GetListContactsIdsResponse get_list_contacts_ids(id)

Fetch all contacts IDs belonging to the list with ID.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Fetch all contacts IDs belonging to the list with ID.
    api_response = api_instance.get_list_contacts_ids(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_list_contacts_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetListContactsIdsResponse**](GetListContactsIdsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lists_of_contact**
> GetListsOfContactResponse get_lists_of_contact(id, page=page, limit=limit)

Return lists which contact belongs to.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Return lists which contact belongs to.
    api_response = api_instance.get_lists_of_contact(id, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_lists_of_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]

### Return type

[**GetListsOfContactResponse**](GetListsOfContactResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_preview**
> GetMessagePreviewResponse get_message_preview(text=text, template_id=template_id, sending_time=sending_time, sending_date_time=sending_date_time, sending_timezone=sending_timezone, contacts=contacts, lists=lists, phones=phones, cut_extra=cut_extra, parts_count=parts_count, reference_id=reference_id, _from=_from, rule=rule, create_chat=create_chat, tts=tts, local=local, local_country=local_country)

Preview message

Get messages preview (with tags merged) up to 100 messages per session.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
text = '\"Test message test\"' # str | Message text. Required if template_id is not set (optional)
template_id = 1 # int | Template used instead of message text. Required if text is not set (optional)
sending_time = 1565606455 # int | DEPRECATED, consider using sendingDateTime and sendingTimezone parameters instead: Optional (required with rrule set). Message sending time in unix timestamp format. Default is now (optional)
sending_date_time = '\"2020-05-27 13:02:33\"' # str | Sending time in Y-m-d H:i:s format (e.g. 2016-05-27 13:02:33). This time is relative to sendingTimezone (optional)
sending_timezone = '\"America/Buenos_Aires\"' # str | ID or ISO-name of timezone used for sending when sendingDateTime parameter is set. E.g. if you specify sendingDateTime = \\\"2016-05-27 13:02:33\\\" and sendingTimezone = \\\"America/Buenos_Aires\\\", your message will be sent at May 27, 2016 13:02:33 Buenos Aires time, or 16:02:33 UTC. Default is account timezone (optional)
contacts = '\"1,2,3,4\"' # str | Comma separated array of contact resources id message will be sent to (optional)
lists = '\"1,2,3,4\"' # str | Comma separated array of list resources id message will be sent to (optional)
phones = '\"+19993322111,+19993322110\"' # str | Comma separated array of E.164 phone numbers message will be sent to (optional)
cut_extra = 0 # int | Should sending method cut extra characters which not fit supplied partsCount or return 400 Bad request response instead. Default is 0 (optional) (default to 0)
parts_count = 6 # int | Maximum message parts count (TextMagic allows sending 1 to 6 message parts). Default is 6 (optional) (default to 6)
reference_id = 1 # int | Custom message reference id which can be used in your application infrastructure (optional)
_from = '\"Testid1\"' # str | One of allowed Sender ID (phone number or alphanumeric sender ID). If specified Sender ID is not allowed for some destinations, a fallback default Sender ID will be used to ensure delivery (optional)
rule = '\"FREQ=YEARLY;BYMONTH=1;BYMONTHDAY=1;COUNT=1\"' # str | iCal RRULE parameter to create recurrent scheduled messages. When used, sendingTime is mandatory as start point of sending. See https://www.textmagic.com/free-tools/rrule-generator for format details (optional)
create_chat = 0 # int | Should sending method try to create new Chat(if not exist) with specified recipients. Default is 0 (optional) (default to 0)
tts = 0 # int | Send Text to Speech message. Default is 0 (optional) (default to 0)
local = 0 # int | Treat phone numbers passed in \\'phones\\' field as local. Default is 0 (optional) (default to 0)
local_country = '\"US\"' # str | 2-letter ISO country code for local phone numbers, used when \\'local\\' is set to true. Default is account country (optional)

try:
    # Preview message
    api_response = api_instance.get_message_preview(text=text, template_id=template_id, sending_time=sending_time, sending_date_time=sending_date_time, sending_timezone=sending_timezone, contacts=contacts, lists=lists, phones=phones, cut_extra=cut_extra, parts_count=parts_count, reference_id=reference_id, _from=_from, rule=rule, create_chat=create_chat, tts=tts, local=local, local_country=local_country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_message_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Message text. Required if template_id is not set | [optional] 
 **template_id** | **int**| Template used instead of message text. Required if text is not set | [optional] 
 **sending_time** | **int**| DEPRECATED, consider using sendingDateTime and sendingTimezone parameters instead: Optional (required with rrule set). Message sending time in unix timestamp format. Default is now | [optional] 
 **sending_date_time** | **str**| Sending time in Y-m-d H:i:s format (e.g. 2016-05-27 13:02:33). This time is relative to sendingTimezone | [optional] 
 **sending_timezone** | **str**| ID or ISO-name of timezone used for sending when sendingDateTime parameter is set. E.g. if you specify sendingDateTime &#x3D; \\\&quot;2016-05-27 13:02:33\\\&quot; and sendingTimezone &#x3D; \\\&quot;America/Buenos_Aires\\\&quot;, your message will be sent at May 27, 2016 13:02:33 Buenos Aires time, or 16:02:33 UTC. Default is account timezone | [optional] 
 **contacts** | **str**| Comma separated array of contact resources id message will be sent to | [optional] 
 **lists** | **str**| Comma separated array of list resources id message will be sent to | [optional] 
 **phones** | **str**| Comma separated array of E.164 phone numbers message will be sent to | [optional] 
 **cut_extra** | **int**| Should sending method cut extra characters which not fit supplied partsCount or return 400 Bad request response instead. Default is 0 | [optional] [default to 0]
 **parts_count** | **int**| Maximum message parts count (TextMagic allows sending 1 to 6 message parts). Default is 6 | [optional] [default to 6]
 **reference_id** | **int**| Custom message reference id which can be used in your application infrastructure | [optional] 
 **_from** | **str**| One of allowed Sender ID (phone number or alphanumeric sender ID). If specified Sender ID is not allowed for some destinations, a fallback default Sender ID will be used to ensure delivery | [optional] 
 **rule** | **str**| iCal RRULE parameter to create recurrent scheduled messages. When used, sendingTime is mandatory as start point of sending. See https://www.textmagic.com/free-tools/rrule-generator for format details | [optional] 
 **create_chat** | **int**| Should sending method try to create new Chat(if not exist) with specified recipients. Default is 0 | [optional] [default to 0]
 **tts** | **int**| Send Text to Speech message. Default is 0 | [optional] [default to 0]
 **local** | **int**| Treat phone numbers passed in \\&#39;phones\\&#39; field as local. Default is 0 | [optional] [default to 0]
 **local_country** | **str**| 2-letter ISO country code for local phone numbers, used when \\&#39;local\\&#39; is set to true. Default is account country | [optional] 

### Return type

[**GetMessagePreviewResponse**](GetMessagePreviewResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_price**
> GetMessagePriceResponse get_message_price(include_blocked=include_blocked, text=text, template_id=template_id, sending_time=sending_time, sending_date_time=sending_date_time, sending_timezone=sending_timezone, contacts=contacts, lists=lists, phones=phones, cut_extra=cut_extra, parts_count=parts_count, reference_id=reference_id, _from=_from, rule=rule, create_chat=create_chat, tts=tts, local=local, local_country=local_country)

Check price

Check pricing for a new outbound message.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
include_blocked = 0 # int | Should we show pricing for the blocked contacts. (optional) (default to 0)
text = '\"Test message test\"' # str | Message text. Required if template_id is not set (optional)
template_id = 1 # int | Template used instead of message text. Required if text is not set (optional)
sending_time = 1565606455 # int | DEPRECATED, consider using sendingDateTime and sendingTimezone parameters instead: Optional (required with rrule set). Message sending time in unix timestamp format. Default is now (optional)
sending_date_time = '\"2020-05-27 13:02:33\"' # str | Sending time in Y-m-d H:i:s format (e.g. 2016-05-27 13:02:33). This time is relative to sendingTimezone (optional)
sending_timezone = '\"America/Buenos_Aires\"' # str | ID or ISO-name of timezone used for sending when sendingDateTime parameter is set. E.g. if you specify sendingDateTime = \\\"2016-05-27 13:02:33\\\" and sendingTimezone = \\\"America/Buenos_Aires\\\", your message will be sent at May 27, 2016 13:02:33 Buenos Aires time, or 16:02:33 UTC. Default is account timezone (optional)
contacts = '\"1,2,3,4\"' # str | Comma separated array of contact resources id message will be sent to (optional)
lists = '\"1,2,3,4\"' # str | Comma separated array of list resources id message will be sent to (optional)
phones = '\"+19993322111,+19993322110\"' # str | Comma separated array of E.164 phone numbers message will be sent to (optional)
cut_extra = 0 # int | Should sending method cut extra characters which not fit supplied partsCount or return 400 Bad request response instead. Default is 0 (optional) (default to 0)
parts_count = 6 # int | Maximum message parts count (TextMagic allows sending 1 to 6 message parts). Default is 6 (optional) (default to 6)
reference_id = 1 # int | Custom message reference id which can be used in your application infrastructure (optional)
_from = '\"Testid1\"' # str | One of allowed Sender ID (phone number or alphanumeric sender ID). If specified Sender ID is not allowed for some destinations, a fallback default Sender ID will be used to ensure delivery (optional)
rule = '\"FREQ=YEARLY;BYMONTH=1;BYMONTHDAY=1;COUNT=1\"' # str | iCal RRULE parameter to create recurrent scheduled messages. When used, sendingTime is mandatory as start point of sending. See https://www.textmagic.com/free-tools/rrule-generator for format details (optional)
create_chat = 0 # int | Should sending method try to create new Chat(if not exist) with specified recipients. Default is 0 (optional) (default to 0)
tts = 0 # int | Send Text to Speech message. Default is 0 (optional) (default to 0)
local = 0 # int | Treat phone numbers passed in \\'phones\\' field as local. Default is 0 (optional) (default to 0)
local_country = '\"US\"' # str | 2-letter ISO country code for local phone numbers, used when \\'local\\' is set to true. Default is account country (optional)

try:
    # Check price
    api_response = api_instance.get_message_price(include_blocked=include_blocked, text=text, template_id=template_id, sending_time=sending_time, sending_date_time=sending_date_time, sending_timezone=sending_timezone, contacts=contacts, lists=lists, phones=phones, cut_extra=cut_extra, parts_count=parts_count, reference_id=reference_id, _from=_from, rule=rule, create_chat=create_chat, tts=tts, local=local, local_country=local_country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_message_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_blocked** | **int**| Should we show pricing for the blocked contacts. | [optional] [default to 0]
 **text** | **str**| Message text. Required if template_id is not set | [optional] 
 **template_id** | **int**| Template used instead of message text. Required if text is not set | [optional] 
 **sending_time** | **int**| DEPRECATED, consider using sendingDateTime and sendingTimezone parameters instead: Optional (required with rrule set). Message sending time in unix timestamp format. Default is now | [optional] 
 **sending_date_time** | **str**| Sending time in Y-m-d H:i:s format (e.g. 2016-05-27 13:02:33). This time is relative to sendingTimezone | [optional] 
 **sending_timezone** | **str**| ID or ISO-name of timezone used for sending when sendingDateTime parameter is set. E.g. if you specify sendingDateTime &#x3D; \\\&quot;2016-05-27 13:02:33\\\&quot; and sendingTimezone &#x3D; \\\&quot;America/Buenos_Aires\\\&quot;, your message will be sent at May 27, 2016 13:02:33 Buenos Aires time, or 16:02:33 UTC. Default is account timezone | [optional] 
 **contacts** | **str**| Comma separated array of contact resources id message will be sent to | [optional] 
 **lists** | **str**| Comma separated array of list resources id message will be sent to | [optional] 
 **phones** | **str**| Comma separated array of E.164 phone numbers message will be sent to | [optional] 
 **cut_extra** | **int**| Should sending method cut extra characters which not fit supplied partsCount or return 400 Bad request response instead. Default is 0 | [optional] [default to 0]
 **parts_count** | **int**| Maximum message parts count (TextMagic allows sending 1 to 6 message parts). Default is 6 | [optional] [default to 6]
 **reference_id** | **int**| Custom message reference id which can be used in your application infrastructure | [optional] 
 **_from** | **str**| One of allowed Sender ID (phone number or alphanumeric sender ID). If specified Sender ID is not allowed for some destinations, a fallback default Sender ID will be used to ensure delivery | [optional] 
 **rule** | **str**| iCal RRULE parameter to create recurrent scheduled messages. When used, sendingTime is mandatory as start point of sending. See https://www.textmagic.com/free-tools/rrule-generator for format details | [optional] 
 **create_chat** | **int**| Should sending method try to create new Chat(if not exist) with specified recipients. Default is 0 | [optional] [default to 0]
 **tts** | **int**| Send Text to Speech message. Default is 0 | [optional] [default to 0]
 **local** | **int**| Treat phone numbers passed in \\&#39;phones\\&#39; field as local. Default is 0 | [optional] [default to 0]
 **local_country** | **str**| 2-letter ISO country code for local phone numbers, used when \\&#39;local\\&#39; is set to true. Default is account country | [optional] 

### Return type

[**GetMessagePriceResponse**](GetMessagePriceResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_prices**
> GetMessagePricesResponse get_message_prices()

Get pricing

Get message prices for all countries.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Get pricing
    api_response = api_instance.get_message_prices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_message_prices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMessagePricesResponse**](GetMessagePricesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_session**
> MessageSession get_message_session(id)

Get a message session.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a message session.
    api_response = api_instance.get_message_session(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_message_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MessageSession**](MessageSession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_session_stat**
> GetMessageSessionStatResponse get_message_session_stat(id, include_deleted=include_deleted)

Get sending session statistics.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
include_deleted = 0 # int | Search also in deleted messages (optional) (default to 0)

try:
    # Get sending session statistics.
    api_response = api_instance.get_message_session_stat(id, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_message_session_stat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **include_deleted** | **int**| Search also in deleted messages | [optional] [default to 0]

### Return type

[**GetMessageSessionStatResponse**](GetMessageSessionStatResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages_by_session_id**
> GetMessagesBySessionIdResponse get_messages_by_session_id(id, page=page, limit=limit, statuses=statuses, include_deleted=include_deleted)

Fetch messages by given session id.

A useful synonym for \"messages/search\" command with provided \"sessionId\" parameter.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
statuses = 'statuses_example' # str | Find messages by status (optional)
include_deleted = 0 # int | Search also in deleted messages (optional) (default to 0)

try:
    # Fetch messages by given session id.
    api_response = api_instance.get_messages_by_session_id(id, page=page, limit=limit, statuses=statuses, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_messages_by_session_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **statuses** | **str**| Find messages by status | [optional] 
 **include_deleted** | **int**| Search also in deleted messages | [optional] [default to 0]

### Return type

[**GetMessagesBySessionIdResponse**](GetMessagesBySessionIdResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messaging_counters**
> GetMessagingCountersResponse get_messaging_counters()

Return counters for messaging data views.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Return counters for messaging data views.
    api_response = api_instance.get_messaging_counters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_messaging_counters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMessagingCountersResponse**](GetMessagingCountersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messaging_stat**
> GetMessagingStatResponse get_messaging_stat(by=by, start=start, end=end)

Return messaging statistics.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
by = 'off' # str | Group results by specified period: off, day, month or year. Default is off (optional) (default to off)
start = 56 # int | Start date in unix timestamp format. Default is 7 days ago (optional)
end = 'end_example' # str | End date in unix timestamp format. Default is now (optional)

try:
    # Return messaging statistics.
    api_response = api_instance.get_messaging_stat(by=by, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_messaging_stat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **by** | **str**| Group results by specified period: off, day, month or year. Default is off | [optional] [default to off]
 **start** | **int**| Start date in unix timestamp format. Default is 7 days ago | [optional] 
 **end** | **str**| End date in unix timestamp format. Default is now | [optional] 

### Return type

[**GetMessagingStatResponse**](GetMessagingStatResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbound_message**
> MessageOut get_outbound_message(id)

Get a single message

Get a single outgoing message.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single message
    api_response = api_instance.get_outbound_message(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_outbound_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MessageOut**](MessageOut.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbound_messages_history**
> GetOutboundMessagesHistoryResponse get_outbound_messages_history(limit=limit, last_id=last_id, query=query, order_by=order_by, direction=direction)

Get history

Get outbound messages history.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
limit = 10 # int | How many results to return (optional) (default to 10)
last_id = 56 # int | Filter results by ID, selecting all values lesser than the specified ID. (optional)
query = 'query_example' # str | Find message by specified search query (optional)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)

try:
    # Get history
    api_response = api_instance.get_outbound_messages_history(limit=limit, last_id=last_id, query=query, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_outbound_messages_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **last_id** | **int**| Filter results by ID, selecting all values lesser than the specified ID. | [optional] 
 **query** | **str**| Find message by specified search query | [optional] 
 **order_by** | **str**| Order results by some field. Default is id | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc | [optional] [default to desc]

### Return type

[**GetOutboundMessagesHistoryResponse**](GetOutboundMessagesHistoryResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_push_tokens**
> GetPushTokensResponse get_push_tokens()

Get all device tokens assigned to the current account

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Get all device tokens assigned to the current account
    api_response = api_instance.get_push_tokens()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_push_tokens: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPushTokensResponse**](GetPushTokensResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_message**
> MessagesIcs get_scheduled_message(id)

Get message schedule.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get message schedule.
    api_response = api_instance.get_scheduled_message(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_scheduled_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MessagesIcs**](MessagesIcs.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sender_id**
> SenderId get_sender_id(id)

Get a single Sender ID.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single Sender ID.
    api_response = api_instance.get_sender_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_sender_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SenderId**](SenderId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sender_ids**
> GetSenderIdsResponse get_sender_ids(page=page, limit=limit)

Get all sender IDs of current user.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Get all sender IDs of current user.
    api_response = api_instance.get_sender_ids(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_sender_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]

### Return type

[**GetSenderIdsResponse**](GetSenderIdsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sender_settings**
> GetSenderSettingsResponse get_sender_settings(country=country)

Get current user sender settings.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
country = 'country_example' # str | Return sender settings enabled for sending to specified country. Two upper case characters (optional)

try:
    # Get current user sender settings.
    api_response = api_instance.get_sender_settings(country=country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_sender_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Return sender settings enabled for sending to specified country. Two upper case characters | [optional] 

### Return type

[**GetSenderSettingsResponse**](GetSenderSettingsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spending_stat**
> GetSpendingStatResponse get_spending_stat(page=page, limit=limit, start=start, end=end)

Return account spending statistics.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
start = 56 # int | Optional. Start date in unix timestamp format. Default is 7 days ago (optional)
end = 56 # int | Optional. End date in unix timestamp format. Default is now (optional)

try:
    # Return account spending statistics.
    api_response = api_instance.get_spending_stat(page=page, limit=limit, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_spending_stat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **start** | **int**| Optional. Start date in unix timestamp format. Default is 7 days ago | [optional] 
 **end** | **int**| Optional. End date in unix timestamp format. Default is now | [optional] 

### Return type

[**GetSpendingStatResponse**](GetSpendingStatResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state**
> GetStateResponse get_state()

Get current entities state

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Get current entities state
    api_response = api_instance.get_state()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_state: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetStateResponse**](GetStateResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subaccount**
> User get_subaccount(id)

Get a single subaccount.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single subaccount.
    api_response = api_instance.get_subaccount(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_subaccount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**User**](User.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subaccounts**
> User get_subaccounts(page=page, limit=limit)

Get all subaccounts of current user.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Get all subaccounts of current user.
    api_response = api_instance.get_subaccounts(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_subaccounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]

### Return type

[**User**](User.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subaccounts_with_tokens**
> GetSubaccountsWithTokensResponse get_subaccounts_with_tokens(get_subaccounts_with_tokens_input_object, page=page, limit=limit, x_ignore_null_values=x_ignore_null_values)

Get all subaccounts with their REST API tokens associated with specified app name.

When more than one token related to app name, last key will be returned.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
get_subaccounts_with_tokens_input_object = TextMagic.GetSubaccountsWithTokensInputObject() # GetSubaccountsWithTokensInputObject | 
page = 1 # float | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Get all subaccounts with their REST API tokens associated with specified app name.
    api_response = api_instance.get_subaccounts_with_tokens(get_subaccounts_with_tokens_input_object, page=page, limit=limit, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_subaccounts_with_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_subaccounts_with_tokens_input_object** | [**GetSubaccountsWithTokensInputObject**](GetSubaccountsWithTokensInputObject.md)|  | 
 **page** | **float**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**GetSubaccountsWithTokensResponse**](GetSubaccountsWithTokensResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_survey**
> Survey get_survey(id)

Get a survey by id.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a survey by id.
    api_response = api_instance.get_survey(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Survey**](Survey.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_survey_node**
> SurveyNode get_survey_node(id)

Get a node by id.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a node by id.
    api_response = api_instance.get_survey_node(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_survey_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SurveyNode**](SurveyNode.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_survey_nodes**
> GetSurveyNodesResponse get_survey_nodes(id)

Fetch nodes by given survey id.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Fetch nodes by given survey id.
    api_response = api_instance.get_survey_nodes(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_survey_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetSurveyNodesResponse**](GetSurveyNodesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_surveys**
> GetSurveysResponse get_surveys(page=page, limit=limit)

Get all user surveys.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Get all user surveys.
    api_response = api_instance.get_surveys(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_surveys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]

### Return type

[**GetSurveysResponse**](GetSurveysResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> MessageTemplate get_template(id)

Get a single template.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single template.
    api_response = api_instance.get_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MessageTemplate**](MessageTemplate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timezones**
> object get_timezones(full=full)

Return all available timezone IDs.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
full = 0 # int | Return full info about timezones in array (0 or 1). Default is 0 (optional) (default to 0)

try:
    # Return all available timezone IDs.
    api_response = api_instance.get_timezones(full=full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_timezones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full** | **int**| Return full info about timezones in array (0 or 1). Default is 0 | [optional] [default to 0]

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unread_messages_total**
> GetUnreadMessagesTotalResponse get_unread_messages_total()

Get total amount of unread messages in the current user chats.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Get total amount of unread messages in the current user chats.
    api_response = api_instance.get_unread_messages_total()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_unread_messages_total: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetUnreadMessagesTotalResponse**](GetUnreadMessagesTotalResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unsubscribed_contact**
> UnsubscribedContact get_unsubscribed_contact(id)

Get a single unsubscribed contact.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single unsubscribed contact.
    api_response = api_instance.get_unsubscribed_contact(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_unsubscribed_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UnsubscribedContact**](UnsubscribedContact.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unsubscribers**
> GetUnsubscribersResponse get_unsubscribers(page=page, limit=limit)

Get all contact have unsubscribed from your communication.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Get all contact have unsubscribed from your communication.
    api_response = api_instance.get_unsubscribers(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_unsubscribers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]

### Return type

[**GetUnsubscribersResponse**](GetUnsubscribersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_dedicated_numbers**
> GetUserDedicatedNumbersResponse get_user_dedicated_numbers(page=page, limit=limit, survey_id=survey_id)

Get user's dedicated numbers.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
survey_id = 56 # int | Fetch only that numbers which are ready for the survey (optional)

try:
    # Get user's dedicated numbers.
    api_response = api_instance.get_user_dedicated_numbers(page=page, limit=limit, survey_id=survey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_user_dedicated_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **survey_id** | **int**| Fetch only that numbers which are ready for the survey | [optional] 

### Return type

[**GetUserDedicatedNumbersResponse**](GetUserDedicatedNumbersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_lists**
> GetUserListsResponse get_user_lists(page=page, limit=limit, order_by=order_by, direction=direction, favorite_only=favorite_only, only_mine=only_mine)

Get all user lists.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)
favorite_only = 0 # int | Return only favorite lists (optional) (default to 0)
only_mine = 0 # int | Return only current user lists (optional) (default to 0)

try:
    # Get all user lists.
    api_response = api_instance.get_user_lists(page=page, limit=limit, order_by=order_by, direction=direction, favorite_only=favorite_only, only_mine=only_mine)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_user_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **order_by** | **str**| Order results by some field. Default is id | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc | [optional] [default to desc]
 **favorite_only** | **int**| Return only favorite lists | [optional] [default to 0]
 **only_mine** | **int**| Return only current user lists | [optional] [default to 0]

### Return type

[**GetUserListsResponse**](GetUserListsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versions**
> GetVersionsResponse get_versions()

Get minimal valid apps versions

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Get minimal valid apps versions
    api_response = api_instance.get_versions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetVersionsResponse**](GetVersionsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_subaccount**
> invite_subaccount(invite_subaccount_input_object, x_ignore_null_values=x_ignore_null_values)

Invite new subaccount.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
invite_subaccount_input_object = TextMagic.InviteSubaccountInputObject() # InviteSubaccountInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Invite new subaccount.
    api_instance.invite_subaccount(invite_subaccount_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->invite_subaccount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_subaccount_input_object** | [**InviteSubaccountInputObject**](InviteSubaccountInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_chats_read_bulk**
> mark_chats_read_bulk(mark_chats_read_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Mark several chats as read by chat ids or mark all chats as read

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
mark_chats_read_bulk_input_object = TextMagic.MarkChatsReadBulkInputObject() # MarkChatsReadBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Mark several chats as read by chat ids or mark all chats as read
    api_instance.mark_chats_read_bulk(mark_chats_read_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->mark_chats_read_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mark_chats_read_bulk_input_object** | [**MarkChatsReadBulkInputObject**](MarkChatsReadBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_chats_unread_bulk**
> mark_chats_unread_bulk(mark_chats_unread_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Mark several chats as UNread by chat ids or mark all chats as UNread

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
mark_chats_unread_bulk_input_object = TextMagic.MarkChatsUnreadBulkInputObject() # MarkChatsUnreadBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Mark several chats as UNread by chat ids or mark all chats as UNread
    api_instance.mark_chats_unread_bulk(mark_chats_unread_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->mark_chats_unread_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mark_chats_unread_bulk_input_object** | [**MarkChatsUnreadBulkInputObject**](MarkChatsUnreadBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_survey_nodes**
> merge_survey_nodes(merge_survey_nodes_input_object, x_ignore_null_values=x_ignore_null_values)

Merge two question nodes.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
merge_survey_nodes_input_object = TextMagic.MergeSurveyNodesInputObject() # MergeSurveyNodesInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Merge two question nodes.
    api_instance.merge_survey_nodes(merge_survey_nodes_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->merge_survey_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merge_survey_nodes_input_object** | [**MergeSurveyNodesInputObject**](MergeSurveyNodesInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mute_chat**
> ResourceLinkResponse mute_chat(mute_chat_input_object, x_ignore_null_values=x_ignore_null_values)

Set mute mode.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
mute_chat_input_object = TextMagic.MuteChatInputObject() # MuteChatInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Set mute mode.
    api_response = api_instance.mute_chat(mute_chat_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->mute_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mute_chat_input_object** | [**MuteChatInputObject**](MuteChatInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mute_chats_bulk**
> mute_chats_bulk(mute_chats_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Mute several chats by chat ids or mute all chats

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
mute_chats_bulk_input_object = TextMagic.MuteChatsBulkInputObject() # MuteChatsBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Mute several chats by chat ids or mute all chats
    api_instance.mute_chats_bulk(mute_chats_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->mute_chats_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mute_chats_bulk_input_object** | [**MuteChatsBulkInputObject**](MuteChatsBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping**
> PingResponse ping()

Just does a pong.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Just does a pong.
    api_response = api_instance.ping()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->ping: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PingResponse**](PingResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reopen_chats_bulk**
> reopen_chats_bulk(reopen_chats_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Reopen chats by chat ids or reopen all chats

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
reopen_chats_bulk_input_object = TextMagic.ReopenChatsBulkInputObject() # ReopenChatsBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Reopen chats by chat ids or reopen all chats
    api_instance.reopen_chats_bulk(reopen_chats_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->reopen_chats_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reopen_chats_bulk_input_object** | [**ReopenChatsBulkInputObject**](ReopenChatsBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_new_subaccount_token**
> User request_new_subaccount_token(request_new_subaccount_token_input_object, x_ignore_null_values=x_ignore_null_values)

Request a new REST API token for subaccount.

Returning user object, key and app name.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
request_new_subaccount_token_input_object = TextMagic.RequestNewSubaccountTokenInputObject() # RequestNewSubaccountTokenInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Request a new REST API token for subaccount.
    api_response = api_instance.request_new_subaccount_token(request_new_subaccount_token_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->request_new_subaccount_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_new_subaccount_token_input_object** | [**RequestNewSubaccountTokenInputObject**](RequestNewSubaccountTokenInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**User**](User.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_sender_id**
> ResourceLinkResponse request_sender_id(request_sender_id_input_object, x_ignore_null_values=x_ignore_null_values)

Request for a new Sender ID.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
request_sender_id_input_object = TextMagic.RequestSenderIdInputObject() # RequestSenderIdInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Request for a new Sender ID.
    api_response = api_instance.request_sender_id(request_sender_id_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->request_sender_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_sender_id_input_object** | [**RequestSenderIdInputObject**](RequestSenderIdInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_survey**
> ResourceLinkResponse reset_survey(id)

Reset a survey flow.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Reset a survey flow.
    api_response = api_instance.reset_survey(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->reset_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_chats**
> SearchChatsResponse search_chats(page=page, limit=limit, query=query)

Find chats by inbound or outbound messages text.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
query = 'query_example' # str | Find chats by specified search query (optional)

try:
    # Find chats by inbound or outbound messages text.
    api_response = api_instance.search_chats(page=page, limit=limit, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->search_chats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **query** | **str**| Find chats by specified search query | [optional] 

### Return type

[**SearchChatsResponse**](SearchChatsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_chats_by_ids**
> SearchChatsByIdsResponse search_chats_by_ids(page=page, limit=limit, ids=ids)

Find chats by IDs.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
ids = 'ids_example' # str | Find chats by ID(s) (optional)

try:
    # Find chats by IDs.
    api_response = api_instance.search_chats_by_ids(page=page, limit=limit, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->search_chats_by_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **ids** | **str**| Find chats by ID(s) | [optional] 

### Return type

[**SearchChatsByIdsResponse**](SearchChatsByIdsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_chats_by_receipent**
> SearchChatsByReceipentResponse search_chats_by_receipent(page=page, limit=limit, query=query, order_by=order_by)

Find chats by recipient (contact, list name or phone number).

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
query = 'query_example' # str | Find chats by specified search query (optional)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)

try:
    # Find chats by recipient (contact, list name or phone number).
    api_response = api_instance.search_chats_by_receipent(page=page, limit=limit, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->search_chats_by_receipent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **query** | **str**| Find chats by specified search query | [optional] 
 **order_by** | **str**| Order results by some field. Default is id | [optional] [default to id]

### Return type

[**SearchChatsByReceipentResponse**](SearchChatsByReceipentResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_contacts**
> SearchContactsResponse search_contacts(page=page, limit=limit, shared=shared, ids=ids, list_id=list_id, include_blocked=include_blocked, query=query, local=local, country=country, order_by=order_by, direction=direction)

Find user contacts by given parameters.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
shared = 0 # int | Should shared contacts to be included (optional) (default to 0)
ids = 'ids_example' # str | Find contact by ID(s) (optional)
list_id = 56 # int | Find contact by List ID (optional)
include_blocked = 56 # int | Should blocked contacts to be included (optional)
query = 'query_example' # str | Find contacts by specified search query (optional)
local = 0 # int | Treat phone number passed in 'query' field as local. Default is 0 (optional) (default to 0)
country = 'country_example' # str | 2-letter ISO country code for local phone numbers, used when 'local' is set to true. Default is account country (optional)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)

try:
    # Find user contacts by given parameters.
    api_response = api_instance.search_contacts(page=page, limit=limit, shared=shared, ids=ids, list_id=list_id, include_blocked=include_blocked, query=query, local=local, country=country, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->search_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **shared** | **int**| Should shared contacts to be included | [optional] [default to 0]
 **ids** | **str**| Find contact by ID(s) | [optional] 
 **list_id** | **int**| Find contact by List ID | [optional] 
 **include_blocked** | **int**| Should blocked contacts to be included | [optional] 
 **query** | **str**| Find contacts by specified search query | [optional] 
 **local** | **int**| Treat phone number passed in &#39;query&#39; field as local. Default is 0 | [optional] [default to 0]
 **country** | **str**| 2-letter ISO country code for local phone numbers, used when &#39;local&#39; is set to true. Default is account country | [optional] 
 **order_by** | **str**| Order results by some field. Default is id | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc | [optional] [default to desc]

### Return type

[**SearchContactsResponse**](SearchContactsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_inbound_messages**
> SearchInboundMessagesResponse search_inbound_messages(page=page, limit=limit, ids=ids, query=query, order_by=order_by, direction=direction, expand=expand)

Find inbound messages by given parameters.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
ids = 'ids_example' # str | Find message by ID(s) (optional)
query = 'query_example' # str | Find recipients by specified search query (optional)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)
expand = 0 # int | Expand by adding firstName, lastName and contactId (optional) (default to 0)

try:
    # Find inbound messages by given parameters.
    api_response = api_instance.search_inbound_messages(page=page, limit=limit, ids=ids, query=query, order_by=order_by, direction=direction, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->search_inbound_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **ids** | **str**| Find message by ID(s) | [optional] 
 **query** | **str**| Find recipients by specified search query | [optional] 
 **order_by** | **str**| Order results by some field. Default is id | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc | [optional] [default to desc]
 **expand** | **int**| Expand by adding firstName, lastName and contactId | [optional] [default to 0]

### Return type

[**SearchInboundMessagesResponse**](SearchInboundMessagesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_lists**
> SearchListsResponse search_lists(page=page, limit=limit, ids=ids, query=query, only_mine=only_mine, only_default=only_default, order_by=order_by, direction=direction)

Find contact lists by given parameters.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
ids = '\"1,2,3,4\"' # str | Find lists by ID(s) (optional)
query = '\"A\"' # str | Find lists by specified search query (optional)
only_mine = 0 # int | Return only current user lists (optional) (default to 0)
only_default = 0 # int | Return only default lists (optional) (default to 0)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)

try:
    # Find contact lists by given parameters.
    api_response = api_instance.search_lists(page=page, limit=limit, ids=ids, query=query, only_mine=only_mine, only_default=only_default, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->search_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **ids** | **str**| Find lists by ID(s) | [optional] 
 **query** | **str**| Find lists by specified search query | [optional] 
 **only_mine** | **int**| Return only current user lists | [optional] [default to 0]
 **only_default** | **int**| Return only default lists | [optional] [default to 0]
 **order_by** | **str**| Order results by some field. Default is id | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc | [optional] [default to desc]

### Return type

[**SearchListsResponse**](SearchListsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_outbound_messages**
> SearchOutboundMessagesResponse search_outbound_messages(page=page, limit=limit, last_id=last_id, ids=ids, session_id=session_id, statuses=statuses, include_deleted=include_deleted, query=query)

Find messages

Find outbound messages by given parameters.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
last_id = 56 # int | Filter results by ID, selecting all values lesser than the specified ID. Note that \\'page\\' parameter is ignored when \\'lastId\\' is specified (optional)
ids = 'ids_example' # str | Find message by ID(s) (optional)
session_id = 56 # int | Find messages by session ID (optional)
statuses = '\"q\"' # str | Find messages by status (optional)
include_deleted = 0 # int | Search also in deleted messages (optional) (default to 0)
query = 'query_example' # str | Find messages by specified search query (optional)

try:
    # Find messages
    api_response = api_instance.search_outbound_messages(page=page, limit=limit, last_id=last_id, ids=ids, session_id=session_id, statuses=statuses, include_deleted=include_deleted, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->search_outbound_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **last_id** | **int**| Filter results by ID, selecting all values lesser than the specified ID. Note that \\&#39;page\\&#39; parameter is ignored when \\&#39;lastId\\&#39; is specified | [optional] 
 **ids** | **str**| Find message by ID(s) | [optional] 
 **session_id** | **int**| Find messages by session ID | [optional] 
 **statuses** | **str**| Find messages by status | [optional] 
 **include_deleted** | **int**| Search also in deleted messages | [optional] [default to 0]
 **query** | **str**| Find messages by specified search query | [optional] 

### Return type

[**SearchOutboundMessagesResponse**](SearchOutboundMessagesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_scheduled_messages**
> SearchScheduledMessagesResponse search_scheduled_messages(page=page, limit=limit, query=query, ids=ids, status=status, order_by=order_by, direction=direction)

Find scheduled messages by given parameters.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
query = 'query_example' # str | Find messages by specified search query (optional)
ids = 'ids_example' # str | Find schedules by ID(s) (optional)
status = 'x' # str | Fetch schedules with the specific status: a - actual, c - completed, x - all (optional) (default to x)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)

try:
    # Find scheduled messages by given parameters.
    api_response = api_instance.search_scheduled_messages(page=page, limit=limit, query=query, ids=ids, status=status, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->search_scheduled_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **query** | **str**| Find messages by specified search query | [optional] 
 **ids** | **str**| Find schedules by ID(s) | [optional] 
 **status** | **str**| Fetch schedules with the specific status: a - actual, c - completed, x - all | [optional] [default to x]
 **order_by** | **str**| Order results by some field. Default is id | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc | [optional] [default to desc]

### Return type

[**SearchScheduledMessagesResponse**](SearchScheduledMessagesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_templates**
> SearchTemplatesResponse search_templates(page=page, limit=limit, ids=ids, name=name, content=content)

Find user templates by given parameters.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
ids = 'ids_example' # str | Find template by ID(s) (optional)
name = 'name_example' # str | Find template by name (optional)
content = 'content_example' # str | Find template by content (optional)

try:
    # Find user templates by given parameters.
    api_response = api_instance.search_templates(page=page, limit=limit, ids=ids, name=name, content=content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->search_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **ids** | **str**| Find template by ID(s) | [optional] 
 **name** | **str**| Find template by name | [optional] 
 **content** | **str**| Find template by content | [optional] 

### Return type

[**SearchTemplatesResponse**](SearchTemplatesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_verification_code**
> send_email_verification_code()

Send user email verification

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Send user email verification
    api_instance.send_email_verification_code()
except ApiException as e:
    print("Exception when calling TextMagicApi->send_email_verification_code: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message**
> SendMessageResponse send_message(send_message_input_object, x_ignore_null_values=x_ignore_null_values)

Send message

The main entrypoint to send messages. See examples above for the reference.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
send_message_input_object = TextMagic.SendMessageInputObject() # SendMessageInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Send message
    api_response = api_instance.send_message(send_message_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->send_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_message_input_object** | [**SendMessageInputObject**](SendMessageInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**SendMessageResponse**](SendMessageResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_phone_verification_code**
> send_phone_verification_code()

Send user phone verification

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Send user phone verification
    api_instance.send_phone_verification_code()
except ApiException as e:
    print("Exception when calling TextMagicApi->send_phone_verification_code: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_chat_status**
> ResourceLinkResponse set_chat_status(set_chat_status_input_object, x_ignore_null_values=x_ignore_null_values)

Set status of the chat given by ID.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
set_chat_status_input_object = TextMagic.SetChatStatusInputObject() # SetChatStatusInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Set status of the chat given by ID.
    api_response = api_instance.set_chat_status(set_chat_status_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->set_chat_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_chat_status_input_object** | [**SetChatStatusInputObject**](SetChatStatusInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_survey**
> ResourceLinkResponse start_survey(id)

Start a survey.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Start a survey.
    api_response = api_instance.start_survey(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->start_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unblock_contact**
> unblock_contact(unblock_contact_input_object, x_ignore_null_values=x_ignore_null_values)

Unblock contact by phone number.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
unblock_contact_input_object = TextMagic.UnblockContactInputObject() # UnblockContactInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Unblock contact by phone number.
    api_instance.unblock_contact(unblock_contact_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->unblock_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unblock_contact_input_object** | [**UnblockContactInputObject**](UnblockContactInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unblock_contacts_bulk**
> unblock_contacts_bulk(unblock_contacts_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Unblock several contacts by blocked contact ids or unblock all contacts

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
unblock_contacts_bulk_input_object = TextMagic.UnblockContactsBulkInputObject() # UnblockContactsBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Unblock several contacts by blocked contact ids or unblock all contacts
    api_instance.unblock_contacts_bulk(unblock_contacts_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->unblock_contacts_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unblock_contacts_bulk_input_object** | [**UnblockContactsBulkInputObject**](UnblockContactsBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unmute_chats_bulk**
> unmute_chats_bulk(unmute_chats_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Unmute several chats by chat ids or unmute all chats

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
unmute_chats_bulk_input_object = TextMagic.UnmuteChatsBulkInputObject() # UnmuteChatsBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Unmute several chats by chat ids or unmute all chats
    api_instance.unmute_chats_bulk(unmute_chats_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->unmute_chats_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unmute_chats_bulk_input_object** | [**UnmuteChatsBulkInputObject**](UnmuteChatsBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_contact**
> ResourceLinkResponse unsubscribe_contact(unsubscribe_contact_input_object, x_ignore_null_values=x_ignore_null_values)

Unsubscribe contact from your communication by phone number.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
unsubscribe_contact_input_object = TextMagic.UnsubscribeContactInputObject() # UnsubscribeContactInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Unsubscribe contact from your communication by phone number.
    api_response = api_instance.unsubscribe_contact(unsubscribe_contact_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->unsubscribe_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unsubscribe_contact_input_object** | [**UnsubscribeContactInputObject**](UnsubscribeContactInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_balance_notification_settings**
> update_balance_notification_settings(update_balance_notification_settings_input_object, x_ignore_null_values=x_ignore_null_values)

Update balance notification settings

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_balance_notification_settings_input_object = TextMagic.UpdateBalanceNotificationSettingsInputObject() # UpdateBalanceNotificationSettingsInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update balance notification settings
    api_instance.update_balance_notification_settings(update_balance_notification_settings_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_balance_notification_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_balance_notification_settings_input_object** | [**UpdateBalanceNotificationSettingsInputObject**](UpdateBalanceNotificationSettingsInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_callback_settings**
> update_callback_settings(update_callback_settings_input_object, x_ignore_null_values=x_ignore_null_values)

Update callback URL settings

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_callback_settings_input_object = TextMagic.UpdateCallbackSettingsInputObject() # UpdateCallbackSettingsInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update callback URL settings
    api_instance.update_callback_settings(update_callback_settings_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_callback_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_callback_settings_input_object** | [**UpdateCallbackSettingsInputObject**](UpdateCallbackSettingsInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_chat_desktop_notification_settings**
> update_chat_desktop_notification_settings(update_chat_desktop_notification_settings_input_object, x_ignore_null_values=x_ignore_null_values)

Update chat desktop notification settings

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_chat_desktop_notification_settings_input_object = TextMagic.UpdateChatDesktopNotificationSettingsInputObject() # UpdateChatDesktopNotificationSettingsInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update chat desktop notification settings
    api_instance.update_chat_desktop_notification_settings(update_chat_desktop_notification_settings_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_chat_desktop_notification_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_chat_desktop_notification_settings_input_object** | [**UpdateChatDesktopNotificationSettingsInputObject**](UpdateChatDesktopNotificationSettingsInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> ResourceLinkResponse update_contact(update_contact_input_object, id, x_ignore_null_values=x_ignore_null_values)

Update existing contact.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_contact_input_object = TextMagic.UpdateContactInputObject() # UpdateContactInputObject | 
id = 1 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update existing contact.
    api_response = api_instance.update_contact(update_contact_input_object, id, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_contact_input_object** | [**UpdateContactInputObject**](UpdateContactInputObject.md)|  | 
 **id** | **int**|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact_note**
> ResourceLinkResponse update_contact_note(update_contact_note_input_object, id, x_ignore_null_values=x_ignore_null_values)

Update existing contact note.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_contact_note_input_object = TextMagic.UpdateContactNoteInputObject() # UpdateContactNoteInputObject | 
id = 1 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update existing contact note.
    api_response = api_instance.update_contact_note(update_contact_note_input_object, id, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_contact_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_contact_note_input_object** | [**UpdateContactNoteInputObject**](UpdateContactNoteInputObject.md)|  | 
 **id** | **int**|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_current_user**
> UpdateCurrentUserResponse update_current_user(update_current_user_input_object, x_ignore_null_values=x_ignore_null_values)

Update current user info.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_current_user_input_object = TextMagic.UpdateCurrentUserInputObject() # UpdateCurrentUserInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update current user info.
    api_response = api_instance.update_current_user(update_current_user_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_current_user_input_object** | [**UpdateCurrentUserInputObject**](UpdateCurrentUserInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**UpdateCurrentUserResponse**](UpdateCurrentUserResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field**
> ResourceLinkResponse update_custom_field(update_custom_field_input_object, id, x_ignore_null_values=x_ignore_null_values)

Update existing custom field.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_custom_field_input_object = TextMagic.UpdateCustomFieldInputObject() # UpdateCustomFieldInputObject | 
id = 1 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update existing custom field.
    api_response = api_instance.update_custom_field(update_custom_field_input_object, id, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_custom_field_input_object** | [**UpdateCustomFieldInputObject**](UpdateCustomFieldInputObject.md)|  | 
 **id** | **int**|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field_value**
> ResourceLinkResponse update_custom_field_value(update_custom_field_value_input_object, id, x_ignore_null_values=x_ignore_null_values)

Update contact's custom field value.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_custom_field_value_input_object = TextMagic.UpdateCustomFieldValueInputObject() # UpdateCustomFieldValueInputObject | 
id = 'id_example' # str | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update contact's custom field value.
    api_response = api_instance.update_custom_field_value(update_custom_field_value_input_object, id, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_custom_field_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_custom_field_value_input_object** | [**UpdateCustomFieldValueInputObject**](UpdateCustomFieldValueInputObject.md)|  | 
 **id** | **str**|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inbound_messages_notification_settings**
> update_inbound_messages_notification_settings(update_inbound_messages_notification_settings_input_object, x_ignore_null_values=x_ignore_null_values)

Update inbound messages notification settings

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_inbound_messages_notification_settings_input_object = TextMagic.UpdateInboundMessagesNotificationSettingsInputObject() # UpdateInboundMessagesNotificationSettingsInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update inbound messages notification settings
    api_instance.update_inbound_messages_notification_settings(update_inbound_messages_notification_settings_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_inbound_messages_notification_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_inbound_messages_notification_settings_input_object** | [**UpdateInboundMessagesNotificationSettingsInputObject**](UpdateInboundMessagesNotificationSettingsInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_list**
> ResourceLinkResponse update_list(id, update_list_object=update_list_object)

Update existing list.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
update_list_object = TextMagic.UpdateListObject() # UpdateListObject |  (optional)

try:
    # Update existing list.
    api_response = api_instance.update_list(id, update_list_object=update_list_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_list_object** | [**UpdateListObject**](UpdateListObject.md)|  | [optional] 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password**
> update_password(update_password_input_object, x_ignore_null_values=x_ignore_null_values)

Change user password.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_password_input_object = TextMagic.UpdatePasswordInputObject() # UpdatePasswordInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Change user password.
    api_instance.update_password(update_password_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_password_input_object** | [**UpdatePasswordInputObject**](UpdatePasswordInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sender_setting**
> update_sender_setting(update_sender_setting_input_object, x_ignore_null_values=x_ignore_null_values)

Change sender settings for specified country.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_sender_setting_input_object = TextMagic.UpdateSenderSettingInputObject() # UpdateSenderSettingInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Change sender settings for specified country.
    api_instance.update_sender_setting(update_sender_setting_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_sender_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_sender_setting_input_object** | [**UpdateSenderSettingInputObject**](UpdateSenderSettingInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_survey**
> ResourceLinkResponse update_survey(update_survey_input_object, id, x_ignore_null_values=x_ignore_null_values)

Update existing survey.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_survey_input_object = TextMagic.UpdateSurveyInputObject() # UpdateSurveyInputObject | 
id = 1 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update existing survey.
    api_response = api_instance.update_survey(update_survey_input_object, id, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_survey_input_object** | [**UpdateSurveyInputObject**](UpdateSurveyInputObject.md)|  | 
 **id** | **int**|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_survey_node**
> ResourceLinkResponse update_survey_node(update_survey_node_input_object, id, x_ignore_null_values=x_ignore_null_values)

Update existing node.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_survey_node_input_object = TextMagic.UpdateSurveyNodeInputObject() # UpdateSurveyNodeInputObject | 
id = 1 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update existing node.
    api_response = api_instance.update_survey_node(update_survey_node_input_object, id, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_survey_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_survey_node_input_object** | [**UpdateSurveyNodeInputObject**](UpdateSurveyNodeInputObject.md)|  | 
 **id** | **int**|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> ResourceLinkResponse update_template(update_template_input_object, id, x_ignore_null_values=x_ignore_null_values)

Update existing template.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_template_input_object = TextMagic.UpdateTemplateInputObject() # UpdateTemplateInputObject | 
id = 1 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update existing template.
    api_response = api_instance.update_template(update_template_input_object, id, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_template_input_object** | [**UpdateTemplateInputObject**](UpdateTemplateInputObject.md)|  | 
 **id** | **int**|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_avatar**
> upload_avatar(image)

Add an avatar for the current user.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
image = '/path/to/file.txt' # file | User avatar. Should be PNG or JPG file not more than 10 MB

try:
    # Add an avatar for the current user.
    api_instance.upload_avatar(image)
except ApiException as e:
    print("Exception when calling TextMagicApi->upload_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **file**| User avatar. Should be PNG or JPG file not more than 10 MB | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_contact_avatar**
> ResourceLinkResponse upload_contact_avatar(image, id)

Add an avatar for the contact.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
image = '/path/to/file.txt' # file | Contact avatar. Should be PNG or JPG file not more than 10 MB
id = 56 # int | 

try:
    # Add an avatar for the contact.
    api_response = api_instance.upload_contact_avatar(image, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->upload_contact_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **file**| Contact avatar. Should be PNG or JPG file not more than 10 MB | 
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_list_avatar**
> ResourceLinkResponse upload_list_avatar(image, id)

Add an avatar for the list.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
image = '/path/to/file.txt' # file | List avatar. Should be PNG or JPG file not more than 10 MB
id = 1 # int | 

try:
    # Add an avatar for the list.
    api_response = api_instance.upload_list_avatar(image, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->upload_list_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **file**| List avatar. Should be PNG or JPG file not more than 10 MB | 
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_message_attachment**
> UploadMessageAttachmentResponse upload_message_attachment(file)

Upload message attachment

Upload a new file to insert it as a link.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
file = '/path/to/file.txt' # file | Attachment. Supports .jpg, .gif, .png, .pdf, .txt, .csv, .doc, .docx, .xls, .xlsx, .ppt, .pptx & .vcf file formats

try:
    # Upload message attachment
    api_response = api_instance.upload_message_attachment(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->upload_message_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| Attachment. Supports .jpg, .gif, .png, .pdf, .txt, .csv, .doc, .docx, .xls, .xlsx, .ppt, .pptx &amp; .vcf file formats | 

### Return type

[**UploadMessageAttachmentResponse**](UploadMessageAttachmentResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
