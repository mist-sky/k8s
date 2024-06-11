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


class V1beta1APIServiceSpec(object):
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
        'ca_bundle': 'str',
        'group': 'str',
        'group_priority_minimum': 'int',
        'insecure_skip_tls_verify': 'bool',
        'service': 'ApiregistrationV1beta1ServiceReference',
        'version': 'str',
        'version_priority': 'int'
    }

    attribute_map = {
        'ca_bundle': 'caBundle',
        'group': 'group',
        'group_priority_minimum': 'groupPriorityMinimum',
        'insecure_skip_tls_verify': 'insecureSkipTLSVerify',
        'service': 'service',
        'version': 'version',
        'version_priority': 'versionPriority'
    }

    def __init__(self, ca_bundle=None, group=None, group_priority_minimum=None, insecure_skip_tls_verify=None, service=None, version=None, version_priority=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1APIServiceSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ca_bundle = None
        self._group = None
        self._group_priority_minimum = None
        self._insecure_skip_tls_verify = None
        self._service = None
        self._version = None
        self._version_priority = None
        self.discriminator = None

        if ca_bundle is not None:
            self.ca_bundle = ca_bundle
        if group is not None:
            self.group = group
        self.group_priority_minimum = group_priority_minimum
        if insecure_skip_tls_verify is not None:
            self.insecure_skip_tls_verify = insecure_skip_tls_verify
        if service is not None:
            self.service = service
        if version is not None:
            self.version = version
        self.version_priority = version_priority

    @property
    def ca_bundle(self):
        """Gets the ca_bundle of this V1beta1APIServiceSpec.  # noqa: E501

        CABundle is a PEM encoded CA bundle which will be used to validate an API server's serving certificate. If unspecified, system trust roots on the apiserver are used.  # noqa: E501

        :return: The ca_bundle of this V1beta1APIServiceSpec.  # noqa: E501
        :rtype: str
        """
        return self._ca_bundle

    @ca_bundle.setter
    def ca_bundle(self, ca_bundle):
        """Sets the ca_bundle of this V1beta1APIServiceSpec.

        CABundle is a PEM encoded CA bundle which will be used to validate an API server's serving certificate. If unspecified, system trust roots on the apiserver are used.  # noqa: E501

        :param ca_bundle: The ca_bundle of this V1beta1APIServiceSpec.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                ca_bundle is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', ca_bundle)):  # noqa: E501
            raise ValueError(r"Invalid value for `ca_bundle`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._ca_bundle = ca_bundle

    @property
    def group(self):
        """Gets the group of this V1beta1APIServiceSpec.  # noqa: E501

        Group is the API group name this server hosts  # noqa: E501

        :return: The group of this V1beta1APIServiceSpec.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this V1beta1APIServiceSpec.

        Group is the API group name this server hosts  # noqa: E501

        :param group: The group of this V1beta1APIServiceSpec.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def group_priority_minimum(self):
        """Gets the group_priority_minimum of this V1beta1APIServiceSpec.  # noqa: E501

        GroupPriorityMininum is the priority this group should have at least. Higher priority means that the group is preferred by clients over lower priority ones. Note that other versions of this group might specify even higher GroupPriorityMininum values such that the whole group gets a higher priority. The primary sort is based on GroupPriorityMinimum, ordered highest number to lowest (20 before 10). The secondary sort is based on the alphabetical comparison of the name of the object.  (v1.bar before v1.foo) We'd recommend something like: *.k8s.io (except extensions) at 18000 and PaaSes (OpenShift, Deis) are recommended to be in the 2000s  # noqa: E501

        :return: The group_priority_minimum of this V1beta1APIServiceSpec.  # noqa: E501
        :rtype: int
        """
        return self._group_priority_minimum

    @group_priority_minimum.setter
    def group_priority_minimum(self, group_priority_minimum):
        """Sets the group_priority_minimum of this V1beta1APIServiceSpec.

        GroupPriorityMininum is the priority this group should have at least. Higher priority means that the group is preferred by clients over lower priority ones. Note that other versions of this group might specify even higher GroupPriorityMininum values such that the whole group gets a higher priority. The primary sort is based on GroupPriorityMinimum, ordered highest number to lowest (20 before 10). The secondary sort is based on the alphabetical comparison of the name of the object.  (v1.bar before v1.foo) We'd recommend something like: *.k8s.io (except extensions) at 18000 and PaaSes (OpenShift, Deis) are recommended to be in the 2000s  # noqa: E501

        :param group_priority_minimum: The group_priority_minimum of this V1beta1APIServiceSpec.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and group_priority_minimum is None:  # noqa: E501
            raise ValueError("Invalid value for `group_priority_minimum`, must not be `None`")  # noqa: E501

        self._group_priority_minimum = group_priority_minimum

    @property
    def insecure_skip_tls_verify(self):
        """Gets the insecure_skip_tls_verify of this V1beta1APIServiceSpec.  # noqa: E501

        InsecureSkipTLSVerify disables TLS certificate verification when communicating with this server. This is strongly discouraged.  You should use the CABundle instead.  # noqa: E501

        :return: The insecure_skip_tls_verify of this V1beta1APIServiceSpec.  # noqa: E501
        :rtype: bool
        """
        return self._insecure_skip_tls_verify

    @insecure_skip_tls_verify.setter
    def insecure_skip_tls_verify(self, insecure_skip_tls_verify):
        """Sets the insecure_skip_tls_verify of this V1beta1APIServiceSpec.

        InsecureSkipTLSVerify disables TLS certificate verification when communicating with this server. This is strongly discouraged.  You should use the CABundle instead.  # noqa: E501

        :param insecure_skip_tls_verify: The insecure_skip_tls_verify of this V1beta1APIServiceSpec.  # noqa: E501
        :type: bool
        """

        self._insecure_skip_tls_verify = insecure_skip_tls_verify

    @property
    def service(self):
        """Gets the service of this V1beta1APIServiceSpec.  # noqa: E501


        :return: The service of this V1beta1APIServiceSpec.  # noqa: E501
        :rtype: ApiregistrationV1beta1ServiceReference
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this V1beta1APIServiceSpec.


        :param service: The service of this V1beta1APIServiceSpec.  # noqa: E501
        :type: ApiregistrationV1beta1ServiceReference
        """

        self._service = service

    @property
    def version(self):
        """Gets the version of this V1beta1APIServiceSpec.  # noqa: E501

        Version is the API version this server hosts.  For example, \"v1\"  # noqa: E501

        :return: The version of this V1beta1APIServiceSpec.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1beta1APIServiceSpec.

        Version is the API version this server hosts.  For example, \"v1\"  # noqa: E501

        :param version: The version of this V1beta1APIServiceSpec.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def version_priority(self):
        """Gets the version_priority of this V1beta1APIServiceSpec.  # noqa: E501

        VersionPriority controls the ordering of this API version inside of its group.  Must be greater than zero. The primary sort is based on VersionPriority, ordered highest to lowest (20 before 10). Since it's inside of a group, the number can be small, probably in the 10s. In case of equal version priorities, the version string will be used to compute the order inside a group. If the version string is \"kube-like\", it will sort above non \"kube-like\" version strings, which are ordered lexicographically. \"Kube-like\" versions start with a \"v\", then are followed by a number (the major version), then optionally the string \"alpha\" or \"beta\" and another number (the minor version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10.  # noqa: E501

        :return: The version_priority of this V1beta1APIServiceSpec.  # noqa: E501
        :rtype: int
        """
        return self._version_priority

    @version_priority.setter
    def version_priority(self, version_priority):
        """Sets the version_priority of this V1beta1APIServiceSpec.

        VersionPriority controls the ordering of this API version inside of its group.  Must be greater than zero. The primary sort is based on VersionPriority, ordered highest to lowest (20 before 10). Since it's inside of a group, the number can be small, probably in the 10s. In case of equal version priorities, the version string will be used to compute the order inside a group. If the version string is \"kube-like\", it will sort above non \"kube-like\" version strings, which are ordered lexicographically. \"Kube-like\" versions start with a \"v\", then are followed by a number (the major version), then optionally the string \"alpha\" or \"beta\" and another number (the minor version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10.  # noqa: E501

        :param version_priority: The version_priority of this V1beta1APIServiceSpec.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and version_priority is None:  # noqa: E501
            raise ValueError("Invalid value for `version_priority`, must not be `None`")  # noqa: E501

        self._version_priority = version_priority

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
        if not isinstance(other, V1beta1APIServiceSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1APIServiceSpec):
            return True

        return self.to_dict() != other.to_dict()
