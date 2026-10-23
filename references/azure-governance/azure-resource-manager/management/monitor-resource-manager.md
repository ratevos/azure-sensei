# Monitor Azure Resource Manager

> Source: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/monitor-resource-manager  
> Microsoft doc last updated: 02/27/2026


For more information, see [Monitor Azure Monitor Resource Group insights](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-group-insights).

For more information about the resource types for Resource Manager, see [Azure Resource Manager monitoring data reference](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/monitor-resource-manager-reference).

For a list of available metrics for Resource Manager, see [Azure Resource Manager monitoring data reference](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/monitor-resource-manager-reference#metrics).

When you create and manage resources in Azure, Azure Resource Manager orchestrates your requests through Azure's [control plane](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/control-plane-and-data-plane). This article describes how to monitor the volume and latency of control plane requests made to Azure.

With these metrics, you can observe traffic and latency for control plane requests throughout your subscriptions. For example, you can figure out when your requests are throttled by [examining throttled requests](#examining-throttled-requests). Determine if they failed by filtering for specific status codes and [examining server errors](#examining-server-errors).

The metrics are available for up to three months (93 days) and only track synchronous requests. For a scenario like a virtual machine creation, the metrics don't represent the performance or reliability of the long-running asynchronous operation.

### Accessing Azure Resource Manager metrics

Azure Resource Manager offers enhanced integration with Azure Monitor Metrics for your subscriptions. You can have deeper visibility and more granular monitoring capabilities for your Resource Manager operations.

You can access control plane metrics by using the Azure Monitor REST APIs, SDKs, and the Azure portal by selecting the **Azure Resource Manager** metric. For an overview on Azure Monitor, see [Azure Monitor Metrics](https://learn.microsoft.com/en-us/azure/azure-monitor/data-platform).

There's no opt-in or sign-up process to access control plane metrics.

Dimensions Available:
You can analyze and filter your metrics using the following new dimensions:

- Operation type: By high customer demand, you can now distinguish between different operation categories (read, write, delete)!
- ARM request region: Identify where requests originate and monitor regional trends.
- HTTP method: Break down metrics by request type (GET, POST, etc.).
- HTTP status code: Track specific response codes for better troubleshooting.
- HTTP status code class: Group responses by class (2xx, 4xx, 5xx) for high-level insights.
- Resource type: Filter metrics by the type of Azure resource.
- RP namespace: Analyze metrics by resource provider namespace.
These dimensions empower you to create more targeted alerts, dashboards, and reports, helping you optimize performance and quickly identify issues across your Azure environment.

For guidance on how to retrieve a bearer token and make requests to Azure, see [Azure REST API reference](https://learn.microsoft.com/en-us/rest/api/azure/#create-the-request).

### Metric definition

The definition for Azure Resource Manager metrics in Azure Monitor is only accessible through the 2017-12-01-preview API version. To retrieve the definition, run the following snippet. Replace `00000000-0000-0000-0000-000000000000` with your subscription ID.

```bash
curl --location --request GET 'https://management.azure.com/subscriptions/ffff5f5f-aa6a-bb7b-cc8c-dddddd9d9d9d/providers/microsoft.insights/metricDefinitions?api-version=2017-12-01-preview&metricnamespace=microsoft.resources/subscriptions' \
--header 'Authorization: bearer {{bearerToken}}'
```

This snippet returns the definition for the metrics schema. Notably, this schema includes [the dimensions you can filter on with the Monitor API](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/monitor-resource-manager-reference#metric-dimensions).

### Metrics examples

Here are some scenarios that can help you explore Azure Resource Manager metrics.

#### Query traffic and latency control plane metrics with Azure portal

First, navigate to the Azure Monitor page within the [portal](https://portal.azure.com):

After selecting **Explore Metrics**, select a single subscription and then select the **Azure Resource Manager** metric:

Then, after selecting **Apply**, you can visualize your Traffic or Latency control plane metrics with custom filtering and splitting:

Select **Latency** as your Metric:

View **Traffic**:

Here are additional dimensions you can view to further analyze your call behavior - select **Add filter** to deep dive into one value like "reads," or select **Apply splitting** to view a breakdown of your operations.

With our newest dimension **Operation Type**, you can filter or split your requests by reads, writes, or deletes to analyze your request behavior for a specific operation.

#### Query traffic and latency control plane metrics with REST API

After you authenticate with Azure, make a request to retrieve control plane metrics for your subscription. In the script, replace `00000000-0000-0000-0000-000000000000` with your subscription ID. The script retrieves the average request latency, in seconds, and the total request count for the two-day timespan, broken down by one-day intervals:

```bash
curl --location --request GET "https://management.azure.com/subscriptions/ffff5f5f-aa6a-bb7b-cc8c-dddddd9d9d9d/providers/microsoft.insights/metrics?api-version=2021-05-01&interval=P1D&metricnames=Latency&metricnamespace=microsoft.resources/subscriptions&region=global&aggregation=average,count&timespan=2021-11-01T00:00:00Z/2021-11-03T00:00:00Z" \
--header "Authorization: bearer {{bearerToken}}"
```

For Azure Resource Manager metrics, you can retrieve the traffic count by using the Latency metric and including the `count` aggregation. You see a JSON response for the request:

```Json
{
    "cost": 5758,
    "timespan": "2021-11-01T00:00:00Z/2021-11-03T00:00:00Z",
    "interval": "P1D",
    "value": [
        {
            "id": "subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/providers/Microsoft.Insights/metrics/Latency",
            "type": "Microsoft.Insights/metrics",
            "name": {
                "value": "Latency",
                "localizedValue": "Latency"
            },
            "displayDescription": "Latency data for all requests to Azure Resource Manager",
            "unit": "Seconds",
            "timeseries": [
                {
                    "metadatavalues": [],
                    "data": [
                        {
                            "timeStamp": "2021-11-01T00:00:00Z",
                            "count": 1406.0,
                            "average": 0.19345163584637273
                        },
                        {
                            "timeStamp": "2021-11-02T00:00:00Z",
                            "count": 1517.0,
                            "average": 0.28294792353328935
                        }
                    ]
                }
            ],
            "errorCode": "Success"
        }
    ],
    "namespace": "microsoft.resources/subscriptions",
    "resourceregion": "global"
}
```

To retrieve only the traffic count, use the Traffic metric with the `count` aggregation:

```bash
curl --location --request GET 'https://management.azure.com/subscriptions/ffff5f5f-aa6a-bb7b-cc8c-dddddd9d9d9d/providers/microsoft.insights/metrics?api-version=2021-05-01&interval=P1D&metricnames=Traffic&metricnamespace=microsoft.resources/subscriptions&region=global&aggregation=count&timespan=2021-11-01T00:00:00Z/2021-11-03T00:00:00Z' \
--header 'Authorization: bearer {{bearerToken}}'
```

The response for the request is:

```Json
{
    "cost": 2879,
    "timespan": "2021-11-01T00:00:00Z/2021-11-03T00:00:00Z",
    "interval": "P1D",
    "value": [
        {
            "id": "subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/providers/Microsoft.Insights/metrics/Traffic",
            "type": "Microsoft.Insights/metrics",
            "name": {
                "value": "Traffic",
                "localizedValue": "Traffic"
            },
            "displayDescription": "Traffic data for all requests to Azure Resource Manager",
            "unit": "Count",
            "timeseries": [
                {
                    "metadatavalues": [],
                    "data": [
                        {
                            "timeStamp": "2021-11-01T00:00:00Z",
                            "count": 1406.0
                        },
                        {
                            "timeStamp": "2021-11-02T00:00:00Z",
                            "count": 1517.0
                        }
                    ]
                }
            ],
            "errorCode": "Success"
        }
    ],
    "namespace": "microsoft.resources/subscriptions",
    "resourceregion": "global"
}
```

For the metrics supporting dimensions, you need to specify the dimension value to see the corresponding metrics values. For example, if you want to focus on the **Latency** for successful requests to Resource Manager, filter the **StatusCodeClass** dimension with **2XX**.

If you want to look at the number of requests made in your subscription for Networking resources, like Virtual Networks and Load Balancers, filter the **Namespace** dimension for **MICROSOFT.NETWORK**.

#### Examining Throttled Requests

You can set your **HTTP Status Code**. To view only your throttled requests, filter for 429 status code responses. For REST API calls, use the [$filter property](https://learn.microsoft.com/en-us/rest/api/monitor/Metrics/List#uri-parameters) and the StatusCode dimension by appending: `%24filter=StatusCode eq '429'`. The following snippet shows this filter at the end of the request:

```bash
curl --location --request GET 'https://management.azure.com/subscriptions/ffff5f5f-aa6a-bb7b-cc8c-dddddd9d9d9d/providers/microsoft.insights/metrics?api-version=2021-05-01&interval=P1D&metricnames=Latency&metricnamespace=microsoft.resources/subscriptions&region=global&aggregation=count,average&timespan=2021-11-01T00:00:00Z/2021-11-03T00:00:00Z&%24filter=StatusCode%20eq%20%27429%27' \
--header 'Authorization: bearer {{bearerToken}}'
```

You can also filter directly in portal:

#### Examining Server Errors

Similar to looking at throttled requests, you view *all* requests that returned a server error response code by filtering 5xx responses. To filter REST API calls, use the [$filter property](https://learn.microsoft.com/en-us/rest/api/monitor/Metrics/List#uri-parameters) and the StatusCodeClass dimension by appending: `%24filter=StatusCodeClass eq '5xx'` at the end of the request in the following snippet:

```bash
curl --location --request GET 'https://management.azure.com/subscriptions/ffff5f5f-aa6a-bb7b-cc8c-dddddd9d9d9d/providers/microsoft.insights/metrics?api-version=2021-05-01&interval=P1D&metricnames=Latency&metricnamespace=microsoft.resources/subscriptions&region=global&aggregation=count,average&timespan=2021-11-01T00:00:00Z/2021-11-03T00:00:00Z&%24filter=StatusCodeClass%20eq%20%275xx%27' \
--header 'Authorization: bearer {{bearerToken}}'
```

You can also filter generic server errors in the portal by setting the filter property to `StatusCodeClass` and the value to `5xx`, similar to what you did in the throttling example.

### Resource Manager alert rules

You can set alerts for any metric, log entry, or activity log entry listed in the [Azure Resource Manager monitoring data reference](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/monitor-resource-manager-reference).

## Related content

- See [Azure Resource Manager monitoring data reference](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/monitor-resource-manager-reference) for a reference of the metrics, logs, and other important values created for Resource Manager.
- See [Monitoring Azure resources with Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/monitor-azure-resource) for general details on monitoring Azure resources.
