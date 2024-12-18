# coding: utf-8

"""
    Cart Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cart.models.cart_add_products_response import CartAddProductsResponse

class TestCartAddProductsResponse(unittest.TestCase):
    """CartAddProductsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CartAddProductsResponse:
        """Test CartAddProductsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CartAddProductsResponse`
        """
        model = CartAddProductsResponse()
        if include_optional:
            return CartAddProductsResponse(
                items = [
                    cart.models.cart_add_products_response_item.cartAddProductsResponseItem(
                        id = '', 
                        product_grn = '', 
                        quantity = 56, 
                        configuration_selections = [
                            cart.models.cart_product_configuration_selection.cartProductConfigurationSelection(
                                step_grn = '', 
                                options = [
                                    cart.models.cart_product_configuration_selection_option.cartProductConfigurationSelectionOption(
                                        grn = '', 
                                        quantity = 56, )
                                    ], )
                            ], )
                    ]
            )
        else:
            return CartAddProductsResponse(
        )
        """

    def testCartAddProductsResponse(self):
        """Test CartAddProductsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
