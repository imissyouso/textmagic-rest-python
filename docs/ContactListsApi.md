# TextMagic.ContactListsApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_contacts_to_list**](ContactListsApi.md#assign_contacts_to_list) | **PUT** /api/v2/lists/{id}/contacts | Assign contacts to the specified list.
[**clear_and_assign_contacts_to_list**](ContactListsApi.md#clear_and_assign_contacts_to_list) | **POST** /api/v2/lists/{id}/contacts | Reset list members to the specified contacts.
[**create_list**](ContactListsApi.md#create_list) | **POST** /api/v2/lists | Create a new list from the submitted data.
[**delete_contacts_from_list**](ContactListsApi.md#delete_contacts_from_list) | **DELETE** /api/v2/lists/{id}/contacts | Unassign contacts from the specified list.
[**delete_list**](ContactListsApi.md#delete_list) | **DELETE** /api/v2/lists/{id} | Delete a single list.
[**delete_list_avatar**](ContactListsApi.md#delete_list_avatar) | **DELETE** /api/v2/lists/{id}/avatar | Delete an avatar for the list.
[**delete_list_contacts_bulk**](ContactListsApi.md#delete_list_contacts_bulk) | **POST** /api/v2/lists/{id}/contacts/delete | Delete contact from list by given ID(s) or all contacts from list.
[**delete_lists_bulk**](ContactListsApi.md#delete_lists_bulk) | **POST** /api/v2/lists/delete | Delete list by given ID(s) or delete all lists.
[**get_contacts_by_list_id**](ContactListsApi.md#get_contacts_by_list_id) | **GET** /api/v2/lists/{id}/contacts | Fetch user contacts by given group id.
[**get_list**](ContactListsApi.md#get_list) | **GET** /api/v2/lists/{id} | Get a single list.
[**get_list_contacts_ids**](ContactListsApi.md#get_list_contacts_ids) | **GET** /api/v2/lists/{id}/contacts/ids | Fetch all contacts IDs belonging to the list with ID.
[**get_lists_of_contact**](ContactListsApi.md#get_lists_of_contact) | **GET** /api/v2/contacts/{id}/lists | Return lists which contact belongs to.
[**get_user_lists**](ContactListsApi.md#get_user_lists) | **GET** /api/v2/lists | Get all user lists.
[**search_lists**](ContactListsApi.md#search_lists) | **GET** /api/v2/lists/search | Find contact lists by given parameters.
[**update_list**](ContactListsApi.md#update_list) | **PUT** /api/v2/lists/{id} | Update existing list.
[**upload_list_avatar**](ContactListsApi.md#upload_list_avatar) | **POST** /api/v2/lists/{id}/avatar | Add an avatar for the list.


# **assign_contacts_to_list**
> ResourceLinkResponse assign_contacts_to_list(assign_contacts_to_list_input_object, id)

Assign contacts to the specified list.

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
api_instance = TextMagic.ContactListsApi(TextMagic.ApiClient(configuration))
assign_contacts_to_list_input_object = TextMagic.AssignContactsToListInputObject() # AssignContactsToListInputObject | Contact ID(s), separated by comma or 'all' to add all contacts belonging to the current user
id = 1 # int | 

try:
    # Assign contacts to the specified list.
    api_response = api_instance.assign_contacts_to_list(assign_contacts_to_list_input_object, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactListsApi->assign_contacts_to_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assign_contacts_to_list_input_object** | [**AssignContactsToListInputObject**](AssignContactsToListInputObject.md)| Contact ID(s), separated by comma or &#39;all&#39; to add all contacts belonging to the current user | 
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_and_assign_contacts_to_list**
> ResourceLinkResponse clear_and_assign_contacts_to_list(clear_and_assign_contacts_to_list_input_object, id)

Reset list members to the specified contacts.

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
api_instance = TextMagic.ContactListsApi(TextMagic.ApiClient(configuration))
clear_and_assign_contacts_to_list_input_object = TextMagic.ClearAndAssignContactsToListInputObject() # ClearAndAssignContactsToListInputObject | Contact ID(s), separated by comma or 'all' to add all contacts belonging to the current user
id = 1 # int | 

try:
    # Reset list members to the specified contacts.
    api_response = api_instance.clear_and_assign_contacts_to_list(clear_and_assign_contacts_to_list_input_object, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactListsApi->clear_and_assign_contacts_to_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clear_and_assign_contacts_to_list_input_object** | [**ClearAndAssignContactsToListInputObject**](ClearAndAssignContactsToListInputObject.md)| Contact ID(s), separated by comma or &#39;all&#39; to add all contacts belonging to the current user | 
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_list**
> ResourceLinkResponse create_list(create_list_input_object, x_ignore_null_values=x_ignore_null_values)

Create a new list from the submitted data.

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
api_instance = TextMagic.ContactListsApi(TextMagic.ApiClient(configuration))
create_list_input_object = TextMagic.CreateListInputObject() # CreateListInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Create a new list from the submitted data.
    api_response = api_instance.create_list(create_list_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactListsApi->create_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_list_input_object** | [**CreateListInputObject**](CreateListInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contacts_from_list**
> delete_contacts_from_list(delete_contacs_from_list_object, id)

Unassign contacts from the specified list.

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
api_instance = TextMagic.ContactListsApi(TextMagic.ApiClient(configuration))
delete_contacs_from_list_object = TextMagic.DeleteContacsFromListObject() # DeleteContacsFromListObject | Contact ID(s), separated by comma
id = 1 # int | 

try:
    # Unassign contacts from the specified list.
    api_instance.delete_contacts_from_list(delete_contacs_from_list_object, id)
except ApiException as e:
    print("Exception when calling ContactListsApi->delete_contacts_from_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_contacs_from_list_object** | [**DeleteContacsFromListObject**](DeleteContacsFromListObject.md)| Contact ID(s), separated by comma | 
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list**
> delete_list(id)

Delete a single list.

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
api_instance = TextMagic.ContactListsApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a single list.
    api_instance.delete_list(id)
except ApiException as e:
    print("Exception when calling ContactListsApi->delete_list: %s\n" % e)
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

# **delete_list_avatar**
> delete_list_avatar(id)

Delete an avatar for the list.

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
api_instance = TextMagic.ContactListsApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete an avatar for the list.
    api_instance.delete_list_avatar(id)
except ApiException as e:
    print("Exception when calling ContactListsApi->delete_list_avatar: %s\n" % e)
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

# **delete_list_contacts_bulk**
> delete_list_contacts_bulk(delete_list_contacts_bulk_input_object, id, x_ignore_null_values=x_ignore_null_values)

Delete contact from list by given ID(s) or all contacts from list.

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
api_instance = TextMagic.ContactListsApi(TextMagic.ApiClient(configuration))
delete_list_contacts_bulk_input_object = TextMagic.DeleteListContactsBulkInputObject() # DeleteListContactsBulkInputObject | 
id = 1 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete contact from list by given ID(s) or all contacts from list.
    api_instance.delete_list_contacts_bulk(delete_list_contacts_bulk_input_object, id, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling ContactListsApi->delete_list_contacts_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_list_contacts_bulk_input_object** | [**DeleteListContactsBulkInputObject**](DeleteListContactsBulkInputObject.md)|  | 
 **id** | **int**|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lists_bulk**
> delete_lists_bulk(delete_lists_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Delete list by given ID(s) or delete all lists.

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
api_instance = TextMagic.ContactListsApi(TextMagic.ApiClient(configuration))
delete_lists_bulk_input_object = TextMagic.DeleteListsBulkInputObject() # DeleteListsBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete list by given ID(s) or delete all lists.
    api_instance.delete_lists_bulk(delete_lists_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling ContactListsApi->delete_lists_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_lists_bulk_input_object** | [**DeleteListsBulkInputObject**](DeleteListsBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts_by_list_id**
> dict(str, object) get_contacts_by_list_id(id, page=page, limit=limit, order_by=order_by, direction=direction)

Fetch user contacts by given group id.

A useful synonym for \"contacts/search\" command with provided \"listId\" parameter.

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
api_instance = TextMagic.ContactListsApi(TextMagic.ApiClient(configuration))
id = 1 # int | Given group Id.
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)

try:
    # Fetch user contacts by given group id.
    api_response = api_instance.get_contacts_by_list_id(id, page=page, limit=limit, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactListsApi->get_contacts_by_list_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Given group Id. | 
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

# **get_list**
> Group get_list(id)

Get a single list.

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
api_instance = TextMagic.ContactListsApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single list.
    api_response = api_instance.get_list(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactListsApi->get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Group**](Group.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_contacts_ids**
> GetListContactsIdsResponse get_list_contacts_ids(id)

Fetch all contacts IDs belonging to the list with ID.

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
api_instance = TextMagic.ContactListsApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Fetch all contacts IDs belonging to the list with ID.
    api_response = api_instance.get_list_contacts_ids(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactListsApi->get_list_contacts_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetListContactsIdsResponse**](GetListContactsIdsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lists_of_contact**
> dict(str, object) get_lists_of_contact(id, page=page, limit=limit)

Return lists which contact belongs to.

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
api_instance = TextMagic.ContactListsApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Return lists which contact belongs to.
    api_response = api_instance.get_lists_of_contact(id, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactListsApi->get_lists_of_contact: %s\n" % e)
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

# **get_user_lists**
> dict(str, object) get_user_lists(page=page, limit=limit, order_by=order_by, direction=direction, favorite_only=favorite_only, only_mine=only_mine)

Get all user lists.

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
api_instance = TextMagic.ContactListsApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)
favorite_only = 0 # int | Return only favorite lists (optional) (default to 0)
only_mine = 0 # int | Return only current user lists (optional) (default to 0)

try:
    # Get all user lists.
    api_response = api_instance.get_user_lists(page=page, limit=limit, order_by=order_by, direction=direction, favorite_only=favorite_only, only_mine=only_mine)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactListsApi->get_user_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **order_by** | **str**| Order results by some field. Default is id | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc | [optional] [default to desc]
 **favorite_only** | **int**| Return only favorite lists | [optional] [default to 0]
 **only_mine** | **int**| Return only current user lists | [optional] [default to 0]

### Return type

**dict(str, object)**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_lists**
> dict(str, object) search_lists(page=page, limit=limit, ids=ids, query=query, only_mine=only_mine, only_default=only_default, order_by=order_by, direction=direction)

Find contact lists by given parameters.

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
api_instance = TextMagic.ContactListsApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
ids = '\"1,2,3,4\"' # str | Find lists by ID(s) (optional)
query = '\"A\"' # str | Find lists by specified search query (optional)
only_mine = 0 # int | Return only current user lists (optional) (default to 0)
only_default = 0 # int | Return only default lists (optional) (default to 0)
order_by = 'id' # str | Order results by some field. Default is id (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc (optional) (default to desc)

try:
    # Find contact lists by given parameters.
    api_response = api_instance.search_lists(page=page, limit=limit, ids=ids, query=query, only_mine=only_mine, only_default=only_default, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactListsApi->search_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **ids** | **str**| Find lists by ID(s) | [optional] 
 **query** | **str**| Find lists by specified search query | [optional] 
 **only_mine** | **int**| Return only current user lists | [optional] [default to 0]
 **only_default** | **int**| Return only default lists | [optional] [default to 0]
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

# **update_list**
> ResourceLinkResponse update_list(id, update_list_object=update_list_object)

Update existing list.

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
api_instance = TextMagic.ContactListsApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
update_list_object = TextMagic.UpdateListObject() # UpdateListObject |  (optional)

try:
    # Update existing list.
    api_response = api_instance.update_list(id, update_list_object=update_list_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactListsApi->update_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_list_object** | [**UpdateListObject**](UpdateListObject.md)|  | [optional] 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_list_avatar**
> ResourceLinkResponse upload_list_avatar(image, id)

Add an avatar for the list.

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
api_instance = TextMagic.ContactListsApi(TextMagic.ApiClient(configuration))
image = '/path/to/file.txt' # file | List avatar. Should be PNG or JPG file not more than 10 MB
id = 1 # int | 

try:
    # Add an avatar for the list.
    api_response = api_instance.upload_list_avatar(image, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactListsApi->upload_list_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **file**| List avatar. Should be PNG or JPG file not more than 10 MB | 
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

