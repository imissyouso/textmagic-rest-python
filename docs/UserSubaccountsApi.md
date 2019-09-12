# TextMagic.UserSubaccountsApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_subaccount**](UserSubaccountsApi.md#close_subaccount) | **DELETE** /api/v2/subaccounts/{id} | Close subaccount.
[**get_subaccount**](UserSubaccountsApi.md#get_subaccount) | **GET** /api/v2/subaccounts/{id} | Get a single subaccount.
[**get_subaccounts**](UserSubaccountsApi.md#get_subaccounts) | **GET** /api/v2/subaccounts | Get all subaccounts of current user.
[**get_subaccounts_with_tokens**](UserSubaccountsApi.md#get_subaccounts_with_tokens) | **POST** /api/v2/subaccounts/tokens/list | Get all subaccounts with their REST API tokens associated with specified app name.
[**invite_subaccount**](UserSubaccountsApi.md#invite_subaccount) | **POST** /api/v2/subaccounts | Invite new subaccount.
[**request_new_subaccount_token**](UserSubaccountsApi.md#request_new_subaccount_token) | **POST** /api/v2/subaccounts/tokens | Request a new REST API token for subaccount.


# **close_subaccount**
> close_subaccount(id)

Close subaccount.

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
api_instance = TextMagic.UserSubaccountsApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Close subaccount.
    api_instance.close_subaccount(id)
except ApiException as e:
    print("Exception when calling UserSubaccountsApi->close_subaccount: %s\n" % e)
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

# **get_subaccount**
> User get_subaccount(id)

Get a single subaccount.

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
api_instance = TextMagic.UserSubaccountsApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single subaccount.
    api_response = api_instance.get_subaccount(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSubaccountsApi->get_subaccount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**User**](User.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subaccounts**
> User get_subaccounts(page=page, limit=limit)

Get all subaccounts of current user.

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
api_instance = TextMagic.UserSubaccountsApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Get all subaccounts of current user.
    api_response = api_instance.get_subaccounts(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSubaccountsApi->get_subaccounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]

### Return type

[**User**](User.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subaccounts_with_tokens**
> GetSubaccountsWithTokensResponse get_subaccounts_with_tokens(get_subaccounts_with_tokens_input_object, page=page, limit=limit, x_ignore_null_values=x_ignore_null_values)

Get all subaccounts with their REST API tokens associated with specified app name.

When more than one token related to app name, last key will be returned.

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
api_instance = TextMagic.UserSubaccountsApi(TextMagic.ApiClient(configuration))
get_subaccounts_with_tokens_input_object = TextMagic.GetSubaccountsWithTokensInputObject() # GetSubaccountsWithTokensInputObject | 
page = 1 # float | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Get all subaccounts with their REST API tokens associated with specified app name.
    api_response = api_instance.get_subaccounts_with_tokens(get_subaccounts_with_tokens_input_object, page=page, limit=limit, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSubaccountsApi->get_subaccounts_with_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_subaccounts_with_tokens_input_object** | [**GetSubaccountsWithTokensInputObject**](GetSubaccountsWithTokensInputObject.md)|  | 
 **page** | **float**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**GetSubaccountsWithTokensResponse**](GetSubaccountsWithTokensResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_subaccount**
> invite_subaccount(invite_subaccount_input_object, x_ignore_null_values=x_ignore_null_values)

Invite new subaccount.

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
api_instance = TextMagic.UserSubaccountsApi(TextMagic.ApiClient(configuration))
invite_subaccount_input_object = TextMagic.InviteSubaccountInputObject() # InviteSubaccountInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Invite new subaccount.
    api_instance.invite_subaccount(invite_subaccount_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling UserSubaccountsApi->invite_subaccount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_subaccount_input_object** | [**InviteSubaccountInputObject**](InviteSubaccountInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_new_subaccount_token**
> User request_new_subaccount_token(request_new_subaccount_token_input_object, x_ignore_null_values=x_ignore_null_values)

Request a new REST API token for subaccount.

Returning user object, key and app name.

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
api_instance = TextMagic.UserSubaccountsApi(TextMagic.ApiClient(configuration))
request_new_subaccount_token_input_object = TextMagic.RequestNewSubaccountTokenInputObject() # RequestNewSubaccountTokenInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Request a new REST API token for subaccount.
    api_response = api_instance.request_new_subaccount_token(request_new_subaccount_token_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSubaccountsApi->request_new_subaccount_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_new_subaccount_token_input_object** | [**RequestNewSubaccountTokenInputObject**](RequestNewSubaccountTokenInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**User**](User.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

