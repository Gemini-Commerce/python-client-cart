# cart.PaymentsApi

All URIs are relative to *https://cart.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_payment_methods**](PaymentsApi.md#list_payment_methods) | **POST** /cart.Cart/ListPaymentMethods | List Payment Methods
[**set_set_payments**](PaymentsApi.md#set_set_payments) | **POST** /cart.Cart/SetPayments | Set SetPayments


# **list_payment_methods**
> CartListPaymentMethodsResponse list_payment_methods(body)

List Payment Methods

List payment methods

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_list_payment_methods_request import CartListPaymentMethodsRequest
from cart.models.cart_list_payment_methods_response import CartListPaymentMethodsResponse
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
    api_instance = cart.PaymentsApi(api_client)
    body = cart.CartListPaymentMethodsRequest() # CartListPaymentMethodsRequest | 

    try:
        # List Payment Methods
        api_response = api_instance.list_payment_methods(body)
        print("The response of PaymentsApi->list_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->list_payment_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartListPaymentMethodsRequest**](CartListPaymentMethodsRequest.md)|  | 

### Return type

[**CartListPaymentMethodsResponse**](CartListPaymentMethodsResponse.md)

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

# **set_set_payments**
> CartSetPaymentsResponse set_set_payments(body)

Set SetPayments

Set SetPayments

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_set_payments_request import CartSetPaymentsRequest
from cart.models.cart_set_payments_response import CartSetPaymentsResponse
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
    api_instance = cart.PaymentsApi(api_client)
    body = cart.CartSetPaymentsRequest() # CartSetPaymentsRequest | 

    try:
        # Set SetPayments
        api_response = api_instance.set_set_payments(body)
        print("The response of PaymentsApi->set_set_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->set_set_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartSetPaymentsRequest**](CartSetPaymentsRequest.md)|  | 

### Return type

[**CartSetPaymentsResponse**](CartSetPaymentsResponse.md)

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

