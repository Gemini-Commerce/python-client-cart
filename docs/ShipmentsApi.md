# cart.ShipmentsApi

All URIs are relative to *https://cart.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_shipment_methods**](ShipmentsApi.md#list_shipment_methods) | **POST** /cart.Cart/ListShipmentMethods | List Shipment Methods
[**set_shipments**](ShipmentsApi.md#set_shipments) | **POST** /cart.Cart/SetShipments | Set Shipments


# **list_shipment_methods**
> CartListShipmentMethodsResponse list_shipment_methods(body)

List Shipment Methods

List shipment methods

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_list_shipment_methods_request import CartListShipmentMethodsRequest
from cart.models.cart_list_shipment_methods_response import CartListShipmentMethodsResponse
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
    api_instance = cart.ShipmentsApi(api_client)
    body = cart.CartListShipmentMethodsRequest() # CartListShipmentMethodsRequest | 

    try:
        # List Shipment Methods
        api_response = api_instance.list_shipment_methods(body)
        print("The response of ShipmentsApi->list_shipment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentsApi->list_shipment_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartListShipmentMethodsRequest**](CartListShipmentMethodsRequest.md)|  | 

### Return type

[**CartListShipmentMethodsResponse**](CartListShipmentMethodsResponse.md)

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

# **set_shipments**
> object set_shipments(body)

Set Shipments

Set shipments

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_set_shipments_request import CartSetShipmentsRequest
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
    api_instance = cart.ShipmentsApi(api_client)
    body = cart.CartSetShipmentsRequest() # CartSetShipmentsRequest | 

    try:
        # Set Shipments
        api_response = api_instance.set_shipments(body)
        print("The response of ShipmentsApi->set_shipments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentsApi->set_shipments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartSetShipmentsRequest**](CartSetShipmentsRequest.md)|  | 

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
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

