# DoAuthInputObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Account username or email | 
**password** | **str** | Account password | 
**app_name** | **str** | Application name | [optional] 
**app_version** | **str** | Application version | [optional] 
**device_id** | **str** | Device ID for push notification service | [optional] 
**push_service_type** | **str** | required when deviceId provided. Push notification service type: a for Apple Push Notifications, g for Google Cloud Messaging | [optional] 
**tfa_code** | **str** | required when 2FA enabled on account. 2FA challenge response (SMS code or security question answer) | [optional] 
**tfa_id** | **str** | required when 2FA enabled on account. 2FA challenge response (SMS code or security question answer) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


