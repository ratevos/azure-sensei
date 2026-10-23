# Monitor the ingress-nginx controller metrics in the application routing add-on with Prometheus

> Source: https://learn.microsoft.com/en-us/azure/aks/app-routing-nginx-prometheus  
> Microsoft doc last updated: 09/15/2025


> [!CAUTION]
>
> The [Kubernetes SIG Network](https://github.com/kubernetes/community/blob/master/sig-network/README.md) and the Security Response Committee [announced the retirement](https://www.kubernetes.dev/blog/2025/11/12/ingress-nginx-retirement/) of the [Ingress NGINX project](https://github.com/kubernetes/ingress-nginx/), with maintenance that ended in March 2026. Microsoft will provide official support for critical security patches for application routing add-on NGINX Ingress resources through **November 2026**.
>
> AKS aligns with upstream Kubernetes and uses **[Gateway API](https://gateway-api.sigs.k8s.io) as the long-term standard for ingress and L7 traffic management**. Migrate before support ends in November 2026, based on your requirements:
>
> - **Application routing add-on users** and **OSS NGINX users**: Migrate to the [application routing Gateway API implementation](https://learn.microsoft.com/en-us/azure/aks/app-routing-gateway-api) for a Gateway API-based ingress traffic management experience, or to [Application Gateway for Containers](https://learn.microsoft.com/en-us/azure/application-gateway/for-containers/overview), which supports both Ingress API and Gateway API.
> - **Service mesh or advanced ingress requirements**: Consider [Gateway API ingress with the Istio service mesh add-on](https://learn.microsoft.com/en-us/azure/aks/istio-gateway-api). You can use it for ingress without injecting sidecars into your workloads. If you need request header and body size limits, Lua scripts, or rate limiting, review the [Gateway API limitations and alternatives](https://learn.microsoft.com/en-us/azure/aks/app-routing-gateway-api#limitations).

The ingress-nginx controller in the application routing add-on exposes many metrics for requests, the nginx process, and the controller that can be helpful in analyzing the performance and usage of your application.

The application routing add-on exposes the Prometheus metrics endpoint at `/metrics` on port 10254 and a private Service `nginx-metrics`.

## Prerequisites

- An Azure Kubernetes Service (AKS) cluster with the [application routing add-on enabled][app-routing].
- A Prometheus instance, such as Azure Monitor managed service for Prometheus.

## Validating the metrics endpoint

To validate the metrics are being collected, you can set up a port forward from a local port to port 10254 on the `nginx-metrics` service.

```bash
kubectl port-forward -n app-routing-system service/nginx-metrics :10254
```

```bash 
Forwarding from 127.0.0.1:43307 -> 10254
Forwarding from [::1]:43307 -> 10254
```

Note the local port (`43307` in this case) and open http://localhost:43307/metrics in your browser. You should see the ingress-nginx controller metrics loading.

You can now terminate the `port-forward` process to close the forwarding.

## Configuring Azure Monitor managed service for Prometheus

Azure Monitor managed service for Prometheus is a fully managed Prometheus-compatible service that supports industry standard features such as PromQL, Grafana dashboards, and Prometheus alerts. This service requires configuring the metrics add-on for the Azure Monitor agent, which sends data to Prometheus. If your cluster isn't configured with the add-on, you can follow this article to configure your Azure Kubernetes Service (AKS) cluster to send data to Azure Monitor managed service for Prometheus.

### Enable Service Monitor based scraping

Once your cluster is updated with the Azure Monitor agent, you need to configure the agent to enable scraping the metrics endpoint. You can [create a Pod or a Service Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/containers/prometheus-metrics-scrape-crd) to accomplish this.

The following creates a Service Monitor scrape metrics from the ingress-nginx controller deployed by the application routing add-on.

```bash
kubectl apply -f - <<EOF
apiVersion: azmonitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: nginx-monitor
  namespace: app-routing-system
spec:
  labelLimit: 63
  labelNameLengthLimit: 511
  labelValueLengthLimit: 1023
  selector:
    matchLabels:
      app.kubernetes.io/component: ingress-controller
      app.kubernetes.io/managed-by: aks-app-routing-operator
      app.kubernetes.io/name: nginx
  endpoints:
  - port: prometheus
EOF
```

In a few minutes, the `ama-metrics` pods in the `kube-system` namespace should restart and pick up the new configuration.

## Review visualization of metrics in Azure Managed Grafana

Now that you have Azure Monitor managed service for Prometheus and Azure Managed Grafana configured, you should [access your Managed Grafana instance][access-grafana].

There are two [official ingress-nginx dashboards](https://github.com/kubernetes/ingress-nginx/tree/main/deploy/grafana/dashboards) dashboards that you can download and import into your Grafana instance:

- Ingress-nginx controller dashboard
- Request handling performance dashboard

### Ingress-nginx controller dashboard

This dashboard gives you visibility of request volume, connections, success rates, config reloads and configs out of sync. You can also use it to view the network IO pressure, memory and CPU use of the ingress controller. Finally, it also shows the P50, P95, and P99 percentile response times of your ingresses and their throughput.

You can download this dashboard from [GitHub][grafana-nginx-dashboard].

### Request handling performance dashboard

This dashboard gives you visibility into the request handling performance of the different ingress upstream destinations, which are your applications' endpoints that the ingress controller is forwarding traffic to. It shows the P50, P95 and P99 percentile of total request and upstream response times. You can also view aggregates of request errors and latency. Use this dashboard to review and improve the performance and scalability of your applications.

You can download this dashboard from [GitHub][grafana-nginx-request-performance-dashboard].

### Importing a dashboard

To import a Grafana dashboard, expand the left menu and click on **Import** under Dashboards.

Then upload the desired dashboard file and click on **Load**.

## Next steps

- You can configure scaling your workloads using ingress metrics scraped with Prometheus using [Kubernetes Event Driven Autoscaler (KEDA)][KEDA]. Learn more about [integrating KEDA with AKS][keda-prometheus].
- Create and run a load test with [Azure Load Testing][azure-load-testing] to test workload performance and optimize the scalability of your applications.

[az-aks-create]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-create
[app-routing]: https://learn.microsoft.com/en-us/azure/aks/app-routing
[managed-prometheus]: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview
[managed-prometheus-configure]: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-enable?tabs=cli
[managed-prometheus-custom-annotations]: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-scrape-configuration#pod-annotation-based-scraping
[managed-grafana]: https://learn.microsoft.com/en-us/azure/managed-grafana/overview
[create-grafana]: https://learn.microsoft.com/en-us/azure/managed-grafana/quickstart-managed-grafana-portal
[access-grafana]: https://learn.microsoft.com/en-us/azure/managed-grafana/quickstart-managed-grafana-portal#access-your-managed-grafana-instance
[keda]: https://learn.microsoft.com/en-us/azure/aks/keda-about
[keda-prometheus]: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/integrate-keda#scalers
[azure-load-testing]: https://learn.microsoft.com/en-us/azure/load-testing/quickstart-create-and-run-load-test
[az-aks-show]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-show
[az-aks-enable-addons]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-enable-addons
[az-aks-disable-addons]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-disable-addons
[az-aks-install-cli]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-install-cli
[az-aks-get-credentials]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-get-credentials
[az-extension-add]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-add
[az-extension-update]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-update
[install-azure-cli]: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
[az-keyvault-create]: https://learn.microsoft.com/en-us/cli/azure/keyvault#az-keyvault-create
[az-keyvault-certificate-import]: https://learn.microsoft.com/en-us/cli/azure/keyvault/certificate#az-keyvault-certificate-import
[az-keyvault-certificate-show]: https://learn.microsoft.com/en-us/cli/azure/keyvault/certificate#az-keyvault-certificate-show
[az-network-dns-zone-create]: https://learn.microsoft.com/en-us/cli/azure/network/dns/zone#az-network-dns-zone-create
[az-network-dns-zone-show]: https://learn.microsoft.com/en-us/cli/azure/network/dns/zone#az-network-dns-zone-show
[az-role-assignment-create]: https://learn.microsoft.com/en-us/cli/azure/role/assignment#az-role-assignment-create
[az-aks-addon-update]: https://learn.microsoft.com/en-us/cli/azure/aks/addon#az-aks-addon-update
[az-keyvault-set-policy]: https://learn.microsoft.com/en-us/cli/azure/keyvault#az-keyvault-set-policy

[osm-release]: https://github.com/openservicemesh/osm/releases/
[nginx]: https://kubernetes.github.io/ingress-nginx/
[external-dns]: https://github.com/kubernetes-incubator/external-dns
[kubectl]: https://kubernetes.io/docs/reference/kubectl/
[kubectl-apply]: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply
[grafana-nginx-dashboard]: https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/grafana/dashboards/nginx.json
[grafana-nginx-request-performance-dashboard]: https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/grafana/dashboards/request-handling-performance.json
