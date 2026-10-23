# Windows Container Considerations in Azure Kubernetes Service (AKS)

> Source: https://learn.microsoft.com/en-us/azure/aks/windows-vs-linux-containers  
> Microsoft doc last updated: 07/07/2025


When you create deployments that use Windows Server containers on Azure Kubernetes Service (AKS), there are a few differences relative to Linux deployments you should keep in mind. For a detailed comparison of the differences between Windows and Linux in upstream Kubernetes, see [Windows containers in Kubernetes](https://kubernetes.io/docs/concepts/windows/intro/).

Some of the major differences include:

- **Identity**: Windows Server uses a larger binary security identifier (SID) that's stored in the Windows Security Access Manager (SAM) database. This database isn't shared between the host and containers or between containers.
- **File permissions**: Windows Server uses an access control list based on SIDs rather than a bitmask of permissions and UID+GID.
- **File paths**: The convention on Windows Server is to use \ instead of /. In pod specs that mount volumes, specify the path correctly for Windows Server containers. For example, rather than a mount point of */mnt/volume* in a Linux container, specify a drive letter and location such as */K/Volume* to mount as the *K:* drive.

> [!IMPORTANT]
> Starting on March 01, 2026, Azure Kubernetes Service (AKS) no longer supports Windows Server 2019 node pools. Node pools running Kubernetes version 1.33+ can't use Windows Server 2019. Starting on April 01, 2027, AKS will remove all existing node images for Windows Server 2019, meaning that scaling operations will fail. For more information on this retirement, see the [Retirement GitHub issue](https://github.com/Azure/AKS/issues/4091) and the [Azure Updates retirement announcement](https://azure.microsoft.com/updates?id=aks-will-stop-support-for-windows-server-2019-on-march-1-2026). To stay informed on announcements and updates, follow the [AKS release notes](https://github.com/Azure/AKS/releases).

> [!IMPORTANT]
> Starting on June 30, 2028, Azure Kubernetes Service (AKS) no longer supports Windows Server 2022 node pools. Windows Server 2022 isn't supported in Kubernetes version 1.37 and later. Starting on June 30, 2029, AKS will remove all existing node images for Windows Server 2022, meaning that scaling operations will fail. For more information on this retirement, see the [Retirement GitHub issue](https://github.com/Azure/AKS/issues/4168) and the [Azure Updates retirement announcement](https://azure.microsoft.com/updates?id=ws2022-retirement-aks). To stay informed about announcements and updates, follow the [AKS release notes](https://github.com/Azure/AKS/releases).

> [!IMPORTANT]
> Starting on **May 15, 2026**, AKS no longer supports Windows Server Annual Channel (Preview). AKS will no longer produce new Windows Server Annual Channel node images or provide security patches. You won't be able to create new node pools with Windows Server Annual Channel. On **May 15, 2027**, AKS will remove all existing Windows Server Annual Channel node images, which will cause scaling and remediation (reimage and redeploy) operations to fail. To avoid disruption, we recommend migrating to the [Long Term Servicing Channel (LTSC)](https://learn.microsoft.com/en-us/azure/aks/upgrade-windows-os).
>
> - Windows Server Annual Channel uses Windows Server 2022 base images, which will run on Windows Server 2022 and Windows Server 2025.
> - If you're using [Host Process Containers (HPC)](https://learn.microsoft.com/en-us/azure/aks/use-windows-hpc) or running other privileged containers for administration purposes, you need to do extra testing.
>
> For more information on this retirement, see the [Retirement GitHub issue](https://aka.ms/aks/windows-annual-channel-retirement). To stay informed on announcements and updates, follow the [AKS release notes](https://github.com/Azure/AKS/releases).

This article covers important considerations to keep in mind when using Windows containers instead of Linux containers in Kubernetes. For an in-depth comparison of Windows and Linux containers, see [Comparison with Linux][comparison-with-linux].

## Considerations

| Feature | Windows considerations |
|-----------|:-----------|
| [Cluster creation][cluster-configuration] | • The first system node pool *must* be Linux.<br/> • The maximum number of nodes per cluster is 5000.<br/> • The Windows Server node pool name has a limit of six characters. |
| [Privileged containers][privileged-containers] | Not supported. The equivalent is **HostProcess Containers (HPC) containers**. |
| [HPC containers][hpc-containers] | • HostProcess containers are the Windows alternative to Linux privileged containers. For more information, see [Create a Windows HostProcess pod](https://kubernetes.io/docs/tasks/configure-pod-container/create-hostprocess-pod/). |
| [Azure Network Policy Manager (Azure)][azure-network-policy] | Azure Network Policy Manager doesn't support:<br/> • Named ports<br/> • SCTP protocol<br/> • Negative match labels or namespace selectors (all labels except "debug=true")<br/> • "except" CIDR blocks (a CIDR with exceptions)<br/> • Windows Server 2019<br/> |
| [Node upgrade][node-upgrade] | Windows Server nodes on AKS don't automatically apply Windows updates. Instead, you perform a node pool upgrade or [node image upgrade][node-image-upgrade]. These upgrades deploy new nodes with the latest Window Server 2019 and Windows Server 2022 base node image and security patches. |
| [AKS Image Cleaner][aks-image-cleaner] | Not supported. |
| [BYOCNI][byo-cni] | Not supported. |
| [Open Service Mesh][open-service-mesh] | Not supported. |
| [GPU][gpu] | Supported in preview. |
| [Multi-instance GPU][multi-instance-gpu] | Not supported. |
| [Generation 2 VMs][gen-2-vms] | Supported. Default in Windows Server 2025. |
| [Custom node config][custom-node-config] | • Custom node config has two configurations:<br/> • [kubelet][custom-kubelet-parameters]: Supported.<br/> • OS config: Not supported. |

## Next steps

For more information on Windows containers, see the [Windows Server containers FAQ][windows-server-containers-faq].

[aks-release-notes]: https://github.com/Azure/AKS/releases
[comparison-with-linux]: https://kubernetes.io/docs/concepts/windows/intro/#compatibility-linux-similarities

[cluster-configuration]: https://learn.microsoft.com/en-us/azure/aks/quotas-skus-regions#cluster-configuration-presets-in-the-azure-portal
[privileged-containers]: https://learn.microsoft.com/en-us/azure/aks/use-windows-hpc#limitations
[hpc-containers]: https://learn.microsoft.com/en-us/azure/aks/use-windows-hpc#limitations
[node-upgrade]: https://learn.microsoft.com/en-us/azure/aks/manage-node-pools#upgrade-a-single-node-pool
[aks-image-cleaner]: https://learn.microsoft.com/en-us/azure/aks/image-cleaner#limitations
[windows-server-containers-faq]: windows-faq.yml
[azure-network-policy]: https://learn.microsoft.com/en-us/azure/aks/use-network-policies#overview-of-network-policy
[node-image-upgrade]: https://learn.microsoft.com/en-us/azure/aks/node-image-upgrade
[byo-cni]: https://learn.microsoft.com/en-us/azure/aks/use-byo-cni
[open-service-mesh]: https://learn.microsoft.com/en-us/azure/aks/open-service-mesh-about
[gpu]: https://learn.microsoft.com/en-us/azure/aks/use-windows-gpu
[multi-instance-gpu]: https://learn.microsoft.com/en-us/azure/aks/gpu-multi-instance
[gen-2-vms]: https://learn.microsoft.com/en-us/azure/aks/generation-2-vms
[custom-node-config]: https://learn.microsoft.com/en-us/azure/aks/custom-node-configuration
[custom-kubelet-parameters]: https://learn.microsoft.com/en-us/azure/aks/custom-node-configuration#kubelet-configuration
