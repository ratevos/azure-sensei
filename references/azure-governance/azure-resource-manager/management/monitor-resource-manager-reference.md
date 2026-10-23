# Monitoring data reference for Azure Resource Manager

> Source: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/monitor-resource-manager-reference  
> Microsoft doc last updated: 10/29/2025


See [Monitor Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/monitor-resource-manager) for details on the data you can collect for Azure Resource Manager and how to use it.

### Supported metrics for microsoft.resources/subscriptions

The following table lists the metrics available for the microsoft.resources/subscriptions resource type.

| Dimension name | Description |
|:-------------- |:----------- |
| IsCustomerOriginated | |
| Microsoft.SubscriptionId | |
| Method | The HTTP method used in the request made to Azure Resource Manager. Possible values are: <br/>- GET<br/>- HEAD<br/>- PUT<br/>- POST<br/>- PATCH<br/>- DELETE |
| Namespace | The namespace for the Resource Provider, in all caps, like *MICROSOFT.COMPUTE*. |
| RequestRegion | The Azure Resource Manager region where your control plane requests land, like *EastUS2*. This region isn't the resource's location. |
| ResourceType | Any resource type in Azure that you created or sent a request to, in all caps, like *VIRTUALMACHINES*. |
| StatusCode | Response type from Azure Resource Manager for your control plane request. Possible values are (but not limited to): <br/>- 0<br/>- 200<br/>- 201<br/>- 400<br/>- 404<br/>- 429<br/>- 500<br/>- 502 |
| StatusCodeClass | The class for the status code returned from Azure Resource Manager. Possible values are: <br/>- 2xx<br/>- 4xx<br/>- 5xx |

- [Microsoft.Resources resource provider operations](https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations#management-and-governance)

## Related content

- See [Monitor Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/monitor-resource-manager) for a description of monitoring Resource Manager.
- See [Monitor Azure resources with Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/monitor-azure-resource) for details on monitoring Azure resources.
