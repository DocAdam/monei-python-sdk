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


class Card(object):
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
        'number': 'str',
        'cvc': 'str',
        'exp_month': 'str',
        'exp_year': 'str',
        'cardholder_name': 'str',
        'cardholder_email': 'str'
    }

    attribute_map = {
        'number': 'number',
        'cvc': 'cvc',
        'exp_month': 'expMonth',
        'exp_year': 'expYear',
        'cardholder_name': 'cardholderName',
        'cardholder_email': 'cardholderEmail'
    }

    def __init__(self, number=None, cvc=None, exp_month=None, exp_year=None, cardholder_name=None, cardholder_email=None, local_vars_configuration=None):  # noqa: E501
        """Card - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._number = None
        self._cvc = None
        self._exp_month = None
        self._exp_year = None
        self._cardholder_name = None
        self._cardholder_email = None
        self.discriminator = None

        if number is not None:
            self.number = number
        if cvc is not None:
            self.cvc = cvc
        if exp_month is not None:
            self.exp_month = exp_month
        if exp_year is not None:
            self.exp_year = exp_year
        if cardholder_name is not None:
            self.cardholder_name = cardholder_name
        if cardholder_email is not None:
            self.cardholder_email = cardholder_email

    @property
    def number(self):
        """Gets the number of this Card.  # noqa: E501

        The card number, as a string without any separators.  # noqa: E501

        :return: The number of this Card.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Card.

        The card number, as a string without any separators.  # noqa: E501

        :param number: The number of this Card.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def cvc(self):
        """Gets the cvc of this Card.  # noqa: E501

        Card security code.  # noqa: E501

        :return: The cvc of this Card.  # noqa: E501
        :rtype: str
        """
        return self._cvc

    @cvc.setter
    def cvc(self, cvc):
        """Sets the cvc of this Card.

        Card security code.  # noqa: E501

        :param cvc: The cvc of this Card.  # noqa: E501
        :type: str
        """

        self._cvc = cvc

    @property
    def exp_month(self):
        """Gets the exp_month of this Card.  # noqa: E501

        Two-digit number representing the card’s expiration month.  # noqa: E501

        :return: The exp_month of this Card.  # noqa: E501
        :rtype: str
        """
        return self._exp_month

    @exp_month.setter
    def exp_month(self, exp_month):
        """Sets the exp_month of this Card.

        Two-digit number representing the card’s expiration month.  # noqa: E501

        :param exp_month: The exp_month of this Card.  # noqa: E501
        :type: str
        """

        self._exp_month = exp_month

    @property
    def exp_year(self):
        """Gets the exp_year of this Card.  # noqa: E501

        Two-digit number representing the card’s expiration year.  # noqa: E501

        :return: The exp_year of this Card.  # noqa: E501
        :rtype: str
        """
        return self._exp_year

    @exp_year.setter
    def exp_year(self, exp_year):
        """Sets the exp_year of this Card.

        Two-digit number representing the card’s expiration year.  # noqa: E501

        :param exp_year: The exp_year of this Card.  # noqa: E501
        :type: str
        """

        self._exp_year = exp_year

    @property
    def cardholder_name(self):
        """Gets the cardholder_name of this Card.  # noqa: E501

        The cardholder's name, as stated in the credit card.  # noqa: E501

        :return: The cardholder_name of this Card.  # noqa: E501
        :rtype: str
        """
        return self._cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, cardholder_name):
        """Sets the cardholder_name of this Card.

        The cardholder's name, as stated in the credit card.  # noqa: E501

        :param cardholder_name: The cardholder_name of this Card.  # noqa: E501
        :type: str
        """

        self._cardholder_name = cardholder_name

    @property
    def cardholder_email(self):
        """Gets the cardholder_email of this Card.  # noqa: E501

        The cardholder's email address.  # noqa: E501

        :return: The cardholder_email of this Card.  # noqa: E501
        :rtype: str
        """
        return self._cardholder_email

    @cardholder_email.setter
    def cardholder_email(self, cardholder_email):
        """Sets the cardholder_email of this Card.

        The cardholder's email address.  # noqa: E501

        :param cardholder_email: The cardholder_email of this Card.  # noqa: E501
        :type: str
        """

        self._cardholder_email = cardholder_email

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
        if not isinstance(other, Card):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Card):
            return True

        return self.to_dict() != other.to_dict()
