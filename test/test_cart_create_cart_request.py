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

from cart.models.cart_create_cart_request import CartCreateCartRequest

class TestCartCreateCartRequest(unittest.TestCase):
    """CartCreateCartRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CartCreateCartRequest:
        """Test CartCreateCartRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CartCreateCartRequest`
        """
        model = CartCreateCartRequest()
        if include_optional:
            return CartCreateCartRequest(
                tenant_id = '',
                channel = '',
                market = '',
                locale = '',
                customer_grn = '',
                currency = 'XXX'
            )
        else:
            return CartCreateCartRequest(
        )
        """

    def testCartCreateCartRequest(self):
        """Test CartCreateCartRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
