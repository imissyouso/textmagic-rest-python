# TextMagic.NumbersApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buy_dedicated_number**](NumbersApi.md#buy_dedicated_number) | **POST** /api/v2/numbers | Buy a dedicated number and assign it to the specified account.
[**delete_dedicated_number**](NumbersApi.md#delete_dedicated_number) | **DELETE** /api/v2/numbers/{id} | Cancel dedicated number subscription.
[**delete_sender_id**](NumbersApi.md#delete_sender_id) | **DELETE** /api/v2/senderids/{id} | Delete a Sender ID.
[**get_available_dedicated_numbers**](NumbersApi.md#get_available_dedicated_numbers) | **GET** /api/v2/numbers/available | Find available dedicated numbers to buy.
[**get_dedicated_number**](NumbersApi.md#get_dedicated_number) | **GET** /api/v2/numbers/{id} | Get a single dedicated number.
[**get_sender_id**](NumbersApi.md#get_sender_id) | **GET** /api/v2/senderids/{id} | Get a single Sender ID.
[**get_sender_ids**](NumbersApi.md#get_sender_ids) | **GET** /api/v2/senderids | Get all sender IDs of current user.
[**get_sender_settings**](NumbersApi.md#get_sender_settings) | **GET** /api/v2/sender/settings | Get current user sender settings.
[**get_user_dedicated_numbers**](NumbersApi.md#get_user_dedicated_numbers) | **GET** /api/v2/numbers | Get user&#39;s dedicated numbers.
[**request_sender_id**](NumbersApi.md#request_sender_id) | **POST** /api/v2/senderids | Request for a new Sender ID.
[**update_sender_setting**](NumbersApi.md#update_sender_setting) | **PUT** /api/v2/sender/settings | Change sender settings for specified country.


# **buy_dedicated_number**
> buy_dedicated_number(buy_dedicated_number_input_object, x_ignore_null_values=x_ignore_null_values)

Buy a dedicated number and assign it to the specified account.

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
api_instance = TextMagic.NumbersApi(TextMagic.ApiClient(configuration))
buy_dedicated_number_input_object = TextMagic.BuyDedicatedNumberInputObject() # BuyDedicatedNumberInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Buy a dedicated number and assign it to the specified account.
    api_instance.buy_dedicated_number(buy_dedicated_number_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling NumbersApi->buy_dedicated_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buy_dedicated_number_input_object** | [**BuyDedicatedNumberInputObject**](BuyDedicatedNumberInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dedicated_number**
> delete_dedicated_number(id)

Cancel dedicated number subscription.

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
api_instance = TextMagic.NumbersApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Cancel dedicated number subscription.
    api_instance.delete_dedicated_number(id)
except ApiException as e:
    print("Exception when calling NumbersApi->delete_dedicated_number: %s\n" % e)
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

# **delete_sender_id**
> delete_sender_id(id)

Delete a Sender ID.

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
api_instance = TextMagic.NumbersApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a Sender ID.
    api_instance.delete_sender_id(id)
except ApiException as e:
    print("Exception when calling NumbersApi->delete_sender_id: %s\n" % e)
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

# **get_available_dedicated_numbers**
> GetAvailableDedicatedNumbersResponse get_available_dedicated_numbers(country, prefix=prefix, tollfree=tollfree)

Find available dedicated numbers to buy.

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
api_instance = TextMagic.NumbersApi(TextMagic.ApiClient(configuration))
country = '\"GB\"' # str | Dedicated number country. Two letters in upper case
prefix = 1 # int | Desired number prefix. Should include country code (i.e. 447 for GB). In case provide tollfree = 1 parameter and there are available tollfree numbers, this parameter will be ignore. (optional) (default to 1)
tollfree = 0 # int | Should we show only tollfree numbers (tollfree available only for US). Default is false. (optional) (default to 0)

try:
    # Find available dedicated numbers to buy.
    api_response = api_instance.get_available_dedicated_numbers(country, prefix=prefix, tollfree=tollfree)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumbersApi->get_available_dedicated_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Dedicated number country. Two letters in upper case | 
 **prefix** | **int**| Desired number prefix. Should include country code (i.e. 447 for GB). In case provide tollfree &#x3D; 1 parameter and there are available tollfree numbers, this parameter will be ignore. | [optional] [default to 1]
 **tollfree** | **int**| Should we show only tollfree numbers (tollfree available only for US). Default is false. | [optional] [default to 0]

### Return type

[**GetAvailableDedicatedNumbersResponse**](GetAvailableDedicatedNumbersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dedicated_number**
> UsersInbound get_dedicated_number(id)

Get a single dedicated number.

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
api_instance = TextMagic.NumbersApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single dedicated number.
    api_response = api_instance.get_dedicated_number(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumbersApi->get_dedicated_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UsersInbound**](UsersInbound.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sender_id**
> SenderId get_sender_id(id)

Get a single Sender ID.

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
api_instance = TextMagic.NumbersApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single Sender ID.
    api_response = api_instance.get_sender_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumbersApi->get_sender_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SenderId**](SenderId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sender_ids**
> dict(str, object) get_sender_ids(page=page, limit=limit)

Get all sender IDs of current user.

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
api_instance = TextMagic.NumbersApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)

try:
    # Get all sender IDs of current user.
    api_response = api_instance.get_sender_ids(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumbersApi->get_sender_ids: %s\n" % e)
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

# **get_sender_settings**
> GetSenderSettingsResponse get_sender_settings(country=country)

Get current user sender settings.

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
api_instance = TextMagic.NumbersApi(TextMagic.ApiClient(configuration))
country = 'country_example' # str | Return sender settings enabled for sending to specified country. Two upper case characters (optional)

try:
    # Get current user sender settings.
    api_response = api_instance.get_sender_settings(country=country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumbersApi->get_sender_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Return sender settings enabled for sending to specified country. Two upper case characters | [optional] 

### Return type

[**GetSenderSettingsResponse**](GetSenderSettingsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_dedicated_numbers**
> dict(str, object) get_user_dedicated_numbers(page=page, limit=limit, survey_id=survey_id)

Get user's dedicated numbers.

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
api_instance = TextMagic.NumbersApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page (optional) (default to 1)
limit = 10 # int | How many results to return (optional) (default to 10)
survey_id = 56 # int | Fetch only that numbers which are ready for the survey (optional)

try:
    # Get user's dedicated numbers.
    api_response = api_instance.get_user_dedicated_numbers(page=page, limit=limit, survey_id=survey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumbersApi->get_user_dedicated_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page | [optional] [default to 1]
 **limit** | **int**| How many results to return | [optional] [default to 10]
 **survey_id** | **int**| Fetch only that numbers which are ready for the survey | [optional] 

### Return type

**dict(str, object)**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_sender_id**
> ResourceLinkResponse request_sender_id(request_sender_id_input_object, x_ignore_null_values=x_ignore_null_values)

Request for a new Sender ID.

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
api_instance = TextMagic.NumbersApi(TextMagic.ApiClient(configuration))
request_sender_id_input_object = TextMagic.RequestSenderIdInputObject() # RequestSenderIdInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Request for a new Sender ID.
    api_response = api_instance.request_sender_id(request_sender_id_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumbersApi->request_sender_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_sender_id_input_object** | [**RequestSenderIdInputObject**](RequestSenderIdInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sender_setting**
> update_sender_setting(update_sender_setting_input_object, x_ignore_null_values=x_ignore_null_values)

Change sender settings for specified country.

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
api_instance = TextMagic.NumbersApi(TextMagic.ApiClient(configuration))
update_sender_setting_input_object = TextMagic.UpdateSenderSettingInputObject() # UpdateSenderSettingInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Change sender settings for specified country.
    api_instance.update_sender_setting(update_sender_setting_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling NumbersApi->update_sender_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_sender_setting_input_object** | [**UpdateSenderSettingInputObject**](UpdateSenderSettingInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

