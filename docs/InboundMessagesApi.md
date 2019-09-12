# TextMagic.InboundMessagesApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_inbound_message**](InboundMessagesApi.md#delete_inbound_message) | **DELETE** /api/v2/replies/{id} | Delete the incoming message.
[**delete_inbound_messages_bulk**](InboundMessagesApi.md#delete_inbound_messages_bulk) | **POST** /api/v2/replies/delete | Delete inbound messages by given ID(s) or delete all inbound messages.
[**get_all_inbound_messages**](InboundMessagesApi.md#get_all_inbound_messages) | **GET** /api/v2/replies | Get all inbox messages.
[**get_inbound_message**](InboundMessagesApi.md#get_inbound_message) | **GET** /api/v2/replies/{id} | Get a single inbox message.
[**search_inbound_messages**](InboundMessagesApi.md#search_inbound_messages) | **GET** /api/v2/replies/search | Find inbound messages by given parameters.


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
api_instance = TextMagic.InboundMessagesApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete the incoming message.
    api_instance.delete_inbound_message(id)
except ApiException as e:
    print("Exception when calling InboundMessagesApi->delete_inbound_message: %s\n" % e)
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
api_instance = TextMagic.InboundMessagesApi(TextMagic.ApiClient(configuration))
delete_inbound_messages_bulk_input_object = TextMagic.DeleteInboundMessagesBulkInputObject() # DeleteInboundMessagesBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete inbound messages by given ID(s) or delete all inbound messages.
    api_instance.delete_inbound_messages_bulk(delete_inbound_messages_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling InboundMessagesApi->delete_inbound_messages_bulk: %s\n" % e)
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

# **get_all_inbound_messages**
> dict(str, object) get_all_inbound_messages(page=page, limit=limit, order_by=order_by, direction=direction)

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
api_instance = TextMagic.InboundMessagesApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)

try:
    # Get all inbox messages.
    api_response = api_instance.get_all_inbound_messages(page=page, limit=limit, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundMessagesApi->get_all_inbound_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
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
api_instance = TextMagic.InboundMessagesApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single inbox message.
    api_response = api_instance.get_inbound_message(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundMessagesApi->get_inbound_message: %s\n" % e)
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

# **search_inbound_messages**
> dict(str, object) search_inbound_messages(page=page, limit=limit, ids=ids, query=query, order_by=order_by, direction=direction, expand=expand)

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
api_instance = TextMagic.InboundMessagesApi(TextMagic.ApiClient(configuration))
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
    print("Exception when calling InboundMessagesApi->search_inbound_messages: %s\n" % e)
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

**dict(str, object)**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

