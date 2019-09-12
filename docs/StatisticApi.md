# TextMagic.StatisticApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_messaging_counters**](StatisticApi.md#get_messaging_counters) | **GET** /api/v2/stats/messaging/data | Return counters for messaging data views.
[**get_messaging_stat**](StatisticApi.md#get_messaging_stat) | **GET** /api/v2/stats/messaging | Return messaging statistics.


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
api_instance = TextMagic.StatisticApi(TextMagic.ApiClient(configuration))

try:
    # Return counters for messaging data views.
    api_response = api_instance.get_messaging_counters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticApi->get_messaging_counters: %s\n" % e)
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
api_instance = TextMagic.StatisticApi(TextMagic.ApiClient(configuration))
by = 'off' # str | Group results by specified period: off, day, month or year. Default is off (optional) (default to off)
start = 56 # int | Start date in unix timestamp format. Default is 7 days ago (optional)
end = 'end_example' # str | End date in unix timestamp format. Default is now (optional)

try:
    # Return messaging statistics.
    api_response = api_instance.get_messaging_stat(by=by, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticApi->get_messaging_stat: %s\n" % e)
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

