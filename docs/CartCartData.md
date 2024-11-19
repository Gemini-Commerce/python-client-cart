# # CartCartData


## Properties 


Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id**| **str** |   | [optional]
**grn**| **str** |   | [optional]
**channel**| **str** |   | [optional]
**market**| **str** |   | [optional]
**locale**| **str** |   | [optional]
**items**| [**List[CartCartItem]**](CartCartItem.md) |   | [optional]
**payments**| [**List[CartPaymentData]**](CartPaymentData.md) |   | [optional]
**shipments**| [**List[CartShipmentData]**](CartShipmentData.md) |   | [optional]
**promotions**| [**List[CartPromotionData]**](CartPromotionData.md) |   | [optional]
**currency**| [**CartCurrency**](CartCurrency.md) |  for more information please, see Model/CartCurrency.php  | [optional] [default to CartCurrency.XXX]
**subtotals**| [**List[CartCartSubtotal]**](CartCartSubtotal.md) |   | [optional]
**total**| [**CartMoney**](CartMoney.md) |   | [optional]
**total_due**| [**CartMoney**](CartMoney.md) |   | [optional]
**vat_included**| **bool** |   | [optional]
**billing_address**| [**CartPostalAddress**](CartPostalAddress.md) |   | [optional]
**shipping_address**| [**CartPostalAddress**](CartPostalAddress.md) |   | [optional]
**status**| [**CartCartStatus**](CartCartStatus.md) |  for more information please, see Model/CartCartStatus.php  | [optional] [default to CartCartStatus.UNKNOWN]
**customer**| [**CartCustomerData**](CartCustomerData.md) |   | [optional]
**notes**| **str** |   | [optional]
**created_at**| **datetime** |   | [optional]
**updated_at**| **datetime** |   | [optional]


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

