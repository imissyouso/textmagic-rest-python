# MessagesIcs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Schedule ID. | 
**next_send** | **datetime** | Next send date in [ISO 8601](https://en.wikipedia.org/?title&#x3D;ISO_8601) format.  | 
**rrule** | **str** | [iCal RRULE](http://www.kanzaki.com/docs/ical/rrule.html) string.  | 
**session** | [**MessageSession**](MessageSession.md) |  | 
**last_sent** | **datetime** | Date and time when last message has been sent. | 
**contact_name** | **str** |  | 
**parameters** | [**MessagesIcsParameters**](MessagesIcsParameters.md) |  | 
**type** | **str** |  | 
**summary** | **str** |  | 
**text_parameters** | [**MessagesIcsTextParameters**](MessagesIcsTextParameters.md) |  | 
**first_occurrence** | **datetime** |  | 
**last_occurrence** | **datetime** |  | 
**recipients_count** | **int** | Amount of actual recipients. | 
**timezone** | **str** | User-friendly timezone name (with spaces replaced by underscores). | 
**completed** | **bool** | Indicates that schedling has been completed. | 
**avatar** | **str** | null | 
**created_at** | **datetime** | Scheduling creation time. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


