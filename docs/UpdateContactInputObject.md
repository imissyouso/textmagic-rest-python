# UpdateContactInputObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Contact first name | [optional] 
**last_name** | **str** | Contact last name | [optional] 
**phone** | **str** | Contact phone number in E.164 (international) format without leading + or zeroes | 
**email** | **str** | Contact email | [optional] 
**company_name** | **str** | Contact company name | [optional] 
**lists** | **str** | Array of list resources id contact will be assigned to | 
**favorited** | **bool** | Is contact favorited | [optional] 
**blocked** | **bool** | Is contact blocked for outgoing and incoming messaging | [optional] 
**type** | **int** | Force type of phone. Possible values: 0 - landline, 1 - mobile. Default is -1 (auto detection) | [optional] 
**custom_field_values** | **object** |  | [optional] 
**local** | **int** | Treat phone number passed in request body as local | [optional] 
**country** | **str** | 2-letter ISO country code for local phone numbers, used when local is  set to true. Default is account country | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


