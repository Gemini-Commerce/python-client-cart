# cart_client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.1.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Gemini-Commerce/python-client-cart.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Gemini-Commerce/python-client-cart.git`)

Then import the package:
```python
import cart
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cart
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import cart
from cart.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://cart.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cart.Configuration(
    host = "https://cart.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'


# Enter a context with an instance of the API client
with cart.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cart.AddressesApi(api_client)
    body = cart.CartSetBillingAddressRequest() # CartSetBillingAddressRequest | 

    try:
        # Set Billing Address
        api_response = api_instance.set_billing_address(body)
        print("The response of AddressesApi->set_billing_address:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddressesApi->set_billing_address: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://cart.api.gogemini.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AddressesApi* | [**set_billing_address**](docs/AddressesApi.md#set_billing_address) | **POST** /cart.Cart/SetBillingAddress | Set Billing Address
*AddressesApi* | [**set_shipment_address**](docs/AddressesApi.md#set_shipment_address) | **POST** /cart.Cart/SetShipmentAddress | Set Shipment Address
*BasicOperationsApi* | [**add_products**](docs/BasicOperationsApi.md#add_products) | **POST** /cart.Cart/AddProducts | Add Products
*BasicOperationsApi* | [**create_cart**](docs/BasicOperationsApi.md#create_cart) | **POST** /cart.Cart/CreateCart | Create Cart
*BasicOperationsApi* | [**get_active_cart_by_customer**](docs/BasicOperationsApi.md#get_active_cart_by_customer) | **POST** /cart.Cart/GetActiveCartByCustomer | Get Active Cart By Customer
*BasicOperationsApi* | [**get_cart**](docs/BasicOperationsApi.md#get_cart) | **POST** /cart.Cart/GetCart | Get Cart
*BasicOperationsApi* | [**list_carts**](docs/BasicOperationsApi.md#list_carts) | **POST** /cart.Cart/ListCarts | List Carts
*BasicOperationsApi* | [**merge_carts**](docs/BasicOperationsApi.md#merge_carts) | **POST** /cart.Cart/MergeCarts | Merge Carts
*BasicOperationsApi* | [**remove_products**](docs/BasicOperationsApi.md#remove_products) | **POST** /cart.Cart/RemoveProducts | Remove Products
*BasicOperationsApi* | [**set_additional_info**](docs/BasicOperationsApi.md#set_additional_info) | **POST** /cart.Cart/SetAdditionalInfo | Set Additional Info
*BasicOperationsApi* | [**set_notes**](docs/BasicOperationsApi.md#set_notes) | **POST** /cart.Cart/SetNotes | Set Notes
*BasicOperationsApi* | [**trigger_realignment**](docs/BasicOperationsApi.md#trigger_realignment) | **POST** /cart.Cart/TriggerRealignment | Trigger Realignment
*BasicOperationsApi* | [**update_cart**](docs/BasicOperationsApi.md#update_cart) | **POST** /cart.Cart/UpdateCart | Update Cart
*BasicOperationsApi* | [**update_products**](docs/BasicOperationsApi.md#update_products) | **POST** /cart.Cart/UpdateProducts | Update Products
*CartApi* | [**cart_set_custom_price_on_items**](docs/CartApi.md#cart_set_custom_price_on_items) | **POST** /cart.Cart/SetCustomPriceOnItems | 
*PaymentsApi* | [**list_payment_methods**](docs/PaymentsApi.md#list_payment_methods) | **POST** /cart.Cart/ListPaymentMethods | List Payment Methods
*PaymentsApi* | [**set_set_payments**](docs/PaymentsApi.md#set_set_payments) | **POST** /cart.Cart/SetPayments | Set SetPayments
*PromotionsApi* | [**apply_coupons**](docs/PromotionsApi.md#apply_coupons) | **POST** /cart.Cart/ApplyCoupons | Apply Coupons
*PromotionsApi* | [**remove_coupons**](docs/PromotionsApi.md#remove_coupons) | **POST** /cart.Cart/RemoveCoupons | Remove Coupons
*ShipmentsApi* | [**list_shipment_methods**](docs/ShipmentsApi.md#list_shipment_methods) | **POST** /cart.Cart/ListShipmentMethods | List Shipment Methods
*ShipmentsApi* | [**set_shipments**](docs/ShipmentsApi.md#set_shipments) | **POST** /cart.Cart/SetShipments | Set Shipments


## Documentation For Models

 - [CartAddProductsRequest](docs/CartAddProductsRequest.md)
 - [CartAddProductsRequestItem](docs/CartAddProductsRequestItem.md)
 - [CartAddProductsResponse](docs/CartAddProductsResponse.md)
 - [CartAddProductsResponseItem](docs/CartAddProductsResponseItem.md)
 - [CartApplyCouponsRequest](docs/CartApplyCouponsRequest.md)
 - [CartCartData](docs/CartCartData.md)
 - [CartCartItem](docs/CartCartItem.md)
 - [CartCartStatus](docs/CartCartStatus.md)
 - [CartCartSubtotal](docs/CartCartSubtotal.md)
 - [CartCreateCartRequest](docs/CartCreateCartRequest.md)
 - [CartCreateCartResponse](docs/CartCreateCartResponse.md)
 - [CartCurrency](docs/CartCurrency.md)
 - [CartCustomerData](docs/CartCustomerData.md)
 - [CartGetActiveCartByCustomerRequest](docs/CartGetActiveCartByCustomerRequest.md)
 - [CartGetActiveCartByCustomerResponse](docs/CartGetActiveCartByCustomerResponse.md)
 - [CartGetCartRequest](docs/CartGetCartRequest.md)
 - [CartGetCartResponse](docs/CartGetCartResponse.md)
 - [CartItemCustomPrice](docs/CartItemCustomPrice.md)
 - [CartListCartsRequest](docs/CartListCartsRequest.md)
 - [CartListCartsResponse](docs/CartListCartsResponse.md)
 - [CartListPaymentMethodsRequest](docs/CartListPaymentMethodsRequest.md)
 - [CartListPaymentMethodsResponse](docs/CartListPaymentMethodsResponse.md)
 - [CartListShipmentMethodsRequest](docs/CartListShipmentMethodsRequest.md)
 - [CartListShipmentMethodsResponse](docs/CartListShipmentMethodsResponse.md)
 - [CartLocalizedText](docs/CartLocalizedText.md)
 - [CartMergeCartsRequest](docs/CartMergeCartsRequest.md)
 - [CartMergeCartsResponse](docs/CartMergeCartsResponse.md)
 - [CartMoney](docs/CartMoney.md)
 - [CartPaymentData](docs/CartPaymentData.md)
 - [CartPostalAddress](docs/CartPostalAddress.md)
 - [CartProductConfigurationSelection](docs/CartProductConfigurationSelection.md)
 - [CartProductConfigurationSelectionOption](docs/CartProductConfigurationSelectionOption.md)
 - [CartProductConfigurationStep](docs/CartProductConfigurationStep.md)
 - [CartProductConfigurationStepOption](docs/CartProductConfigurationStepOption.md)
 - [CartPromotionData](docs/CartPromotionData.md)
 - [CartRemoveCouponsRequest](docs/CartRemoveCouponsRequest.md)
 - [CartRemoveProductsRequest](docs/CartRemoveProductsRequest.md)
 - [CartSetAdditionalInfoRequest](docs/CartSetAdditionalInfoRequest.md)
 - [CartSetBillingAddressRequest](docs/CartSetBillingAddressRequest.md)
 - [CartSetCustomPriceOnItemsRequest](docs/CartSetCustomPriceOnItemsRequest.md)
 - [CartSetCustomPriceOnItemsRequestCartItem](docs/CartSetCustomPriceOnItemsRequestCartItem.md)
 - [CartSetNotesRequest](docs/CartSetNotesRequest.md)
 - [CartSetPaymentsRequest](docs/CartSetPaymentsRequest.md)
 - [CartSetPaymentsResponse](docs/CartSetPaymentsResponse.md)
 - [CartSetShipmentAddressRequest](docs/CartSetShipmentAddressRequest.md)
 - [CartSetShipmentsRequest](docs/CartSetShipmentsRequest.md)
 - [CartShipmentData](docs/CartShipmentData.md)
 - [CartSortOrder](docs/CartSortOrder.md)
 - [CartSubtotalCode](docs/CartSubtotalCode.md)
 - [CartTriggerRealignmentRequest](docs/CartTriggerRealignmentRequest.md)
 - [CartTriggerRealignmentResponse](docs/CartTriggerRealignmentResponse.md)
 - [CartUpdateCartRequest](docs/CartUpdateCartRequest.md)
 - [CartUpdateProductsRequest](docs/CartUpdateProductsRequest.md)
 - [CartUpdateProductsRequestItem](docs/CartUpdateProductsRequestItem.md)
 - [ListCartsRequestFilter](docs/ListCartsRequestFilter.md)
 - [ListCartsRequestFilterCartStatus](docs/ListCartsRequestFilterCartStatus.md)
 - [ListCartsRequestFilterDate](docs/ListCartsRequestFilterDate.md)
 - [ListCartsRequestSort](docs/ListCartsRequestSort.md)
 - [OptionImage](docs/OptionImage.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [ProtobufNullValue](docs/ProtobufNullValue.md)
 - [RpcStatus](docs/RpcStatus.md)
 - [SortSortField](docs/SortSortField.md)
 - [UpdateCartRequestPayload](docs/UpdateCartRequestPayload.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Authorization"></a>
### Authorization

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

<a id="standardAuthorization"></a>
### standardAuthorization

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: 
- **Scopes**: N/A


## Author

info@gemini-commerce.com


