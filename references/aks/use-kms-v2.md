# Migrate to Key Management Service (KMS) v2 in Azure Kubernetes Service (AKS) (legacy)

> Source: https://learn.microsoft.com/en-us/azure/aks/use-kms-v2  
> Microsoft doc last updated: 12/22/2025


> [!IMPORTANT]
> This article applies to clusters using the legacy KMS experience that need to migrate from KMS v1 to KMS v2. For clusters running Kubernetes version 1.33 or later, we recommend using the new [KMS data encryption](https://learn.microsoft.com/en-us/azure/aks/kms-data-encryption) experience, which offers platform-managed keys, customer-managed keys with automatic key rotation, and a simplified configuration experience.

In this article, you learn how to migrate to KMS v2 for clusters with versions older than 1.27. Beginning in AKS version 1.27, turning on the KMS feature configures KMS v2. With KMS v2, you aren't limited to the 2,000 secrets that earlier versions support. For more information, see [KMS v2 improvements](https://kubernetes.io/blog/2023/05/16/kms-v2-moves-to-beta/).

> [!IMPORTANT]
> If your cluster version is older than 1.27 and you already turned on KMS, the upgrade to cluster version 1.27 or later is blocked.

## Turn off KMS

1. Disable KMS on an existing cluster using the [`az aks update`][az-aks-update] command with the `--disable-azure-keyvault-kms` parameter.

    ```azurecli-interactive
    az aks update --name $CLUSTER_NAME --resource-group $RESOURCE_GROUP --disable-azure-keyvault-kms
    ```

1. Update all secrets using the `kubectl get secrets` command to ensure the secrets created earlier are no longer encrypted. For larger clusters, you might want to subdivide the secrets by namespace or create an update script. If the previous command to update KMS fails, still run the following command to avoid unexpected state for KMS plugin.

    ```bash
    kubectl get secrets --all-namespaces -o json | kubectl replace -f -
    ```

    When you run the command, the following error is safe to ignore:

    ```output
    The object has been modified; please apply your changes to the latest version and try again.
    ```

## Upgrade your AKS cluster and turn on KMS

1. Upgrade your AKS cluster to version 1.27 or later using the [`az aks upgrade`][az-aks-upgrade] command with the `--kubernetes-version` parameter set to your desired version. The following example upgrades to version `1.27.1`:

    ```azurecli-interactive
    az aks upgrade --resource-group $RESOURCE_GROUP --name $CLUSTER_NAME --kubernetes-version 1.27.1
    ```

1. Once the upgrade completes, you can turn on KMS for a public or private key vault using one of the following resources:

    - [Enable a public key vault and KMS on an existing AKS cluster](https://learn.microsoft.com/en-us/azure/aks/use-kms-etcd-encryption#enable-a-public-key-vault-and-kms-on-an-existing-aks-cluster)
    - [Update an existing AKS cluster to turn on KMS etcd encryption for a private key vault](https://learn.microsoft.com/en-us/azure/aks/use-kms-etcd-encryption#update-an-existing-aks-cluster-to-turn-on-kms-etcd-encryption-for-a-private-key-vault)

1. Update all secrets using the `kubectl get secrets` command to ensure the secrets created earlier are no longer encrypted. For larger clusters, you might want to subdivide the secrets by namespace or create an update script. If the previous command to update KMS fails, still run the following command to avoid unexpected state for KMS plugin.

    ```bash
    kubectl get secrets --all-namespaces -o json | kubectl replace -f -
    ```

    When you run the command, the following error is safe to ignore:

    ```output
    The object has been modified; please apply your changes to the latest version and try again.
    ```

## Next steps

For more information on using KMS with AKS, see the following articles:

- [Update the key vault mode for an Azure Kubernetes Service (AKS) cluster with KMS etcd encryption](https://learn.microsoft.com/en-us/azure/aks/update-kms-key-vault)
- [Observability for KMS etcd encryption in Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/kms-observability)

[az-aks-upgrade]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-upgrade
[az-aks-update]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-update
