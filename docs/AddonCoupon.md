# AddonCoupon


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**code** | **str** |  | 
**percent** | **float** |  | 
**max_uses** | **int** |  | 
**expires_at** | **datetime** | A future date less than 2 weeks from today | 
**bound_user_id** | **int, none_type** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**addon** | [**Addon**](Addon.md) |  | [optional] 
**bound_user** | [**User**](User.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


