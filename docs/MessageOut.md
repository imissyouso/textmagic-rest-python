# MessageOut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Message ID. | 
**sender** | **str** | Message sender (phone number or alphanumeric Sender ID). | [optional] 
**receiver** | **str** | Recipient phone number. | [optional] 
**text** | **str** |  | 
**status** | **str** | Delivery status of the message. TODO: Please see the table below to see different delivery statuses.  | 
**contact_id** | **int** |  | 
**session_id** | **int** |  | 
**message_time** | **datetime** | Sending time. | 
**avatar** | **str** |  | 
**deleted** | **bool** |  | [optional] 
**charset** | **str** | Message charset. Could be: *   **ISO-8859-1** for plaintext SMS *   **UTF-16BE** for Unicode SMS  | 
**charset_label** | **str** |  | 
**first_name** | **str** | Contact first name. Could be substituted from your [Contacts](http://docs.textmagictesting.com/#tag/Contacts) (even if you submitted phone number instead of contact ID).  | 
**last_name** | **str** | Contact last name. | 
**country** | **str** | Two-letter ISO country code of the recipient phone number.  | 
**phone** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**parts_count** | **int** | Message parts (multiples of 160 characters) count. | 
**from_email** | **str** |  | [optional] 
**from_number** | **str** |  | [optional] 
**smsc_id** | **str** |  | [optional] 
**contact** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**delivered_count** | **int** |  | [optional] 
**numbers_count** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**credits_price** | **str** |  | [optional] 
**chars** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


