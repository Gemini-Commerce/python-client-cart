# cart.BasicOperationsApi

All URIs are relative to *https://cart.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_products**](BasicOperationsApi.md#add_products) | **POST** /cart.Cart/AddProducts | Add Products
[**create_cart**](BasicOperationsApi.md#create_cart) | **POST** /cart.Cart/CreateCart | Create Cart
[**get_active_cart_by_customer**](BasicOperationsApi.md#get_active_cart_by_customer) | **POST** /cart.Cart/GetActiveCartByCustomer | Get Active Cart By Customer
[**get_cart**](BasicOperationsApi.md#get_cart) | **POST** /cart.Cart/GetCart | Get Cart
[**list_carts**](BasicOperationsApi.md#list_carts) | **POST** /cart.Cart/ListCarts | List Carts
[**merge_carts**](BasicOperationsApi.md#merge_carts) | **POST** /cart.Cart/MergeCarts | Merge Carts
[**remove_products**](BasicOperationsApi.md#remove_products) | **POST** /cart.Cart/RemoveProducts | Remove Products
[**set_additional_info**](BasicOperationsApi.md#set_additional_info) | **POST** /cart.Cart/SetAdditionalInfo | Set Additional Info
[**set_notes**](BasicOperationsApi.md#set_notes) | **POST** /cart.Cart/SetNotes | Set Notes
[**trigger_realignment**](BasicOperationsApi.md#trigger_realignment) | **POST** /cart.Cart/TriggerRealignment | Trigger Realignment
[**update_cart**](BasicOperationsApi.md#update_cart) | **POST** /cart.Cart/UpdateCart | Update Cart
[**update_products**](BasicOperationsApi.md#update_products) | **POST** /cart.Cart/UpdateProducts | Update Products


# **add_products**
> CartAddProductsResponse add_products(body)

Add Products

This endpoint allows you to add products to a shopping cart. The AddProducts method enables you to specify the tenantId and cartId to identify the target shopping cart, and provide a list of items to be added.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_add_products_request import CartAddProductsRequest
from cart.models.cart_add_products_response import CartAddProductsResponse
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
    api_instance = cart.BasicOperationsApi(api_client)
    body = cart.CartAddProductsRequest() # CartAddProductsRequest | 

    try:
        # Add Products
        api_response = api_instance.add_products(body)
        print("The response of BasicOperationsApi->add_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->add_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartAddProductsRequest**](CartAddProductsRequest.md)|  | 

### Return type

[**CartAddProductsResponse**](CartAddProductsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cart**
> CartCreateCartResponse create_cart(body)

Create Cart

The CreateCart endpoint allows users to create a new cart for their shopping session. By making a request to this endpoint, users can initiate a new cart and obtain a unique identifier for future cart operations. This endpoint enables seamless cart management and provides a foundation for adding products and performing checkout operations.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_create_cart_request import CartCreateCartRequest
from cart.models.cart_create_cart_response import CartCreateCartResponse
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
    api_instance = cart.BasicOperationsApi(api_client)
    body = cart.CartCreateCartRequest() # CartCreateCartRequest | 

    try:
        # Create Cart
        api_response = api_instance.create_cart(body)
        print("The response of BasicOperationsApi->create_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->create_cart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartCreateCartRequest**](CartCreateCartRequest.md)|  | 

### Return type

[**CartCreateCartResponse**](CartCreateCartResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_cart_by_customer**
> CartGetActiveCartByCustomerResponse get_active_cart_by_customer(body)

Get Active Cart By Customer

Get the active cart by customer

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_get_active_cart_by_customer_request import CartGetActiveCartByCustomerRequest
from cart.models.cart_get_active_cart_by_customer_response import CartGetActiveCartByCustomerResponse
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
    api_instance = cart.BasicOperationsApi(api_client)
    body = cart.CartGetActiveCartByCustomerRequest() # CartGetActiveCartByCustomerRequest | 

    try:
        # Get Active Cart By Customer
        api_response = api_instance.get_active_cart_by_customer(body)
        print("The response of BasicOperationsApi->get_active_cart_by_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->get_active_cart_by_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartGetActiveCartByCustomerRequest**](CartGetActiveCartByCustomerRequest.md)|  | 

### Return type

[**CartGetActiveCartByCustomerResponse**](CartGetActiveCartByCustomerResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart**
> CartGetCartResponse get_cart(body)

Get Cart

Get the cart

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_get_cart_request import CartGetCartRequest
from cart.models.cart_get_cart_response import CartGetCartResponse
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
    api_instance = cart.BasicOperationsApi(api_client)
    body = cart.CartGetCartRequest() # CartGetCartRequest | Get cart request

    try:
        # Get Cart
        api_response = api_instance.get_cart(body)
        print("The response of BasicOperationsApi->get_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->get_cart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartGetCartRequest**](CartGetCartRequest.md)| Get cart request | 

### Return type

[**CartGetCartResponse**](CartGetCartResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_carts**
> CartListCartsResponse list_carts(body)

List Carts

List all carts

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_list_carts_request import CartListCartsRequest
from cart.models.cart_list_carts_response import CartListCartsResponse
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
    api_instance = cart.BasicOperationsApi(api_client)
    body = cart.CartListCartsRequest() # CartListCartsRequest | 

    try:
        # List Carts
        api_response = api_instance.list_carts(body)
        print("The response of BasicOperationsApi->list_carts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->list_carts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartListCartsRequest**](CartListCartsRequest.md)|  | 

### Return type

[**CartListCartsResponse**](CartListCartsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_carts**
> CartMergeCartsResponse merge_carts(body)

Merge Carts

Merge carts

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_merge_carts_request import CartMergeCartsRequest
from cart.models.cart_merge_carts_response import CartMergeCartsResponse
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
    api_instance = cart.BasicOperationsApi(api_client)
    body = cart.CartMergeCartsRequest() # CartMergeCartsRequest | 

    try:
        # Merge Carts
        api_response = api_instance.merge_carts(body)
        print("The response of BasicOperationsApi->merge_carts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->merge_carts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartMergeCartsRequest**](CartMergeCartsRequest.md)|  | 

### Return type

[**CartMergeCartsResponse**](CartMergeCartsResponse.md)

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

# **remove_products**
> object remove_products(body)

Remove Products

Remove products from the cart

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_remove_products_request import CartRemoveProductsRequest
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
    api_instance = cart.BasicOperationsApi(api_client)
    body = cart.CartRemoveProductsRequest() # CartRemoveProductsRequest | 

    try:
        # Remove Products
        api_response = api_instance.remove_products(body)
        print("The response of BasicOperationsApi->remove_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->remove_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartRemoveProductsRequest**](CartRemoveProductsRequest.md)|  | 

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
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_additional_info**
> object set_additional_info(body)

Set Additional Info

Set additional info

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_set_additional_info_request import CartSetAdditionalInfoRequest
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
    api_instance = cart.BasicOperationsApi(api_client)
    body = cart.CartSetAdditionalInfoRequest() # CartSetAdditionalInfoRequest | 

    try:
        # Set Additional Info
        api_response = api_instance.set_additional_info(body)
        print("The response of BasicOperationsApi->set_additional_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->set_additional_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartSetAdditionalInfoRequest**](CartSetAdditionalInfoRequest.md)|  | 

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

# **set_notes**
> object set_notes(body)

Set Notes

Set notes

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_set_notes_request import CartSetNotesRequest
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
    api_instance = cart.BasicOperationsApi(api_client)
    body = cart.CartSetNotesRequest() # CartSetNotesRequest | 

    try:
        # Set Notes
        api_response = api_instance.set_notes(body)
        print("The response of BasicOperationsApi->set_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->set_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartSetNotesRequest**](CartSetNotesRequest.md)|  | 

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

# **trigger_realignment**
> CartTriggerRealignmentResponse trigger_realignment(body)

Trigger Realignment

Trigger realignment

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_trigger_realignment_request import CartTriggerRealignmentRequest
from cart.models.cart_trigger_realignment_response import CartTriggerRealignmentResponse
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
    api_instance = cart.BasicOperationsApi(api_client)
    body = cart.CartTriggerRealignmentRequest() # CartTriggerRealignmentRequest | 

    try:
        # Trigger Realignment
        api_response = api_instance.trigger_realignment(body)
        print("The response of BasicOperationsApi->trigger_realignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->trigger_realignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartTriggerRealignmentRequest**](CartTriggerRealignmentRequest.md)|  | 

### Return type

[**CartTriggerRealignmentResponse**](CartTriggerRealignmentResponse.md)

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

# **update_cart**
> object update_cart(body)

Update Cart

Update the cart

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_update_cart_request import CartUpdateCartRequest
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
    api_instance = cart.BasicOperationsApi(api_client)
    body = cart.CartUpdateCartRequest() # CartUpdateCartRequest | 

    try:
        # Update Cart
        api_response = api_instance.update_cart(body)
        print("The response of BasicOperationsApi->update_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->update_cart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartUpdateCartRequest**](CartUpdateCartRequest.md)|  | 

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
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_products**
> object update_products(body)

Update Products

Update products in the cart

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_update_products_request import CartUpdateProductsRequest
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
    api_instance = cart.BasicOperationsApi(api_client)
    body = cart.CartUpdateProductsRequest() # CartUpdateProductsRequest | 

    try:
        # Update Products
        api_response = api_instance.update_products(body)
        print("The response of BasicOperationsApi->update_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->update_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartUpdateProductsRequest**](CartUpdateProductsRequest.md)|  | 

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
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

