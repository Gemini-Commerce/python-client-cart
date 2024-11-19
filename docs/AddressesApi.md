# cart.AddressesApi

All URIs are relative to *https://cart.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**set_billing_address**](AddressesApi.md#set_billing_address) | **POST** /cart.Cart/SetBillingAddress | Set Billing Address
[**set_shipment_address**](AddressesApi.md#set_shipment_address) | **POST** /cart.Cart/SetShipmentAddress | Set Shipment Address


# **set_billing_address**
> object set_billing_address(body)

Set Billing Address

Set billing address

### Example

* Api Key Authentication (Authorization):

```python
import cart
from cart.models.cart_set_billing_address_request import CartSetBillingAddressRequest
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
    except Exception as e:
        print("Exception when calling AddressesApi->set_billing_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartSetBillingAddressRequest**](CartSetBillingAddressRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_shipment_address**
> object set_shipment_address(body)

Set Shipment Address

Set shipment address

### Example

* Api Key Authentication (Authorization):

```python
import cart
from cart.models.cart_set_shipment_address_request import CartSetShipmentAddressRequest
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
    body = cart.CartSetShipmentAddressRequest() # CartSetShipmentAddressRequest | 

    try:
        # Set Shipment Address
        api_response = api_instance.set_shipment_address(body)
        print("The response of AddressesApi->set_shipment_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->set_shipment_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartSetShipmentAddressRequest**](CartSetShipmentAddressRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

