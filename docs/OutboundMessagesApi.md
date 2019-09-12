# TextMagic.OutboundMessagesApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_all_outbound_messages**](OutboundMessagesApi.md#delete_all_outbound_messages) | **DELETE** /api/v2/message/all | Delete all messages
[**delete_outbound_message**](OutboundMessagesApi.md#delete_outbound_message) | **DELETE** /api/v2/messages/{id} | Delete message
[**delete_outbound_messages_bulk**](OutboundMessagesApi.md#delete_outbound_messages_bulk) | **POST** /api/v2/messages/delete | Delete messages by IDs
[**get_all_outbound_messages**](OutboundMessagesApi.md#get_all_outbound_messages) | **GET** /api/v2/messages | Get all messages
[**get_message_preview**](OutboundMessagesApi.md#get_message_preview) | **GET** /api/v2/messages/preview | Preview message
[**get_message_price**](OutboundMessagesApi.md#get_message_price) | **GET** /api/v2/messages/price | Check price
[**get_message_prices**](OutboundMessagesApi.md#get_message_prices) | **GET** /api/v2/messages/prices | Get pricing
[**get_outbound_message**](OutboundMessagesApi.md#get_outbound_message) | **GET** /api/v2/messages/{id} | Get a single message
[**get_outbound_messages_history**](OutboundMessagesApi.md#get_outbound_messages_history) | **GET** /api/v2/history | Get history
[**search_outbound_messages**](OutboundMessagesApi.md#search_outbound_messages) | **GET** /api/v2/messages/search | Find messages
[**send_message**](OutboundMessagesApi.md#send_message) | **POST** /api/v2/messages | Send message
[**upload_message_attachment**](OutboundMessagesApi.md#upload_message_attachment) | **POST** /api/v2/messages/attachment | Upload message attachment


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
api_instance = TextMagic.OutboundMessagesApi(TextMagic.ApiClient(configuration))

try:
    # Delete all messages
    api_instance.delete_all_outbound_messages()
except ApiException as e:
    print("Exception when calling OutboundMessagesApi->delete_all_outbound_messages: %s\n" % e)
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
api_instance = TextMagic.OutboundMessagesApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete message
    api_instance.delete_outbound_message(id)
except ApiException as e:
    print("Exception when calling OutboundMessagesApi->delete_outbound_message: %s\n" % e)
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
api_instance = TextMagic.OutboundMessagesApi(TextMagic.ApiClient(configuration))
delete_outbound_messages_bulk_input_object = TextMagic.DeleteOutboundMessagesBulkInputObject() # DeleteOutboundMessagesBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete messages by IDs
    api_instance.delete_outbound_messages_bulk(delete_outbound_messages_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling OutboundMessagesApi->delete_outbound_messages_bulk: %s\n" % e)
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

# **get_all_outbound_messages**
> dict(str, object) get_all_outbound_messages(page=page, limit=limit, last_id=last_id)

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
api_instance = TextMagic.OutboundMessagesApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
last_id = 56 # int | Filter results by ID, selecting all values lesser than the specified ID. Note that \\'page\\' parameter is ignored when \\'lastId\\' is specified (optional)

try:
    # Get all messages
    api_response = api_instance.get_all_outbound_messages(page=page, limit=limit, last_id=last_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundMessagesApi->get_all_outbound_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **last_id** | **int**| Filter results by ID, selecting all values lesser than the specified ID. Note that \\&#39;page\\&#39; parameter is ignored when \\&#39;lastId\\&#39; is specified | [optional] 

### Return type

**dict(str, object)**

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
api_instance = TextMagic.OutboundMessagesApi(TextMagic.ApiClient(configuration))
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
    print("Exception when calling OutboundMessagesApi->get_message_preview: %s\n" % e)
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
api_instance = TextMagic.OutboundMessagesApi(TextMagic.ApiClient(configuration))
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
    print("Exception when calling OutboundMessagesApi->get_message_price: %s\n" % e)
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
api_instance = TextMagic.OutboundMessagesApi(TextMagic.ApiClient(configuration))

try:
    # Get pricing
    api_response = api_instance.get_message_prices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundMessagesApi->get_message_prices: %s\n" % e)
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
api_instance = TextMagic.OutboundMessagesApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single message
    api_response = api_instance.get_outbound_message(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundMessagesApi->get_outbound_message: %s\n" % e)
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
> dict(str, object) get_outbound_messages_history(limit=limit, last_id=last_id, query=query, order_by=order_by, direction=direction)

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
api_instance = TextMagic.OutboundMessagesApi(TextMagic.ApiClient(configuration))
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
    print("Exception when calling OutboundMessagesApi->get_outbound_messages_history: %s\n" % e)
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

**dict(str, object)**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_outbound_messages**
> dict(str, object) search_outbound_messages(page=page, limit=limit, last_id=last_id, ids=ids, session_id=session_id, statuses=statuses, include_deleted=include_deleted, query=query)

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
api_instance = TextMagic.OutboundMessagesApi(TextMagic.ApiClient(configuration))
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
    print("Exception when calling OutboundMessagesApi->search_outbound_messages: %s\n" % e)
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

**dict(str, object)**

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
api_instance = TextMagic.OutboundMessagesApi(TextMagic.ApiClient(configuration))
send_message_input_object = TextMagic.SendMessageInputObject() # SendMessageInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Send message
    api_response = api_instance.send_message(send_message_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundMessagesApi->send_message: %s\n" % e)
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
api_instance = TextMagic.OutboundMessagesApi(TextMagic.ApiClient(configuration))
file = '/path/to/file.txt' # file | Attachment. Supports .jpg, .gif, .png, .pdf, .txt, .csv, .doc, .docx, .xls, .xlsx, .ppt, .pptx & .vcf file formats

try:
    # Upload message attachment
    api_response = api_instance.upload_message_attachment(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundMessagesApi->upload_message_attachment: %s\n" % e)
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

