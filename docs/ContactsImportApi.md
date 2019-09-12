# TextMagic.ContactsImportApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_contact_import_session_progress**](ContactsImportApi.md#get_contact_import_session_progress) | **GET** /api/v2/contacts/import/progress/{id} | Get contact import session progress.


# **get_contact_import_session_progress**
> GetContactImportSessionProgressResponse get_contact_import_session_progress(id)

Get contact import session progress.

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
api_instance = TextMagic.ContactsImportApi(TextMagic.ApiClient(configuration))
id = 56 # int | 

try:
    # Get contact import session progress.
    api_response = api_instance.get_contact_import_session_progress(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsImportApi->get_contact_import_session_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetContactImportSessionProgressResponse**](GetContactImportSessionProgressResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

