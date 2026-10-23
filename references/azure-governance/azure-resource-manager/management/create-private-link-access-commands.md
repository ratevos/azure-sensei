# Manage resources through private link

> Source: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/create-private-link-access-commands  
> Microsoft doc last updated: 02/27/2026


This article explains how to use [Azure Private Link](../../private-link/index.yml) to restrict access for managing resources in your subscriptions.

Private links enable you to access Azure services over a private endpoint in your virtual network. When you combine private links with Azure Resource Manager's operations, you allow users to use a specific endpoint from managing resources.

Private link provides the following security benefits:

* **Private Access** - users can manage resources from a private network via a private endpoint.

> [!NOTE]
> Azure Kubernetes Service (AKS) currently doesn't support the ARM private endpoint implementation.
>
> Azure Bastion doesn't support private links. It is recommended to use a private DNS zone for your resource management private link private endpoint configuration, but due to the overlap with the management.azure.com name, your Bastion instance will stop working. For more information, view [Azure Bastion FAQ](https://learn.microsoft.com/en-us/azure/bastion/bastion-faq#dns).

## Understand architecture

> [!IMPORTANT]
> For this release, you can only apply private link management access at the level of the root [management group](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview). This limitation means private link access is applied across your tenant.

There are two resource types you'll use when implementing management through a private link.

* Resource management private link (Microsoft.Authorization/resourceManagementPrivateLinks)
* Private link association (Microsoft.Authorization/privateLinkAssociations)

The following image shows how to construct a solution that restricts access for managing resources.

The private link association extends the root management group. The private link association and the private endpoints reference the resource management private link.

> [!IMPORTANT]
> Multi-tenant accounts aren't currently supported for managing resources through a private link. You can't connect private link associations on different tenants to a single resource management private link.
>
> If your account accesses more than one tenant, define a private link for only one of them.

## Workflow

To set up a private link for resources, use the following steps. The steps are described in greater detail later in this article.

1. Create the resource management private link.
1. Create a private link association. The private link association extends the root management group. It also references the resource ID for the resource management private link.
1. Add a private endpoint that references the resource management private link.

After completing those steps, you can manage Azure resources that are within the hierarchy of the scope. You use a private endpoint that is connected to the subnet.

You can monitor access to the private link. For more information, see [Logging and monitoring](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview#logging-and-monitoring).

## Required permissions

> [!IMPORTANT]
> For this release, you can only apply private link management access at the level of the root [management group](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview). This limitation means private link access is applied across your tenant.

To set up the private link for resource management, you need the following access:

* Owner on the subscription. This access is needed to create resource management private link resource.
* Owner or Contributor at the root management group. This access is needed to create the private link association resource.
* The Global Administrator for the Microsoft Entra ID doesn't automatically have permission to assign roles at the root management group. To enable creating resource management private links, the Global Administrator must have permission to read root management group and [elevate access](https://learn.microsoft.com/en-us/azure/role-based-access-control/elevate-access-global-admin) to have User Access Administrator permission on all subscriptions and management groups in the tenant. After you get the User Access Administrator permission, the Global Administrator must grant Owner or Contributor permission at the root management group to the user creating the private link association.

## Create resource management private link

To create resource management private link, send the following request:

# [Azure CLI](#tab/azure-cli)

  ### Example

  ```azurecli
  # Login first with az login if not using Cloud Shell
  az resourcemanagement private-link create --location WestUS --resource-group PrivateLinkTestRG --name NewRMPL
  ```

# [PowerShell](#tab/azure-powershell)

  ### Example

  ```azurepowershell-interactive
  # Login first with Connect-AzAccount if not using Cloud Shell
  New-AzResourceManagementPrivateLink -ResourceGroupName PrivateLinkTestRG -Name NewRMPL
  ```

# [REST](#tab/REST)

  REST call

  ```http
  PUT
  https://management.azure.com/subscriptions/{subscriptionID}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/resourceManagementPrivateLinks/{rmplName}?api-version=2020-05-01
  ```

  In the request body, include the location you want for the resource:

  ```json
  {
    "location":"{region}"
  }
  ```

  The operation returns:

  ```json
  {  
    "id": "/subscriptions/{subID}/resourceGroups/{rgName}/providers/Microsoft.Authorization/resourceManagementPrivateLinks/{name}",
    "location": "{region}",
    "name": "{rmplName}",
    "properties": {
      "privateEndpointConnections": []
    },
    "resourceGroup": "{rgName}",
    "type": "Microsoft.Authorization/resourceManagementPrivateLinks"
  }
  ```
  
---

Note the ID that is returned for the new resource management private link. You use it for creating the private link association.

## Create private link association

The resource name of a private link association resource must be a GUID, and you can't disable the `publicNetworkAccess` field.

To create the private link association, use:

# [Azure CLI](#tab/azure-cli)

  ### Example

  ```azurecli
  # Login first with az login if not using Cloud Shell
  az private-link association create --management-group-id fc096d27-0434-4460-a3ea-110df0422a2d --name 1d7942d1-288b-48de-8d0f-2d2aa8e03ad4 --privatelink "/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/PrivateLinkTestRG/providers/Microsoft.Authorization/resourceManagementPrivateLinks/newRMPL"
  ```

# [PowerShell](#tab/azure-powershell)

  ### Example

  ```azurepowershell-interactive
  # Login first with Connect-AzAccount if not using Cloud Shell
  New-AzPrivateLinkAssociation -ManagementGroupId fc096d27-0434-4460-a3ea-110df0422a2d -Name 1d7942d1-288b-48de-8d0f-2d2aa8e03ad4 -PrivateLink "/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/PrivateLinkTestRG/providers/Microsoft.Authorization/resourceManagementPrivateLinks/newRMPL" -PublicNetworkAccess enabled | fl
  ```

# [REST](#tab/REST)

  REST call

  ```http
  PUT
  https://management.azure.com/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Authorization/privateLinkAssociations/{GUID}?api-version=2020-05-01 
  ```

  In the request body, include:

  ```json
  {
    "properties": {
      "privateLink": "/subscriptions/{subscription-id}/resourceGroups/{rg-name}/providers/Microsoft.Authorization/resourceManagementPrivateLinks/{rmplName}",
      "publicNetworkAccess": "enabled"
    }
  }
  ```

  The operation returns:

  ```json
  {
    "id": {plaResourceId},
    "name": {plaName},
    "properties": {
      "privateLink": {rmplResourceId},
      "publicNetworkAccess": "Enabled",
      "tenantId": "{tenantId}",
      "scope": "/providers/Microsoft.Management/managementGroups/{managementGroupId}"
    },
    "type": "Microsoft.Authorization/privateLinkAssociations"
  }
  ```

---

## Add private endpoint

This article assumes you already have a virtual network. In the subnet that you plan to use for the private endpoint, you must turn off private endpoint network policies. To turn off private endpoint network policies, see [Disable network policies for private endpoints](https://learn.microsoft.com/en-us/azure/private-link/disable-private-endpoint-network-policy).

To create a private endpoint, see Private Endpoint documentation for creating via [Portal](https://learn.microsoft.com/en-us/azure/private-link/create-private-endpoint-portal), [PowerShell](https://learn.microsoft.com/en-us/azure/private-link/create-private-endpoint-powershell), [CLI](https://learn.microsoft.com/en-us/azure/private-link/create-private-endpoint-cli), [Bicep](https://learn.microsoft.com/en-us/azure/private-link/create-private-endpoint-bicep), or [template](https://learn.microsoft.com/en-us/azure/private-link/create-private-endpoint-template).

In the request body, set the `privateServiceLinkId` to the ID from your resource management private link. The `groupIds` must contain `ResourceManagement`. The location of the private endpoint must be the same as the location of the subnet.

```json
{
  "location": "westus2",
  "properties": {
    "privateLinkServiceConnections": [
      {
        "name": "{connection-name}",
        "properties": {
           "privateLinkServiceId": "/subscriptions/{subID}/resourceGroups/{rgName}/providers/Microsoft.Authorization/resourceManagementPrivateLinks/{name}",
           "groupIds": [
              "ResourceManagement"
           ]
         }
      }
    ],
    "subnet": {
      "id": "/subscriptions/{subID}/resourceGroups/{rgName}/providers/Microsoft.Network/virtualNetworks/{vnet-name}/subnets/{subnet-name}"
    }
  }
}
```

The next step varies depending whether you're using automatic or manual approval. For more information about approval, see [Access to a private link resource using approval workflow](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview#access-to-a-private-link-resource-using-approval-workflow).

The response includes approval state.

```json
"privateLinkServiceConnectionState": {
    "actionsRequired": "None",
    "description": "",
    "status": "Approved"
},
```

If your request is automatically approved, you can continue to the next section. If your request requires manual approval, wait for the network admin to approve your private endpoint connection.

## Next steps

To learn more about private links, see [Azure Private Link](../../private-link/index.yml).
