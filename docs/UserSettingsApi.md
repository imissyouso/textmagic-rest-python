# TextMagic.UserSettingsApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_sender_setting_options**](UserSettingsApi.md#get_available_sender_setting_options) | **GET** /api/v2/sources | Get all available sender setting options which could be used in \&quot;from\&quot; parameter of POST messages method.
[**get_balance_notification_options**](UserSettingsApi.md#get_balance_notification_options) | **GET** /api/v2/user/notification/balance/bundles | Returns the list of available balance options which can be used as a bound to determine when to send email to user with low balance notification. See https://my.textmagic.com/online/account/notifications/balance
[**get_balance_notification_settings**](UserSettingsApi.md#get_balance_notification_settings) | **GET** /api/v2/user/notification/balance | Get balance notification settings
[**get_callback_settings**](UserSettingsApi.md#get_callback_settings) | **GET** /api/v2/callback/settings | Fetch callback URL settings
[**get_inbound_messages_notification_settings**](UserSettingsApi.md#get_inbound_messages_notification_settings) | **GET** /api/v2/user/notification/inbound | Get inbound messages notification settings
[**update_balance_notification_settings**](UserSettingsApi.md#update_balance_notification_settings) | **PUT** /api/v2/user/notification/balance | Update balance notification settings
[**update_callback_settings**](UserSettingsApi.md#update_callback_settings) | **PUT** /api/v2/callback/settings | Update callback URL settings
[**update_chat_desktop_notification_settings**](UserSettingsApi.md#update_chat_desktop_notification_settings) | **PUT** /api/v2/user/desktop/notification | Update chat desktop notification settings
[**update_inbound_messages_notification_settings**](UserSettingsApi.md#update_inbound_messages_notification_settings) | **PUT** /api/v2/user/notification/inbound | Update inbound messages notification settings


# **get_available_sender_setting_options**
> GetAvailableSenderSettingOptionsResponse get_available_sender_setting_options(country=country)

Get all available sender setting options which could be used in \"from\" parameter of POST messages method.

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
api_instance = TextMagic.UserSettingsApi(TextMagic.ApiClient(configuration))
country = 'country_example' # str | Return sender setting options available in specific country only. Two upper case characters (optional)

try:
    # Get all available sender setting options which could be used in \"from\" parameter of POST messages method.
    api_response = api_instance.get_available_sender_setting_options(country=country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSettingsApi->get_available_sender_setting_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Return sender setting options available in specific country only. Two upper case characters | [optional] 

### Return type

[**GetAvailableSenderSettingOptionsResponse**](GetAvailableSenderSettingOptionsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_notification_options**
> GetBalanceNotificationOptionsResponse get_balance_notification_options()

Returns the list of available balance options which can be used as a bound to determine when to send email to user with low balance notification. See https://my.textmagic.com/online/account/notifications/balance

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
api_instance = TextMagic.UserSettingsApi(TextMagic.ApiClient(configuration))

try:
    # Returns the list of available balance options which can be used as a bound to determine when to send email to user with low balance notification. See https://my.textmagic.com/online/account/notifications/balance
    api_response = api_instance.get_balance_notification_options()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSettingsApi->get_balance_notification_options: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBalanceNotificationOptionsResponse**](GetBalanceNotificationOptionsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_notification_settings**
> GetBalanceNotificationSettingsResponse get_balance_notification_settings()

Get balance notification settings

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
api_instance = TextMagic.UserSettingsApi(TextMagic.ApiClient(configuration))

try:
    # Get balance notification settings
    api_response = api_instance.get_balance_notification_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSettingsApi->get_balance_notification_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBalanceNotificationSettingsResponse**](GetBalanceNotificationSettingsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_callback_settings**
> GetCallbackSettingsResponse get_callback_settings()

Fetch callback URL settings

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
api_instance = TextMagic.UserSettingsApi(TextMagic.ApiClient(configuration))

try:
    # Fetch callback URL settings
    api_response = api_instance.get_callback_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSettingsApi->get_callback_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetCallbackSettingsResponse**](GetCallbackSettingsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound_messages_notification_settings**
> GetInboundMessagesNotificationSettingsResponse get_inbound_messages_notification_settings()

Get inbound messages notification settings

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
api_instance = TextMagic.UserSettingsApi(TextMagic.ApiClient(configuration))

try:
    # Get inbound messages notification settings
    api_response = api_instance.get_inbound_messages_notification_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSettingsApi->get_inbound_messages_notification_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetInboundMessagesNotificationSettingsResponse**](GetInboundMessagesNotificationSettingsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_balance_notification_settings**
> update_balance_notification_settings(update_balance_notification_settings_input_object, x_ignore_null_values=x_ignore_null_values)

Update balance notification settings

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
api_instance = TextMagic.UserSettingsApi(TextMagic.ApiClient(configuration))
update_balance_notification_settings_input_object = TextMagic.UpdateBalanceNotificationSettingsInputObject() # UpdateBalanceNotificationSettingsInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update balance notification settings
    api_instance.update_balance_notification_settings(update_balance_notification_settings_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling UserSettingsApi->update_balance_notification_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_balance_notification_settings_input_object** | [**UpdateBalanceNotificationSettingsInputObject**](UpdateBalanceNotificationSettingsInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_callback_settings**
> update_callback_settings(update_callback_settings_input_object, x_ignore_null_values=x_ignore_null_values)

Update callback URL settings

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
api_instance = TextMagic.UserSettingsApi(TextMagic.ApiClient(configuration))
update_callback_settings_input_object = TextMagic.UpdateCallbackSettingsInputObject() # UpdateCallbackSettingsInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update callback URL settings
    api_instance.update_callback_settings(update_callback_settings_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling UserSettingsApi->update_callback_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_callback_settings_input_object** | [**UpdateCallbackSettingsInputObject**](UpdateCallbackSettingsInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_chat_desktop_notification_settings**
> update_chat_desktop_notification_settings(update_chat_desktop_notification_settings_input_object, x_ignore_null_values=x_ignore_null_values)

Update chat desktop notification settings

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
api_instance = TextMagic.UserSettingsApi(TextMagic.ApiClient(configuration))
update_chat_desktop_notification_settings_input_object = TextMagic.UpdateChatDesktopNotificationSettingsInputObject() # UpdateChatDesktopNotificationSettingsInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update chat desktop notification settings
    api_instance.update_chat_desktop_notification_settings(update_chat_desktop_notification_settings_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling UserSettingsApi->update_chat_desktop_notification_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_chat_desktop_notification_settings_input_object** | [**UpdateChatDesktopNotificationSettingsInputObject**](UpdateChatDesktopNotificationSettingsInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inbound_messages_notification_settings**
> update_inbound_messages_notification_settings(update_inbound_messages_notification_settings_input_object, x_ignore_null_values=x_ignore_null_values)

Update inbound messages notification settings

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
api_instance = TextMagic.UserSettingsApi(TextMagic.ApiClient(configuration))
update_inbound_messages_notification_settings_input_object = TextMagic.UpdateInboundMessagesNotificationSettingsInputObject() # UpdateInboundMessagesNotificationSettingsInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Update inbound messages notification settings
    api_instance.update_inbound_messages_notification_settings(update_inbound_messages_notification_settings_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling UserSettingsApi->update_inbound_messages_notification_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_inbound_messages_notification_settings_input_object** | [**UpdateInboundMessagesNotificationSettingsInputObject**](UpdateInboundMessagesNotificationSettingsInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

