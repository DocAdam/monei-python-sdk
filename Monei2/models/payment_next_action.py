# coding: utf-8

"""
    MONEI API v1

    The MONEI API is organized around [REST](https://en.wikipedia.org/wiki/Representational_State_Transfer). Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from Monei.configuration import Configuration


class PaymentNextAction(object):
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
        'type': 'str',
        'must_redirect': 'bool',
        'redirect_url': 'str'
    }

    attribute_map = {
        'type': 'type',
        'must_redirect': 'mustRedirect',
        'redirect_url': 'redirectUrl'
    }

    def __init__(self, type=None, must_redirect=None, redirect_url=None, local_vars_configuration=None):  # noqa: E501
        """PaymentNextAction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._must_redirect = None
        self._redirect_url = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if must_redirect is not None:
            self.must_redirect = must_redirect
        if redirect_url is not None:
            self.redirect_url = redirect_url

    @property
    def type(self):
        """Gets the type of this PaymentNextAction.  # noqa: E501

        - `CONFIRM` - Your customer needs to be redirected to a   [hosted payment page](https://docs.monei.net/docs/use-prebuilt-payment-page)   or confirm payment using   [payment token](https://docs.monei.net/docs/accept-card-payment#3-submitting-the-payment-to-monei-client-side).   The **redirectUrl** will point to the hosted payment page. - `CHALLENGE` - Your customer needs to be redirected to the   3d secure challenge page provided by the bank. The **redirectUrl**   will point to the 3d secure challenge page provided by the bank. - `COMPLETE` - The payment is completed. The **redirectUrl** will be   the **completeUrl** if it was provided when the payment was created.  # noqa: E501

        :return: The type of this PaymentNextAction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PaymentNextAction.

        - `CONFIRM` - Your customer needs to be redirected to a   [hosted payment page](https://docs.monei.net/docs/use-prebuilt-payment-page)   or confirm payment using   [payment token](https://docs.monei.net/docs/accept-card-payment#3-submitting-the-payment-to-monei-client-side).   The **redirectUrl** will point to the hosted payment page. - `CHALLENGE` - Your customer needs to be redirected to the   3d secure challenge page provided by the bank. The **redirectUrl**   will point to the 3d secure challenge page provided by the bank. - `COMPLETE` - The payment is completed. The **redirectUrl** will be   the **completeUrl** if it was provided when the payment was created.  # noqa: E501

        :param type: The type of this PaymentNextAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["CONFIRM", "CHALLENGE", "COMPLETE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def must_redirect(self):
        """Gets the must_redirect of this PaymentNextAction.  # noqa: E501

        If `true` you have to redirect your customer to the **redirectUrl** to continue payment process.  # noqa: E501

        :return: The must_redirect of this PaymentNextAction.  # noqa: E501
        :rtype: bool
        """
        return self._must_redirect

    @must_redirect.setter
    def must_redirect(self, must_redirect):
        """Sets the must_redirect of this PaymentNextAction.

        If `true` you have to redirect your customer to the **redirectUrl** to continue payment process.  # noqa: E501

        :param must_redirect: The must_redirect of this PaymentNextAction.  # noqa: E501
        :type: bool
        """

        self._must_redirect = must_redirect

    @property
    def redirect_url(self):
        """Gets the redirect_url of this PaymentNextAction.  # noqa: E501

        Redirect your customer to this url to continue payment process.  # noqa: E501

        :return: The redirect_url of this PaymentNextAction.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this PaymentNextAction.

        Redirect your customer to this url to continue payment process.  # noqa: E501

        :param redirect_url: The redirect_url of this PaymentNextAction.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

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
        if not isinstance(other, PaymentNextAction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentNextAction):
            return True

        return self.to_dict() != other.to_dict()