# coding: utf-8

"""
    MONEI API v1

    The MONEI API is organized around [REST](https://en.wikipedia.org/wiki/Representational_State_Transfer). Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs. <br/><br/> **Base URL:** https://api.monei.com/v1 <br/><br/> **Client libraries:** <ul>   <li><a target=\"_blank\" href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li>   <li><a target=\"_blank\" href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li>   <li><a target=\"_blank\" href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li>   <li><a target=\"_blank\" href=\"https://postman.monei.com/\">Postman Collection</a></li> </ul>  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import Monei
from Monei.models.activate_subscription_request import ActivateSubscriptionRequest  # noqa: E501
from Monei.rest import ApiException

class TestActivateSubscriptionRequest(unittest.TestCase):
    """ActivateSubscriptionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ActivateSubscriptionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = Monei.models.activate_subscription_request.ActivateSubscriptionRequest()  # noqa: E501
        if include_optional :
            return ActivateSubscriptionRequest(
                payment_token = null, 
                session_id = '39603551437913', 
                add_amount = null, 
                sequence_id = '62b23b9f3627cc38b08ff471ccd313ad', 
                complete_url = 'https://example.com/checkout/complete', 
                fail_url = 'https://example.com/checkout/fail', 
                cancel_url = 'https://example.com/checkout/cancel'
            )
        else :
            return ActivateSubscriptionRequest(
        )

    def testActivateSubscriptionRequest(self):
        """Test ActivateSubscriptionRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()