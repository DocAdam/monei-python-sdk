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


class UpdateSubscriptionRequest(object):
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
        'amount': 'int',
        'interval': 'SubscriptionInterval',
        'interval_count': 'int',
        'description': 'str',
        'customer': 'PaymentCustomer',
        'billing_details': 'PaymentBillingDetails',
        'shipping_details': 'PaymentShippingDetails',
        'trial_period_end': 'float',
        'callback_url': 'str',
        'payment_callback_url': 'str',
        'pause_at_period_end': 'bool',
        'cancel_at_period_end': 'bool',
        'pause_interval_count': 'int'
    }

    attribute_map = {
        'amount': 'amount',
        'interval': 'interval',
        'interval_count': 'intervalCount',
        'description': 'description',
        'customer': 'customer',
        'billing_details': 'billingDetails',
        'shipping_details': 'shippingDetails',
        'trial_period_end': 'trialPeriodEnd',
        'callback_url': 'callbackUrl',
        'payment_callback_url': 'paymentCallbackUrl',
        'pause_at_period_end': 'pauseAtPeriodEnd',
        'cancel_at_period_end': 'cancelAtPeriodEnd',
        'pause_interval_count': 'pauseIntervalCount'
    }

    def __init__(self, amount=None, interval=None, interval_count=None, description=None, customer=None, billing_details=None, shipping_details=None, trial_period_end=None, callback_url=None, payment_callback_url=None, pause_at_period_end=None, cancel_at_period_end=None, pause_interval_count=None, local_vars_configuration=None):  # noqa: E501
        """UpdateSubscriptionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._interval = None
        self._interval_count = None
        self._description = None
        self._customer = None
        self._billing_details = None
        self._shipping_details = None
        self._trial_period_end = None
        self._callback_url = None
        self._payment_callback_url = None
        self._pause_at_period_end = None
        self._cancel_at_period_end = None
        self._pause_interval_count = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if interval is not None:
            self.interval = interval
        if interval_count is not None:
            self.interval_count = interval_count
        if description is not None:
            self.description = description
        if customer is not None:
            self.customer = customer
        if billing_details is not None:
            self.billing_details = billing_details
        if shipping_details is not None:
            self.shipping_details = shipping_details
        if trial_period_end is not None:
            self.trial_period_end = trial_period_end
        if callback_url is not None:
            self.callback_url = callback_url
        if payment_callback_url is not None:
            self.payment_callback_url = payment_callback_url
        if pause_at_period_end is not None:
            self.pause_at_period_end = pause_at_period_end
        if cancel_at_period_end is not None:
            self.cancel_at_period_end = cancel_at_period_end
        if pause_interval_count is not None:
            self.pause_interval_count = pause_interval_count

    @property
    def amount(self):
        """Gets the amount of this UpdateSubscriptionRequest.  # noqa: E501

        Amount intended to be collected by this payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge 1.00 USD).   # noqa: E501

        :return: The amount of this UpdateSubscriptionRequest.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this UpdateSubscriptionRequest.

        Amount intended to be collected by this payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge 1.00 USD).   # noqa: E501

        :param amount: The amount of this UpdateSubscriptionRequest.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def interval(self):
        """Gets the interval of this UpdateSubscriptionRequest.  # noqa: E501


        :return: The interval of this UpdateSubscriptionRequest.  # noqa: E501
        :rtype: SubscriptionInterval
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this UpdateSubscriptionRequest.


        :param interval: The interval of this UpdateSubscriptionRequest.  # noqa: E501
        :type: SubscriptionInterval
        """

        self._interval = interval

    @property
    def interval_count(self):
        """Gets the interval_count of this UpdateSubscriptionRequest.  # noqa: E501

        Number of intervals between subscription payments.  # noqa: E501

        :return: The interval_count of this UpdateSubscriptionRequest.  # noqa: E501
        :rtype: int
        """
        return self._interval_count

    @interval_count.setter
    def interval_count(self, interval_count):
        """Sets the interval_count of this UpdateSubscriptionRequest.

        Number of intervals between subscription payments.  # noqa: E501

        :param interval_count: The interval_count of this UpdateSubscriptionRequest.  # noqa: E501
        :type: int
        """

        self._interval_count = interval_count

    @property
    def description(self):
        """Gets the description of this UpdateSubscriptionRequest.  # noqa: E501

        An arbitrary string attached to the subscription. Often useful for displaying to users.   # noqa: E501

        :return: The description of this UpdateSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateSubscriptionRequest.

        An arbitrary string attached to the subscription. Often useful for displaying to users.   # noqa: E501

        :param description: The description of this UpdateSubscriptionRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def customer(self):
        """Gets the customer of this UpdateSubscriptionRequest.  # noqa: E501


        :return: The customer of this UpdateSubscriptionRequest.  # noqa: E501
        :rtype: PaymentCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this UpdateSubscriptionRequest.


        :param customer: The customer of this UpdateSubscriptionRequest.  # noqa: E501
        :type: PaymentCustomer
        """

        self._customer = customer

    @property
    def billing_details(self):
        """Gets the billing_details of this UpdateSubscriptionRequest.  # noqa: E501


        :return: The billing_details of this UpdateSubscriptionRequest.  # noqa: E501
        :rtype: PaymentBillingDetails
        """
        return self._billing_details

    @billing_details.setter
    def billing_details(self, billing_details):
        """Sets the billing_details of this UpdateSubscriptionRequest.


        :param billing_details: The billing_details of this UpdateSubscriptionRequest.  # noqa: E501
        :type: PaymentBillingDetails
        """

        self._billing_details = billing_details

    @property
    def shipping_details(self):
        """Gets the shipping_details of this UpdateSubscriptionRequest.  # noqa: E501


        :return: The shipping_details of this UpdateSubscriptionRequest.  # noqa: E501
        :rtype: PaymentShippingDetails
        """
        return self._shipping_details

    @shipping_details.setter
    def shipping_details(self, shipping_details):
        """Sets the shipping_details of this UpdateSubscriptionRequest.


        :param shipping_details: The shipping_details of this UpdateSubscriptionRequest.  # noqa: E501
        :type: PaymentShippingDetails
        """

        self._shipping_details = shipping_details

    @property
    def trial_period_end(self):
        """Gets the trial_period_end of this UpdateSubscriptionRequest.  # noqa: E501

        The end date of the trial period. Measured in seconds since the Unix epoch.  # noqa: E501

        :return: The trial_period_end of this UpdateSubscriptionRequest.  # noqa: E501
        :rtype: float
        """
        return self._trial_period_end

    @trial_period_end.setter
    def trial_period_end(self, trial_period_end):
        """Sets the trial_period_end of this UpdateSubscriptionRequest.

        The end date of the trial period. Measured in seconds since the Unix epoch.  # noqa: E501

        :param trial_period_end: The trial_period_end of this UpdateSubscriptionRequest.  # noqa: E501
        :type: float
        """

        self._trial_period_end = trial_period_end

    @property
    def callback_url(self):
        """Gets the callback_url of this UpdateSubscriptionRequest.  # noqa: E501

        The URL will be called each time subscription status changes.   # noqa: E501

        :return: The callback_url of this UpdateSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this UpdateSubscriptionRequest.

        The URL will be called each time subscription status changes.   # noqa: E501

        :param callback_url: The callback_url of this UpdateSubscriptionRequest.  # noqa: E501
        :type: str
        """

        self._callback_url = callback_url

    @property
    def payment_callback_url(self):
        """Gets the payment_callback_url of this UpdateSubscriptionRequest.  # noqa: E501

        The URL will be called each time subscription creates a new payments.   # noqa: E501

        :return: The payment_callback_url of this UpdateSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._payment_callback_url

    @payment_callback_url.setter
    def payment_callback_url(self, payment_callback_url):
        """Sets the payment_callback_url of this UpdateSubscriptionRequest.

        The URL will be called each time subscription creates a new payments.   # noqa: E501

        :param payment_callback_url: The payment_callback_url of this UpdateSubscriptionRequest.  # noqa: E501
        :type: str
        """

        self._payment_callback_url = payment_callback_url

    @property
    def pause_at_period_end(self):
        """Gets the pause_at_period_end of this UpdateSubscriptionRequest.  # noqa: E501

        If true, the subscription will be paused at the end of the current period.   # noqa: E501

        :return: The pause_at_period_end of this UpdateSubscriptionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._pause_at_period_end

    @pause_at_period_end.setter
    def pause_at_period_end(self, pause_at_period_end):
        """Sets the pause_at_period_end of this UpdateSubscriptionRequest.

        If true, the subscription will be paused at the end of the current period.   # noqa: E501

        :param pause_at_period_end: The pause_at_period_end of this UpdateSubscriptionRequest.  # noqa: E501
        :type: bool
        """

        self._pause_at_period_end = pause_at_period_end

    @property
    def cancel_at_period_end(self):
        """Gets the cancel_at_period_end of this UpdateSubscriptionRequest.  # noqa: E501

        If true, the subscription will be canceled at the end of the current period.   # noqa: E501

        :return: The cancel_at_period_end of this UpdateSubscriptionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._cancel_at_period_end

    @cancel_at_period_end.setter
    def cancel_at_period_end(self, cancel_at_period_end):
        """Sets the cancel_at_period_end of this UpdateSubscriptionRequest.

        If true, the subscription will be canceled at the end of the current period.   # noqa: E501

        :param cancel_at_period_end: The cancel_at_period_end of this UpdateSubscriptionRequest.  # noqa: E501
        :type: bool
        """

        self._cancel_at_period_end = cancel_at_period_end

    @property
    def pause_interval_count(self):
        """Gets the pause_interval_count of this UpdateSubscriptionRequest.  # noqa: E501

        Number of intervals when subscription will be paused before it activates again.  # noqa: E501

        :return: The pause_interval_count of this UpdateSubscriptionRequest.  # noqa: E501
        :rtype: int
        """
        return self._pause_interval_count

    @pause_interval_count.setter
    def pause_interval_count(self, pause_interval_count):
        """Sets the pause_interval_count of this UpdateSubscriptionRequest.

        Number of intervals when subscription will be paused before it activates again.  # noqa: E501

        :param pause_interval_count: The pause_interval_count of this UpdateSubscriptionRequest.  # noqa: E501
        :type: int
        """

        self._pause_interval_count = pause_interval_count

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
        if not isinstance(other, UpdateSubscriptionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateSubscriptionRequest):
            return True

        return self.to_dict() != other.to_dict()
