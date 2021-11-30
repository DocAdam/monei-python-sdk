# coding: utf-8

"""
    MONEI API v1

    <p>The MONEI API is organized around <a href=\"https://en.wikipedia.org/wiki/Representational_State_Transfer\">REST</a>. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.</p> <h4 id=\"base-url\">Base URL:</h4> <p><a href=\"https://api.monei.com/v1\">https://api.monei.com/v1</a></p> <h4 id=\"client-libraries\">Client libraries:</h4> <ul> <li><a href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li> <li><a href=\"https://postman.monei.com/\">Postman Collection</a></li> </ul>   # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from Monei.configuration import Configuration


class ActivateSubscriptionRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'payment_token': 'str',
        'session_id': 'str',
        'add_amount': 'int',
        'sequence_id': 'str',
        'complete_url': 'str',
        'fail_url': 'str',
        'cancel_url': 'str'
    }

    attribute_map = {
        'payment_token': 'paymentToken',
        'session_id': 'sessionId',
        'add_amount': 'addAmount',
        'sequence_id': 'sequenceId',
        'complete_url': 'completeUrl',
        'fail_url': 'failUrl',
        'cancel_url': 'cancelUrl'
    }

    def __init__(self, payment_token=None, session_id=None, add_amount=None, sequence_id=None, complete_url=None, fail_url=None, cancel_url=None, local_vars_configuration=None):  # noqa: E501
        """ActivateSubscriptionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._payment_token = None
        self._session_id = None
        self._add_amount = None
        self._sequence_id = None
        self._complete_url = None
        self._fail_url = None
        self._cancel_url = None
        self.discriminator = None

        if payment_token is not None:
            self.payment_token = payment_token
        if session_id is not None:
            self.session_id = session_id
        if add_amount is not None:
            self.add_amount = add_amount
        if sequence_id is not None:
            self.sequence_id = sequence_id
        if complete_url is not None:
            self.complete_url = complete_url
        if fail_url is not None:
            self.fail_url = fail_url
        if cancel_url is not None:
            self.cancel_url = cancel_url

    @property
    def payment_token(self):
        """Gets the payment_token of this ActivateSubscriptionRequest.  # noqa: E501

        A payment token generated by monei.js [Components](https://docs.monei.com/docs/monei-js-overview) or a paymentToken [saved after a previous successful payment](https://docs.monei.com/docs/save-payment-method). In case of the first one, you will also need to send the `sessionId` used to generate the token in the first place.   # noqa: E501

        :return: The payment_token of this ActivateSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._payment_token

    @payment_token.setter
    def payment_token(self, payment_token):
        """Sets the payment_token of this ActivateSubscriptionRequest.

        A payment token generated by monei.js [Components](https://docs.monei.com/docs/monei-js-overview) or a paymentToken [saved after a previous successful payment](https://docs.monei.com/docs/save-payment-method). In case of the first one, you will also need to send the `sessionId` used to generate the token in the first place.   # noqa: E501

        :param payment_token: The payment_token of this ActivateSubscriptionRequest.  # noqa: E501
        :type: str
        """

        self._payment_token = payment_token

    @property
    def session_id(self):
        """Gets the session_id of this ActivateSubscriptionRequest.  # noqa: E501

        A unique identifier within your system that adds security to the payment process. You need to pass the same session ID as the one used on the frontend to initialize MONEI Component (if you needed to). This is required if a payment token (not permanent) was already generated in the frontend.   # noqa: E501

        :return: The session_id of this ActivateSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this ActivateSubscriptionRequest.

        A unique identifier within your system that adds security to the payment process. You need to pass the same session ID as the one used on the frontend to initialize MONEI Component (if you needed to). This is required if a payment token (not permanent) was already generated in the frontend.   # noqa: E501

        :param session_id: The session_id of this ActivateSubscriptionRequest.  # noqa: E501
        :type: str
        """

        self._session_id = session_id

    @property
    def add_amount(self):
        """Gets the add_amount of this ActivateSubscriptionRequest.  # noqa: E501

        The amount to be added to the subscription's initial payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge 1.00 USD).   # noqa: E501

        :return: The add_amount of this ActivateSubscriptionRequest.  # noqa: E501
        :rtype: int
        """
        return self._add_amount

    @add_amount.setter
    def add_amount(self, add_amount):
        """Sets the add_amount of this ActivateSubscriptionRequest.

        The amount to be added to the subscription's initial payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge 1.00 USD).   # noqa: E501

        :param add_amount: The add_amount of this ActivateSubscriptionRequest.  # noqa: E501
        :type: int
        """

        self._add_amount = add_amount

    @property
    def sequence_id(self):
        """Gets the sequence_id of this ActivateSubscriptionRequest.  # noqa: E501

        A permanent identifier that refers to the initial payment of a sequence of payments. This value needs to be sent in the path for `RECURRING` payments.   # noqa: E501

        :return: The sequence_id of this ActivateSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._sequence_id

    @sequence_id.setter
    def sequence_id(self, sequence_id):
        """Sets the sequence_id of this ActivateSubscriptionRequest.

        A permanent identifier that refers to the initial payment of a sequence of payments. This value needs to be sent in the path for `RECURRING` payments.   # noqa: E501

        :param sequence_id: The sequence_id of this ActivateSubscriptionRequest.  # noqa: E501
        :type: str
        """

        self._sequence_id = sequence_id

    @property
    def complete_url(self):
        """Gets the complete_url of this ActivateSubscriptionRequest.  # noqa: E501

        The URL the customer will be directed to after transaction completed (successful or failed - except if `failUrl` is provided).   # noqa: E501

        :return: The complete_url of this ActivateSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._complete_url

    @complete_url.setter
    def complete_url(self, complete_url):
        """Sets the complete_url of this ActivateSubscriptionRequest.

        The URL the customer will be directed to after transaction completed (successful or failed - except if `failUrl` is provided).   # noqa: E501

        :param complete_url: The complete_url of this ActivateSubscriptionRequest.  # noqa: E501
        :type: str
        """

        self._complete_url = complete_url

    @property
    def fail_url(self):
        """Gets the fail_url of this ActivateSubscriptionRequest.  # noqa: E501

        The URL the customer will be directed to after transaction has failed, instead of `completeUrl` (used in hosted payment page). This allows to provide two different URLs for successful and failed payments.   # noqa: E501

        :return: The fail_url of this ActivateSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._fail_url

    @fail_url.setter
    def fail_url(self, fail_url):
        """Sets the fail_url of this ActivateSubscriptionRequest.

        The URL the customer will be directed to after transaction has failed, instead of `completeUrl` (used in hosted payment page). This allows to provide two different URLs for successful and failed payments.   # noqa: E501

        :param fail_url: The fail_url of this ActivateSubscriptionRequest.  # noqa: E501
        :type: str
        """

        self._fail_url = fail_url

    @property
    def cancel_url(self):
        """Gets the cancel_url of this ActivateSubscriptionRequest.  # noqa: E501

        The URL the customer will be directed to if they decide to cancel payment and return to your website (used in hosted payment page).   # noqa: E501

        :return: The cancel_url of this ActivateSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._cancel_url

    @cancel_url.setter
    def cancel_url(self, cancel_url):
        """Sets the cancel_url of this ActivateSubscriptionRequest.

        The URL the customer will be directed to if they decide to cancel payment and return to your website (used in hosted payment page).   # noqa: E501

        :param cancel_url: The cancel_url of this ActivateSubscriptionRequest.  # noqa: E501
        :type: str
        """

        self._cancel_url = cancel_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ActivateSubscriptionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActivateSubscriptionRequest):
            return True

        return self.to_dict() != other.to_dict()
