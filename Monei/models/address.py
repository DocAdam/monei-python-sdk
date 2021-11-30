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


class Address(object):
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
        'city': 'str',
        'line1': 'str',
        'line2': 'str',
        'zip': 'str',
        'state': 'str'
    }

    attribute_map = {
        'country': 'country',
        'city': 'city',
        'line1': 'line1',
        'line2': 'line2',
        'zip': 'zip',
        'state': 'state'
    }

    def __init__(self, country=None, city=None, line1=None, line2=None, zip=None, state=None, local_vars_configuration=None):  # noqa: E501
        """Address - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._country = None
        self._city = None
        self._line1 = None
        self._line2 = None
        self._zip = None
        self._state = None
        self.discriminator = None

        if country is not None:
            self.country = country
        if city is not None:
            self.city = city
        if line1 is not None:
            self.line1 = line1
        if line2 is not None:
            self.line2 = line2
        if zip is not None:
            self.zip = zip
        if state is not None:
            self.state = state

    @property
    def country(self):
        """Gets the country of this Address.  # noqa: E501

        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).  # noqa: E501

        :return: The country of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Address.

        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).  # noqa: E501

        :param country: The country of this Address.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501

        City, district, suburb, town, or village.  # noqa: E501

        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.

        City, district, suburb, town, or village.  # noqa: E501

        :param city: The city of this Address.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def line1(self):
        """Gets the line1 of this Address.  # noqa: E501

        Address line 1 (e.g., street, PO Box, or company name).  # noqa: E501

        :return: The line1 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._line1

    @line1.setter
    def line1(self, line1):
        """Sets the line1 of this Address.

        Address line 1 (e.g., street, PO Box, or company name).  # noqa: E501

        :param line1: The line1 of this Address.  # noqa: E501
        :type: str
        """

        self._line1 = line1

    @property
    def line2(self):
        """Gets the line2 of this Address.  # noqa: E501

        Address line 2 (e.g., apartment, suite, unit, or building).  # noqa: E501

        :return: The line2 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._line2

    @line2.setter
    def line2(self, line2):
        """Sets the line2 of this Address.

        Address line 2 (e.g., apartment, suite, unit, or building).  # noqa: E501

        :param line2: The line2 of this Address.  # noqa: E501
        :type: str
        """

        self._line2 = line2

    @property
    def zip(self):
        """Gets the zip of this Address.  # noqa: E501

        ZIP or postal code.  # noqa: E501

        :return: The zip of this Address.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this Address.

        ZIP or postal code.  # noqa: E501

        :param zip: The zip of this Address.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def state(self):
        """Gets the state of this Address.  # noqa: E501

        State, county, province, or region.  # noqa: E501

        :return: The state of this Address.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Address.

        State, county, province, or region.  # noqa: E501

        :param state: The state of this Address.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if not isinstance(other, Address):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Address):
            return True

        return self.to_dict() != other.to_dict()
