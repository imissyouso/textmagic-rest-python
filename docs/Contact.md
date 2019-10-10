# Contact

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Contact ID. | 
**favorited** | **bool** | Is the Contact favourite? [Custom fields list](http://docs.textmagictesting.com/#operation/getFavourites). | 
**blocked** | **bool** | Is the Contact blocked? [Custom fields list](http://docs.textmagictesting.com/#operation/getBlockedContacts). | 
**first_name** | **str** | Contact first name. | 
**last_name** | **str** | Contact last name. | 
**company_name** | **str** | Company name. | 
**phone** | **str** | Phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164). | 
**email** | **str** | Contact email address. | 
**country** | [**Country**](Country.md) | Contact country. | 
**custom_fields** | [**list[ContactCustomField]**](ContactCustomField.md) | See [Custom Fields](http://docs.textmagictesting.com/#tag/Custom-Fields) section. | 
**user** | [**User**](User.md) |  | 
**lists** | [**list[List]**](List.md) |  | 
**phone_type** | **str** |  | 
**avatar** | [**ContactImage**](ContactImage.md) |  | 
**notes** | [**list[ContactNote]**](ContactNote.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


