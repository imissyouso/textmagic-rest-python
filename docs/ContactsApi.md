# TextMagic.ContactsApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**block_contact**](ContactsApi.md#block_contact) | **POST** /api/v2/contacts/block | Block contact from inbound and outbound communication by phone number.
[**create_contact**](ContactsApi.md#create_contact) | **POST** /api/v2/contacts | Create a new contact from the submitted data.
[**delete_all_contacts**](ContactsApi.md#delete_all_contacts) | **DELETE** /api/v2/contact/all | Delete all contacts.
[**delete_contact**](ContactsApi.md#delete_contact) | **DELETE** /api/v2/contacts/{id} | Delete a single contact.
[**delete_contact_avatar**](ContactsApi.md#delete_contact_avatar) | **DELETE** /api/v2/contacts/{id}/avatar | Delete an avatar for the contact.
[**delete_contacts_by_ids**](ContactsApi.md#delete_contacts_by_ids) | **POST** /api/v2/contacts/delete | Delete contact by given ID(s) or delete all contacts.
[**get_blocked_contacts**](ContactsApi.md#get_blocked_contacts) | **GET** /api/v2/contacts/block/list | Get blocked contacts.
[**get_contact**](ContactsApi.md#get_contact) | **GET** /api/v2/contacts/{id} | Get a single contact.
[**get_contact_by_phone**](ContactsApi.md#get_contact_by_phone) | **GET** /api/v2/contacts/phone/{phone} | Get a single contact by phone number.
[**get_contact_if_blocked**](ContactsApi.md#get_contact_if_blocked) | **GET** /api/v2/contacts/block/phone | Check is that phone number blocked
[**get_contacts**](ContactsApi.md#get_contacts) | **GET** /api/v2/contacts | Get all user contacts.
[**get_contacts_autocomplete**](ContactsApi.md#get_contacts_autocomplete) | **GET** /api/v2/contacts/autocomplete | Get contacts autocomplete suggestions by given search term.
[**get_favourites**](ContactsApi.md#get_favourites) | **GET** /api/v2/contacts/favorite | Get favorite contacts and lists.
[**get_unsubscribed_contact**](ContactsApi.md#get_unsubscribed_contact) | **GET** /api/v2/unsubscribers/{id} | Get a single unsubscribed contact.
[**get_unsubscribers**](ContactsApi.md#get_unsubscribers) | **GET** /api/v2/unsubscribers | Get all contact have unsubscribed from your communication.
[**search_contacts**](ContactsApi.md#search_contacts) | **GET** /api/v2/contacts/search | Find user contacts by given parameters.
[**unblock_contact**](ContactsApi.md#unblock_contact) | **POST** /api/v2/contacts/unblock | Unblock contact by phone number.
[**unblock_contacts_bulk**](ContactsApi.md#unblock_contacts_bulk) | **POST** /api/v2/contacts/unblock/bulk | Unblock several contacts by blocked contact ids or unblock all contacts
[**unsubscribe_contact**](ContactsApi.md#unsubscribe_contact) | **POST** /api/v2/unsubscribers | Unsubscribe contact from your communication by phone number.
[**update_contact**](ContactsApi.md#update_contact) | **PUT** /api/v2/contacts/{id} | Update existing contact.
[**upload_contact_avatar**](ContactsApi.md#upload_contact_avatar) | **POST** /api/v2/contacts/{id}/avatar | Add an avatar for the contact.


# **block_contact**
> ResourceLinkResponse block_contact(block_contact_input_object, x_ignore_null_values=x_ignore_null_values)

Block contact from inbound and outbound communication by phone number.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
block_contact_input_object = TextMagic.BlockContactInputObject() # BlockContactInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Block contact from inbound and outbound communication by phone number.
    api_response = api_instance.block_contact(block_contact_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->block_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_contact_input_object** | [**BlockContactInputObject**](BlockContactInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact**
> ResourceLinkResponse create_contact(create_contact_input_object, x_ignore_null_values=x_ignore_null_values)

Create a new contact from the submitted data.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
create_contact_input_object = TextMagic.CreateContactInputObject() # CreateContactInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Create a new contact from the submitted data.
    api_response = api_instance.create_contact(create_contact_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->create_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_contact_input_object** | [**CreateContactInputObject**](CreateContactInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_contacts**
> delete_all_contacts()

Delete all contacts.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))

try:
    # Delete all contacts.
    api_instance.delete_all_contacts()
except ApiException as e:
    print("Exception when calling ContactsApi->delete_all_contacts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> delete_contact(id)

Delete a single contact.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a single contact.
    api_instance.delete_contact(id)
except ApiException as e:
    print("Exception when calling ContactsApi->delete_contact: %s\n" % e)
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

# **delete_contact_avatar**
> delete_contact_avatar(id)

Delete an avatar for the contact.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete an avatar for the contact.
    api_instance.delete_contact_avatar(id)
except ApiException as e:
    print("Exception when calling ContactsApi->delete_contact_avatar: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contacts_by_ids**
> delete_contacts_by_ids(delete_contacts_by_ids_input_object, x_ignore_null_values=x_ignore_null_values)

Delete contact by given ID(s) or delete all contacts.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
delete_contacts_by_ids_input_object = TextMagic.DeleteContactsByIdsInputObject() # DeleteContactsByIdsInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete contact by given ID(s) or delete all contacts.
    api_instance.delete_contacts_by_ids(delete_contacts_by_ids_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling ContactsApi->delete_contacts_by_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_contacts_by_ids_input_object** | [**DeleteContactsByIdsInputObject**](DeleteContactsByIdsInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blocked_contacts**
> dict(str, object) get_blocked_contacts(page=page, limit=limit, query=query, order_by=order_by, direction=direction)

Get blocked contacts.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
query = 'query_example' # str | Find blocked contacts by specified search query (optional)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)

try:
    # Get blocked contacts.
    api_response = api_instance.get_blocked_contacts(page=page, limit=limit, query=query, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_blocked_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **query** | **str**| Find blocked contacts by specified search query | [optional] 
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

# **get_contact**
> Contact get_contact(id)

Get a single contact.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
id = 1 # int | The contact id

try:
    # Get a single contact.
    api_response = api_instance.get_contact(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The contact id | 

### Return type

[**Contact**](Contact.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_by_phone**
> Contact get_contact_by_phone(phone)

Get a single contact by phone number.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
phone = 'phone_example' # str | 

try:
    # Get a single contact by phone number.
    api_response = api_instance.get_contact_by_phone(phone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_contact_by_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_if_blocked**
> Contact get_contact_if_blocked(phone)

Check is that phone number blocked

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
phone = '9997339956475' # str | Phone number to check

try:
    # Check is that phone number blocked
    api_response = api_instance.get_contact_if_blocked(phone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_contact_if_blocked: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**| Phone number to check | 

### Return type

[**Contact**](Contact.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts**
> dict(str, object) get_contacts(page=page, limit=limit, shared=shared, order_by=order_by, direction=direction)

Get all user contacts.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
shared = 0 # int | Should shared contacts to be included (optional) (default to 0)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)

try:
    # Get all user contacts.
    api_response = api_instance.get_contacts(page=page, limit=limit, shared=shared, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **shared** | **int**| Should shared contacts to be included | [optional] [default to 0]
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

# **get_contacts_autocomplete**
> list[GetContactsAutocompleteResponse] get_contacts_autocomplete(query, limit=limit, lists=lists)

Get contacts autocomplete suggestions by given search term.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
query = '\"A\"' # str | Find recipients by specified search query
limit = 10 # int | How many results to return (optional) (default to 10)
lists = 0 # int | Should lists be returned or not (optional) (default to 0)

try:
    # Get contacts autocomplete suggestions by given search term.
    api_response = api_instance.get_contacts_autocomplete(query, limit=limit, lists=lists)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_contacts_autocomplete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Find recipients by specified search query | 
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **lists** | **int**| Should lists be returned or not | [optional] [default to 0]

### Return type

[**list[GetContactsAutocompleteResponse]**](GetContactsAutocompleteResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favourites**
> dict(str, object) get_favourites(page=page, limit=limit, query=query)

Get favorite contacts and lists.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
query = 'A' # str | Find contacts or lists by specified search query (optional) (default to A)

try:
    # Get favorite contacts and lists.
    api_response = api_instance.get_favourites(page=page, limit=limit, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_favourites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **query** | **str**| Find contacts or lists by specified search query | [optional] [default to A]

### Return type

**dict(str, object)**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unsubscribed_contact**
> UnsubscribedContact get_unsubscribed_contact(id)

Get a single unsubscribed contact.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single unsubscribed contact.
    api_response = api_instance.get_unsubscribed_contact(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_unsubscribed_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UnsubscribedContact**](UnsubscribedContact.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unsubscribers**
> dict(str, object) get_unsubscribers(page=page, limit=limit)

Get all contact have unsubscribed from your communication.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Get all contact have unsubscribed from your communication.
    api_response = api_instance.get_unsubscribers(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_unsubscribers: %s\n" % e)
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

# **search_contacts**
> dict(str, object) search_contacts(page=page, limit=limit, shared=shared, ids=ids, list_id=list_id, include_blocked=include_blocked, query=query, local=local, country=country, order_by=order_by, direction=direction)

Find user contacts by given parameters.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
shared = 0 # int | Should shared contacts to be included (optional) (default to 0)
ids = 'ids_example' # str | Find contact by ID(s) (optional)
list_id = 56 # int | Find contact by List ID (optional)
include_blocked = 56 # int | Should blocked contacts to be included (optional)
query = 'query_example' # str | Find contacts by specified search query (optional)
local = 0 # int | Treat phone number passed in 'query' field as local. Default is 0 (optional) (default to 0)
country = 'country_example' # str | 2-letter ISO country code for local phone numbers, used when 'local' is set to true. Default is account country (optional)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)

try:
    # Find user contacts by given parameters.
    api_response = api_instance.search_contacts(page=page, limit=limit, shared=shared, ids=ids, list_id=list_id, include_blocked=include_blocked, query=query, local=local, country=country, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->search_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **shared** | **int**| Should shared contacts to be included | [optional] [default to 0]
 **ids** | **str**| Find contact by ID(s) | [optional] 
 **list_id** | **int**| Find contact by List ID | [optional] 
 **include_blocked** | **int**| Should blocked contacts to be included | [optional] 
 **query** | **str**| Find contacts by specified search query | [optional] 
 **local** | **int**| Treat phone number passed in &#39;query&#39; field as local. Default is 0 | [optional] [default to 0]
 **country** | **str**| 2-letter ISO country code for local phone numbers, used when &#39;local&#39; is set to true. Default is account country | [optional] 
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

# **unblock_contact**
> unblock_contact(unblock_contact_input_object, x_ignore_null_values=x_ignore_null_values)

Unblock contact by phone number.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
unblock_contact_input_object = TextMagic.UnblockContactInputObject() # UnblockContactInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Unblock contact by phone number.
    api_instance.unblock_contact(unblock_contact_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling ContactsApi->unblock_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unblock_contact_input_object** | [**UnblockContactInputObject**](UnblockContactInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unblock_contacts_bulk**
> unblock_contacts_bulk(unblock_contacts_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Unblock several contacts by blocked contact ids or unblock all contacts

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
unblock_contacts_bulk_input_object = TextMagic.UnblockContactsBulkInputObject() # UnblockContactsBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Unblock several contacts by blocked contact ids or unblock all contacts
    api_instance.unblock_contacts_bulk(unblock_contacts_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling ContactsApi->unblock_contacts_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unblock_contacts_bulk_input_object** | [**UnblockContactsBulkInputObject**](UnblockContactsBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_contact**
> ResourceLinkResponse unsubscribe_contact(unsubscribe_contact_input_object, x_ignore_null_values=x_ignore_null_values)

Unsubscribe contact from your communication by phone number.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
unsubscribe_contact_input_object = TextMagic.UnsubscribeContactInputObject() # UnsubscribeContactInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Unsubscribe contact from your communication by phone number.
    api_response = api_instance.unsubscribe_contact(unsubscribe_contact_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->unsubscribe_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unsubscribe_contact_input_object** | [**UnsubscribeContactInputObject**](UnsubscribeContactInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> ResourceLinkResponse update_contact(update_contact_input_object, id, x_ignore_null_values=x_ignore_null_values)

Update existing contact.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
update_contact_input_object = TextMagic.UpdateContactInputObject() # UpdateContactInputObject | 
id = 1 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update existing contact.
    api_response = api_instance.update_contact(update_contact_input_object, id, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->update_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_contact_input_object** | [**UpdateContactInputObject**](UpdateContactInputObject.md)|  | 
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

# **upload_contact_avatar**
> ResourceLinkResponse upload_contact_avatar(image, id)

Add an avatar for the contact.

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
api_instance = TextMagic.ContactsApi(TextMagic.ApiClient(configuration))
image = '/path/to/file.txt' # file | Contact avatar. Should be PNG or JPG file not more than 10 MB
id = 56 # int | 

try:
    # Add an avatar for the contact.
    api_response = api_instance.upload_contact_avatar(image, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->upload_contact_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **file**| Contact avatar. Should be PNG or JPG file not more than 10 MB | 
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

