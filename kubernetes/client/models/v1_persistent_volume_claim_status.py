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


class V1PersistentVolumeClaimStatus(object):
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
        'access_modes': 'list[str]',
        'allocated_resource_statuses': 'dict(str, str)',
        'allocated_resources': 'dict(str, str)',
        'capacity': 'dict(str, str)',
        'conditions': 'list[V1PersistentVolumeClaimCondition]',
        'current_volume_attributes_class_name': 'str',
        'modify_volume_status': 'V1ModifyVolumeStatus',
        'phase': 'str'
    }

    attribute_map = {
        'access_modes': 'accessModes',
        'allocated_resource_statuses': 'allocatedResourceStatuses',
        'allocated_resources': 'allocatedResources',
        'capacity': 'capacity',
        'conditions': 'conditions',
        'current_volume_attributes_class_name': 'currentVolumeAttributesClassName',
        'modify_volume_status': 'modifyVolumeStatus',
        'phase': 'phase'
    }

    def __init__(self, access_modes=None, allocated_resource_statuses=None, allocated_resources=None, capacity=None, conditions=None, current_volume_attributes_class_name=None, modify_volume_status=None, phase=None, local_vars_configuration=None):  # noqa: E501
        """V1PersistentVolumeClaimStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_modes = None
        self._allocated_resource_statuses = None
        self._allocated_resources = None
        self._capacity = None
        self._conditions = None
        self._current_volume_attributes_class_name = None
        self._modify_volume_status = None
        self._phase = None
        self.discriminator = None

        if access_modes is not None:
            self.access_modes = access_modes
        if allocated_resource_statuses is not None:
            self.allocated_resource_statuses = allocated_resource_statuses
        if allocated_resources is not None:
            self.allocated_resources = allocated_resources
        if capacity is not None:
            self.capacity = capacity
        if conditions is not None:
            self.conditions = conditions
        if current_volume_attributes_class_name is not None:
            self.current_volume_attributes_class_name = current_volume_attributes_class_name
        if modify_volume_status is not None:
            self.modify_volume_status = modify_volume_status
        if phase is not None:
            self.phase = phase

    @property
    def access_modes(self):
        """Gets the access_modes of this V1PersistentVolumeClaimStatus.  # noqa: E501

        accessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1  # noqa: E501

        :return: The access_modes of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_modes

    @access_modes.setter
    def access_modes(self, access_modes):
        """Sets the access_modes of this V1PersistentVolumeClaimStatus.

        accessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1  # noqa: E501

        :param access_modes: The access_modes of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :type: list[str]
        """

        self._access_modes = access_modes

    @property
    def allocated_resource_statuses(self):
        """Gets the allocated_resource_statuses of this V1PersistentVolumeClaimStatus.  # noqa: E501

        allocatedResourceStatuses stores status of resource being resized for the given PVC. Key names follow standard Kubernetes label syntax. Valid values are either:  * Un-prefixed keys:   - storage - the capacity of the volume.  * Custom resources must use implementation-defined prefixed names such as \"example.com/my-custom-resource\" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  ClaimResourceStatus can be in any of following states:  - ControllerResizeInProgress:   State set when resize controller starts resizing the volume in control-plane.  - ControllerResizeFailed:   State set when resize has failed in resize controller with a terminal error.  - NodeResizePending:   State set when resize controller has finished resizing the volume but further resizing of   volume is needed on the node.  - NodeResizeInProgress:   State set when kubelet starts resizing the volume.  - NodeResizeFailed:   State set when resizing has failed in kubelet with a terminal error. Transient errors don't set   NodeResizeFailed. For example: if expanding a PVC for more capacity - this field can be one of the following states:  - pvc.status.allocatedResourceStatus['storage'] = \"ControllerResizeInProgress\"      - pvc.status.allocatedResourceStatus['storage'] = \"ControllerResizeFailed\"      - pvc.status.allocatedResourceStatus['storage'] = \"NodeResizePending\"      - pvc.status.allocatedResourceStatus['storage'] = \"NodeResizeInProgress\"      - pvc.status.allocatedResourceStatus['storage'] = \"NodeResizeFailed\" When this field is not set, it means that no resize operation is in progress for the given PVC.  A controller that receives PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.  This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.  # noqa: E501

        :return: The allocated_resource_statuses of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._allocated_resource_statuses

    @allocated_resource_statuses.setter
    def allocated_resource_statuses(self, allocated_resource_statuses):
        """Sets the allocated_resource_statuses of this V1PersistentVolumeClaimStatus.

        allocatedResourceStatuses stores status of resource being resized for the given PVC. Key names follow standard Kubernetes label syntax. Valid values are either:  * Un-prefixed keys:   - storage - the capacity of the volume.  * Custom resources must use implementation-defined prefixed names such as \"example.com/my-custom-resource\" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  ClaimResourceStatus can be in any of following states:  - ControllerResizeInProgress:   State set when resize controller starts resizing the volume in control-plane.  - ControllerResizeFailed:   State set when resize has failed in resize controller with a terminal error.  - NodeResizePending:   State set when resize controller has finished resizing the volume but further resizing of   volume is needed on the node.  - NodeResizeInProgress:   State set when kubelet starts resizing the volume.  - NodeResizeFailed:   State set when resizing has failed in kubelet with a terminal error. Transient errors don't set   NodeResizeFailed. For example: if expanding a PVC for more capacity - this field can be one of the following states:  - pvc.status.allocatedResourceStatus['storage'] = \"ControllerResizeInProgress\"      - pvc.status.allocatedResourceStatus['storage'] = \"ControllerResizeFailed\"      - pvc.status.allocatedResourceStatus['storage'] = \"NodeResizePending\"      - pvc.status.allocatedResourceStatus['storage'] = \"NodeResizeInProgress\"      - pvc.status.allocatedResourceStatus['storage'] = \"NodeResizeFailed\" When this field is not set, it means that no resize operation is in progress for the given PVC.  A controller that receives PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.  This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.  # noqa: E501

        :param allocated_resource_statuses: The allocated_resource_statuses of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._allocated_resource_statuses = allocated_resource_statuses

    @property
    def allocated_resources(self):
        """Gets the allocated_resources of this V1PersistentVolumeClaimStatus.  # noqa: E501

        allocatedResources tracks the resources allocated to a PVC including its capacity. Key names follow standard Kubernetes label syntax. Valid values are either:  * Un-prefixed keys:   - storage - the capacity of the volume.  * Custom resources must use implementation-defined prefixed names such as \"example.com/my-custom-resource\" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  Capacity reported here may be larger than the actual capacity when a volume expansion operation is requested. For storage quota, the larger value from allocatedResources and PVC.spec.resources is used. If allocatedResources is not set, PVC.spec.resources alone is used for quota calculation. If a volume expansion capacity request is lowered, allocatedResources is only lowered if there are no expansion operations in progress and if the actual volume capacity is equal or lower than the requested capacity.  A controller that receives PVC update with previously unknown resourceName should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.  This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.  # noqa: E501

        :return: The allocated_resources of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._allocated_resources

    @allocated_resources.setter
    def allocated_resources(self, allocated_resources):
        """Sets the allocated_resources of this V1PersistentVolumeClaimStatus.

        allocatedResources tracks the resources allocated to a PVC including its capacity. Key names follow standard Kubernetes label syntax. Valid values are either:  * Un-prefixed keys:   - storage - the capacity of the volume.  * Custom resources must use implementation-defined prefixed names such as \"example.com/my-custom-resource\" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  Capacity reported here may be larger than the actual capacity when a volume expansion operation is requested. For storage quota, the larger value from allocatedResources and PVC.spec.resources is used. If allocatedResources is not set, PVC.spec.resources alone is used for quota calculation. If a volume expansion capacity request is lowered, allocatedResources is only lowered if there are no expansion operations in progress and if the actual volume capacity is equal or lower than the requested capacity.  A controller that receives PVC update with previously unknown resourceName should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.  This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.  # noqa: E501

        :param allocated_resources: The allocated_resources of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._allocated_resources = allocated_resources

    @property
    def capacity(self):
        """Gets the capacity of this V1PersistentVolumeClaimStatus.  # noqa: E501

        capacity represents the actual resources of the underlying volume.  # noqa: E501

        :return: The capacity of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this V1PersistentVolumeClaimStatus.

        capacity represents the actual resources of the underlying volume.  # noqa: E501

        :param capacity: The capacity of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._capacity = capacity

    @property
    def conditions(self):
        """Gets the conditions of this V1PersistentVolumeClaimStatus.  # noqa: E501

        conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'.  # noqa: E501

        :return: The conditions of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: list[V1PersistentVolumeClaimCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1PersistentVolumeClaimStatus.

        conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'.  # noqa: E501

        :param conditions: The conditions of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :type: list[V1PersistentVolumeClaimCondition]
        """

        self._conditions = conditions

    @property
    def current_volume_attributes_class_name(self):
        """Gets the current_volume_attributes_class_name of this V1PersistentVolumeClaimStatus.  # noqa: E501

        currentVolumeAttributesClassName is the current name of the VolumeAttributesClass the PVC is using. When unset, there is no VolumeAttributeClass applied to this PersistentVolumeClaim This is an alpha field and requires enabling VolumeAttributesClass feature.  # noqa: E501

        :return: The current_volume_attributes_class_name of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: str
        """
        return self._current_volume_attributes_class_name

    @current_volume_attributes_class_name.setter
    def current_volume_attributes_class_name(self, current_volume_attributes_class_name):
        """Sets the current_volume_attributes_class_name of this V1PersistentVolumeClaimStatus.

        currentVolumeAttributesClassName is the current name of the VolumeAttributesClass the PVC is using. When unset, there is no VolumeAttributeClass applied to this PersistentVolumeClaim This is an alpha field and requires enabling VolumeAttributesClass feature.  # noqa: E501

        :param current_volume_attributes_class_name: The current_volume_attributes_class_name of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :type: str
        """

        self._current_volume_attributes_class_name = current_volume_attributes_class_name

    @property
    def modify_volume_status(self):
        """Gets the modify_volume_status of this V1PersistentVolumeClaimStatus.  # noqa: E501


        :return: The modify_volume_status of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: V1ModifyVolumeStatus
        """
        return self._modify_volume_status

    @modify_volume_status.setter
    def modify_volume_status(self, modify_volume_status):
        """Sets the modify_volume_status of this V1PersistentVolumeClaimStatus.


        :param modify_volume_status: The modify_volume_status of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :type: V1ModifyVolumeStatus
        """

        self._modify_volume_status = modify_volume_status

    @property
    def phase(self):
        """Gets the phase of this V1PersistentVolumeClaimStatus.  # noqa: E501

        phase represents the current phase of PersistentVolumeClaim.  # noqa: E501

        :return: The phase of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this V1PersistentVolumeClaimStatus.

        phase represents the current phase of PersistentVolumeClaim.  # noqa: E501

        :param phase: The phase of this V1PersistentVolumeClaimStatus.  # noqa: E501
        :type: str
        """

        self._phase = phase

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
        if not isinstance(other, V1PersistentVolumeClaimStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1PersistentVolumeClaimStatus):
            return True

        return self.to_dict() != other.to_dict()
