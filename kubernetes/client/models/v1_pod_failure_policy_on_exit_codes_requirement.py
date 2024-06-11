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


class V1PodFailurePolicyOnExitCodesRequirement(object):
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
        'container_name': 'str',
        'operator': 'str',
        'values': 'list[int]'
    }

    attribute_map = {
        'container_name': 'containerName',
        'operator': 'operator',
        'values': 'values'
    }

    def __init__(self, container_name=None, operator=None, values=None, local_vars_configuration=None):  # noqa: E501
        """V1PodFailurePolicyOnExitCodesRequirement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._container_name = None
        self._operator = None
        self._values = None
        self.discriminator = None

        if container_name is not None:
            self.container_name = container_name
        self.operator = operator
        self.values = values

    @property
    def container_name(self):
        """Gets the container_name of this V1PodFailurePolicyOnExitCodesRequirement.  # noqa: E501

        Restricts the check for exit codes to the container with the specified name. When null, the rule applies to all containers. When specified, it should match one the container or initContainer names in the pod template.  # noqa: E501

        :return: The container_name of this V1PodFailurePolicyOnExitCodesRequirement.  # noqa: E501
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this V1PodFailurePolicyOnExitCodesRequirement.

        Restricts the check for exit codes to the container with the specified name. When null, the rule applies to all containers. When specified, it should match one the container or initContainer names in the pod template.  # noqa: E501

        :param container_name: The container_name of this V1PodFailurePolicyOnExitCodesRequirement.  # noqa: E501
        :type: str
        """

        self._container_name = container_name

    @property
    def operator(self):
        """Gets the operator of this V1PodFailurePolicyOnExitCodesRequirement.  # noqa: E501

        Represents the relationship between the container exit code(s) and the specified values. Containers completed with success (exit code 0) are excluded from the requirement check. Possible values are:  - In: the requirement is satisfied if at least one container exit code   (might be multiple if there are multiple containers not restricted   by the 'containerName' field) is in the set of specified values. - NotIn: the requirement is satisfied if at least one container exit code   (might be multiple if there are multiple containers not restricted   by the 'containerName' field) is not in the set of specified values. Additional values are considered to be added in the future. Clients should react to an unknown operator by assuming the requirement is not satisfied.  # noqa: E501

        :return: The operator of this V1PodFailurePolicyOnExitCodesRequirement.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this V1PodFailurePolicyOnExitCodesRequirement.

        Represents the relationship between the container exit code(s) and the specified values. Containers completed with success (exit code 0) are excluded from the requirement check. Possible values are:  - In: the requirement is satisfied if at least one container exit code   (might be multiple if there are multiple containers not restricted   by the 'containerName' field) is in the set of specified values. - NotIn: the requirement is satisfied if at least one container exit code   (might be multiple if there are multiple containers not restricted   by the 'containerName' field) is not in the set of specified values. Additional values are considered to be added in the future. Clients should react to an unknown operator by assuming the requirement is not satisfied.  # noqa: E501

        :param operator: The operator of this V1PodFailurePolicyOnExitCodesRequirement.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and operator is None:  # noqa: E501
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

    @property
    def values(self):
        """Gets the values of this V1PodFailurePolicyOnExitCodesRequirement.  # noqa: E501

        Specifies the set of values. Each returned container exit code (might be multiple in case of multiple containers) is checked against this set of values with respect to the operator. The list of values must be ordered and must not contain duplicates. Value '0' cannot be used for the In operator. At least one element is required. At most 255 elements are allowed.  # noqa: E501

        :return: The values of this V1PodFailurePolicyOnExitCodesRequirement.  # noqa: E501
        :rtype: list[int]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this V1PodFailurePolicyOnExitCodesRequirement.

        Specifies the set of values. Each returned container exit code (might be multiple in case of multiple containers) is checked against this set of values with respect to the operator. The list of values must be ordered and must not contain duplicates. Value '0' cannot be used for the In operator. At least one element is required. At most 255 elements are allowed.  # noqa: E501

        :param values: The values of this V1PodFailurePolicyOnExitCodesRequirement.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and values is None:  # noqa: E501
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

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
        if not isinstance(other, V1PodFailurePolicyOnExitCodesRequirement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1PodFailurePolicyOnExitCodesRequirement):
            return True

        return self.to_dict() != other.to_dict()
