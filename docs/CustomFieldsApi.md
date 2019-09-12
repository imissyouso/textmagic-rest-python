# TextMagic.CustomFieldsApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_field**](CustomFieldsApi.md#create_custom_field) | **POST** /api/v2/customfields | Create a new custom field from the submitted data.
[**delete_custom_field**](CustomFieldsApi.md#delete_custom_field) | **DELETE** /api/v2/customfields/{id} | Delete a single custom field.
[**get_custom_field**](CustomFieldsApi.md#get_custom_field) | **GET** /api/v2/customfields/{id} | Get a single custom field.
[**get_custom_fields**](CustomFieldsApi.md#get_custom_fields) | **GET** /api/v2/customfields | Get all contact custom fields.
[**update_custom_field**](CustomFieldsApi.md#update_custom_field) | **PUT** /api/v2/customfields/{id} | Update existing custom field.
[**update_custom_field_value**](CustomFieldsApi.md#update_custom_field_value) | **PUT** /api/v2/customfields/{id}/update | Update contact&#39;s custom field value.


# **create_custom_field**
> ResourceLinkResponse create_custom_field(create_custom_field_input_object, x_ignore_null_values=x_ignore_null_values)

Create a new custom field from the submitted data.

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
api_instance = TextMagic.CustomFieldsApi(TextMagic.ApiClient(configuration))
create_custom_field_input_object = TextMagic.CreateCustomFieldInputObject() # CreateCustomFieldInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Create a new custom field from the submitted data.
    api_response = api_instance.create_custom_field(create_custom_field_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->create_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_custom_field_input_object** | [**CreateCustomFieldInputObject**](CreateCustomFieldInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_field**
> delete_custom_field(id)

Delete a single custom field.

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
api_instance = TextMagic.CustomFieldsApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a single custom field.
    api_instance.delete_custom_field(id)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->delete_custom_field: %s\n" % e)
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

# **get_custom_field**
> UserCustomField get_custom_field(id)

Get a single custom field.

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
api_instance = TextMagic.CustomFieldsApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single custom field.
    api_response = api_instance.get_custom_field(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->get_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UserCustomField**](UserCustomField.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_fields**
> dict(str, object) get_custom_fields(page=page, limit=limit)

Get all contact custom fields.

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
api_instance = TextMagic.CustomFieldsApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Get all contact custom fields.
    api_response = api_instance.get_custom_fields(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->get_custom_fields: %s\n" % e)
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

# **update_custom_field**
> ResourceLinkResponse update_custom_field(update_custom_field_input_object, id, x_ignore_null_values=x_ignore_null_values)

Update existing custom field.

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
api_instance = TextMagic.CustomFieldsApi(TextMagic.ApiClient(configuration))
update_custom_field_input_object = TextMagic.UpdateCustomFieldInputObject() # UpdateCustomFieldInputObject | 
id = 1 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update existing custom field.
    api_response = api_instance.update_custom_field(update_custom_field_input_object, id, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->update_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_custom_field_input_object** | [**UpdateCustomFieldInputObject**](UpdateCustomFieldInputObject.md)|  | 
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

# **update_custom_field_value**
> ResourceLinkResponse update_custom_field_value(update_custom_field_value_input_object, id, x_ignore_null_values=x_ignore_null_values)

Update contact's custom field value.

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
api_instance = TextMagic.CustomFieldsApi(TextMagic.ApiClient(configuration))
update_custom_field_value_input_object = TextMagic.UpdateCustomFieldValueInputObject() # UpdateCustomFieldValueInputObject | 
id = 'id_example' # str | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update contact's custom field value.
    api_response = api_instance.update_custom_field_value(update_custom_field_value_input_object, id, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->update_custom_field_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_custom_field_value_input_object** | [**UpdateCustomFieldValueInputObject**](UpdateCustomFieldValueInputObject.md)|  | 
 **id** | **str**|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

