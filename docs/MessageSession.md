# MessageSession

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Session ID. | 
**start_time** | **str** | Session creation time. | 
**text** | **str** | Session text. If a template was used for the session text (see [Messages: Send](#tag/Outbound-Messages) for details), it may contain template tags.  | 
**source** | **str** | *   **O** for TextMagic Online *   **A** for API *   **M** for TextMagic Messenger *   **E** for [Email to SMS](/docs/api/send-email-to-sms/) *   **X** for [Distribution lists](/docs/api/distribution-lists/)  | 
**reference_id** | **str** | Custom reference ID (see [Messages: Send](/docs/api/send-sms/) for details).  | 
**price** | **float** | Session cost (in account currency). | 
**numbers_count** | **int** | Session recipient count. | 
**destination** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


