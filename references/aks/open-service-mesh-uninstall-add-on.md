# Uninstall the Open Service Mesh (OSM) add-on from your Azure Kubernetes Service (AKS) cluster

> Source: https://learn.microsoft.com/en-us/azure/aks/open-service-mesh-uninstall-add-on  
> Microsoft doc last updated: 09/25/2024


This article shows you how to uninstall the OMS add-on and related resources from your AKS cluster.

> [!IMPORTANT]
> Starting on **September 30, 2027**, Azure Kubernetes Service (AKS) no longer supports the Open Service Mesh (OSM) add-on. The upstream [Open Service Mesh project](https://www.cncf.io/projects/open-service-mesh/) has been retired.
>
> If your cluster uses the OSM add-on, migrate to the Istio add-on before the end-of-support date. This retirement notice applies only to the managed OSM add-on and doesn't address open-source or self-managed service mesh installations. For migration steps, see [Migration guidance from the OSM add-on to the Istio add-on](https://learn.microsoft.com/en-us/azure/aks/open-service-mesh-istio-migration-guidance). To stay informed about AKS announcements and updates, follow the [AKS release notes](https://github.com/Azure/AKS/releases).

## Disable the OSM add-on from your cluster

* Disable the OSM add-on from your cluster using the [`az aks disable-addon`][az-aks-disable-addon] command and the `--addons` parameter.

    ```azurecli-interactive
    az aks disable-addons \
      --resource-group myResourceGroup \
      --name myAKSCluster \
      --addons open-service-mesh
    ```

## Remove OSM resources

* Uninstall the remaining resources on the cluster using the `osm uninstall cluster-wide-resources` command.

    ```console
    osm uninstall cluster-wide-resources
    ```

    > [!NOTE]
    > For version 1.1, the command is `osm uninstall mesh --delete-cluster-wide-resources`

    > [!IMPORTANT]
    > You must remove these additional resources after you disable the OSM add-on. Leaving these resources on your cluster may cause issues if you enable the OSM add-on again in the future.

## Next steps

Learn more about [Open Service Mesh][osm].

[az-aks-disable-addon]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-disable-addons
[osm]: https://learn.microsoft.com/en-us/azure/aks/open-service-mesh-about
