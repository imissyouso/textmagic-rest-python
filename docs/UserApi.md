# TextMagic.UserApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_avatar**](UserApi.md#delete_avatar) | **DELETE** /api/v2/user/avatar | Delete an avatar for the current user.\\
[**get_current_user**](UserApi.md#get_current_user) | **GET** /api/v2/user | Get current user info.
[**get_disallowed_rules**](UserApi.md#get_disallowed_rules) | **GET** /api/v2/user/disallowed-rules | Get an array of all rules that are disallowed to the current account.
[**update_current_user**](UserApi.md#update_current_user) | **PUT** /api/v2/user | Update current user info.
[**upload_avatar**](UserApi.md#upload_avatar) | **POST** /api/v2/user/avatar | Add an avatar for the current user.


# **delete_avatar**
> delete_avatar()

Delete an avatar for the current user.\\

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
api_instance = TextMagic.UserApi(TextMagic.ApiClient(configuration))

try:
    # Delete an avatar for the current user.\\
    api_instance.delete_avatar()
except ApiException as e:
    print("Exception when calling UserApi->delete_avatar: %s\n" % e)
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

# **get_current_user**
> User get_current_user()

Get current user info.

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
api_instance = TextMagic.UserApi(TextMagic.ApiClient(configuration))

try:
    # Get current user info.
    api_response = api_instance.get_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disallowed_rules**
> list[str] get_disallowed_rules()

Get an array of all rules that are disallowed to the current account.

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
api_instance = TextMagic.UserApi(TextMagic.ApiClient(configuration))

try:
    # Get an array of all rules that are disallowed to the current account.
    api_response = api_instance.get_disallowed_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_disallowed_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_current_user**
> UpdateCurrentUserResponse update_current_user(update_current_user_input_object, x_ignore_null_values=x_ignore_null_values)

Update current user info.

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
api_instance = TextMagic.UserApi(TextMagic.ApiClient(configuration))
update_current_user_input_object = TextMagic.UpdateCurrentUserInputObject() # UpdateCurrentUserInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update current user info.
    api_response = api_instance.update_current_user(update_current_user_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_current_user_input_object** | [**UpdateCurrentUserInputObject**](UpdateCurrentUserInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**UpdateCurrentUserResponse**](UpdateCurrentUserResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_avatar**
> upload_avatar(image)

Add an avatar for the current user.

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
api_instance = TextMagic.UserApi(TextMagic.ApiClient(configuration))
image = '/path/to/file.txt' # file | User avatar. Should be PNG or JPG file not more than 10 MB

try:
    # Add an avatar for the current user.
    api_instance.upload_avatar(image)
except ApiException as e:
    print("Exception when calling UserApi->upload_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **file**| User avatar. Should be PNG or JPG file not more than 10 MB | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

