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

from cart.models.cart_add_products_request_item import CartAddProductsRequestItem

class TestCartAddProductsRequestItem(unittest.TestCase):
    """CartAddProductsRequestItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CartAddProductsRequestItem:
        """Test CartAddProductsRequestItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CartAddProductsRequestItem`
        """
        model = CartAddProductsRequestItem()
        if include_optional:
            return CartAddProductsRequestItem(
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
                    ]
            )
        else:
            return CartAddProductsRequestItem(
        )
        """

    def testCartAddProductsRequestItem(self):
        """Test CartAddProductsRequestItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
