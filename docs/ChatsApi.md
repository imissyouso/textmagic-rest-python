# TextMagic.ChatsApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_chats_bulk**](ChatsApi.md#close_chats_bulk) | **POST** /api/v2/chats/close/bulk | Close chats by chat ids or close all chats
[**close_read_chats**](ChatsApi.md#close_read_chats) | **POST** /api/v2/chats/close/read | Close all chats that have no unread messages.
[**delete_chat_messages**](ChatsApi.md#delete_chat_messages) | **POST** /api/v2/chats/{id}/messages/delete | Delete messages from chat by given messages ID(s).
[**delete_chats_bulk**](ChatsApi.md#delete_chats_bulk) | **POST** /api/v2/chats/delete | Delete chats by given ID(s) or delete all chats.
[**get_all_chats**](ChatsApi.md#get_all_chats) | **GET** /api/v2/chats | Get all user chats.
[**get_chat**](ChatsApi.md#get_chat) | **GET** /api/v2/chats/{id} | Get a single chat.
[**get_chat_by_phone**](ChatsApi.md#get_chat_by_phone) | **GET** /api/v2/chats/{phone}/by/phone | Find chats by phone.
[**get_chat_messages**](ChatsApi.md#get_chat_messages) | **GET** /api/v2/chats/{id}/message | Fetch messages from chat with specified chat id.
[**get_unread_messages_total**](ChatsApi.md#get_unread_messages_total) | **GET** /api/v2/chats/unread/count | Get total amount of unread messages in the current user chats.
[**mark_chats_read_bulk**](ChatsApi.md#mark_chats_read_bulk) | **POST** /api/v2/chats/read/bulk | Mark several chats as read by chat ids or mark all chats as read
[**mark_chats_unread_bulk**](ChatsApi.md#mark_chats_unread_bulk) | **POST** /api/v2/chats/unread/bulk | Mark several chats as UNread by chat ids or mark all chats as UNread
[**mute_chat**](ChatsApi.md#mute_chat) | **POST** /api/v2/chats/mute | Set mute mode.
[**mute_chats_bulk**](ChatsApi.md#mute_chats_bulk) | **POST** /api/v2/chats/mute/bulk | Mute several chats by chat ids or mute all chats
[**reopen_chats_bulk**](ChatsApi.md#reopen_chats_bulk) | **POST** /api/v2/chats/reopen/bulk | Reopen chats by chat ids or reopen all chats
[**search_chats**](ChatsApi.md#search_chats) | **GET** /api/v2/chats/search | Find chats by inbound or outbound messages text.
[**search_chats_by_ids**](ChatsApi.md#search_chats_by_ids) | **GET** /api/v2/chats/search/ids | Find chats by IDs.
[**search_chats_by_receipent**](ChatsApi.md#search_chats_by_receipent) | **GET** /api/v2/chats/search/recipients | Find chats by recipient (contact, list name or phone number).
[**set_chat_status**](ChatsApi.md#set_chat_status) | **POST** /api/v2/chats/status | Set status of the chat given by ID.
[**unmute_chats_bulk**](ChatsApi.md#unmute_chats_bulk) | **POST** /api/v2/chats/unmute/bulk | Unmute several chats by chat ids or unmute all chats


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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))
close_chats_bulk_input_object = TextMagic.CloseChatsBulkInputObject() # CloseChatsBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Close chats by chat ids or close all chats
    api_instance.close_chats_bulk(close_chats_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling ChatsApi->close_chats_bulk: %s\n" % e)
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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))

try:
    # Close all chats that have no unread messages.
    api_instance.close_read_chats()
except ApiException as e:
    print("Exception when calling ChatsApi->close_read_chats: %s\n" % e)
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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))
delete_chat_messages_bulk_input_object = TextMagic.DeleteChatMessagesBulkInputObject() # DeleteChatMessagesBulkInputObject | 
id = 1 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete messages from chat by given messages ID(s).
    api_instance.delete_chat_messages(delete_chat_messages_bulk_input_object, id, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling ChatsApi->delete_chat_messages: %s\n" % e)
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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))
delete_chats_bulk_input_object = TextMagic.DeleteChatsBulkInputObject() # DeleteChatsBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete chats by given ID(s) or delete all chats.
    api_instance.delete_chats_bulk(delete_chats_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling ChatsApi->delete_chats_bulk: %s\n" % e)
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

# **get_all_chats**
> dict(str, object) get_all_chats(status=status, page=page, limit=limit, order_by=order_by, voice=voice, flat=flat)

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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))
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
    print("Exception when calling ChatsApi->get_all_chats: %s\n" % e)
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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single chat.
    api_response = api_instance.get_chat(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatsApi->get_chat: %s\n" % e)
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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))
phone = 'phone_example' # str | 
upsert = 0 # int | Create a new chat if not found (optional) (default to 0)
reopen = 0 # int | Reopen chat if found or do not change status (optional) (default to 0)

try:
    # Find chats by phone.
    api_response = api_instance.get_chat_by_phone(phone, upsert=upsert, reopen=reopen)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatsApi->get_chat_by_phone: %s\n" % e)
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
> dict(str, object) get_chat_messages(id, page=page, limit=limit, query=query, start=start, end=end, direction=direction, voice=voice)

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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))
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
    print("Exception when calling ChatsApi->get_chat_messages: %s\n" % e)
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

**dict(str, object)**

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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))

try:
    # Get total amount of unread messages in the current user chats.
    api_response = api_instance.get_unread_messages_total()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatsApi->get_unread_messages_total: %s\n" % e)
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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))
mark_chats_read_bulk_input_object = TextMagic.MarkChatsReadBulkInputObject() # MarkChatsReadBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Mark several chats as read by chat ids or mark all chats as read
    api_instance.mark_chats_read_bulk(mark_chats_read_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling ChatsApi->mark_chats_read_bulk: %s\n" % e)
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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))
mark_chats_unread_bulk_input_object = TextMagic.MarkChatsUnreadBulkInputObject() # MarkChatsUnreadBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Mark several chats as UNread by chat ids or mark all chats as UNread
    api_instance.mark_chats_unread_bulk(mark_chats_unread_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling ChatsApi->mark_chats_unread_bulk: %s\n" % e)
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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))
mute_chat_input_object = TextMagic.MuteChatInputObject() # MuteChatInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Set mute mode.
    api_response = api_instance.mute_chat(mute_chat_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatsApi->mute_chat: %s\n" % e)
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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))
mute_chats_bulk_input_object = TextMagic.MuteChatsBulkInputObject() # MuteChatsBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Mute several chats by chat ids or mute all chats
    api_instance.mute_chats_bulk(mute_chats_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling ChatsApi->mute_chats_bulk: %s\n" % e)
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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))
reopen_chats_bulk_input_object = TextMagic.ReopenChatsBulkInputObject() # ReopenChatsBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Reopen chats by chat ids or reopen all chats
    api_instance.reopen_chats_bulk(reopen_chats_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling ChatsApi->reopen_chats_bulk: %s\n" % e)
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

# **search_chats**
> object search_chats(page=page, limit=limit, query=query)

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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
query = 'query_example' # str | Find chats by specified search query (optional)

try:
    # Find chats by inbound or outbound messages text.
    api_response = api_instance.search_chats(page=page, limit=limit, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatsApi->search_chats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **query** | **str**| Find chats by specified search query | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_chats_by_ids**
> dict(str, object) search_chats_by_ids(page=page, limit=limit, ids=ids)

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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
ids = 'ids_example' # str | Find chats by ID(s) (optional)

try:
    # Find chats by IDs.
    api_response = api_instance.search_chats_by_ids(page=page, limit=limit, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatsApi->search_chats_by_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **ids** | **str**| Find chats by ID(s) | [optional] 

### Return type

**dict(str, object)**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_chats_by_receipent**
> dict(str, object) search_chats_by_receipent(page=page, limit=limit, query=query, order_by=order_by)

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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
query = 'query_example' # str | Find chats by specified search query (optional)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)

try:
    # Find chats by recipient (contact, list name or phone number).
    api_response = api_instance.search_chats_by_receipent(page=page, limit=limit, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatsApi->search_chats_by_receipent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **query** | **str**| Find chats by specified search query | [optional] 
 **order_by** | **str**| Order results by some field. Default is id | [optional] [default to id]

### Return type

**dict(str, object)**

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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))
set_chat_status_input_object = TextMagic.SetChatStatusInputObject() # SetChatStatusInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Set status of the chat given by ID.
    api_response = api_instance.set_chat_status(set_chat_status_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatsApi->set_chat_status: %s\n" % e)
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
api_instance = TextMagic.ChatsApi(TextMagic.ApiClient(configuration))
unmute_chats_bulk_input_object = TextMagic.UnmuteChatsBulkInputObject() # UnmuteChatsBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Unmute several chats by chat ids or unmute all chats
    api_instance.unmute_chats_bulk(unmute_chats_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling ChatsApi->unmute_chats_bulk: %s\n" % e)
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

