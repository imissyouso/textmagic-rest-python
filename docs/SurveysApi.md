# TextMagic.SurveysApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_survey**](SurveysApi.md#cancel_survey) | **PUT** /api/v2/surveys/{id}/cancel | Cancel a survey.
[**create_survey**](SurveysApi.md#create_survey) | **POST** /api/v2/surveys | Create a new survey from the submitted data.
[**create_survey_node**](SurveysApi.md#create_survey_node) | **POST** /api/v2/surveys/{id}/nodes | Create a new node from the submitted data.
[**delete_survey**](SurveysApi.md#delete_survey) | **DELETE** /api/v2/surveys/{id} | Delete a survey.
[**delete_survey_node**](SurveysApi.md#delete_survey_node) | **DELETE** /api/v2/surveys/nodes/{id} | Delete a node.
[**duplicate_survey**](SurveysApi.md#duplicate_survey) | **PUT** /api/v2/surveys/{id}/duplicate | Duplicate a survey.
[**get_survey**](SurveysApi.md#get_survey) | **GET** /api/v2/surveys/{id} | Get a survey by id.
[**get_survey_node**](SurveysApi.md#get_survey_node) | **GET** /api/v2/surveys/nodes/{id} | Get a node by id.
[**get_survey_nodes**](SurveysApi.md#get_survey_nodes) | **GET** /api/v2/surveys/{id}/nodes | Fetch nodes by given survey id.
[**get_surveys**](SurveysApi.md#get_surveys) | **GET** /api/v2/surveys | Get all user surveys.
[**merge_survey_nodes**](SurveysApi.md#merge_survey_nodes) | **POST** /api/v2/surveys/nodes/merge | Merge two question nodes.
[**reset_survey**](SurveysApi.md#reset_survey) | **PUT** /api/v2/surveys/{id}/reset | Reset a survey flow.
[**start_survey**](SurveysApi.md#start_survey) | **PUT** /api/v2/surveys/{id}/start | Start a survey.
[**update_survey**](SurveysApi.md#update_survey) | **PUT** /api/v2/surveys/{id} | Update existing survey.
[**update_survey_node**](SurveysApi.md#update_survey_node) | **PUT** /api/v2/surveys/nodes/{id} | Update existing node.


# **cancel_survey**
> ResourceLinkResponse cancel_survey(id)

Cancel a survey.

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
api_instance = TextMagic.SurveysApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Cancel a survey.
    api_response = api_instance.cancel_survey(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->cancel_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_survey**
> ResourceLinkResponse create_survey(create_survey_input_object, x_ignore_null_values=x_ignore_null_values)

Create a new survey from the submitted data.

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
api_instance = TextMagic.SurveysApi(TextMagic.ApiClient(configuration))
create_survey_input_object = TextMagic.CreateSurveyInputObject() # CreateSurveyInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Create a new survey from the submitted data.
    api_response = api_instance.create_survey(create_survey_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->create_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_survey_input_object** | [**CreateSurveyInputObject**](CreateSurveyInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_survey_node**
> ResourceLinkResponse create_survey_node(create_survey_node_input_object, id, x_ignore_null_values=x_ignore_null_values)

Create a new node from the submitted data.

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
api_instance = TextMagic.SurveysApi(TextMagic.ApiClient(configuration))
create_survey_node_input_object = TextMagic.CreateSurveyNodeInputObject() # CreateSurveyNodeInputObject | 
id = 1 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Create a new node from the submitted data.
    api_response = api_instance.create_survey_node(create_survey_node_input_object, id, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->create_survey_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_survey_node_input_object** | [**CreateSurveyNodeInputObject**](CreateSurveyNodeInputObject.md)|  | 
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

# **delete_survey**
> delete_survey(id)

Delete a survey.

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
api_instance = TextMagic.SurveysApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a survey.
    api_instance.delete_survey(id)
except ApiException as e:
    print("Exception when calling SurveysApi->delete_survey: %s\n" % e)
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

# **delete_survey_node**
> delete_survey_node(id)

Delete a node.

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
api_instance = TextMagic.SurveysApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a node.
    api_instance.delete_survey_node(id)
except ApiException as e:
    print("Exception when calling SurveysApi->delete_survey_node: %s\n" % e)
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

# **duplicate_survey**
> ResourceLinkResponse duplicate_survey(id)

Duplicate a survey.

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
api_instance = TextMagic.SurveysApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Duplicate a survey.
    api_response = api_instance.duplicate_survey(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->duplicate_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_survey**
> Survey get_survey(id)

Get a survey by id.

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
api_instance = TextMagic.SurveysApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a survey by id.
    api_response = api_instance.get_survey(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->get_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Survey**](Survey.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_survey_node**
> SurveyNode get_survey_node(id)

Get a node by id.

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
api_instance = TextMagic.SurveysApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a node by id.
    api_response = api_instance.get_survey_node(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->get_survey_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SurveyNode**](SurveyNode.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_survey_nodes**
> GetSurveyNodesResponse get_survey_nodes(id)

Fetch nodes by given survey id.

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
api_instance = TextMagic.SurveysApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Fetch nodes by given survey id.
    api_response = api_instance.get_survey_nodes(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->get_survey_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetSurveyNodesResponse**](GetSurveyNodesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_surveys**
> dict(str, object) get_surveys(page=page, limit=limit)

Get all user surveys.

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
api_instance = TextMagic.SurveysApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Get all user surveys.
    api_response = api_instance.get_surveys(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->get_surveys: %s\n" % e)
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

# **merge_survey_nodes**
> merge_survey_nodes(merge_survey_nodes_input_object, x_ignore_null_values=x_ignore_null_values)

Merge two question nodes.

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
api_instance = TextMagic.SurveysApi(TextMagic.ApiClient(configuration))
merge_survey_nodes_input_object = TextMagic.MergeSurveyNodesInputObject() # MergeSurveyNodesInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Merge two question nodes.
    api_instance.merge_survey_nodes(merge_survey_nodes_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling SurveysApi->merge_survey_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merge_survey_nodes_input_object** | [**MergeSurveyNodesInputObject**](MergeSurveyNodesInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_survey**
> ResourceLinkResponse reset_survey(id)

Reset a survey flow.

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
api_instance = TextMagic.SurveysApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Reset a survey flow.
    api_response = api_instance.reset_survey(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->reset_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_survey**
> ResourceLinkResponse start_survey(id)

Start a survey.

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
api_instance = TextMagic.SurveysApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Start a survey.
    api_response = api_instance.start_survey(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->start_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_survey**
> ResourceLinkResponse update_survey(update_survey_input_object, id, x_ignore_null_values=x_ignore_null_values)

Update existing survey.

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
api_instance = TextMagic.SurveysApi(TextMagic.ApiClient(configuration))
update_survey_input_object = TextMagic.UpdateSurveyInputObject() # UpdateSurveyInputObject | 
id = 1 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update existing survey.
    api_response = api_instance.update_survey(update_survey_input_object, id, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->update_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_survey_input_object** | [**UpdateSurveyInputObject**](UpdateSurveyInputObject.md)|  | 
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

# **update_survey_node**
> ResourceLinkResponse update_survey_node(update_survey_node_input_object, id, x_ignore_null_values=x_ignore_null_values)

Update existing node.

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
api_instance = TextMagic.SurveysApi(TextMagic.ApiClient(configuration))
update_survey_node_input_object = TextMagic.UpdateSurveyNodeInputObject() # UpdateSurveyNodeInputObject | 
id = 1 # int | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update existing node.
    api_response = api_instance.update_survey_node(update_survey_node_input_object, id, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveysApi->update_survey_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_survey_node_input_object** | [**UpdateSurveyNodeInputObject**](UpdateSurveyNodeInputObject.md)|  | 
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

