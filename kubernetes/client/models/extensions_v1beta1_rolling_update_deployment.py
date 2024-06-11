# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.17
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class ExtensionsV1beta1RollingUpdateDeployment(object):
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
        'max_surge': 'object',
        'max_unavailable': 'object'
    }

    attribute_map = {
        'max_surge': 'maxSurge',
        'max_unavailable': 'maxUnavailable'
    }

    def __init__(self, max_surge=None, max_unavailable=None, local_vars_configuration=None):  # noqa: E501
        """ExtensionsV1beta1RollingUpdateDeployment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._max_surge = None
        self._max_unavailable = None
        self.discriminator = None

        if max_surge is not None:
            self.max_surge = max_surge
        if max_unavailable is not None:
            self.max_unavailable = max_unavailable

    @property
    def max_surge(self):
        """Gets the max_surge of this ExtensionsV1beta1RollingUpdateDeployment.  # noqa: E501

        The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. By default, a value of 1 is used. Example: when this is set to 30%, the new RC can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new RC can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods.  # noqa: E501

        :return: The max_surge of this ExtensionsV1beta1RollingUpdateDeployment.  # noqa: E501
        :rtype: object
        """
        return self._max_surge

    @max_surge.setter
    def max_surge(self, max_surge):
        """Sets the max_surge of this ExtensionsV1beta1RollingUpdateDeployment.

        The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. By default, a value of 1 is used. Example: when this is set to 30%, the new RC can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new RC can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods.  # noqa: E501

        :param max_surge: The max_surge of this ExtensionsV1beta1RollingUpdateDeployment.  # noqa: E501
        :type: object
        """

        self._max_surge = max_surge

    @property
    def max_unavailable(self):
        """Gets the max_unavailable of this ExtensionsV1beta1RollingUpdateDeployment.  # noqa: E501

        The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. By default, a fixed value of 1 is used. Example: when this is set to 30%, the old RC can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old RC can be scaled down further, followed by scaling up the new RC, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods.  # noqa: E501

        :return: The max_unavailable of this ExtensionsV1beta1RollingUpdateDeployment.  # noqa: E501
        :rtype: object
        """
        return self._max_unavailable

    @max_unavailable.setter
    def max_unavailable(self, max_unavailable):
        """Sets the max_unavailable of this ExtensionsV1beta1RollingUpdateDeployment.

        The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. By default, a fixed value of 1 is used. Example: when this is set to 30%, the old RC can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old RC can be scaled down further, followed by scaling up the new RC, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods.  # noqa: E501

        :param max_unavailable: The max_unavailable of this ExtensionsV1beta1RollingUpdateDeployment.  # noqa: E501
        :type: object
        """

        self._max_unavailable = max_unavailable

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
        if not isinstance(other, ExtensionsV1beta1RollingUpdateDeployment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExtensionsV1beta1RollingUpdateDeployment):
            return True

        return self.to_dict() != other.to_dict()
