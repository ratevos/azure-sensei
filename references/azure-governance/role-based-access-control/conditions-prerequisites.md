# Prerequisites for Azure role assignment conditions - Azure ABAC

> Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-prerequisites  
> Microsoft doc last updated: 12/01/2023


To add or edit Azure role assignment conditions, you must have the following prerequisites.

## Storage accounts

For conditions that use blob index tags, you must use a storage account that is compatible with the blob index feature. For example, only General Purpose v2 (GPv2) storage accounts with hierarchical namespace (HNS) disabled are currently supported. For more information, see [Manage and find Azure Blob data with blob index tags](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-manage-find-blobs#regional-availability-and-storage-account-support)

## Azure PowerShell

When using Azure PowerShell to add or update conditions, you must use the following versions:

- [Az module 5.5.0 or later](https://www.powershellgallery.com/packages/Az/5.5.0)
- [Az.Resources module 3.2.1 or later](https://www.powershellgallery.com/packages/Az.Resources/3.2.1)
    - Included with Az module v5.5.0 and later, but can be manually installed through PowerShell Gallery
- [Az.Storage preview module 2.5.2-preview or later](https://www.powershellgallery.com/packages/Az.Storage/2.5.2-preview)

## Azure CLI

When using Azure CLI to add or update conditions, you must use the following versions:

- [Azure CLI 2.18 or later](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)

## REST API

When using the REST API to add or update conditions, you must use the following versions:

- `2020-03-01-preview` or later
- `2020-04-01-preview` or later if you want to utilize the `description` property for role assignments
- `2022-04-01` is the first stable version

For more information, see [API versions of Azure RBAC REST APIs](https://learn.microsoft.com/en-us/rest/api/authorization/versions).

## Permissions

Just like role assignments, to add or update conditions, you must be signed in to Azure with a user that has the `Microsoft.Authorization/roleAssignments/write` and `Microsoft.Authorization/roleAssignments/delete` permissions, such as [Role Based Access Control Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator).

## Principal attributes

To use principal attributes ([custom security attributes in Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/custom-security-attributes-overview)), you must have the following:

- [Attribute Assignment Administrator](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#attribute-assignment-administrator) at attribute set or tenant scope
- Custom security attributes defined in Microsoft Entra ID

For more information about custom security attributes, see:

- [Principal does not appear in Attribute source](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-troubleshoot#symptom---principal-does-not-appear-in-attribute-source)
- [Add or deactivate custom security attributes in Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/custom-security-attributes-add)

## Environment attributes

To use the [Private endpoint](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-auth-abac-attributes#private-endpoint) attribute, you must have at least one private endpoint configured in your subscription.

To use the [Subnet](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-auth-abac-attributes#subnet) attribute, you must have at least one virtual network subnet using [service endpoints](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security#grant-access-from-a-virtual-network) configured in your subscription.

## Next steps

- [Example Azure role assignment conditions for Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-auth-abac-examples)
- [Tutorial: Add a role assignment condition to restrict access to blobs using the Azure portal](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-auth-abac-portal)
