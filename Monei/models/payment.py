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


class Payment(object):
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
        'id': 'str',
        'amount': 'int',
        'currency': 'str',
        'order_id': 'str',
        'description': 'str',
        'account_id': 'str',
        'authorization_code': 'str',
        'livemode': 'bool',
        'status': 'PaymentStatus',
        'status_code': 'str',
        'status_message': 'str',
        'customer': 'PaymentCustomer',
        'shop': 'PaymentShop',
        'billing_details': 'PaymentBillingDetails',
        'shipping_details': 'PaymentShippingDetails',
        'refunded_amount': 'int',
        'last_refund_amount': 'int',
        'last_refund_reason': 'PaymentLastRefundReason',
        'cancellation_reason': 'PaymentCancellationReason',
        'session_details': 'PaymentSessionDetails',
        'trace_details': 'PaymentTraceDetails',
        'payment_token': 'str',
        'payment_method': 'PaymentPaymentMethod',
        'sequence': 'PaymentSequence',
        'sequence_id': 'str',
        'point_of_sale_id': 'str',
        'next_action': 'PaymentNextAction',
        'created_at': 'int',
        'updated_at': 'int'
    }

    attribute_map = {
        'id': 'id',
        'amount': 'amount',
        'currency': 'currency',
        'order_id': 'orderId',
        'description': 'description',
        'account_id': 'accountId',
        'authorization_code': 'authorizationCode',
        'livemode': 'livemode',
        'status': 'status',
        'status_code': 'statusCode',
        'status_message': 'statusMessage',
        'customer': 'customer',
        'shop': 'shop',
        'billing_details': 'billingDetails',
        'shipping_details': 'shippingDetails',
        'refunded_amount': 'refundedAmount',
        'last_refund_amount': 'lastRefundAmount',
        'last_refund_reason': 'lastRefundReason',
        'cancellation_reason': 'cancellationReason',
        'session_details': 'sessionDetails',
        'trace_details': 'traceDetails',
        'payment_token': 'paymentToken',
        'payment_method': 'paymentMethod',
        'sequence': 'sequence',
        'sequence_id': 'sequenceId',
        'point_of_sale_id': 'pointOfSaleId',
        'next_action': 'nextAction',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, id=None, amount=None, currency=None, order_id=None, description=None, account_id=None, authorization_code=None, livemode=None, status=None, status_code=None, status_message=None, customer=None, shop=None, billing_details=None, shipping_details=None, refunded_amount=None, last_refund_amount=None, last_refund_reason=None, cancellation_reason=None, session_details=None, trace_details=None, payment_token=None, payment_method=None, sequence=None, sequence_id=None, point_of_sale_id=None, next_action=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """Payment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._amount = None
        self._currency = None
        self._order_id = None
        self._description = None
        self._account_id = None
        self._authorization_code = None
        self._livemode = None
        self._status = None
        self._status_code = None
        self._status_message = None
        self._customer = None
        self._shop = None
        self._billing_details = None
        self._shipping_details = None
        self._refunded_amount = None
        self._last_refund_amount = None
        self._last_refund_reason = None
        self._cancellation_reason = None
        self._session_details = None
        self._trace_details = None
        self._payment_token = None
        self._payment_method = None
        self._sequence = None
        self._sequence_id = None
        self._point_of_sale_id = None
        self._next_action = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if order_id is not None:
            self.order_id = order_id
        if description is not None:
            self.description = description
        if account_id is not None:
            self.account_id = account_id
        if authorization_code is not None:
            self.authorization_code = authorization_code
        if livemode is not None:
            self.livemode = livemode
        if status is not None:
            self.status = status
        if status_code is not None:
            self.status_code = status_code
        if status_message is not None:
            self.status_message = status_message
        if customer is not None:
            self.customer = customer
        if shop is not None:
            self.shop = shop
        if billing_details is not None:
            self.billing_details = billing_details
        if shipping_details is not None:
            self.shipping_details = shipping_details
        if refunded_amount is not None:
            self.refunded_amount = refunded_amount
        if last_refund_amount is not None:
            self.last_refund_amount = last_refund_amount
        if last_refund_reason is not None:
            self.last_refund_reason = last_refund_reason
        if cancellation_reason is not None:
            self.cancellation_reason = cancellation_reason
        if session_details is not None:
            self.session_details = session_details
        if trace_details is not None:
            self.trace_details = trace_details
        if payment_token is not None:
            self.payment_token = payment_token
        if payment_method is not None:
            self.payment_method = payment_method
        if sequence is not None:
            self.sequence = sequence
        if sequence_id is not None:
            self.sequence_id = sequence_id
        if point_of_sale_id is not None:
            self.point_of_sale_id = point_of_sale_id
        if next_action is not None:
            self.next_action = next_action
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Payment.  # noqa: E501

        Unique identifier for the payment.  # noqa: E501

        :return: The id of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Payment.

        Unique identifier for the payment.  # noqa: E501

        :param id: The id of this Payment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def amount(self):
        """Gets the amount of this Payment.  # noqa: E501

        Amount intended to be collected by this payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge 1.00 USD).   # noqa: E501

        :return: The amount of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Payment.

        Amount intended to be collected by this payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge 1.00 USD).   # noqa: E501

        :param amount: The amount of this Payment.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this Payment.  # noqa: E501

        Three-letter [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217), in uppercase. Must be a supported currency.   # noqa: E501

        :return: The currency of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Payment.

        Three-letter [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217), in uppercase. Must be a supported currency.   # noqa: E501

        :param currency: The currency of this Payment.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def order_id(self):
        """Gets the order_id of this Payment.  # noqa: E501

        An order ID from your system. A unique identifier that can be used to reconcile the payment with your internal system.   # noqa: E501

        :return: The order_id of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Payment.

        An order ID from your system. A unique identifier that can be used to reconcile the payment with your internal system.   # noqa: E501

        :param order_id: The order_id of this Payment.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def description(self):
        """Gets the description of this Payment.  # noqa: E501

        An arbitrary string attached to the payment. Often useful for displaying to users.   # noqa: E501

        :return: The description of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Payment.

        An arbitrary string attached to the payment. Often useful for displaying to users.   # noqa: E501

        :param description: The description of this Payment.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def account_id(self):
        """Gets the account_id of this Payment.  # noqa: E501

        MONEI Account identifier.  # noqa: E501

        :return: The account_id of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Payment.

        MONEI Account identifier.  # noqa: E501

        :param account_id: The account_id of this Payment.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def authorization_code(self):
        """Gets the authorization_code of this Payment.  # noqa: E501

        Unique identifier provided by the bank performing transaction.   # noqa: E501

        :return: The authorization_code of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._authorization_code

    @authorization_code.setter
    def authorization_code(self, authorization_code):
        """Sets the authorization_code of this Payment.

        Unique identifier provided by the bank performing transaction.   # noqa: E501

        :param authorization_code: The authorization_code of this Payment.  # noqa: E501
        :type: str
        """

        self._authorization_code = authorization_code

    @property
    def livemode(self):
        """Gets the livemode of this Payment.  # noqa: E501

        Has the value `true` if the resource exists in live mode or the value `false` if the resource exists in test mode.  # noqa: E501

        :return: The livemode of this Payment.  # noqa: E501
        :rtype: bool
        """
        return self._livemode

    @livemode.setter
    def livemode(self, livemode):
        """Sets the livemode of this Payment.

        Has the value `true` if the resource exists in live mode or the value `false` if the resource exists in test mode.  # noqa: E501

        :param livemode: The livemode of this Payment.  # noqa: E501
        :type: bool
        """

        self._livemode = livemode

    @property
    def status(self):
        """Gets the status of this Payment.  # noqa: E501


        :return: The status of this Payment.  # noqa: E501
        :rtype: PaymentStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Payment.


        :param status: The status of this Payment.  # noqa: E501
        :type: PaymentStatus
        """

        self._status = status

    @property
    def status_code(self):
        """Gets the status_code of this Payment.  # noqa: E501

        Payment status code.   # noqa: E501

        :return: The status_code of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this Payment.

        Payment status code.   # noqa: E501

        :param status_code: The status_code of this Payment.  # noqa: E501
        :type: str
        """

        self._status_code = status_code

    @property
    def status_message(self):
        """Gets the status_message of this Payment.  # noqa: E501

        Human readable status message, can be displayed to a user.   # noqa: E501

        :return: The status_message of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this Payment.

        Human readable status message, can be displayed to a user.   # noqa: E501

        :param status_message: The status_message of this Payment.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    @property
    def customer(self):
        """Gets the customer of this Payment.  # noqa: E501


        :return: The customer of this Payment.  # noqa: E501
        :rtype: PaymentCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this Payment.


        :param customer: The customer of this Payment.  # noqa: E501
        :type: PaymentCustomer
        """

        self._customer = customer

    @property
    def shop(self):
        """Gets the shop of this Payment.  # noqa: E501


        :return: The shop of this Payment.  # noqa: E501
        :rtype: PaymentShop
        """
        return self._shop

    @shop.setter
    def shop(self, shop):
        """Sets the shop of this Payment.


        :param shop: The shop of this Payment.  # noqa: E501
        :type: PaymentShop
        """

        self._shop = shop

    @property
    def billing_details(self):
        """Gets the billing_details of this Payment.  # noqa: E501


        :return: The billing_details of this Payment.  # noqa: E501
        :rtype: PaymentBillingDetails
        """
        return self._billing_details

    @billing_details.setter
    def billing_details(self, billing_details):
        """Sets the billing_details of this Payment.


        :param billing_details: The billing_details of this Payment.  # noqa: E501
        :type: PaymentBillingDetails
        """

        self._billing_details = billing_details

    @property
    def shipping_details(self):
        """Gets the shipping_details of this Payment.  # noqa: E501


        :return: The shipping_details of this Payment.  # noqa: E501
        :rtype: PaymentShippingDetails
        """
        return self._shipping_details

    @shipping_details.setter
    def shipping_details(self, shipping_details):
        """Sets the shipping_details of this Payment.


        :param shipping_details: The shipping_details of this Payment.  # noqa: E501
        :type: PaymentShippingDetails
        """

        self._shipping_details = shipping_details

    @property
    def refunded_amount(self):
        """Gets the refunded_amount of this Payment.  # noqa: E501

        Amount in cents refunded (can be less than the amount attribute on the payment if a partial refund was issued).   # noqa: E501

        :return: The refunded_amount of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._refunded_amount

    @refunded_amount.setter
    def refunded_amount(self, refunded_amount):
        """Sets the refunded_amount of this Payment.

        Amount in cents refunded (can be less than the amount attribute on the payment if a partial refund was issued).   # noqa: E501

        :param refunded_amount: The refunded_amount of this Payment.  # noqa: E501
        :type: int
        """

        self._refunded_amount = refunded_amount

    @property
    def last_refund_amount(self):
        """Gets the last_refund_amount of this Payment.  # noqa: E501

        Amount in cents refunded in the last transaction.  # noqa: E501

        :return: The last_refund_amount of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._last_refund_amount

    @last_refund_amount.setter
    def last_refund_amount(self, last_refund_amount):
        """Sets the last_refund_amount of this Payment.

        Amount in cents refunded in the last transaction.  # noqa: E501

        :param last_refund_amount: The last_refund_amount of this Payment.  # noqa: E501
        :type: int
        """

        self._last_refund_amount = last_refund_amount

    @property
    def last_refund_reason(self):
        """Gets the last_refund_reason of this Payment.  # noqa: E501


        :return: The last_refund_reason of this Payment.  # noqa: E501
        :rtype: PaymentLastRefundReason
        """
        return self._last_refund_reason

    @last_refund_reason.setter
    def last_refund_reason(self, last_refund_reason):
        """Sets the last_refund_reason of this Payment.


        :param last_refund_reason: The last_refund_reason of this Payment.  # noqa: E501
        :type: PaymentLastRefundReason
        """

        self._last_refund_reason = last_refund_reason

    @property
    def cancellation_reason(self):
        """Gets the cancellation_reason of this Payment.  # noqa: E501


        :return: The cancellation_reason of this Payment.  # noqa: E501
        :rtype: PaymentCancellationReason
        """
        return self._cancellation_reason

    @cancellation_reason.setter
    def cancellation_reason(self, cancellation_reason):
        """Sets the cancellation_reason of this Payment.


        :param cancellation_reason: The cancellation_reason of this Payment.  # noqa: E501
        :type: PaymentCancellationReason
        """

        self._cancellation_reason = cancellation_reason

    @property
    def session_details(self):
        """Gets the session_details of this Payment.  # noqa: E501


        :return: The session_details of this Payment.  # noqa: E501
        :rtype: PaymentSessionDetails
        """
        return self._session_details

    @session_details.setter
    def session_details(self, session_details):
        """Sets the session_details of this Payment.


        :param session_details: The session_details of this Payment.  # noqa: E501
        :type: PaymentSessionDetails
        """

        self._session_details = session_details

    @property
    def trace_details(self):
        """Gets the trace_details of this Payment.  # noqa: E501


        :return: The trace_details of this Payment.  # noqa: E501
        :rtype: PaymentTraceDetails
        """
        return self._trace_details

    @trace_details.setter
    def trace_details(self, trace_details):
        """Sets the trace_details of this Payment.


        :param trace_details: The trace_details of this Payment.  # noqa: E501
        :type: PaymentTraceDetails
        """

        self._trace_details = trace_details

    @property
    def payment_token(self):
        """Gets the payment_token of this Payment.  # noqa: E501

        A permanent token represents a payment method used in the payment. Pass `generatePaymentToken: true` when you creating a payment to generate it. You can pass it as `paymentToken` parameter to create other payments with the same payment method. This token does not expire, and should only be used server-side.   # noqa: E501

        :return: The payment_token of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._payment_token

    @payment_token.setter
    def payment_token(self, payment_token):
        """Sets the payment_token of this Payment.

        A permanent token represents a payment method used in the payment. Pass `generatePaymentToken: true` when you creating a payment to generate it. You can pass it as `paymentToken` parameter to create other payments with the same payment method. This token does not expire, and should only be used server-side.   # noqa: E501

        :param payment_token: The payment_token of this Payment.  # noqa: E501
        :type: str
        """

        self._payment_token = payment_token

    @property
    def payment_method(self):
        """Gets the payment_method of this Payment.  # noqa: E501


        :return: The payment_method of this Payment.  # noqa: E501
        :rtype: PaymentPaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this Payment.


        :param payment_method: The payment_method of this Payment.  # noqa: E501
        :type: PaymentPaymentMethod
        """

        self._payment_method = payment_method

    @property
    def sequence(self):
        """Gets the sequence of this Payment.  # noqa: E501


        :return: The sequence of this Payment.  # noqa: E501
        :rtype: PaymentSequence
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this Payment.


        :param sequence: The sequence of this Payment.  # noqa: E501
        :type: PaymentSequence
        """

        self._sequence = sequence

    @property
    def sequence_id(self):
        """Gets the sequence_id of this Payment.  # noqa: E501

        A permanent identifier that refers to the initial payment of a sequence of payments. This value needs to be sent in the path for `RECURRING` payments.   # noqa: E501

        :return: The sequence_id of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._sequence_id

    @sequence_id.setter
    def sequence_id(self, sequence_id):
        """Sets the sequence_id of this Payment.

        A permanent identifier that refers to the initial payment of a sequence of payments. This value needs to be sent in the path for `RECURRING` payments.   # noqa: E501

        :param sequence_id: The sequence_id of this Payment.  # noqa: E501
        :type: str
        """

        self._sequence_id = sequence_id

    @property
    def point_of_sale_id(self):
        """Gets the point_of_sale_id of this Payment.  # noqa: E501

        A unique identifier of the Point of Sale. If specified the payment is attached to this Point of Sale. If there is a QR code attached to the same Point of Sale, this payment will be available by scanning the QR code.   # noqa: E501

        :return: The point_of_sale_id of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._point_of_sale_id

    @point_of_sale_id.setter
    def point_of_sale_id(self, point_of_sale_id):
        """Sets the point_of_sale_id of this Payment.

        A unique identifier of the Point of Sale. If specified the payment is attached to this Point of Sale. If there is a QR code attached to the same Point of Sale, this payment will be available by scanning the QR code.   # noqa: E501

        :param point_of_sale_id: The point_of_sale_id of this Payment.  # noqa: E501
        :type: str
        """

        self._point_of_sale_id = point_of_sale_id

    @property
    def next_action(self):
        """Gets the next_action of this Payment.  # noqa: E501


        :return: The next_action of this Payment.  # noqa: E501
        :rtype: PaymentNextAction
        """
        return self._next_action

    @next_action.setter
    def next_action(self, next_action):
        """Sets the next_action of this Payment.


        :param next_action: The next_action of this Payment.  # noqa: E501
        :type: PaymentNextAction
        """

        self._next_action = next_action

    @property
    def created_at(self):
        """Gets the created_at of this Payment.  # noqa: E501

        Time at which the resource was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :return: The created_at of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Payment.

        Time at which the resource was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :param created_at: The created_at of this Payment.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Payment.  # noqa: E501

        Time at which the resource updated last time. Measured in seconds since the Unix epoch.  # noqa: E501

        :return: The updated_at of this Payment.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Payment.

        Time at which the resource updated last time. Measured in seconds since the Unix epoch.  # noqa: E501

        :param updated_at: The updated_at of this Payment.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

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
        if not isinstance(other, Payment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Payment):
            return True

        return self.to_dict() != other.to_dict()
