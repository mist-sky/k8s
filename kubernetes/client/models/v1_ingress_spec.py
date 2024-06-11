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


class V1IngressSpec(object):
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
        'default_backend': 'V1IngressBackend',
        'ingress_class_name': 'str',
        'rules': 'list[V1IngressRule]',
        'tls': 'list[V1IngressTLS]'
    }

    attribute_map = {
        'default_backend': 'defaultBackend',
        'ingress_class_name': 'ingressClassName',
        'rules': 'rules',
        'tls': 'tls'
    }

    def __init__(self, default_backend=None, ingress_class_name=None, rules=None, tls=None, local_vars_configuration=None):  # noqa: E501
        """V1IngressSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._default_backend = None
        self._ingress_class_name = None
        self._rules = None
        self._tls = None
        self.discriminator = None

        if default_backend is not None:
            self.default_backend = default_backend
        if ingress_class_name is not None:
            self.ingress_class_name = ingress_class_name
        if rules is not None:
            self.rules = rules
        if tls is not None:
            self.tls = tls

    @property
    def default_backend(self):
        """Gets the default_backend of this V1IngressSpec.  # noqa: E501


        :return: The default_backend of this V1IngressSpec.  # noqa: E501
        :rtype: V1IngressBackend
        """
        return self._default_backend

    @default_backend.setter
    def default_backend(self, default_backend):
        """Sets the default_backend of this V1IngressSpec.


        :param default_backend: The default_backend of this V1IngressSpec.  # noqa: E501
        :type: V1IngressBackend
        """

        self._default_backend = default_backend

    @property
    def ingress_class_name(self):
        """Gets the ingress_class_name of this V1IngressSpec.  # noqa: E501

        ingressClassName is the name of an IngressClass cluster resource. Ingress controller implementations use this field to know whether they should be serving this Ingress resource, by a transitive connection (controller -> IngressClass -> Ingress resource). Although the `kubernetes.io/ingress.class` annotation (simple constant name) was never formally defined, it was widely supported by Ingress controllers to create a direct binding between Ingress controller and Ingress resources. Newly created Ingress resources should prefer using the field. However, even though the annotation is officially deprecated, for backwards compatibility reasons, ingress controllers should still honor that annotation if present.  # noqa: E501

        :return: The ingress_class_name of this V1IngressSpec.  # noqa: E501
        :rtype: str
        """
        return self._ingress_class_name

    @ingress_class_name.setter
    def ingress_class_name(self, ingress_class_name):
        """Sets the ingress_class_name of this V1IngressSpec.

        ingressClassName is the name of an IngressClass cluster resource. Ingress controller implementations use this field to know whether they should be serving this Ingress resource, by a transitive connection (controller -> IngressClass -> Ingress resource). Although the `kubernetes.io/ingress.class` annotation (simple constant name) was never formally defined, it was widely supported by Ingress controllers to create a direct binding between Ingress controller and Ingress resources. Newly created Ingress resources should prefer using the field. However, even though the annotation is officially deprecated, for backwards compatibility reasons, ingress controllers should still honor that annotation if present.  # noqa: E501

        :param ingress_class_name: The ingress_class_name of this V1IngressSpec.  # noqa: E501
        :type: str
        """

        self._ingress_class_name = ingress_class_name

    @property
    def rules(self):
        """Gets the rules of this V1IngressSpec.  # noqa: E501

        rules is a list of host rules used to configure the Ingress. If unspecified, or no rule matches, all traffic is sent to the default backend.  # noqa: E501

        :return: The rules of this V1IngressSpec.  # noqa: E501
        :rtype: list[V1IngressRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this V1IngressSpec.

        rules is a list of host rules used to configure the Ingress. If unspecified, or no rule matches, all traffic is sent to the default backend.  # noqa: E501

        :param rules: The rules of this V1IngressSpec.  # noqa: E501
        :type: list[V1IngressRule]
        """

        self._rules = rules

    @property
    def tls(self):
        """Gets the tls of this V1IngressSpec.  # noqa: E501

        tls represents the TLS configuration. Currently the Ingress only supports a single TLS port, 443. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension, if the ingress controller fulfilling the ingress supports SNI.  # noqa: E501

        :return: The tls of this V1IngressSpec.  # noqa: E501
        :rtype: list[V1IngressTLS]
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this V1IngressSpec.

        tls represents the TLS configuration. Currently the Ingress only supports a single TLS port, 443. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension, if the ingress controller fulfilling the ingress supports SNI.  # noqa: E501

        :param tls: The tls of this V1IngressSpec.  # noqa: E501
        :type: list[V1IngressTLS]
        """

        self._tls = tls

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
        if not isinstance(other, V1IngressSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1IngressSpec):
            return True

        return self.to_dict() != other.to_dict()
