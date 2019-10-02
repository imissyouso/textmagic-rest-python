# Conversation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**direction** | **str** | Message type: inbound or outbound.  | 
**sender** | **str** | Sender phone number. | 
**message_time** | **datetime** | Time when message arrived at TextMagic. | 
**text** | **str** | Message text. | 
**receiver** | **str** | Receiver phone number. | 
**status** | **str** | Message status (for chats outbound only). See [message delivery statuses](/docs/api/sms-sessions/#message-delivery-statuses) for details. | 
**first_name** | **str** | Contact first name. | 
**last_name** | **str** | Contact last name. | 
**session_id** | **int** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


