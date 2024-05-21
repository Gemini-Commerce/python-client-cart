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

from cart.models.list_carts_request_filter import ListCartsRequestFilter

class TestListCartsRequestFilter(unittest.TestCase):
    """ListCartsRequestFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListCartsRequestFilter:
        """Test ListCartsRequestFilter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListCartsRequestFilter`
        """
        model = ListCartsRequestFilter()
        if include_optional:
            return ListCartsRequestFilter(
                search_terms = [
                    ''
                    ],
                customer_emails = [
                    ''
                    ],
                customer_firstnames = [
                    ''
                    ],
                customer_lastnames = [
                    ''
                    ],
                customer_phones = [
                    ''
                    ],
                cart_ids = [
                    ''
                    ],
                cart_status = 'UNKNOWN',
                created_at = [
                    cart.models.list_carts_request_filter_date.ListCartsRequestFilterDate(
                        from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                agent_grn = ''
            )
        else:
            return ListCartsRequestFilter(
        )
        """

    def testListCartsRequestFilter(self):
        """Test ListCartsRequestFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()