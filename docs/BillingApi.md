# TextMagic.BillingApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invoices**](BillingApi.md#get_invoices) | **GET** /api/v2/invoices | Return account invoices.
[**get_spending_stat**](BillingApi.md#get_spending_stat) | **GET** /api/v2/stats/spending | Return account spending statistics.


# **get_invoices**
> dict(str, object) get_invoices(page=page, limit=limit)

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
api_instance = TextMagic.BillingApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Return account invoices.
    api_response = api_instance.get_invoices(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_invoices: %s\n" % e)
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

# **get_spending_stat**
> dict(str, object) get_spending_stat(page=page, limit=limit, start=start, end=end)

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
api_instance = TextMagic.BillingApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
start = 56 # int | Optional. Start date in unix timestamp format. Default is 7 days ago (optional)
end = 56 # int | Optional. End date in unix timestamp format. Default is now (optional)

try:
    # Return account spending statistics.
    api_response = api_instance.get_spending_stat(page=page, limit=limit, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_spending_stat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **start** | **int**| Optional. Start date in unix timestamp format. Default is 7 days ago | [optional] 
 **end** | **int**| Optional. End date in unix timestamp format. Default is now | [optional] 

### Return type

**dict(str, object)**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

