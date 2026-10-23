# Quickstart: Deploy an application to a new Azure Kubernetes Service (AKS) Automatic cluster from a code repository using Automated Deployments

> Source: https://learn.microsoft.com/en-us/azure/aks/automatic/quick-automatic-from-code  
> Microsoft doc last updated: 05/22/2026


**Applies to:** :heavy_check_mark: AKS Automatic

Use [automated deployments][automated-deployments] to build and deploy an application from a code repository to a new or existing AKS Automatic cluster. Automated deployments simplify the process of setting up a GitHub Action workflow to build and deploy your code. Once connected, every new commit you make kicks off the pipeline. Automated deployments build on [draft.sh](https://draft.sh). When you create a new deployment workflow, you can use an existing Dockerfile, generate a Dockerfile, use existing Kubernetes manifests, or generate Kubernetes manifests. The generated manifests are created with security and resiliency best practices in mind. AKS Automatic also includes a [pod readiness SLA][azure-sla] that guarantees 99.9% of qualifying pod readiness operations complete within 5 minutes, guaranteeing reliable, self-healing infrastructure for your applications. 

In this quickstart, you learn to:

- Connect to a code repository.
- Containerize your application.
- Configure Kubernetes manifests.
- Create an AKS Automatic cluster.
- Deploy the application via a pull request.

## Before you begin

- Have a GitHub account with the application to deploy.
- AKS Automatic will [enable Azure Policy on your AKS cluster][policy-for-kubernetes], but you should pre-register the `Microsoft.PolicyInsights` resource provider in your subscription for a smoother experience. See [Azure resource providers and types][az-provider-register] for more information.

> [!IMPORTANT]
> Starting on AKS 1.36, new AKS Automatic clusters will by default enable [Kubernetes Gateway API via the application routing add-on](https://learn.microsoft.com/en-us/azure/aks/app-routing-gateway-api) instead of [Managed NGINX ingress with the application routing add-on](https://learn.microsoft.com/en-us/azure/aks/app-routing) due to the upstream [Ingress NGINX retirement](https://www.kubernetes.dev/blog/2025/11/12/ingress-nginx-retirement/).
>
> Existing Automatic clusters aren't affected but should begin migration to [Kubernetes Gateway API via the application routing add-on](https://learn.microsoft.com/en-us/azure/aks/app-routing-gateway-api#enable-for-an-existing-cluster).

## Limitations

The following limitations apply to AKS Automatic clusters:

- AKS Automatic is generally available in the following regions: `australiacentral`, `australiaeast`, `australiasoutheast`, `austriaeast`, `belgiumcentral`, `brazilsouth`, `canadacentral`, `canadaeast`, `centralindia`, `centralus`, `chilecentral`, `denmarkeast`, `eastasia`, `eastus`, `eastus2`, `francecentral`, `germanywestcentral`, `indonesiacentral`, `israelcentral`, `italynorth`, `japaneast`, `japanwest`, `koreacentral`, `koreasouth`, `malaysiawest`, `mexicocentral`, `newzealandnorth`, `northcentralus`, `northeurope`, `norwayeast`, `polandcentral`, `southafricanorth`, `southcentralus`, `southeastasia`, `southindia`, `spaincentral`, `swedencentral`, `switzerlandnorth`, `uaenorth`, `uksouth`, `ukwest`, `westcentralus`, `westeurope`, `westus`, `westus2`, `westus3`.
- New AKS Automatic clusters by default enable managed system node pools and [LocalDNS](https://learn.microsoft.com/en-us/azure/aks/dns-concepts#localdns-in-azure-kubernetes-service). You can't create AKS Automatic clusters without managed system node pools in any region.
- AKS Automatic cluster has [node resource group lockdown](https://learn.microsoft.com/en-us/azure/aks/node-resource-group-lockdown) preconfigured, which doesn't allow changes to the `MC_` resource group, preventing virtual network links on the default Private DNS zone. For cross‑VNet or custom DNS scenarios, use custom network and private DNS by following [Create a private Azure Kubernetes Service (AKS) Automatic cluster in a custom virtual network](https://learn.microsoft.com/en-us/azure/aks/automatic/quick-automatic-private-custom-network).
- Azure CLI version 2.86.0 or later is required. To find the version, run `az --version` command. If you need to install or upgrade, see [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli).
- The following extensions aren't supported:
  - [Dapr](https://learn.microsoft.com/en-us/azure/aks/dapr)
  - [Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-attach-kubernetes-anywhere)
- Windows nodes aren't supported.
- Migration from AKS base SKU to automatic SKU isn't supported.
- Migration from an existing AKS Automatic cluster without managed system node pools to AKS Automatic with managed system node pools is supported in preview in regions where managed system node pools are generally available. Migration from AKS Automatic with managed system node pools back to AKS Automatic without managed system node pools isn't supported.

## Bring your application source code

To deploy an application from a code repository, start at the [Azure portal][azure-portal] home page.

1. Search for **Kubernetes services** in the top search bar.
2. Select [**Kubernetes services**][portal-kubernetes-services] in the search results.
3. Select the **Create** button and select **Deploy application**.

### Connect to source code repository

Create and automated deployment workflow and authorize it to connect to the desired source code repository.

1. In the **Basics** tab, select **Deploy your application**.
1. Under **Project details**, choose the **Subscription**, **Resource Group**, and **Region**.
1. Under **Repository details**, enter a name for the workflow, then select **Authorize access** to connect to the desired GitHub repository.
1. Choose the **Repository** and **Branch**.
1. Select the **Next** button.

### Choose the container image configuration

To get an application ready for Kubernetes, you need to build it into a container image and stored into a container registry. You use a Dockerfile to provide instructions on how to build the container image. If your source code repository doesn't already have a Dockerfile, Automated Deployments can generate one for you, otherwise, you can utilize an existing Dockerfile.

#### [Without an existing Dockerfile](#tab/generate-dockerfile)

Use Automated Deployments to generate a Dockerfile for many languages and frameworks such as Go, C#, Node.js, Python, Java, Gradle, Clojure, PHP, Ruby, Erlang, Swift, and Rust. The language support is built on what's available in [draft.sh](https://draft.sh).

1. Select **Auto-containerize (generate Dockerfile)** for the container configuration.
1. Select the **location of where to save the generated Dockerfile** in the repository.
1. Choose the **application environment** from the list of supported languages and frameworks.
1. Enter the **application port**.
1. Select an existing **Azure Container Registry** or create a new one. This registry is used to store the built application image. The [kubelet identity][aks-identities] of the AKS Automatic cluster is given `AcrPull` permissions on that registry.

#### [With an existing Dockerfile](#tab/use-existing-dockerfile)

If your code repository already has a Dockerfile, you can select it to be used to build the application image.

1. Select **Existing Dockerfile** for the container configuration.
1. Select the **Dockerfile** from your repository.
1. Enter the **Dockerfile build context** to pass the set of files and directories to the build process. These files are used to build the image, and they're included in the final image, unless they're ignored by a `.dockerignore` file.
1. Select an existing **Azure Container Registry** or create a new one. This registry is used to store the built application image. The [kubelet identity][aks-identities] of the AKS Automatic cluster is given `AcrPull` permissions on that registry.

---

### Choose the Kubernetes manifest configuration

An application running on Kubernetes consists of many Kubernetes primitive components. These components describe what container image to use, how many replicas to run, if there's a public IP required to expose the application, etc. For more information, see the official [Kubernetes documentation][kubernetes-documentation]. If your source code repository doesn't already have the basic Kubernetes manifests to deploy, Automated Deployments can generate them for you, otherwise, you can utilize a set of existing manifests. You can also choose an existing Helm chart.

#### [Generate manifests](#tab/generate-kubernetes-manifests)

Use Automated Deployments to generate a set of basic Kubernetes manifest files to have your application up and running. At the moment, Automated Deployments creates a `Deployment`, a `Service`, and a `ConfigMap`.

The generated manifests are designed to apply recommendations of [deployment safeguards][deployment-safeguards], such as:

- Automatically generating [liveness, readiness, and startup probes][kubernetes-probes].
- Preferring [pod anti-affinity][pod-anti-affinity] and [topology spread constraints][topology-spread-constraints] that spread replicas onto different nodes for improved resiliency.
- Enforcing the `RuntimeDefault` [secure computing profile][seccomp-profile] which establishes an extra layer of protection against common system call vulnerabilities exploited by malicious actors.
- Dropping all Linux capabilities and only allowing a limited set following the baseline [Kubernetes Pod Security Standards][kubernetes-pod-security-standards].

To generate Kubernetes manifests:

1. Select **Generate application deployment files** for the deployment options.
1. Enter the **application port**. This port is used on the generated `Service`.
1. Select the **location of where to save the generated Kubernetes manifests** in the repository.
1. Select the **Next** button.

#### [With existing Kubernetes manifests](#tab/existing-kubernetes-manifests)

If your code repository already has a Dockerfile, you can select it to be used to build the application image.

1. Select **Use existing Kubernetes manifest deployment files** for the deployment options.
1. Select the **Kubernetes manifest file or folder** from your repository.
1. Select the **Next** button.

#### [With an existing Helm chart](#tab/existing-helm-chart)

If your code repository already has a Helm chart, you can select it to be used to build the application image.

1. Select **Use existing Helm chart** for the deployment options.
1. Select the **Charts path** folder from your repository.
1. Select the **Values.yaml** file path from your repository.
1. Optionally, provide **Helm chart overrides**.
1. Select the **Next** button.

---

## Select where you want to deploy the application

#### [Create a new AKS Automatic cluster](#tab/new-aks-automatic-cluster)

If you don't have a cluster already, you can create a new AKS Automatic cluster as part of this deployment.

1. Select **Create Automatic Kubernetes cluster** for the cluster configuration.
1. Enter a **cluster name**.
1. Choose the **automatic upgrade maintenance schedule** or leave the default selected.
1. Enter the **Kubernetes namespace** where the application is deployed.
1. Choose the **monitoring and logging level** or leave the default selected.
1. Select the **Next** button.

#### [Existing AKS cluster](#tab/existing-aks-cluster)

If you have a cluster, you can use it to deploy the application.

1. Select **Existing AKS cluster** for the cluster configuration.
1. Select the **Subscription**, **Resource Group**, and **Cluster**.
1. Enter the **Kubernetes namespace** where the application is deployed.
1. Select the **Next** button.

---

## Review configuration and deploy

Review the configuration for the cluster, application, and Kubernetes manifests, then select **Deploy**. Creating a cluster takes a few minutes, don't navigate away from deployment page.

1. A new AKS Automatic cluster is created or an existing one is configured.
1. A container registry is created or an existing one is configured with the cluster.
1. Federated credentials are created to allow the GitHub Action workflow to deploy to the cluster.
1. A pull request is created on the code repository with any generated files and the workflow.

### Review and merge pull request

When the deployment succeeds, select the **View pull request** button to view the details of the generated pull request on your code repository.

 

1. Review the changes under **Files changed** and make any desired edits.
1. Select **Merge pull request** to merge the changes into your code repository.

Merging the change runs the GitHub Actions workflow that builds your application into a container image, store it in Azure Container Registry, and deploy it to the cluster.

### Check the deployed resources

After the pipeline is completed, you can review the created Kubernetes `Service` on the Azure portal by selecting **Services and ingresses** under **Kubernetes resources** service menu.

Selecting the **External IP** should open up a new browser page with the running application.

## Delete resources

Once you're done with your cluster, can delete it to avoid incurring Azure charges.

1. In the Azure portal, navigate to your resource group.
1. Select **Delete resource group**.
1. Enter the name of your resource group to confirm deletion and select **Delete**.
1. In the **Delete confirmation** dialog box, select **Delete**.

## Next steps

In this quickstart, you deployed an application to a Kubernetes cluster using [AKS Automatic][what-is-aks-automatic] and set up a continuous integration/continuous deployment (CI/CD) pipeline from a code repository.

To learn more about AKS Automatic, continue to the introduction.

> [Introduction to Azure Kubernetes Service (AKS) Automatic][what-is-aks-automatic]

[what-is-aks-automatic]: https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic
[Azure-Policy-RBAC-permissions]: https://learn.microsoft.com/en-us/azure/governance/policy/overview#azure-rbac-permissions-in-azure-policy
[availability-zones]: https://learn.microsoft.com/en-us/azure/reliability/availability-zones-region-support
[automated-deployments]: https://learn.microsoft.com/en-us/azure/aks/automated-deployments
[azure-portal]: https://portal.azure.com
[portal-kubernetes-services]: https://portal.azure.com/#browse/Microsoft.ContainerService%2FmanagedClusters
[aks-identities]: https://learn.microsoft.com/en-us/azure/aks/managed-identity-overview#summary-of-managed-identities-used-by-aks
[kubernetes-documentation]: https://kubernetes.io/docs/concepts/workloads/
[deployment-safeguards]: https://learn.microsoft.com/en-us/azure/aks/deployment-safeguards
[seccomp-profile]: https://learn.microsoft.com/en-us/azure/aks/secure-container-access#overview-of-default-seccomp-profiles-preview
[kubernetes-probes]: https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/
[kubernetes-pod-security-standards]: https://kubernetes.io/docs/concepts/security/pod-security-standards/
[pod-anti-affinity]: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity
[topology-spread-constraints]: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
[policy-for-kubernetes]: https://learn.microsoft.com/en-us/azure/governance/policy/concepts/policy-for-kubernetes#install-azure-policy-add-on-for-aks
[az-provider-register]: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-providers-and-types#register-resource-provider
[azure-sla]: https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services
