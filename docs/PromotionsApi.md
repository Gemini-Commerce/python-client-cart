# cart.PromotionsApi

All URIs are relative to *https://cart.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_coupons**](PromotionsApi.md#apply_coupons) | **POST** /cart.Cart/ApplyCoupons | Apply Coupons
[**remove_coupons**](PromotionsApi.md#remove_coupons) | **POST** /cart.Cart/RemoveCoupons | Remove Coupons


# **apply_coupons**
> object apply_coupons(body)

Apply Coupons

Apply coupons to the cart

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_apply_coupons_request import CartApplyCouponsRequest
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
    api_instance = cart.PromotionsApi(api_client)
    body = cart.CartApplyCouponsRequest() # CartApplyCouponsRequest | 

    try:
        # Apply Coupons
        api_response = api_instance.apply_coupons(body)
        print("The response of PromotionsApi->apply_coupons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionsApi->apply_coupons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartApplyCouponsRequest**](CartApplyCouponsRequest.md)|  | 

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

# **remove_coupons**
> object remove_coupons(body)

Remove Coupons

Remove coupons from the cart

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_remove_coupons_request import CartRemoveCouponsRequest
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
    api_instance = cart.PromotionsApi(api_client)
    body = cart.CartRemoveCouponsRequest() # CartRemoveCouponsRequest | 

    try:
        # Remove Coupons
        api_response = api_instance.remove_coupons(body)
        print("The response of PromotionsApi->remove_coupons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionsApi->remove_coupons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartRemoveCouponsRequest**](CartRemoveCouponsRequest.md)|  | 

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

