# TextMagic.IntegrationApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_push_token**](IntegrationApi.md#create_push_token) | **POST** /api/v2/push/tokens | Add or update a device token.
[**delete_push_token**](IntegrationApi.md#delete_push_token) | **DELETE** /api/v2/push/tokens/{type}/{deviceId} | Delete a push notification device token.
[**get_push_tokens**](IntegrationApi.md#get_push_tokens) | **GET** /api/v2/push/tokens | Get all device tokens assigned to the current account


# **create_push_token**
> create_push_token(create_push_token_input_object, x_ignore_null_values=x_ignore_null_values)

Add or update a device token.

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
api_instance = TextMagic.IntegrationApi(TextMagic.ApiClient(configuration))
create_push_token_input_object = TextMagic.CreatePushTokenInputObject() # CreatePushTokenInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Add or update a device token.
    api_instance.create_push_token(create_push_token_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling IntegrationApi->create_push_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_push_token_input_object** | [**CreatePushTokenInputObject**](CreatePushTokenInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_push_token**
> delete_push_token(type, device_id)

Delete a push notification device token.

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
api_instance = TextMagic.IntegrationApi(TextMagic.ApiClient(configuration))
type = 'type_example' # str | 
device_id = 56 # int | 

try:
    # Delete a push notification device token.
    api_instance.delete_push_token(type, device_id)
except ApiException as e:
    print("Exception when calling IntegrationApi->delete_push_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **device_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_push_tokens**
> GetPushTokensResponse get_push_tokens()

Get all device tokens assigned to the current account

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
api_instance = TextMagic.IntegrationApi(TextMagic.ApiClient(configuration))

try:
    # Get all device tokens assigned to the current account
    api_response = api_instance.get_push_tokens()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_push_tokens: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPushTokensResponse**](GetPushTokensResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

