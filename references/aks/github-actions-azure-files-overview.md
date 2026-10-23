# Solution overview for deploying highly available GitHub Actions on Azure Kubernetes Service (AKS)

> Source: https://learn.microsoft.com/en-us/azure/aks/github-actions-azure-files-overview  
> Microsoft doc last updated: 06/13/2025


In this guide, you deploy a highly available GitHub Actions controller and self-hosted agents running on Azure Kubernetes Service (AKS). The self-hosted runners use SMB Azure file shares for persistent storage.

> [!IMPORTANT]
>
> Open-source software is mentioned throughout AKS documentation and samples. Software that you deploy is excluded from AKS service-level agreements, limited warranty, and Azure support. As you use open-source technology alongside AKS, consult the support options available from the respective communities and project maintainers to develop a plan.
>
> Microsoft takes responsibility for building the open-source packages that we deploy on AKS. That responsibility includes having complete ownership of the build, scan, sign, validate, and hotfix process, along with control over the binaries in container images. For more information, see [Vulnerability management for AKS](https://learn.microsoft.com/en-us/azure/aks/concepts-vulnerability-management#aks-container-images) and [AKS support coverage](https://learn.microsoft.com/en-us/azure/aks/support-policies#aks-support-coverage).

## What is Actions Runner Controller (ARC)?

[Actions Runner Controller (ARC)][about-arc] is a Kubernetes operator that orchestrates and scales self-hosted runners for GitHub Actions. ARC relies on persistent volumes (PVs) to share job information between the runner pod and the container job pod. For more information, see [About Actions Runner Controller](https://docs.github.com/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/about-actions-runner-controller).

## Why use self-hosted GitHub Actions on AKS?

Self-hosting GitHub Actions runners on AKS provides organizations with greater control, scalability, and security over their CI/CD infrastructure. Instead of relying on GitHub-hosted runners, which are shared and ephemeral, self-hosted runners offer:

* **Custom environments**: Tailor runners to match specific build, test, or deployment requirements.
* **Performance gains**: Leverage persistent storage and caching to reduce build times and improve reliability.
* **Cost efficiency at scale**: Dynamically scale runners within your own infrastructure, optimizing for frequent or long-running workflows.
* **Enhanced security & isolation**: Maintain full control over infrastructure and data, which is ideal for regulated industries or sensitive workloads.

### Common use cases

* **Enterprise CI/CD pipelines**: For teams needing consistent, secure, and scalable build environments.
* **Large monorepos or ML pipelines**: Where caching or artifact persistence is critical.
* **Performance optimization**: Using Azure Files premium SMB shares to reduce metadata latency and increase IOPS.

## Prerequisites

* This guide assumes a basic understanding of [core Kubernetes concepts][core-kubernetes-concepts].
* You need the **Owner** or **User Access Administrator** and the **Contributor** [Azure built-in roles][azure-roles] on a subscription in your Azure account.

* You need an active GitHub account. Refer to the [pricing information](https://github.com/pricing) based on your repository control.
* You need the following resources installed:
  * [Azure CLI][install-azure-cli] version 2.56 or later.
  * [Azure Kubernetes Service (AKS) preview extension][install-aks-preview].
  * [jq][install-jq] version 1.5 or later.
  * [kubectl][install-kubectl] version 1.21.0 or later.
  * [openssl][install-openssl] version 3.3.1 or later.
  * [Visual Studio Code][install-vscode] or another code editor of your choice.

## Deployment process

In this guide, you learn how to:

* Use Azure CLI to create a multizone AKS cluster.
* Deploy an Azure file share to use in AKS persistent volumes.
* Install the GitHub Actions Runner Controller (ARC) on AKS.
* Install an ARC runners scale set and mount the file share on AKS.
* Run a sample workflow using GitHub Actions.

## Deployment architecture

This reference architecture illustrates how to implement a GitHub Actions self-hosted runner solution using AKS and Azure File Share (SMB). The solution enables organizations to execute GitHub workflow jobs securely within their own Azure infrastructure while maintaining efficient storage management and scalability.

The architecture consists of three main components:

1. **GitHub integration layer**: Connects workflows from GitHub repositories to your Azure infrastructure.
2. **AKS orchestration layer**: Manages the containerized runner instances and their lifecycle.
3. **Storage layer**: Provides persistent and ephemeral storage capabilities for runners.

### GitHub integration layer

The GitHub integration layer connects workflows from GitHub repositories to your Azure infrastructure. Workflow jobs are dispatched from GitHub via `api.github.com` and `githubusercontent.com` to self-hosted runners.

### AKS cluster orchestration layer

The AKS cluster orchestration layer manages the containerized runner instances and their lifecycle. The cluster is split into two namespaces: `arc-controller` and `arc-runners`.

`arc-controller` manages runner infrastructure and job listeners. `arc-runners` handles secrets, access control, and runner pods. Runners are containerized, use ephemeral storage, and connect to shared and dedicated volumes.

### Storage layer

The Azure File Shares storage layer provides both NuGet file share with `ReadWriteMany` access for shared dependencies and ephemeral storage for runners, all backed by persistent volume claims.

## Next step

> [Create the infrastructure to deploy highly available GitHub Actions on AKS](https://learn.microsoft.com/en-us/azure/aks/github-actions-azure-files-create-infrastructure)

## Contributors

*Microsoft maintains this article. The following contributors originally wrote it:*

* Jorge Arterio | Senior Cloud Advocate
* Jeff Patterson | Principal Product Manager
* Rena Shah | Senior Product Manager
* Shekhar Singh Sorot | Product Manager 2
* Erin Schaffer | Content Developer 2

[core-kubernetes-concepts]: https://learn.microsoft.com/en-us/azure/aks/concepts-clusters-workloads
[azure-roles]: https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles
[install-aks-preview]: https://learn.microsoft.com/en-us/azure/aks/draft#install-the-aks-preview-azure-cli-extension
[install-jq]: https://jqlang.github.io/jq/
[install-kubectl]: https://kubernetes.io/docs/tasks/tools/install-kubectl/
[install-openssl]: https://www.openssl.org/
[install-vscode]: https://code.visualstudio.com/Download
[install-azure-cli]: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
[about-arc]: https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/about-actions-runner-controller
