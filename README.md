# TextMagic Python SDK

Python client for TextMagic API

For detailed documentation, please visit [http://docs.textmagictesting.com/](http://docs.textmagictesting.com/)

## Requirements
Python 2.7 and 3.4+

## Installation

```shell
pip install git+https://github.com/imissyouso/textmagic-rest-python.git@v2.0.315
```

## Usage Example

```python
import TextMagic
from TextMagic.rest import ApiException

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

send_message_input_object = TextMagic.SendMessageInputObject()
send_message_input_object.text = "I love TextMagic!"
send_message_input_object.phones = "+79998887766"

try:
    response = api_instance.send_message(send_message_input_object)
    print(response)
except ApiException as e:
    print("Exception when calling TextMagicApi->send_message: %s\n" % e)
```