# TextMagic.BulkMessageSessionsApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_bulk_sessions**](BulkMessageSessionsApi.md#get_all_bulk_sessions) | **GET** /api/v2/bulks | Get all bulk sending sessions.
[**get_bulk_session**](BulkMessageSessionsApi.md#get_bulk_session) | **GET** /api/v2/bulks/{id} | Get bulk message session status.


# **get_all_bulk_sessions**
> dict(str, object) get_all_bulk_sessions(page=page, limit=limit)

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
api_instance = TextMagic.BulkMessageSessionsApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Get all bulk sending sessions.
    api_response = api_instance.get_all_bulk_sessions(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkMessageSessionsApi->get_all_bulk_sessions: %s\n" % e)
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
api_instance = TextMagic.BulkMessageSessionsApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get bulk message session status.
    api_response = api_instance.get_bulk_session(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkMessageSessionsApi->get_bulk_session: %s\n" % e)
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

