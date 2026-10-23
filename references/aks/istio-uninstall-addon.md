# Uninstall Istio-based service mesh add-on for Azure Kubernetes Service

> Source: https://learn.microsoft.com/en-us/azure/aks/istio-uninstall-addon  
> Microsoft doc last updated: 03/28/2024


This article shows you how to uninstall the Istio-based service mesh add-on for Azure Kubernetes Service (AKS) cluster and delete sample resources created in the [Getting Started][istio-getting-started] guide.

## Uninstall the add-on

Disabling the service mesh add-on removes all **Istio components** from your cluster. This includes **Istio CRDs and custom resources**, the **Istio control plane**, **ingress and egress gateway configurations**, and the managed namespaces `aks-istio-system` and `aks-istio-ingress` (along with any resources in them). To uninstall the add-on, run the following command:

```azurecli-interactive
az aks mesh disable --resource-group ${RESOURCE_GROUP} --name ${CLUSTER}
```

## Clean up sample resources

Use `kubectl delete` to delete the sample application if it was installed:

```bash
kubectl delete -f https://raw.githubusercontent.com/istio/istio/release-1.24/samples/bookinfo/platform/kube/bookinfo.yaml
```

[istio-getting-started]: https://learn.microsoft.com/en-us/azure/aks/istio-deploy-addon
