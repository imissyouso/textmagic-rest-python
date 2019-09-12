# TextMagic.AuthenticationApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_phone_verification_code**](AuthenticationApi.md#check_phone_verification_code) | **PUT** /api/v2/user/phone/verification | Check user phone verification code
[**do_auth**](AuthenticationApi.md#do_auth) | **POST** /api/v2/auth | Authenticate user by given username and password.
[**send_email_verification_code**](AuthenticationApi.md#send_email_verification_code) | **GET** /api/v2/user/email/verification | Send user email verification
[**send_phone_verification_code**](AuthenticationApi.md#send_phone_verification_code) | **GET** /api/v2/user/phone/verification | Send user phone verification
[**update_password**](AuthenticationApi.md#update_password) | **PUT** /api/v2/user/password/change | Change user password.


# **check_phone_verification_code**
> check_phone_verification_code(check_phone_verification_code_input_object, x_ignore_null_values=x_ignore_null_values)

Check user phone verification code

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
api_instance = TextMagic.AuthenticationApi(TextMagic.ApiClient(configuration))
check_phone_verification_code_input_object = TextMagic.CheckPhoneVerificationCodeInputObject() # CheckPhoneVerificationCodeInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Check user phone verification code
    api_instance.check_phone_verification_code(check_phone_verification_code_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling AuthenticationApi->check_phone_verification_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_phone_verification_code_input_object** | [**CheckPhoneVerificationCodeInputObject**](CheckPhoneVerificationCodeInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_auth**
> DoAuthResponse do_auth(do_auth_input_object, x_ignore_null_values=x_ignore_null_values)

Authenticate user by given username and password.

Returning a username and token that you should pass to the all requests (in X-TM-Username and X-TM-Key, respectively)

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TextMagic.AuthenticationApi()
do_auth_input_object = TextMagic.DoAuthInputObject() # DoAuthInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Authenticate user by given username and password.
    api_response = api_instance.do_auth(do_auth_input_object, x_ignore_null_values=x_ignore_null_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->do_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **do_auth_input_object** | [**DoAuthInputObject**](DoAuthInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

[**DoAuthResponse**](DoAuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_verification_code**
> send_email_verification_code()

Send user email verification

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
api_instance = TextMagic.AuthenticationApi(TextMagic.ApiClient(configuration))

try:
    # Send user email verification
    api_instance.send_email_verification_code()
except ApiException as e:
    print("Exception when calling AuthenticationApi->send_email_verification_code: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_phone_verification_code**
> send_phone_verification_code()

Send user phone verification

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
api_instance = TextMagic.AuthenticationApi(TextMagic.ApiClient(configuration))

try:
    # Send user phone verification
    api_instance.send_phone_verification_code()
except ApiException as e:
    print("Exception when calling AuthenticationApi->send_phone_verification_code: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password**
> update_password(update_password_input_object, x_ignore_null_values=x_ignore_null_values)

Change user password.

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
api_instance = TextMagic.AuthenticationApi(TextMagic.ApiClient(configuration))
update_password_input_object = TextMagic.UpdatePasswordInputObject() # UpdatePasswordInputObject | 
x_ignore_null_values = true # bool |  (optional) (default to true)

try:
    # Change user password.
    api_instance.update_password(update_password_input_object, x_ignore_null_values=x_ignore_null_values)
except ApiException as e:
    print("Exception when calling AuthenticationApi->update_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_password_input_object** | [**UpdatePasswordInputObject**](UpdatePasswordInputObject.md)|  | 
 **x_ignore_null_values** | **bool**|  | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

