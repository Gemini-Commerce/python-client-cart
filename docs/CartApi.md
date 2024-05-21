# cart.CartApi

All URIs are relative to *https://cart.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cart_set_custom_price_on_items**](CartApi.md#cart_set_custom_price_on_items) | **POST** /cart.Cart/SetCustomPriceOnItems | 


# **cart_set_custom_price_on_items**
> object cart_set_custom_price_on_items(body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import cart
from cart.models.cart_set_custom_price_on_items_request import CartSetCustomPriceOnItemsRequest
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
    api_instance = cart.CartApi(api_client)
    body = cart.CartSetCustomPriceOnItemsRequest() # CartSetCustomPriceOnItemsRequest | 

    try:
        api_response = api_instance.cart_set_custom_price_on_items(body)
        print("The response of CartApi->cart_set_custom_price_on_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartApi->cart_set_custom_price_on_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartSetCustomPriceOnItemsRequest**](CartSetCustomPriceOnItemsRequest.md)|  | 

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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

