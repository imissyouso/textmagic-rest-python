# TextMagic.TemplatesApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_template**](TemplatesApi.md#create_template) | **POST** /api/v2/templates | Create a new template from the submitted data.
[**delete_template**](TemplatesApi.md#delete_template) | **DELETE** /api/v2/templates/{id} | Delete a single template.
[**delete_templates_bulk**](TemplatesApi.md#delete_templates_bulk) | **POST** /api/v2/templates/delete | Delete template by given ID(s) or delete all templates.
[**get_all_templates**](TemplatesApi.md#get_all_templates) | **GET** /api/v2/templates | Get all user templates.
[**get_template**](TemplatesApi.md#get_template) | **GET** /api/v2/templates/{id} | Get a single template.
[**search_templates**](TemplatesApi.md#search_templates) | **GET** /api/v2/templates/search | Find user templates by given parameters.
[**update_template**](TemplatesApi.md#update_template) | **PUT** /api/v2/templates/{id} | Update existing template.


# **create_template**
> ResourceLinkResponse create_template(create_template_input_object, x_ignore_null_values=x_ignore_null_values)

Create a new template from the submitted data.

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
api_instance = TextMagic.TemplatesApi(TextMagic.ApiClient(configuration))
create_template_input_object = TextMagic.CreateTemplateInputObject() # CreateTemplateInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Create a new template from the submitted data.
    api_response = api_instance.create_template(create_template_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->create_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_template_input_object** | [**CreateTemplateInputObject**](CreateTemplateInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> delete_template(id)

Delete a single template.

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
api_instance = TextMagic.TemplatesApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a single template.
    api_instance.delete_template(id)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_template: %s\n" % e)
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

# **delete_templates_bulk**
> delete_templates_bulk(delete_templates_bulk_input_object, x_ignore_null_values=x_ignore_null_values)

Delete template by given ID(s) or delete all templates.

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
api_instance = TextMagic.TemplatesApi(TextMagic.ApiClient(configuration))
delete_templates_bulk_input_object = TextMagic.DeleteTemplatesBulkInputObject() # DeleteTemplatesBulkInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Delete template by given ID(s) or delete all templates.
    api_instance.delete_templates_bulk(delete_templates_bulk_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_templates_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_templates_bulk_input_object** | [**DeleteTemplatesBulkInputObject**](DeleteTemplatesBulkInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_templates**
> dict(str, object) get_all_templates(page=page, limit=limit)

Get all user templates.

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
api_instance = TextMagic.TemplatesApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional)
limit = 10 # int | How many results to return (optional)

try:
    # Get all user templates.
    api_response = api_instance.get_all_templates(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_all_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] 
 **limit** | **int**| How many results to return | [optional] 

### Return type

**dict(str, object)**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> MessageTemplate get_template(id)

Get a single template.

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
api_instance = TextMagic.TemplatesApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single template.
    api_response = api_instance.get_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MessageTemplate**](MessageTemplate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_templates**
> dict(str, object) search_templates(page=page, limit=limit, ids=ids, name=name, content=content)

Find user templates by given parameters.

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
api_instance = TextMagic.TemplatesApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
ids = 'ids_example' # str | Find template by ID(s) (optional)
name = 'name_example' # str | Find template by name (optional)
content = 'content_example' # str | Find template by content (optional)

try:
    # Find user templates by given parameters.
    api_response = api_instance.search_templates(page=page, limit=limit, ids=ids, name=name, content=content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->search_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **ids** | **str**| Find template by ID(s) | [optional] 
 **name** | **str**| Find template by name | [optional] 
 **content** | **str**| Find template by content | [optional] 

### Return type

**dict(str, object)**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> ResourceLinkResponse update_template(update_template_input_object, id, x_ignore_null_values=x_ignore_null_values)

Update existing template.

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
api_instance = TextMagic.TemplatesApi(TextMagic.ApiClient(configuration))
update_template_input_object = TextMagic.UpdateTemplateInputObject() # UpdateTemplateInputObject | 
id = 1 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update existing template.
    api_response = api_instance.update_template(update_template_input_object, id, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->update_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_template_input_object** | [**UpdateTemplateInputObject**](UpdateTemplateInputObject.md)|  | 
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

