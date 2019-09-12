# TextMagic Go SDK

Go client for TextMagic API

For detailed documentation, please visit [http://docs.textmagictesting.com/](http://docs.textmagictesting.com/)

## Installation

```
go get -u github.com/imissyouso/textmagic-rest-go
```

## Usage Example

```go
package main

import (
    "context"
    "fmt"
    "github.com/antihax/optional"
    tm "github.com/imissyouso/textmagic-rest-go"
)

func main() {

    cfg := tm.NewConfiguration()
    cfg.BasePath = "http://localhost"
    client := tm.NewAPIClient(cfg)

    auth := context.WithValue(context.Background(), tm.ContextBasicAuth, tm.BasicAuth{
        UserName: "test",
        Password: "mdwpeFrNGc7GyV1V4J6UJawcp0XTLm",
    })

    sendMessageResponse, _, err := client.TextMagicApi.SendMessage(auth, tm.SendMessageInputObject{
        Text: "I love TextMagic!",
        Phones: "+19998887766",
    }, &tm.SendMessageOpts{})

    if err != nil {
        // handle error
    } else {
        fmt.Println(sendMessageResponse.Id)
    }

    getAllOutboundMessageResponse, _, err := client.TextMagicApi.GetAllOutboundMessages(auth, &tm.GetAllOutboundMessagesOpts{
        Page: optional.NewInt32(1),
        Limit: optional.NewInt32(250),
    })

    if err != nil {
        // handle error
    } else {
        fmt.Println(getAllOutboundMessageResponse.Resources[0].Id)
    }
}
```

## Limitations

Due https://github.com/swagger-api/swagger-codegen/issues/7311 issue current version of Go SDK does not support any file uploading API calls.