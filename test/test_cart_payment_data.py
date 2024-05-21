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

from cart.models.cart_payment_data import CartPaymentData

class TestCartPaymentData(unittest.TestCase):
    """CartPaymentData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CartPaymentData:
        """Test CartPaymentData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CartPaymentData`
        """
        model = CartPaymentData()
        if include_optional:
            return CartPaymentData(
                code = '',
                title = cart.models.cart_localized_text.cartLocalizedText(
                    value = {
                        'key' : ''
                        }, ),
                payload = '',
                fee = cart.models.cart_money.cartMoney(
                    units = '', 
                    micros = 56, ),
                amount = cart.models.cart_money.cartMoney(
                    units = '', 
                    micros = 56, ),
                label = cart.models.cart_localized_text.cartLocalizedText(
                    value = {
                        'key' : ''
                        }, ),
                description = cart.models.cart_localized_text.cartLocalizedText(
                    value = {
                        'key' : ''
                        }, ),
                vat_amount = cart.models.cart_money.cartMoney(
                    units = '', 
                    micros = 56, ),
                vat_percentage = 1.337,
                vat_inaccurate = True,
                vat_calculated = True,
                is_upfront = True
            )
        else:
            return CartPaymentData(
        )
        """

    def testCartPaymentData(self):
        """Test CartPaymentData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()