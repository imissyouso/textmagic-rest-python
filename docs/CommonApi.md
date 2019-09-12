# TextMagic.CommonApi

All URIs are relative to *http://my.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_countries**](CommonApi.md#get_countries) | **GET** /api/v2/countries | Return list of countries.
[**get_state**](CommonApi.md#get_state) | **GET** /api/v2/state | Get current entities state
[**get_timezones**](CommonApi.md#get_timezones) | **GET** /api/v2/timezones | Return all available timezone IDs.
[**get_versions**](CommonApi.md#get_versions) | **GET** /api/v2/versions | Get minimal valid apps versions
[**ping**](CommonApi.md#ping) | **GET** /api/v2/ping | Just does a pong.


# **get_countries**
> list[Country] get_countries()

Return list of countries.

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
api_instance = TextMagic.CommonApi(TextMagic.ApiClient(configuration))

try:
    # Return list of countries.
    api_response = api_instance.get_countries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->get_countries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Country]**](Country.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state**
> GetStateResponse get_state()

Get current entities state

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
api_instance = TextMagic.CommonApi(TextMagic.ApiClient(configuration))

try:
    # Get current entities state
    api_response = api_instance.get_state()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->get_state: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetStateResponse**](GetStateResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timezones**
> object get_timezones(full=full)

Return all available timezone IDs.

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
api_instance = TextMagic.CommonApi(TextMagic.ApiClient(configuration))
full = 0 # int | Return full info about timezones in array (0 or 1). Default is 0 (optional) (default to 0)

try:
    # Return all available timezone IDs.
    api_response = api_instance.get_timezones(full=full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->get_timezones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full** | **int**| Return full info about timezones in array (0 or 1). Default is 0 | [optional] [default to 0]

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versions**
> GetVersionsResponse get_versions()

Get minimal valid apps versions

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
api_instance = TextMagic.CommonApi(TextMagic.ApiClient(configuration))

try:
    # Get minimal valid apps versions
    api_response = api_instance.get_versions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->get_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetVersionsResponse**](GetVersionsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping**
> PingResponse ping()

Just does a pong.

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
api_instance = TextMagic.CommonApi(TextMagic.ApiClient(configuration))

try:
    # Just does a pong.
    api_response = api_instance.ping()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->ping: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PingResponse**](PingResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

