# coding: utf-8

"""
    MONEI API v1

    <p>The MONEI API is organized around <a href=\"https://en.wikipedia.org/wiki/Representational_State_Transfer\">REST</a>. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.</p> <h4 id=\"base-url\">Base URL:</h4> <p><a href=\"https://api.monei.com/v1\">https://api.monei.com/v1</a></p> <h4 id=\"client-libraries\">Client libraries:</h4> <ul> <li><a href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li> <li><a href=\"https://postman.monei.com/\">Postman Collection</a></li> </ul>   # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from Monei.configuration import Configuration


class PauseSubscriptionRequest(object):
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
        'pause_at_period_end': 'bool',
        'pause_interval_count': 'int'
    }

    attribute_map = {
        'pause_at_period_end': 'pauseAtPeriodEnd',
        'pause_interval_count': 'pauseIntervalCount'
    }

    def __init__(self, pause_at_period_end=None, pause_interval_count=None, local_vars_configuration=None):  # noqa: E501
        """PauseSubscriptionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pause_at_period_end = None
        self._pause_interval_count = None
        self.discriminator = None

        if pause_at_period_end is not None:
            self.pause_at_period_end = pause_at_period_end
        if pause_interval_count is not None:
            self.pause_interval_count = pause_interval_count

    @property
    def pause_at_period_end(self):
        """Gets the pause_at_period_end of this PauseSubscriptionRequest.  # noqa: E501

        If true, the subscription will be paused at the end of the current period.   # noqa: E501

        :return: The pause_at_period_end of this PauseSubscriptionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._pause_at_period_end

    @pause_at_period_end.setter
    def pause_at_period_end(self, pause_at_period_end):
        """Sets the pause_at_period_end of this PauseSubscriptionRequest.

        If true, the subscription will be paused at the end of the current period.   # noqa: E501

        :param pause_at_period_end: The pause_at_period_end of this PauseSubscriptionRequest.  # noqa: E501
        :type: bool
        """

        self._pause_at_period_end = pause_at_period_end

    @property
    def pause_interval_count(self):
        """Gets the pause_interval_count of this PauseSubscriptionRequest.  # noqa: E501

        Number of intervals when subscription will be paused before it activates again.  # noqa: E501

        :return: The pause_interval_count of this PauseSubscriptionRequest.  # noqa: E501
        :rtype: int
        """
        return self._pause_interval_count

    @pause_interval_count.setter
    def pause_interval_count(self, pause_interval_count):
        """Sets the pause_interval_count of this PauseSubscriptionRequest.

        Number of intervals when subscription will be paused before it activates again.  # noqa: E501

        :param pause_interval_count: The pause_interval_count of this PauseSubscriptionRequest.  # noqa: E501
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
        if not isinstance(other, PauseSubscriptionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PauseSubscriptionRequest):
            return True

        return self.to_dict() != other.to_dict()