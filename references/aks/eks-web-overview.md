# Replicate an AWS web application with AWS WAF in Azure Kubernetes Service (AKS)

> Source: https://learn.microsoft.com/en-us/azure/aks/eks-web-overview  
> Microsoft doc last updated: 11/10/2025


In this article, you learn how to replicate an Amazon Elastic Kubernetes Service (EKS) web application with AWS Web Application Firewall (WAF) using [Azure Web Application Firewall (WAF)][azure-waf] and [Azure Application Gateway for Containers][azure-ag] in [Azure Kubernetes Service (AKS)][aks]. 

This workload implements a WAF to protect a [Yelb][yelb] web-based application running in a Kubernetes cluster. Applications rely on WAFs to block unwanted traffic and protect apps from common vulnerabilities. A centralized web application firewall helps simplify security management and helps ensure better protection against threats or intrusions.

If you plan to migrate an AWS workload to Azure, see [Migrate compute from Amazon Web Services to Azure](https://learn.microsoft.com/en-us/azure/migration/migrate-compute-from-aws), which includes [example migration scenarios](https://learn.microsoft.com/en-us/azure/migration/migrate-compute-from-aws#migration-scenarios) that might align to your use case. For a more detailed understanding of the AWS workload, see [Protecting your Amazon EKS web apps with AWS WAF][eks-aws-waf].

> [!IMPORTANT]
>
> Open-source software is mentioned throughout AKS documentation and samples. Software that you deploy is excluded from AKS service-level agreements, limited warranty, and Azure support. As you use open-source technology alongside AKS, consult the support options available from the respective communities and project maintainers to develop a plan.
>
> Microsoft takes responsibility for building the open-source packages that we deploy on AKS. That responsibility includes having complete ownership of the build, scan, sign, validate, and hotfix process, along with control over the binaries in container images. For more information, see [Vulnerability management for AKS](https://learn.microsoft.com/en-us/azure/aks/concepts-vulnerability-management#aks-container-images) and [AKS support coverage](https://learn.microsoft.com/en-us/azure/aks/support-policies#aks-support-coverage).

## Deployment process

1. [**Understand the conceptual differences**](https://learn.microsoft.com/en-us/azure/aks/eks-web-understand): Start by reviewing the differences between EKS and AKS in terms of services, architecture, and deployment.
1. [**Rearchitect the workload**](https://learn.microsoft.com/en-us/azure/aks/eks-web-rearchitect): Analyze the existing AWS workload architecture and identify the components or services, like the workload infrastructure, application architecture, and deployment process, that you need to redesign to fit AKS.
1. [**Update the application code**](https://learn.microsoft.com/en-us/azure/aks/eks-web-refactor): Ensure your code is compatible with Azure APIs, services, and authentication models.
1. [**Prepare for deployment**](https://learn.microsoft.com/en-us/azure/aks/eks-web-prepare): Modify the AWS deployment process to use the Azure CLI.
1. [**Deploy the workload**](https://learn.microsoft.com/en-us/azure/aks/eks-web-deploy): Deploy the replicated workload in AKS and test the workload to ensure that it functions as expected.

## Prerequisites

- An active [Azure subscription](https://learn.microsoft.com/en-us/azure/guides/developer/azure-developer-guide#understanding-accounts-subscriptions-and-billing). If you don't have one, create a [free Azure account][azure-free] before you begin.
- The **Owner** [Azure built-in role][azure-built-in-roles], or the **User Access Administrator** and **Contributor** built-in roles, on a subscription in your Azure account.
- [Azure CLI][azure-cli] version 2.61.0 or later. For more information, see [Install Azure CLI][azure-cli].
- [Azure Kubernetes Service (AKS) preview extension][aks-preview].
- [jq][install-jq] version 1.5 or later.
- [Python 3][install-python] or later.
- [kubectl][install-kubectl] version 1.21.0 or later
- [Helm][install-helm] version 3.0.0 or later
- [Visual Studio Code][download-vscode] installed on one of the [supported platforms](https://code.visualstudio.com/docs/supporting/requirements#_platforms) along with the [Bicep extension][bicep-extension].
- An existing [Azure Key Vault][azure-kv] resource with a valid TLS certificate for the Yelb web application.
- An existing [Azure DNS Zone][azure-dns] or equivalent DNS server for the name resolution of the [Yelb][yelb] application.

### Download the Azure application code

The **completed** application code for this workflow is available in our [GitHub repository][github-repo].

1. Clone the repository to a directory called `aws-to-azure-web-app-workshop` on your local machine using the following command:

    ```bash
    git clone https://github.com/azure-samples/aks-web-application-replicate-from-aws ./aws-to-azure-web-app-workshop
    ```

2. After you clone the repository, navigate to the `aws-to-azure-web-app-workshop` directory and start Visual Studio Code using the following commands:

    ```bash
    cd aws-to-azure-web-app-workshop
    code .
    ```

## Next step

> [Understand platform differences][eks-web-understand]
  
## Contributors

*Microsoft maintains this article. The following contributors originally wrote it*:

Principal author:
- Dixit Arora | Senior Customer Engineer
- [Paolo Salvatori](https://www.linkedin.com/in/paolo-salvatori) | Principal Customer Engineer

Other contributors:
- [Ken Kilty](https://www.linkedin.com/in/kennethkilty/) | Principal TPM
- [Russell de Pina](https://www.linkedin.com/in/rdepina/) | Principal TPM
- [Erin Schaffer](https://www.linkedin.com/in/erin-schaffer-65800215b/) | Content Developer 2

[yelb]: https://github.com/mreferre/yelb/

[eks-aws-waf]: https://aws.amazon.com/it/blogs/containers/protecting-your-amazon-eks-web-apps-with-aws-waf/
[azure-ag]: https://learn.microsoft.com/en-us/azure/application-gateway/for-containers/overview
[azure-waf]: https://learn.microsoft.com/en-us/azure/web-application-firewall/overview
[aks]: https://learn.microsoft.com/en-us/azure/aks/what-is-aks
[azure-free]: https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn
[azure-built-in-roles]: https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles
[azure-cli]: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
[aks-preview]: https://learn.microsoft.com/en-us/azure/aks/draft#install-the-aks-preview-azure-cli-extension
[install-jq]: https://jqlang.github.io/jq/
[install-python]: https://www.python.org/downloads/
[install-kubectl]: https://kubernetes.io/docs/tasks/tools/install-kubectl/
[install-helm]: https://helm.sh/docs/intro/install/
[download-vscode]: https://code.visualstudio.com/Download
[bicep-extension]: https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-bicep
[github-repo]: https://github.com/azure-samples/aks-web-application-replicate-from-aws
[eks-web-understand]: https://learn.microsoft.com/en-us/azure/aks/eks-web-understand
[azure-kv]: https://learn.microsoft.com/en-us/azure/key-vault/general/overview
[azure-dns]: https://learn.microsoft.com/en-us/azure/dns/dns-overview
