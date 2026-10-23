# Use Service Tags for API Server Authorized IP Ranges in Azure Kubernetes Service (AKS) (preview)

> Source: https://learn.microsoft.com/en-us/azure/aks/api-server-service-tags  
> Microsoft doc last updated: 05/19/2024


Service tags for API server authorized IP ranges is a preview feature that allows you to use service tags to specify authorized IP ranges for the API server in Azure Kubernetes Service (AKS). This feature simplifies the management of authorized IP ranges by allowing you to use predefined service tags instead of manually specifying individual IP addresses or CIDR ranges.

## Prerequisites

- The Azure CLI version 2.0.76 or later installed and configured. Check your version using the `az --version` command. If you need to install or upgrade, see [Install Azure CLI][install-azure-cli].
- The [`aks-preview` Azure CLI extension](#install-the-aks-preview-azure-cli-extension) installed.
- The [`EnableServiceTagAuthorizedIPPreview` feature flag](#register-the-service-tag-authorized-ip-feature-flag) registered in your Azure subscription.

## Limitations

- Only one service tag is allowed in the `--api-server-authorized-ip-ranges` parameter. You can't specify multiple service tags.

## Install the `aks-preview` Azure CLI extension

1. Install the Azure CLI preview extension using the [`az extension add`][az-extension-add] command.

    ```azurecli-interactive
    az extension add --name aks-preview
    ```

1. Update the extension to make sure you have the latest version using the [`az extension update`][az-extension-update] command.

    ```azurecli-interactive
    az extension update --name aks-preview
    ```

## Register the service tag authorized IP feature flag

1. Register the `EnableServiceTagAuthorizedIPPreview` feature flag using the [`az feature register`][az-feature-register] command. It takes a few minutes for the registration to complete.

    ```azurecli-interactive
    az feature register --namespace "Microsoft.ContainerService" --name "EnableServiceTagAuthorizedIPPreview"
    ```

    Example output:

    ```output
    {
      "id": "/subscriptions/<subscription-id>/providers/Microsoft.ContainerService/features/EnableServiceTagAuthorizedIPPreview",
      "name": "EnableServiceTagAuthorizedIPPreview",
      "properties": {
        "state": "Registering"
      },
      "type": "Microsoft.ContainerService/features"
    }
    ```

1. Once the feature flag state changes from `Registering` to `Registered`, refresh the registration of the `Microsoft.ContainerService` resource provider using the [`az provider register`][az-provider-register] command.

    ```azurecli-interactive
    az provider register --namespace "Microsoft.ContainerService"
    ```

1. Verify the registration using the [`az feature show`][az-feature-show] command.

    ```azurecli-interactive
    az feature show --namespace "Microsoft.ContainerService" --name "EnableServiceTagAuthorizedIPPreview"
    ```

    Example output:

    ```output
    {
      "id": "/subscriptions/<subscription-id>/providers/Microsoft.ContainerService/features/EnableServiceTagAuthorizedIPPreview",
      "name": "EnableServiceTagAuthorizedIPPreview",
      "properties": {
        "state": "Registered"
      },
      "type": "Microsoft.ContainerService/features"
    }
    ```

## Create an AKS cluster with service tag authorized IP ranges

- Create a cluster with service tag authorized IP ranges using the [`az aks create`][az-aks-create] command with the `--api-server-authorized-ip-ranges` parameter. The following example creates a cluster named _myAKSCluster_ in the _myResourceGroup_ resource group and authorizes the `AzureCloud` service tag to allow all Azure services to access the API server and specify an extra IP address:

    ```azurecli-interactive
    az aks create --resource-group myResourceGroup --name myAKSCluster --api-server-authorized-ip-ranges AzureCloud,20.20.20.20
    ```

    > [!NOTE]
    > You should be able to curl the API server from an Azure virtual machine (VM) or Azure service that's part of the `AzureCloud` service tag.

[api-server-vnet-integration]: https://learn.microsoft.com/en-us/azure/aks/api-server-vnet-integration
[az-aks-create]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-create
[install-azure-cli]: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
[az-extension-add]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-add
[az-extension-update]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-update
[az-feature-register]: https://learn.microsoft.com/en-us/cli/azure/feature#az-feature-register
[az-feature-show]: https://learn.microsoft.com/en-us/cli/azure/feature#az-feature-show
[az-provider-register]: https://learn.microsoft.com/en-us/cli/azure/provider#az-provider-register
