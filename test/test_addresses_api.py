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

from cart.api.addresses_api import AddressesApi


class TestAddressesApi(unittest.TestCase):
    """AddressesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AddressesApi()

    def tearDown(self) -> None:
        pass

    def test_set_billing_address(self) -> None:
        """Test case for set_billing_address

        Set Billing Address
        """
        pass

    def test_set_shipment_address(self) -> None:
        """Test case for set_shipment_address

        Set Shipment Address
        """
        pass


if __name__ == '__main__':
    unittest.main()
