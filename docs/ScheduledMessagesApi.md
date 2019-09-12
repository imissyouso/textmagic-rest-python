# TextMagic.ScheduledMessagesApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_scheduled_message**](ScheduledMessagesApi.md#delete_scheduled_message) | **DELETE** /api/v2/schedules/{id} | Delete a message session, together with all nested messages.
[**delete_scheduled_messages_bulk**](ScheduledMessagesApi.md#delete_scheduled_messages_bulk) | **POST** /api/v2/schedules/delete | Delete scheduled messages by given ID(s) or delete all scheduled messages.
[**get_all_scheduled_messages**](ScheduledMessagesApi.md#get_all_scheduled_messages) | **GET** /api/v2/schedules | Get all scheduled messages.
[**get_scheduled_message**](ScheduledMessagesApi.md#get_scheduled_message) | **GET** /api/v2/schedules/{id} | Get message schedule.
[**search_scheduled_messages**](ScheduledMessagesApi.md#search_scheduled_messages) | **GET** /api/v2/schedules/search | Find scheduled messages by given parameters.


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
api_instance = TextMagic.ScheduledMessagesApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a message session, together with all nested messages.
    api_instance.delete_scheduled_message(id)
except ApiException as e:
    print("Exception when calling ScheduledMessagesApi->delete_scheduled_message: %s\n" % e)
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
api_instance = TextMagic.ScheduledMessagesApi(TextMagic.ApiClient(configuration))
delete_scheduled_messages_bulk_input_object = TextMagic.DeleteScheduledMessagesBulkInputObject() # DeleteScheduledMessagesBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete scheduled messages by given ID(s) or delete all scheduled messages.
    api_instance.delete_scheduled_messages_bulk(delete_scheduled_messages_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling ScheduledMessagesApi->delete_scheduled_messages_bulk: %s\n" % e)
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

# **get_all_scheduled_messages**
> dict(str, object) get_all_scheduled_messages(page=page, limit=limit, status=status, order_by=order_by, direction=direction)

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
api_instance = TextMagic.ScheduledMessagesApi(TextMagic.ApiClient(configuration))
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
    print("Exception when calling ScheduledMessagesApi->get_all_scheduled_messages: %s\n" % e)
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

**dict(str, object)**

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
api_instance = TextMagic.ScheduledMessagesApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get message schedule.
    api_response = api_instance.get_scheduled_message(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledMessagesApi->get_scheduled_message: %s\n" % e)
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

# **search_scheduled_messages**
> dict(str, object) search_scheduled_messages(page=page, limit=limit, query=query, ids=ids, status=status, order_by=order_by, direction=direction)

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
api_instance = TextMagic.ScheduledMessagesApi(TextMagic.ApiClient(configuration))
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
    print("Exception when calling ScheduledMessagesApi->search_scheduled_messages: %s\n" % e)
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

**dict(str, object)**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

