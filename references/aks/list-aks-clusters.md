# List running Azure Kubernetes Service (AKS) clusters in an Azure subscription

> Source: https://learn.microsoft.com/en-us/azure/aks/list-aks-clusters  
> Microsoft doc last updated: 08/12/2026


You can list Azure Kubernetes Service (AKS) clusters in a subscription by using the Azure portal, Azure CLI, or the AKS REST API. Use Azure CLI or REST API results to identify which clusters are running.

## Before you begin

- An Azure account with access to the subscription that contains the AKS clusters and permission to read the cluster resources.
- The latest version of Azure CLI. For more information, see [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) or [Update Azure CLI](https://learn.microsoft.com/en-us/cli/azure/update-azure-cli). Azure CLI is preinstalled in [Azure Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview).
- A [Microsoft Entra access token for Azure Resource Manager (ARM)](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resources-rest) to call the REST API directly.

## Understand AKS cluster states

AKS cluster details include both a power state and a provisioning state:

- The `powerState.code` property indicates whether the cluster is `Running` or `Stopped`.
- The `provisioningState` property indicates the status of the latest Azure resource operation, such as `Succeeded`, `Creating`, `Starting`, or `Stopping`.

To determine whether a cluster is currently running, use `powerState.code`. A `provisioningState` value of `Succeeded` doesn't indicate whether the cluster is running because a stopped cluster can also have a successful provisioning state.

## List AKS clusters in the Azure portal

1. Sign in to the Azure portal.
1. In the portal search box, enter **Kubernetes services**, and then select **Kubernetes services**.
1. Select the subscription that contains your AKS clusters. You can also filter the list by resource group, location, or other available properties.
1. Select a cluster name to open its **Overview** page and view its configuration.

On the cluster page, select **Connect** to get connection instructions. To view resources in a running cluster, select **Kubernetes resources**. You need permissions for the AKS cluster, the Kubernetes API, and the Kubernetes objects. For more information, see [Access Kubernetes resources by using the Azure portal](https://learn.microsoft.com/en-us/azure/aks/kubernetes-portal).

The portal procedure lists and opens clusters. To determine the power state of clusters consistently across a subscription, use the Azure CLI or REST API method in this article and check `powerState.code`.

## List AKS clusters by using Azure CLI

1. Sign in to Azure.

    ```azurecli-interactive
    az login
    ```

1. If you have access to multiple subscriptions, set the subscription that contains the AKS clusters.

    ```azurecli-interactive
    az account set --subscription <subscription-id>
    ```

1. List the AKS clusters in the selected subscription. The following command displays each cluster's name, resource group, location, power state, and provisioning state:

    ```azurecli-interactive
    az aks list --query "[].{Name:name, ResourceGroup:resourceGroup, Location:location, PowerState:powerState.code, ProvisioningState:provisioningState}" --output table
    ```

    The output resembles the following example:

    ```output
    Name          ResourceGroup    Location    PowerState    ProvisioningState
    ------------  ---------------  ----------  ------------  -------------------
    aks-prod      rg-aks-prod      eastus      Running       Succeeded
    aks-dev       rg-aks-dev       westus2     Stopped       Succeeded
    ```

    To list clusters in a specific resource group, add the `--resource-group` parameter.

    ```azurecli-interactive
    az aks list --resource-group <resource-group-name> --query "[].{Name:name, PowerState:powerState.code}" --output table
    ```

1. To list only running clusters, filter on `powerState.code`.

    ```azurecli-interactive
    az aks list --query "[?powerState.code=='Running'].{Name:name, ResourceGroup:resourceGroup, Location:location}" --output table
    ```

For more information about the command and its output options, see the [`az aks list`](https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-list) reference.

## List AKS clusters by using the REST API

Use the [Managed Clusters - List](https://learn.microsoft.com/en-us/rest/api/aks/managed-clusters/list) operation to get AKS clusters in a subscription. Send the following request, replacing `<subscription-id>` with your Azure subscription ID:

```http
GET https://management.azure.com/subscriptions/<subscription-id>/providers/Microsoft.ContainerService/managedClusters?api-version=2025-09-01
Authorization: Bearer <access-token>
```

The response contains a `value` array of AKS cluster resources. When `properties.powerState.code` is present, its value indicates whether the cluster is `Running` or `Stopped`. If `powerState` is missing or null, treat the cluster's power state as unknown; don't infer it from `provisioningState`. If the response includes `nextLink`, send a GET request to that URL to retrieve the next page of results.

> [!IMPORTANT]
> Azure exposes Kubernetes cluster resources for multiple services. The Azure Operator Nexus Network Cloud operation uses the `Microsoft.NetworkCloud/kubernetesClusters` resource type and doesn't list AKS clusters. To list AKS clusters, use the `Microsoft.ContainerService/managedClusters` operation shown in this article.

## Next steps

- [Connect to an AKS cluster](https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-cli#connect-to-the-cluster)
- [Stop and start an AKS cluster](https://learn.microsoft.com/en-us/azure/aks/start-stop-cluster)
- [Access Kubernetes resources by using the Azure portal](https://learn.microsoft.com/en-us/azure/aks/kubernetes-portal)
