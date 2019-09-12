# TextMagic.OutboundMessageSessionsApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_message_session**](OutboundMessageSessionsApi.md#delete_message_session) | **DELETE** /api/v2/sessions/{id} | Delete a message session, together with all nested messages.
[**delete_message_sessions_bulk**](OutboundMessageSessionsApi.md#delete_message_sessions_bulk) | **POST** /api/v2/sessions/delete | Delete messages sessions, together with all nested messages, by given ID(s) or delete all messages sessions.
[**get_all_message_sessions**](OutboundMessageSessionsApi.md#get_all_message_sessions) | **GET** /api/v2/sessions | Get all message sending sessions.
[**get_message_session**](OutboundMessageSessionsApi.md#get_message_session) | **GET** /api/v2/sessions/{id} | Get a message session.
[**get_message_session_stat**](OutboundMessageSessionsApi.md#get_message_session_stat) | **GET** /api/v2/sessions/{id}/stat | Get sending session statistics.
[**get_messages_by_session_id**](OutboundMessageSessionsApi.md#get_messages_by_session_id) | **GET** /api/v2/sessions/{id}/messages | Fetch messages by given session id.


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
api_instance = TextMagic.OutboundMessageSessionsApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a message session, together with all nested messages.
    api_instance.delete_message_session(id)
except ApiException as e:
    print("Exception when calling OutboundMessageSessionsApi->delete_message_session: %s\n" % e)
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
api_instance = TextMagic.OutboundMessageSessionsApi(TextMagic.ApiClient(configuration))
delete_message_sessions_bulk_input_object = TextMagic.DeleteMessageSessionsBulkInputObject() # DeleteMessageSessionsBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete messages sessions, together with all nested messages, by given ID(s) or delete all messages sessions.
    api_instance.delete_message_sessions_bulk(delete_message_sessions_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling OutboundMessageSessionsApi->delete_message_sessions_bulk: %s\n" % e)
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

# **get_all_message_sessions**
> dict(str, object) get_all_message_sessions(page=page, limit=limit)

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
api_instance = TextMagic.OutboundMessageSessionsApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Get all message sending sessions.
    api_response = api_instance.get_all_message_sessions(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundMessageSessionsApi->get_all_message_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]

### Return type

**dict(str, object)**

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
api_instance = TextMagic.OutboundMessageSessionsApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a message session.
    api_response = api_instance.get_message_session(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundMessageSessionsApi->get_message_session: %s\n" % e)
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
api_instance = TextMagic.OutboundMessageSessionsApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
include_deleted = 0 # int | Search also in deleted messages (optional) (default to 0)

try:
    # Get sending session statistics.
    api_response = api_instance.get_message_session_stat(id, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundMessageSessionsApi->get_message_session_stat: %s\n" % e)
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
> dict(str, object) get_messages_by_session_id(id, page=page, limit=limit, statuses=statuses, include_deleted=include_deleted)

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
api_instance = TextMagic.OutboundMessageSessionsApi(TextMagic.ApiClient(configuration))
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
    print("Exception when calling OutboundMessageSessionsApi->get_messages_by_session_id: %s\n" % e)
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

**dict(str, object)**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

