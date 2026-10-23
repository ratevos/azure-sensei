# Azure Kubernetes Service (AKS) managed NGINX ingress with the application routing add-on

> Source: https://learn.microsoft.com/en-us/azure/aks/app-routing  
> Microsoft doc last updated: 08/03/2026


> [!CAUTION]
>
> The [Kubernetes SIG Network](https://github.com/kubernetes/community/blob/master/sig-network/README.md) and the Security Response Committee [announced the retirement](https://www.kubernetes.dev/blog/2025/11/12/ingress-nginx-retirement/) of the [Ingress NGINX project](https://github.com/kubernetes/ingress-nginx/), with maintenance that ended in March 2026. Microsoft will provide official support for critical security patches for application routing add-on NGINX Ingress resources through **November 2026**.
>
> AKS aligns with upstream Kubernetes and uses **[Gateway API](https://gateway-api.sigs.k8s.io) as the long-term standard for ingress and L7 traffic management**. Migrate before support ends in November 2026, based on your requirements:
>
> - **Application routing add-on users** and **OSS NGINX users**: Migrate to the [application routing Gateway API implementation](https://learn.microsoft.com/en-us/azure/aks/app-routing-gateway-api) for a Gateway API-based ingress traffic management experience, or to [Application Gateway for Containers](https://learn.microsoft.com/en-us/azure/application-gateway/for-containers/overview), which supports both Ingress API and Gateway API.
> - **Service mesh or advanced ingress requirements**: Consider [Gateway API ingress with the Istio service mesh add-on](https://learn.microsoft.com/en-us/azure/aks/istio-gateway-api). You can use it for ingress without injecting sidecars into your workloads. If you need request header and body size limits, Lua scripts, or rate limiting, review the [Gateway API limitations and alternatives](https://learn.microsoft.com/en-us/azure/aks/app-routing-gateway-api#limitations).

One way to route Hypertext Transfer Protocol (HTTP) and secure (HTTPS) traffic to applications running on an Azure Kubernetes Service (AKS) cluster is to use the [Kubernetes Ingress object][kubernetes-ingress-object-overview]. When you enable the application routing add-on with NGINX, it creates, configures, and manages an Ingress controller in your AKS cluster.

This article shows you how to enable the managed NGINX Ingress controller and configure an Ingress object to route traffic to an application in your AKS cluster.

## Application routing add-on with NGINX features

The application routing add-on with NGINX delivers the following:

- Easy configuration of managed NGINX Ingress controllers based on [Kubernetes NGINX Ingress controller][kubernetes-nginx-ingress].
- Integration with [Azure DNS][azure-dns-overview] for public and private zone management.
- SSL termination with certificates stored in Azure Key Vault.

For other configurations, see:

- [DNS and SSL configuration][dns-ssl-configuration].
- [Application routing add-on configuration][custom-ingress-configurations].
- [Configure internal NGINX ingress controller for Azure private DNS zone][create-nginx-private-controller].

> [!IMPORTANT]
> Starting on **September 30, 2027**, Azure Kubernetes Service (AKS) no longer supports the Open Service Mesh (OSM) add-on. The upstream [Open Service Mesh project](https://www.cncf.io/projects/open-service-mesh/) has been retired.
>
> If your cluster uses the OSM add-on, migrate to the Istio add-on before the end-of-support date. This retirement notice applies only to the managed OSM add-on and doesn't address open-source or self-managed service mesh installations. For migration steps, see [Migration guidance from the OSM add-on to the Istio add-on](https://learn.microsoft.com/en-us/azure/aks/open-service-mesh-istio-migration-guidance). To stay informed about AKS announcements and updates, follow the [AKS release notes](https://github.com/Azure/AKS/releases).

## Prerequisites

- An Azure subscription. If you don't have an Azure subscription, you can create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- Azure CLI version 2.54.0 or later installed and configured. Run `az --version` to find the version. If you need to install or upgrade, see [Install Azure CLI][install-azure-cli].

## Limitations

- The application routing add-on supports up to five Azure DNS zones.
- The application routing add-on can only be enabled on AKS clusters with [managed identity][managed-identity].
- All global Azure DNS zones integrated with the add-on have to be in the same resource group.
- All private Azure DNS zones integrated with the add-on have to be in the same resource group.
- Editing the ingress-nginx `ConfigMap` in the `app-routing-system` namespace isn't supported.
- If a snippet annotation value matches any of the following blocked values, the Ingress isn't configured:

    | Blocked value | Effect |
    |--|--|
    | `load_module` | The Ingress isn't configured. |
    | `lua_package` | The Ingress isn't configured. |
    | `_by_lua` | The Ingress isn't configured. |
    | `location` | The Ingress isn't configured. |
    | `root` | The Ingress isn't configured. |
    | `proxy_pass` | The Ingress isn't configured. |
    | `serviceaccount` | The Ingress isn't configured. |
    | `{` | The Ingress isn't configured. |
    | `}` | The Ingress isn't configured. |
    | `'` | The Ingress isn't configured. |

- The add-on doesn't officially support injecting non-Microsoft-managed sidecars (for example, custom telemetry, logging, or security agents) into the ingress-nginx proxy pods that it manages. If you choose to inject your own sidecar into a managed proxy pod, Microsoft provides only best-effort support for any issues you encounter.

## Enable the application routing add-on using Azure CLI

### Enable on a new cluster

To enable application routing on a new cluster, use the [`az aks create`][az-aks-create] command, specifying the `--enable-app-routing` flag.

```azurecli-interactive
az aks create \
    --resource-group <resource-group-name> \
    --name <cluster-name> \
    --location <location> \
    --enable-app-routing \
    --generate-ssh-keys
```

### Enable on an existing cluster

To enable application routing on an existing cluster, use the [`az aks approuting enable`][az-aks-approuting-enable] command.

```azurecli-interactive
az aks approuting enable --resource-group <resource-group-name> --name <cluster-name>
```

---

## Connect to your AKS cluster

To connect to the Kubernetes cluster from your local computer, you use [`kubectl`][kubectl], the Kubernetes command-line client. You can install it locally using the [`az aks install-cli`][az-aks-install-cli] command. If you use the Azure Cloud Shell, `kubectl` is already installed.

Configure `kubectl` to connect to your Kubernetes cluster using the [`az aks get-credentials`][az-aks-get-credentials] command.

```azurecli-interactive
az aks get-credentials --resource-group <resource-group-name> --name <cluster-name>
```

## Deploy an application

Kubernetes Ingress objects define routing rules for an Ingress controller. Use the application routing add-on's managed Ingress class and supported annotations to configure how its controller handles traffic.

1. Create the application namespace called `aks-store` to run the example pods using the `kubectl create namespace` command.

    ```bash
    kubectl create namespace aks-store
    ```

1. Deploy the AKS store application using the following YAML manifest file:

    ```bash
    kubectl apply -f https://raw.githubusercontent.com/Azure-Samples/aks-store-demo/main/sample-manifests/docs/app-routing/aks-store-deployments-and-services.yaml -n aks-store
    ```

  This manifest creates `rabbitmq`, `order-service`, `product-service`, and `store-front` Deployments and corresponding Services. The `store-front` Service exposes port 80, which the Ingress routes to in the next section.

### Create the Ingress object

When you enable the application routing add-on, it creates an Ingress class named _webapprouting.kubernetes.azure.com_. Specify this class in an Ingress object to use the add-on's managed NGINX Ingress controller.

1. Copy the following YAML manifest into a new file named **ingress.yaml** and save the file to your local computer.

    ```yaml
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: store-front
      namespace: aks-store
    spec:
      ingressClassName: webapprouting.kubernetes.azure.com
      rules:
      - http:
          paths:
          - backend:
              service:
                name: store-front
                port:
                  number: 80
            path: /
            pathType: Prefix
    ```

1. Create the ingress resource using the [`kubectl apply`][kubectl-apply] command.

    ```bash
    kubectl apply -f ingress.yaml -n aks-store
    ```

    The following example output shows the created resource:

    ```output
    ingress.networking.k8s.io/store-front created
    ```

## Verify the managed Ingress resource

You can verify the managed Ingress was created using the `kubectl get ingress` command.

```bash
kubectl get ingress -n aks-store
```

The following example output shows the created managed Ingress:

```output
NAME          CLASS                                HOSTS   ADDRESS       PORTS   AGE
store-front   webapprouting.kubernetes.azure.com   *       51.8.10.109   80      110s
```

You can verify that the AKS store works by pointing your browser to the public IP address of the Ingress controller. The following command retrieves the external IP address assigned by the load balancer to the managed NGINX ingress controller's `nginx` Service in the `app-routing-system` namespace:

```bash
kubectl get service -n app-routing-system nginx -o jsonpath="{.status.loadBalancer.ingress[0].ip}"
```

## Remove the application routing add-on

To remove the associated namespace, use the `kubectl delete namespace` command.

```bash
kubectl delete namespace aks-store
```

To remove the application routing add-on from your cluster, use the [`az aks approuting disable`][az-aks-approuting-disable] command.

```azurecli-interactive
az aks approuting disable --name <cluster-name> --resource-group <resource-group-name>
```

> [!NOTE]
> To avoid potential disruption of traffic into the cluster when you disable the application routing add-on, some Kubernetes resources, including _configMaps_, _secrets_, and the _deployment_ that runs the controller, remain on the cluster. These resources are in the _app-routing-system_ namespace. You can remove these resources if they're no longer needed by deleting the namespace with `kubectl delete ns app-routing-system`.

## Related content

- Enable the [application routing Gateway API implementation][app-routing-gateway-api] to manage ingress traffic with the Kubernetes Gateway API.
- [Configure custom ingress configurations][custom-ingress-configurations] shows how to create an advanced Ingress configuration. [Configure a custom domain using Azure DNS to manage DNS zones and setup a secure ingress][dns-ssl-configuration].
- To integrate with an Azure internal load balancer and configure a private Azure DNS zone to enable DNS resolution for the private endpoints to resolve specific domains, see [Configure internal NGINX ingress controller for Azure private DNS zone][create-nginx-private-controller].
- Learn about monitoring the ingress-nginx controller metrics included with the application routing add-on with [Prometheus in Grafana][prometheus-in-grafana] (preview) as part of analyzing the performance and usage of your application.

[azure-dns-overview]: https://learn.microsoft.com/en-us/azure/dns/dns-overview
[az-aks-approuting-enable]: https://learn.microsoft.com/en-us/cli/azure/aks/approuting#az-aks-approuting-enable
[az-aks-approuting-disable]: https://learn.microsoft.com/en-us/cli/azure/aks/approuting#az-aks-approuting-disable
[az-aks-install-cli]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-install-cli
[az-aks-get-credentials]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-get-credentials
[install-azure-cli]: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
[dns-ssl-configuration]: https://learn.microsoft.com/en-us/azure/aks/app-routing-dns-ssl
[custom-ingress-configurations]: https://learn.microsoft.com/en-us/azure/aks/app-routing-nginx-configuration
[az-aks-create]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-create
[prometheus-in-grafana]: https://learn.microsoft.com/en-us/azure/aks/app-routing-nginx-prometheus
[create-nginx-private-controller]: https://learn.microsoft.com/en-us/azure/aks/create-nginx-ingress-private-controller
[managed-identity]: https://learn.microsoft.com/en-us/azure/aks/use-managed-identity
[app-routing-gateway-api]: https://learn.microsoft.com/en-us/azure/aks/app-routing-gateway-api

[kubernetes-ingress-object-overview]: https://kubernetes.io/docs/concepts/services-networking/ingress/
[kubernetes-nginx-ingress]: https://kubernetes.github.io/ingress-nginx/
[kubectl]: https://kubernetes.io/docs/reference/kubectl/
[kubectl-apply]: https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/
