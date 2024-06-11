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


class V1beta2LimitResponse(object):
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
        'queuing': 'V1beta2QueuingConfiguration',
        'type': 'str'
    }

    attribute_map = {
        'queuing': 'queuing',
        'type': 'type'
    }

    def __init__(self, queuing=None, type=None, local_vars_configuration=None):  # noqa: E501
        """V1beta2LimitResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._queuing = None
        self._type = None
        self.discriminator = None

        if queuing is not None:
            self.queuing = queuing
        self.type = type

    @property
    def queuing(self):
        """Gets the queuing of this V1beta2LimitResponse.  # noqa: E501


        :return: The queuing of this V1beta2LimitResponse.  # noqa: E501
        :rtype: V1beta2QueuingConfiguration
        """
        return self._queuing

    @queuing.setter
    def queuing(self, queuing):
        """Sets the queuing of this V1beta2LimitResponse.


        :param queuing: The queuing of this V1beta2LimitResponse.  # noqa: E501
        :type: V1beta2QueuingConfiguration
        """

        self._queuing = queuing

    @property
    def type(self):
        """Gets the type of this V1beta2LimitResponse.  # noqa: E501

        `type` is \"Queue\" or \"Reject\". \"Queue\" means that requests that can not be executed upon arrival are held in a queue until they can be executed or a queuing limit is reached. \"Reject\" means that requests that can not be executed upon arrival are rejected. Required.  # noqa: E501

        :return: The type of this V1beta2LimitResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1beta2LimitResponse.

        `type` is \"Queue\" or \"Reject\". \"Queue\" means that requests that can not be executed upon arrival are held in a queue until they can be executed or a queuing limit is reached. \"Reject\" means that requests that can not be executed upon arrival are rejected. Required.  # noqa: E501

        :param type: The type of this V1beta2LimitResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, V1beta2LimitResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta2LimitResponse):
            return True

        return self.to_dict() != other.to_dict()
