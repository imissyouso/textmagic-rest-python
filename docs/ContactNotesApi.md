# TextMagic.ContactNotesApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact_note**](ContactNotesApi.md#create_contact_note) | **POST** /api/v2/contacts/{id}/notes | Create a new contact note.
[**delete_contact_note**](ContactNotesApi.md#delete_contact_note) | **DELETE** /api/v2/notes/{id} | Delete a single contact note.
[**delete_contact_notes_bulk**](ContactNotesApi.md#delete_contact_notes_bulk) | **POST** /api/v2/contacts/{id}/notes/delete | Delete contact note by given ID(s) or delete all contact notes.
[**get_contact_note**](ContactNotesApi.md#get_contact_note) | **GET** /api/v2/notes/{id} | Get a single contact note.
[**get_contact_notes**](ContactNotesApi.md#get_contact_notes) | **GET** /api/v2/contacts/{id}/notes | Fetch notes assigned to the given contact.
[**update_contact_note**](ContactNotesApi.md#update_contact_note) | **PUT** /api/v2/notes/{id} | Update existing contact note.


# **create_contact_note**
> ResourceLinkResponse create_contact_note(create_contact_note_input_object, id, x_ignore_null_values=x_ignore_null_values)

Create a new contact note.

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
api_instance = TextMagic.ContactNotesApi(TextMagic.ApiClient(configuration))
create_contact_note_input_object = TextMagic.CreateContactNoteInputObject() # CreateContactNoteInputObject | 
id = 56 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Create a new contact note.
    api_response = api_instance.create_contact_note(create_contact_note_input_object, id, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactNotesApi->create_contact_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_contact_note_input_object** | [**CreateContactNoteInputObject**](CreateContactNoteInputObject.md)|  | 
 **id** | **int**|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_note**
> delete_contact_note(id)

Delete a single contact note.

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
api_instance = TextMagic.ContactNotesApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a single contact note.
    api_instance.delete_contact_note(id)
except ApiException as e:
    print("Exception when calling ContactNotesApi->delete_contact_note: %s\n" % e)
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

# **delete_contact_notes_bulk**
> delete_contact_notes_bulk(id, delete_contact_notes_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Delete contact note by given ID(s) or delete all contact notes.

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
api_instance = TextMagic.ContactNotesApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
delete_contact_notes_bulk_input_object = TextMagic.DeleteContactNotesBulkInputObject() # DeleteContactNotesBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete contact note by given ID(s) or delete all contact notes.
    api_instance.delete_contact_notes_bulk(id, delete_contact_notes_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling ContactNotesApi->delete_contact_notes_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **delete_contact_notes_bulk_input_object** | [**DeleteContactNotesBulkInputObject**](DeleteContactNotesBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_note**
> ContactNote get_contact_note(id)

Get a single contact note.

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
api_instance = TextMagic.ContactNotesApi(TextMagic.ApiClient(configuration))
id = 56 # int | 

try:
    # Get a single contact note.
    api_response = api_instance.get_contact_note(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactNotesApi->get_contact_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ContactNote**](ContactNote.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_notes**
> dict(str, object) get_contact_notes(id, page=page, limit=limit)

Fetch notes assigned to the given contact.

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
api_instance = TextMagic.ContactNotesApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Fetch notes assigned to the given contact.
    api_response = api_instance.get_contact_notes(id, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactNotesApi->get_contact_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
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

# **update_contact_note**
> ResourceLinkResponse update_contact_note(update_contact_note_input_object, id, x_ignore_null_values=x_ignore_null_values)

Update existing contact note.

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
api_instance = TextMagic.ContactNotesApi(TextMagic.ApiClient(configuration))
update_contact_note_input_object = TextMagic.UpdateContactNoteInputObject() # UpdateContactNoteInputObject | 
id = 1 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update existing contact note.
    api_response = api_instance.update_contact_note(update_contact_note_input_object, id, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactNotesApi->update_contact_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_contact_note_input_object** | [**UpdateContactNoteInputObject**](UpdateContactNoteInputObject.md)|  | 
 **id** | **int**|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

