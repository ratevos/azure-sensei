# Migrate from Dapr OSS to the Dapr Extension for AKS

> Source: https://learn.microsoft.com/en-us/azure/aks/dapr-migration  
> Microsoft doc last updated: 02/06/2026


This article shows you how to migrate from Dapr OSS to the Dapr extension for AKS.

You can configure the Dapr extension to use and manage the Kubernetes resources created by Dapr OSS by either:
- [Checking for an existing Dapr installation by using the Azure CLI](#check-for-an-existing-dapr-installation) (*default method*)
- [Configuring the existing Dapr installation by using `--configuration-settings`](#configure-the-existing-dapr-installation-using---configuration-settings)

For more information, see [an overview of the Dapr extension for AKS][dapr-extension-aks].

## Check for an existing Dapr installation

When you [install the Dapr extension](https://learn.microsoft.com/en-us/azure/aks/dapr), the extension checks for an existing Dapr installation on your cluster. If Dapr exists, the extension uses and manages the Kubernetes resources created by Dapr OSS.

1. List the details of your current Dapr installation using the `helm list -A` command and save the Dapr release name and namespace from the output.

    ```azurecli-interactive
    helm list -A
    ```

2. Enter the Helm release name and namespace (from `helm list -A`) when prompted with the following questions:

    ```azurecli-interactive
    Enter the Helm release name for Dapr, or press Enter to use the default name [dapr]:
    Enter the namespace where Dapr is installed, or press Enter to use the default namespace [dapr-system]:
    ```

## Configure the existing Dapr installation using `--configuration-settings`

When you [create the Dapr extension](https://learn.microsoft.com/en-us/azure/aks/dapr), you can configure the extension to use and manage the Kubernetes resources created by Dapr OSS using the `--configuration-settings` flag.

1. List the details of your current Dapr installation using the `helm list -A` command and save the Dapr release name and namespace from the output.

    ```azurecli-interactive
    helm list -A
    ```

1. Create the Dapr extension by using [`az k8s-extension create`][az-k8s-extension-create] and use the `--configuration-settings` flags to set the Dapr release name and namespace.

    ```azurecli-interactive
    az k8s-extension create --cluster-type managedClusters \
    --cluster-name <your-AKS-cluster> \
    --resource-group <your-resource-group> \
    --name dapr \
    --extension-type Microsoft.Dapr \
    --configuration-settings "existingDaprReleaseName=dapr" \
    --configuration-settings "existingDaprReleaseNamespace=dapr-system"
    ```

## Update high availability (HA) mode or placement service settings

When installing the Dapr extension on top of an existing Dapr installation, you receive the following message:

```output
The extension will be installed on your existing Dapr installation. Note, if you have updated the default values for global.ha.* or dapr_placement.* in your existing Dapr installation, you must provide them in the configuration settings. Failing to do so will result in an error, since Helm upgrade will try to modify the StatefulSet. See <link> for more information.
```

Kubernetes only allows patching for limited fields in StatefulSets. If any of the HA mode or placement service settings are configured, the upgrade fails. To update the HA mode or placement service settings, you must delete the stateful set and then update the HA mode.

1. Delete the stateful set using the `kubectl delete` command.

   ```azurecli-interactive
   kubectl delete statefulset.apps/dapr-placement-server -n dapr-system
   ```

1. Update the HA mode using the [`az k8s-extension update`][az-k8s-extension-update] command.

   ```azurecli-interactive
   az k8s-extension update --cluster-type managedClusters \
   --cluster-name <your-AKS-cluster> \
   --resource-group <your-resource-group> \
   --name dapr \
   --extension-type Microsoft.Dapr \
   --auto-upgrade-minor-version true \  
   --configuration-settings "global.ha.enabled=true" \    
   ```

For more information, see the [Dapr production guidelines][dapr-prod-guidelines].

## Next step

> [Install the Dapr extension][dapr-howto]

[dapr-overview]: https://learn.microsoft.com/en-us/azure/aks/dapr-overview
[dapr-howto]: https://learn.microsoft.com/en-us/azure/aks/dapr
[dapr-extension-aks]: https://learn.microsoft.com/en-us/azure/aks/dapr-overview
[az-k8s-extension-create]: https://learn.microsoft.com/en-us/cli/azure/k8s-extension#az-k8s-extension-create
[az-k8s-extension-update]: https://learn.microsoft.com/en-us/cli/azure/k8s-extension#az-k8s-extension-update

[dapr-prod-guidelines]: https://docs.dapr.io/operations/hosting/kubernetes/kubernetes-production/#enabling-high-availability-in-an-existing-dapr-deployment
