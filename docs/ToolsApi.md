# TextMagic.ToolsApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**do_carrier_lookup**](ToolsApi.md#do_carrier_lookup) | **GET** /api/v2/lookups/{phone} | Carrier Lookup
[**do_email_lookup**](ToolsApi.md#do_email_lookup) | **GET** /api/v2/email-lookups/{email} | Validate Email address using Email Lookup tool


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
api_instance = TextMagic.ToolsApi(TextMagic.ApiClient(configuration))
phone = '\"1-541-754-3010\"' # str | 
country = 'US' # str | Country code for local formatted numbers (optional) (default to US)

try:
    # Carrier Lookup
    api_response = api_instance.do_carrier_lookup(phone, country=country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolsApi->do_carrier_lookup: %s\n" % e)
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
api_instance = TextMagic.ToolsApi(TextMagic.ApiClient(configuration))
email = '\"andrey.v@textmagic.biz\"' # str | 

try:
    # Validate Email address using Email Lookup tool
    api_response = api_instance.do_email_lookup(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolsApi->do_email_lookup: %s\n" % e)
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

