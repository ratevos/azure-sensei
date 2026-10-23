# Quickstart: Create an Azure Kubernetes Service (AKS) Automatic cluster

> Source: https://learn.microsoft.com/en-us/azure/aks/automatic/quick-automatic-managed-network  
> Microsoft doc last updated: 09/15/2026


**Applies to**: :heavy_check_mark: AKS Automatic

[Azure Kubernetes Service (AKS) Automatic][what-is-aks-automatic] is a managed Kubernetes experience that automates AKS cluster setup and operations and embeds best practice configurations. AKS Automatic also includes a [pod readiness SLA][azure-sla] that guarantees 99.9% of qualifying pod readiness operations complete within 5 minutes, guaranteeing reliable, self-healing infrastructure for your applications. In this quickstart, you learn how to:

- Deploy an AKS Automatic cluster.
- Run a sample multi-container application with a group of microservices and web front ends simulating a retail scenario.

## Before you begin

- This quickstart assumes a basic understanding of Kubernetes concepts. For more information, see [Kubernetes core concepts for Azure Kubernetes Service (AKS)][kubernetes-concepts].
- AKS Automatic [enables Azure Policy on your AKS cluster][policy-for-kubernetes], but you should preregister the `Microsoft.PolicyInsights` resource provider in your subscription. For more information, see [Azure resource providers and types][az-provider-register].

:::zone target="docs" pivot="azure-cli"

- Azure CLI version 2.86.0 or later. To find the version, run `az --version` command. If you need to install or upgrade, see [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli).
- If you have multiple Azure subscriptions, select the appropriate subscription ID to bill resources to using the [`az account set`](https://learn.microsoft.com/en-us/cli/azure/account#az-account-set) command.

:::zone-end

:::zone target="docs" pivot="bicep"

- To deploy a Bicep file, you need write access on the resources you create and access to all operations on the `Microsoft.Resources/deployments` resource type. For example, to create a virtual machine (VM), you need `Microsoft.Compute/virtualMachines/write` and `Microsoft.Resources/deployments/*` permissions. For a list of roles and permissions, see [Azure built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles).

:::zone-end

:::zone target="docs" pivot="terraform"

- [Install and configure Terraform][terraform-install-configure].

> [!NOTE]
> This sample creates the AKS Automatic cluster with the AzureRM provider's [`azurerm_kubernetes_automatic_cluster`](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/kubernetes_automatic_cluster) resource, which requires AzureRM provider version `v4.81` or later. For an equivalent sample that uses the [AzAPI provider](https://registry.terraform.io/providers/Azure/azapi/latest/docs) instead, see [101-aks-automatic-azapi](https://github.com/Azure/terraform/tree/master/quickstart/101-aks-automatic-azapi). Reach for AzAPI when you need direct control over the managed cluster API payload, or an API version or property that the AzureRM provider hasn't surfaced yet.

:::zone-end

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

:::zone target="docs" pivot="azure-cli,bicep"

## Create a resource group

An [Azure resource group][azure-resource-group] is a logical group in which Azure resources are deployed and managed.

Create a resource group using the [`az group create`][az-group-create] command. The following example creates a resource group named _myResourceGroup_ in the _canadacentral_ location:

```azurecli-interactive
az group create --name myResourceGroup --location canadacentral
```

The following sample output resembles successful creation of the resource group:

```output
{
  "id": "/subscriptions/<guid>/resourceGroups/myResourceGroup",
  "location": "canadacentral",
  "managedBy": null,
  "name": "myResourceGroup",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null
}
```

:::zone-end

:::zone target="docs" pivot="azure-cli"

## Create an AKS Automatic cluster

Create an AKS Automatic cluster using the [`az aks create`][az-aks-create] command with the `--sku` parameter set to `automatic`. The following example creates a cluster named _myAKSAutomaticCluster_ with Managed Prometheus and the Container Insights integration enabled:

```azurecli-interactive
az aks create \
    --resource-group myResourceGroup \
    --name myAKSAutomaticCluster \
    --sku automatic
    --enable-hosted-system
```

When the deployment finishes, the output shows a `hostedSystemProfile` property with the `enabled` property set to `true`. You can also run the following command to display the `hostedSystemProfile` properties:

```azurecli-interactive
az aks show \
  --resource-group myResourceGroup \
  --name myAKSAutomaticCluster \
  --query hostedSystemProfile
```

```output
{
  "enabled": true,
  "nodeSubnetId": null,
  "systemNodeSubnetId": null
}
```

:::zone-end

:::zone target="docs" pivot="azure-portal"

## Create Automatic Kubernetes cluster

1. To create an AKS Automatic cluster, search for and select **Kubernetes services**. This takes you to the **Kubernetes center (preview)** page.
1. On the **Kubernetes center (preview)** page, select **Create** > **Automatic Kubernetes cluster**.

    

1. On the **Basics** tab, fill in all the required fields (Subscription, Resource group, Kubernetes cluster name, and Region), and then select **Next**.

    

1. On the **Monitoring** tab, select your desired monitoring configurations from Azure Monitor (Container Insights), Managed Prometheus, Grafana Dashboards, and Alerts, and then select **Next**.

    

1. On the **Advanced** tab, select your desired advanced configurations Private access, Azure Virtual Networking, Managed identity, Container Network Security (ACNS), and Managed Kubernetes Namespaces, and then select **Review + create**.

    

1. Review the configurations on the **Review + create** tab, and then select **Create** to deploy the AKS Automatic cluster.
1. Get started with configuring your first application from GitHub and set up an automated deployment pipeline.

    

:::zone-end

:::zone target="docs" pivot="bicep"

## Review the Bicep file

The following Bicep file defines an AKS Automatic cluster:

```bicep
@description('The name of the managed cluster resource.')
param clusterName string = 'myAKSAutomaticCluster'

@description('The location of the managed cluster resource.')
param location string = resourceGroup().location

resource aks 'Microsoft.ContainerService/managedClusters@2026-02-01' ' = {
  name: clusterName
  location: location
  sku: {
    name: 'Automatic'
  }
  identity: {
    type: 'SystemAssigned'
  }
}
```

For more information about the resource defined in the Bicep file, see the [**Microsoft.ContainerService/managedClusters**](https://learn.microsoft.com/en-us/azure/templates/microsoft.containerservice/managedclusters?tabs=bicep&pivots=deployment-language-bicep) reference.

## Deploy the Bicep file

1. Save the Bicep file as **main.bicep** to your local computer.

    > [!IMPORTANT]
    > The Bicep file sets the `clusterName` param to the string _myAKSAutomaticCluster_. If you want to use a different cluster name, make sure to update the string to your preferred cluster name before saving the file to your computer.

1. Deploy the Bicep file using the [`az deployment group create`][az-deployment-group-create] command.

      ```azurecli-interactive
    az deployment group create --resource-group myResourceGroup --template-file main.bicep
    ```

    It takes a few minutes to create the AKS cluster. Wait for the cluster to be successfully deployed before you move on to the next step.

:::zone-end

:::zone target="docs" pivot="terraform"

## Review the Terraform code

> [!NOTE]
> The sample code for this article is located in the [Azure Terraform GitHub repo](https://github.com/Azure/terraform/tree/master/quickstart/101-aks-automatic). You can view the log file containing the [test results from current and previous versions of Terraform](https://github.com/Azure/terraform/tree/master/quickstart/101-aks-automatic/TestRecord.md).
>
> See more [articles and sample code showing how to use Terraform to manage Azure resources](https://learn.microsoft.com/en-us/azure/terraform).

1. Create a directory to test the sample Terraform code and set it as the current directory.
1. Create a file named `providers.tf` and insert the following code:

    [!code-terraform[master](https://learn.microsoft.com/en-us/azure/aks/terraform_samples/quickstart/101-aks-automatic/providers.tf)]

1. Create a file named `main.tf` and add the following code:

    [!code-terraform[master](https://learn.microsoft.com/en-us/azure/aks/terraform_samples/quickstart/101-aks-automatic/main.tf)]

1. Create a file named `variables.tf` and add the following code:

    [!code-terraform[master](https://learn.microsoft.com/en-us/azure/aks/terraform_samples/quickstart/101-aks-automatic/variables.tf)]

1. Create a file named `outputs.tf` and insert the following code:

    [!code-terraform[master](https://learn.microsoft.com/en-us/azure/aks/terraform_samples/quickstart/101-aks-automatic/outputs.tf)]

## Initialize Terraform

Run [terraform init](https://developer.hashicorp.com/terraform/cli/commands/init) to initialize the Terraform deployment. This command downloads the Azure providers required to manage your Azure resources.

```console
terraform init -upgrade
```

## Create a Terraform execution plan

Run [terraform plan](https://developer.hashicorp.com/terraform/cli/commands/plan) to create an execution plan.

```console
terraform plan -out main.tfplan
```

## Apply a Terraform execution plan

Run [terraform apply](https://developer.hashicorp.com/terraform/cli/commands/apply) to apply the execution plan to your cloud infrastructure.

```console
terraform apply main.tfplan
```

Creating an AKS Automatic cluster takes several minutes to complete.

## Verify the cluster

1. Get the Azure resource group name and cluster name.

    ```console
    resource_group_name=$(terraform output -raw resource_group_name)
    cluster_name=$(terraform output -raw cluster_name)
    ```

1. Run [az aks show][az-aks-show] to display the cluster and confirm it uses the `Automatic` SKU.

    ```azurecli
    az aks show --resource-group $resource_group_name --name $cluster_name --query "{name:name, sku:sku, provisioningState:provisioningState}"
    ```

:::zone-end

## Connect to the cluster

To manage a Kubernetes cluster, use the Kubernetes command-line client, [kubectl][kubectl]. `kubectl` is already installed if you use Azure Cloud Shell. You can install `kubectl` locally using the [`az aks install-cli`][az-aks-install-cli] command. AKS Automatic clusters are configured with [Microsoft Entra ID for Kubernetes role-based access control (RBAC)][aks-entra-rbac].

> [!NOTE]
> When you create a cluster using the Azure CLI, your user is [assigned built-in roles][aks-entra-rbac-builtin-roles] for `Azure Kubernetes Service RBAC Cluster Admin`.

:::zone target="docs" pivot="azure-cli,bicep,azure-portal"

1. Configure `kubectl` to connect to your Kubernetes cluster using the [`az aks get-credentials`][az-aks-get-credentials] command. This command downloads credentials and configures the Kubernetes CLI to use them.

    ```azurecli-interactive
    az aks get-credentials --resource-group myResourceGroup --name myAKSAutomaticCluster
    ```

:::zone-end

:::zone target="docs" pivot="terraform"

1. Configure `kubectl` to connect to your Kubernetes cluster by using the [`az aks get-credentials`][az-aks-get-credentials] command. This command downloads credentials and configures the Kubernetes CLI to use them.

    ```azurecli-interactive
    az aks get-credentials --resource-group $resource_group_name --name $cluster_name
    ```

:::zone-end

2. Verify the connection to your cluster using the [`kubectl get`][kubectl-get] command. This command returns a list of the cluster nodes.

    ```bash
    kubectl get nodes
    ```

    The following sample output shows how you're asked to sign in:

    ```output
    To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code AAAAAAAAA to authenticate.
    ```

    After you sign in, the following sample output shows the managed system node pools. Make sure the node status is _Ready_.

    ```output
    NAME                           STATUS   ROLES    AGE   VERSION
    aks-hostedpool-16652789-vms1   Ready    <none>   19m   v1.34.7
    aks-hostedpool-16652789-vms2   Ready    <none>   19m   v1.34.7
    aks-hostedpool-16652789-vms3   Ready    <none>   19m   v1.34.7
    aks-system-surge-zq4d2         Ready    <none>   19m   v1.34.7
    ```

## Deploy the application

To deploy the application, you use a manifest file to create all the objects required to run the [AKS Store application](https://github.com/Azure-Samples/aks-store-demo). A [Kubernetes manifest file][kubernetes-deployment] defines a cluster's desired state, such as which container images to run. The manifest includes the following Kubernetes deployments and services:

- **Store front**: Web application for customers to view products and place orders.
- **Product service**: Shows product information.
- **Order service**: Places orders.
- **Rabbit MQ**: Message queue for an order queue.

> [!NOTE]
> We don't recommend running stateful containers, such as Rabbit MQ, without persistent storage for production. These are used here for simplicity, but we recommend using managed services, such as Azure Cosmos DB or Azure Service Bus.

1. Create a namespace `aks-store-demo` to deploy the Kubernetes resources into.

    ```bash
    kubectl create ns aks-store-demo
    ```

1. Deploy the application using the [`kubectl apply`][kubectl-apply] command into the `aks-store-demo` namespace. The YAML file defining the deployment is on [GitHub](https://github.com/Azure-Samples/aks-store-demo).

    ```bash
    kubectl apply -n aks-store-demo -f https://raw.githubusercontent.com/Azure-Samples/aks-store-demo/main/aks-store-ingress-quickstart.yaml
    ```

    The following sample output shows the deployments and services:

    ```output
    statefulset.apps/rabbitmq created
    configmap/rabbitmq-enabled-plugins created
    service/rabbitmq created
    deployment.apps/order-service created
    service/order-service created
    deployment.apps/product-service created
    service/product-service created
    deployment.apps/store-front created
    service/store-front created
    ingress/store-front created
    ```

## Test the application

When the application runs, a Kubernetes service exposes the application front end to the internet. This process can take a few minutes to complete.

1. Check the status of the deployed pods using the [kubectl get pods][kubectl-get] command. Make sure all pods are `Running` before proceeding. If this is the first workload you deploy, it might take a few minutes for [node auto provisioning][node-auto-provisioning] to create a node pool to run the pods.

    ```bash
    kubectl get pods -n aks-store-demo
    ```

1. Check for a public IP address for the store-front application. Monitor progress using the [kubectl get service][kubectl-get] command with the `--watch` argument.

    ```bash
    kubectl get ingress store-front -n aks-store-demo --watch
    ```

    The **ADDRESS** output for the `store-front` service initially shows empty:

    ```output
    NAME          CLASS                                HOSTS   ADDRESS        PORTS   AGE
    store-front   webapprouting.kubernetes.azure.com   *                      80      12m
    ```

1. Once the **ADDRESS** changes from blank to an actual public IP address, use `CTRL-C` to stop the `kubectl` watch process.

    The following sample output shows a valid public IP address assigned to the service:

    ```output
    NAME          CLASS                                HOSTS   ADDRESS        PORTS   AGE
    store-front   webapprouting.kubernetes.azure.com   *       4.255.22.196   80      12m
    ```

1. Open a web browser to the external IP address of your ingress to see the Azure Store app in action.

    

## Delete the cluster

If you don't plan on going through the [AKS tutorial][aks-tutorial], clean up unnecessary resources to avoid Azure charges.

:::zone target="docs" pivot="azure-cli,bicep,azure-portal"

Remove the resource group, container service, and all related resources using the [`az group delete`][az-group-delete] command.

```azurecli-interactive
az group delete --name myResourceGroup --yes --no-wait
```

> [!NOTE]
> The AKS cluster was created with a system-assigned managed identity, which is the default identity option used in this quickstart. The platform manages this identity, so you don't need to manually remove it.

:::zone-end

:::zone target="docs" pivot="terraform"

When you no longer need the resources you created by using Terraform, run [terraform plan](https://developer.hashicorp.com/terraform/cli/commands/plan) and specify the `destroy` flag.

```console
terraform plan -destroy -out main.destroy.tfplan
```

Run [terraform apply](https://developer.hashicorp.com/terraform/cli/commands/apply) to apply the execution plan.

```console
terraform apply main.destroy.tfplan
```

:::zone-end

## Related content

In this quickstart, you deployed a Kubernetes cluster using [AKS Automatic][what-is-aks-automatic] and then deployed a simple multi-container application to it. This sample application is for demo purposes only and doesn't represent all the best practices for Kubernetes applications. For guidance on creating full solutions with AKS for production, see [AKS solution guidance][aks-solution-guidance].

To learn more about AKS Automatic, see the [Introduction to Azure Kubernetes Service (AKS) Automatic][what-is-aks-automatic]

[kubectl]: https://kubernetes.io/docs/reference/kubectl/
[kubectl-apply]: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply
[kubectl-get]: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get

[kubernetes-concepts]: https://learn.microsoft.com/en-us/azure/aks/concepts-clusters-workloads
[aks-tutorial]: https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-prepare-app
[azure-resource-group]: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview
[az-aks-create]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-create
[az-aks-get-credentials]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-get-credentials
[az-aks-install-cli]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-install-cli
[az-aks-show]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-show
[az-group-create]: https://learn.microsoft.com/en-us/cli/azure/group#az-group-create
[az-group-delete]: https://learn.microsoft.com/en-us/cli/azure/group#az-group-delete
[node-auto-provisioning]: https://learn.microsoft.com/en-us/azure/aks/node-autoprovision
[kubernetes-deployment]: https://learn.microsoft.com/en-us/azure/aks/concepts-clusters-workloads#deployments-and-yaml-manifests
[aks-solution-guidance]: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-start-here?toc=/azure/aks/toc.json&bc=/azure/aks/breadcrumb/toc.json
[az-provider-register]: https://learn.microsoft.com/en-us/cli/azure/provider#az-provider-register
[what-is-aks-automatic]: https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic
[aks-entra-rbac]: https://learn.microsoft.com/en-us/azure/aks/entra-id-authorization
[aks-entra-rbac-builtin-roles]: https://learn.microsoft.com/en-us/azure/aks/entra-id-authorization#create-role-assignments-for-cluster-access
[policy-for-kubernetes]: https://learn.microsoft.com/en-us/azure/governance/policy/concepts/policy-for-kubernetes#install-azure-policy-add-on-for-aks
[terraform-install-configure]: https://learn.microsoft.com/en-us/azure/developer/terraform/quickstart-configure
