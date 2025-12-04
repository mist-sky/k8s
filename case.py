# -*- coding: utf-8 -*-
from kubernetes.client import api_client as client
from kubernetes.dynamic import DynamicClient, ResourceList
from kubernetes.dynamic.exceptions import ResourceNotFoundError


class BaseMixins:
    def compose_api_class(self, group_version):
        """通过group version 组装对应分组的api class
        """
        return f"{''.join([info.capitalize() for info in group_version.split('/')])}Api"

    def get_api_class(self, api_client):
        """动态通用api mixins"""
        resources = DynamicClient(api_client).resources
        # 校验所填版本是否支持
        if self.version and resources.get(kind=self.resource_kind, api_version=self.version):
            return self.compose_api_class(self.version)

        # 若未填写，选取对应resource 首选版
        try:
            resource = resources.get(kind=self.resource_kind, preferred=True)
        except:  # noqa
            # 无首选版，使用默认第一个版本
            results = resources.search(kind=self.resource_kind)
            # If there are multiple matches, prefer non-List kinds
            if len(results) > 1 and not all([isinstance(x, ResourceList) for x in results]):
                results = [result for result in results if not isinstance(result, ResourceList)]
            if not results:
                raise ResourceNotFoundError(f"No matches found for kind={self.resource_kind}")

            resource = results[0]

        self.version = resource.group_version
        return self.compose_api_class(resource.group_version)


class APPAPIClassMixins(BaseMixins):
    """
    支持资源类型: Deployment/DaemonSet/StatefulSet/ResplicaSet
    """
    pass


class AutoscalingApiClassMixins(BaseMixins):
    """
    支持资源类型: HorizontalPodAutoscaler
    """
    pass


class BatchAPIClassMixins(BaseMixins):
    """
    支持资源类型: Job/CronJob
    """
    pass


class CoreAPIClassMixins(BaseMixins):
    """
    支持资源类型: ConfigMap/Endpoints/Event/Namespace/Node/Pod/PersistentVolume/secret等
    """

    def compose_api_class(self, group_version):
        """通过group version 组装对应分组的api class
        """
        return f"Core{group_version.capitalize()}Api"


class EventAPIClassMixins(BaseMixins):
    """
    支持资源类型: Event
    """

    def compose_api_class(self, group_version):
        """通过group version 组装对应分组的api class
        """
        if "/" not in group_version:
            return f"Core{group_version.capitalize()}Api"
        
        return super().compose_api_class()

    def get_api_class(self, api_client):
        try:
            return super().get_api_class(api_client)
        except:  # noqa
            return "CoreV1Api"


class ExtensionsAPIClassMixins(BaseMixins):
    """
    支持资源类型: Ingress
    """
    pass


class NetworkingAPIClassMixins(BaseMixins):
    """
    支持资源类型: Ingress
    """

    def compose_api_class(self, group_version):
        """通过group version 组装对应分组的api class
        """
        group_version = group_version.replace(".k8s.io", "")
        return f"{''.join([info.capitalize() for info in group_version.split('/')])}Api"


class RbacAuthorizationApiClassMixins(BaseMixins):
    """
    支持资源类型: StorageClass
    """

    def compose_api_class(self, group_version):
        """通过group version 组装对应分组的api class
        """
        group_version = group_version.replace(".k8s.io", "")
        g, v = group_version.split('/')
        return f"{''.join([i.capitalize() for i in g.split('.')])}{v.capitalize()}Api"


class ReplicaSetAPIClassMixins(BaseMixins):
    """
    支持资源类型: ReplicaSet
    """
    def get_api_class(self, api_client):
        try:
            return super().get_api_class(api_client)
        except:  # noqa
            return "AppsV1Api"


class Resource:
    def __init__(self, api_client, version=None):
        """
        :param api_client: k8s client.ApiClient instance
        :param version: k8s resource version, e.g. v1, apps/v1, etc.
        """
        self.version = version
        self.api_client = api_client

    @property
    def api_class(self):
        return self.get_api_class(self.api_client)

    @property
    def api_instance(self):
        return getattr(client, self.api_class)(self.api_client)


class Deployment(Resource, APPAPIClassMixins):
    resource_kind = "Deployment"

    def create(self, namespace, data):
        return self.api_instance.create_namespaced_deployment(namespace, data)


if __name__ == "__main__":
    configure = client.Configuration()
    configure.verify_ssl = False
    configure.host = "https://192.168.163.210:8443/tunnels/clusters/cluster_identifier"
    # make secret
    # configure.cert_file = ""
    # configure.key_file = ""
    configure.api_key = {"Content-Type": "application/json", "authorization": "Bearer xxx"}
    # api_client = client.ApiClient(configure)
    # Deployment(api_client).create("default", {})
