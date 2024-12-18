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

from cart.models.cart_set_shipment_address_request import CartSetShipmentAddressRequest

class TestCartSetShipmentAddressRequest(unittest.TestCase):
    """CartSetShipmentAddressRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CartSetShipmentAddressRequest:
        """Test CartSetShipmentAddressRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CartSetShipmentAddressRequest`
        """
        model = CartSetShipmentAddressRequest()
        if include_optional:
            return CartSetShipmentAddressRequest(
                tenant_id = '',
                cart_id = '',
                address = cart.models.cart_postal_address.cartPostalAddress(
                    revision = 56, 
                    region_code = '', 
                    language_code = '', 
                    postal_code = '', 
                    sorting_code = '', 
                    administrative_area = '', 
                    locality = '', 
                    sublocality = '', 
                    address_lines = [
                        ''
                        ], 
                    recipients = [
                        ''
                        ], 
                    organization = '', 
                    phone_number = '', 
                    additional_info = cart.models.additional_info.additionalInfo(), )
            )
        else:
            return CartSetShipmentAddressRequest(
        )
        """

    def testCartSetShipmentAddressRequest(self):
        """Test CartSetShipmentAddressRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
