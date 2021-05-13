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


class PaymentShippingDetails(object):
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
        'name': 'str',
        'email': 'str',
        'phone': 'str',
        'company': 'str',
        'address': 'Address'
    }

    attribute_map = {
        'name': 'name',
        'email': 'email',
        'phone': 'phone',
        'company': 'company',
        'address': 'address'
    }

    def __init__(self, name=None, email=None, phone=None, company=None, address=None, local_vars_configuration=None):  # noqa: E501
        """PaymentShippingDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._email = None
        self._phone = None
        self._company = None
        self._address = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if company is not None:
            self.company = company
        if address is not None:
            self.address = address

    @property
    def name(self):
        """Gets the name of this PaymentShippingDetails.  # noqa: E501

        The shipping customer’s full name.  # noqa: E501

        :return: The name of this PaymentShippingDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentShippingDetails.

        The shipping customer’s full name.  # noqa: E501

        :param name: The name of this PaymentShippingDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this PaymentShippingDetails.  # noqa: E501

        The shipping customer’s email address.  # noqa: E501

        :return: The email of this PaymentShippingDetails.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PaymentShippingDetails.

        The shipping customer’s email address.  # noqa: E501

        :param email: The email of this PaymentShippingDetails.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this PaymentShippingDetails.  # noqa: E501

        The shipping customer’s phone number.  # noqa: E501

        :return: The phone of this PaymentShippingDetails.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PaymentShippingDetails.

        The shipping customer’s phone number.  # noqa: E501

        :param phone: The phone of this PaymentShippingDetails.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def company(self):
        """Gets the company of this PaymentShippingDetails.  # noqa: E501

        Name of the company where the shipment is going.  # noqa: E501

        :return: The company of this PaymentShippingDetails.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this PaymentShippingDetails.

        Name of the company where the shipment is going.  # noqa: E501

        :param company: The company of this PaymentShippingDetails.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def address(self):
        """Gets the address of this PaymentShippingDetails.  # noqa: E501


        :return: The address of this PaymentShippingDetails.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PaymentShippingDetails.


        :param address: The address of this PaymentShippingDetails.  # noqa: E501
        :type: Address
        """

        self._address = address

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
        if not isinstance(other, PaymentShippingDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentShippingDetails):
            return True

        return self.to_dict() != other.to_dict()
