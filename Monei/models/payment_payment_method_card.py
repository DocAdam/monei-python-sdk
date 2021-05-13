# coding: utf-8

"""
    MONEI API v1

    The MONEI API is organized around [REST](https://en.wikipedia.org/wiki/Representational_State_Transfer). Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs. <br/><br/> **Base URL:** https://api.monei.com/v1 <br/><br/> **Client libraries:** <ul>   <li><a target=\"_blank\" href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li>   <li><a target=\"_blank\" href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li>   <li><a target=\"_blank\" href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li> </ul>  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from Monei.configuration import Configuration


class PaymentPaymentMethodCard(object):
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
        'country': 'str',
        'brand': 'str',
        'type': 'str',
        'three_d_secure': 'bool',
        'three_d_secure_version': 'str',
        'last4': 'str'
    }

    attribute_map = {
        'country': 'country',
        'brand': 'brand',
        'type': 'type',
        'three_d_secure': 'threeDSecure',
        'three_d_secure_version': 'threeDSecureVersion',
        'last4': 'last4'
    }

    def __init__(self, country=None, brand=None, type=None, three_d_secure=None, three_d_secure_version=None, last4=None, local_vars_configuration=None):  # noqa: E501
        """PaymentPaymentMethodCard - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._country = None
        self._brand = None
        self._type = None
        self._three_d_secure = None
        self._three_d_secure_version = None
        self._last4 = None
        self.discriminator = None

        if country is not None:
            self.country = country
        if brand is not None:
            self.brand = brand
        if type is not None:
            self.type = type
        if three_d_secure is not None:
            self.three_d_secure = three_d_secure
        if three_d_secure_version is not None:
            self.three_d_secure_version = three_d_secure_version
        if last4 is not None:
            self.last4 = last4

    @property
    def country(self):
        """Gets the country of this PaymentPaymentMethodCard.  # noqa: E501

        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).  # noqa: E501

        :return: The country of this PaymentPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this PaymentPaymentMethodCard.

        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).  # noqa: E501

        :param country: The country of this PaymentPaymentMethodCard.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def brand(self):
        """Gets the brand of this PaymentPaymentMethodCard.  # noqa: E501

        Card brand.  # noqa: E501

        :return: The brand of this PaymentPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this PaymentPaymentMethodCard.

        Card brand.  # noqa: E501

        :param brand: The brand of this PaymentPaymentMethodCard.  # noqa: E501
        :type: str
        """
        allowed_values = ["visa", "mastercard", "diners", "amex", "jcb", "unionpay", "unknown"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and brand not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `brand` ({0}), must be one of {1}"  # noqa: E501
                .format(brand, allowed_values)
            )

        self._brand = brand

    @property
    def type(self):
        """Gets the type of this PaymentPaymentMethodCard.  # noqa: E501

        Card type `debit` or `credit`.  # noqa: E501

        :return: The type of this PaymentPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PaymentPaymentMethodCard.

        Card type `debit` or `credit`.  # noqa: E501

        :param type: The type of this PaymentPaymentMethodCard.  # noqa: E501
        :type: str
        """
        allowed_values = ["debit", "credit"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def three_d_secure(self):
        """Gets the three_d_secure of this PaymentPaymentMethodCard.  # noqa: E501

        Wether this transaction used 3D Secure authentication.  # noqa: E501

        :return: The three_d_secure of this PaymentPaymentMethodCard.  # noqa: E501
        :rtype: bool
        """
        return self._three_d_secure

    @three_d_secure.setter
    def three_d_secure(self, three_d_secure):
        """Sets the three_d_secure of this PaymentPaymentMethodCard.

        Wether this transaction used 3D Secure authentication.  # noqa: E501

        :param three_d_secure: The three_d_secure of this PaymentPaymentMethodCard.  # noqa: E501
        :type: bool
        """

        self._three_d_secure = three_d_secure

    @property
    def three_d_secure_version(self):
        """Gets the three_d_secure_version of this PaymentPaymentMethodCard.  # noqa: E501

        The protocol version of the 3DS challenge.  # noqa: E501

        :return: The three_d_secure_version of this PaymentPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._three_d_secure_version

    @three_d_secure_version.setter
    def three_d_secure_version(self, three_d_secure_version):
        """Sets the three_d_secure_version of this PaymentPaymentMethodCard.

        The protocol version of the 3DS challenge.  # noqa: E501

        :param three_d_secure_version: The three_d_secure_version of this PaymentPaymentMethodCard.  # noqa: E501
        :type: str
        """

        self._three_d_secure_version = three_d_secure_version

    @property
    def last4(self):
        """Gets the last4 of this PaymentPaymentMethodCard.  # noqa: E501

        The last four digits of the card.  # noqa: E501

        :return: The last4 of this PaymentPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._last4

    @last4.setter
    def last4(self, last4):
        """Sets the last4 of this PaymentPaymentMethodCard.

        The last four digits of the card.  # noqa: E501

        :param last4: The last4 of this PaymentPaymentMethodCard.  # noqa: E501
        :type: str
        """

        self._last4 = last4

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
        if not isinstance(other, PaymentPaymentMethodCard):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentPaymentMethodCard):
            return True

        return self.to_dict() != other.to_dict()
