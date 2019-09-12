# TextMagic.CallsApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_calls_prices**](CallsApi.md#get_calls_prices) | **GET** /api/v2/calls/price | Check pricing for a inbound/outbound call.
[**get_forwarded_calls**](CallsApi.md#get_forwarded_calls) | **GET** /api/v2/calls | Get all forwarded calls.


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
api_instance = TextMagic.CallsApi(TextMagic.ApiClient(configuration))

try:
    # Check pricing for a inbound/outbound call.
    api_response = api_instance.get_calls_prices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->get_calls_prices: %s\n" % e)
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

# **get_forwarded_calls**
> dict(str, object) get_forwarded_calls(page=page, limit=limit)

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
api_instance = TextMagic.CallsApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Get all forwarded calls.
    api_response = api_instance.get_forwarded_calls(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->get_forwarded_calls: %s\n" % e)
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

