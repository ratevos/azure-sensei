# List Azure role assignments using Azure PowerShell - Azure RBAC

> Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-powershell  
> Microsoft doc last updated: 05/06/2026


[Azure role-based access control (Azure RBAC)](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) is the authorization system you use to manage access to Azure resources. To determine what resources users, groups, service principals, or managed identities have access to, you list their role assignments. This article describes how to list role assignments using Azure PowerShell.

> [!NOTE]
> If your organization has outsourced management functions to a service provider who uses [Azure Lighthouse](https://learn.microsoft.com/en-us/azure/lighthouse/overview), role assignments authorized by that service provider won't be shown here. Similarly, users in the service provider tenant won't see role assignments for users in a customer's tenant, regardless of the role they've been assigned.

## Prerequisites

- [PowerShell in Azure Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview) or [Azure PowerShell](https://learn.microsoft.com/en-us/powershell/azure/install-azure-powershell)

## List role assignments for the current subscription

The easiest way to get a list of all the role assignments in the current subscription (including inherited role assignments from root and management groups) is to use [Get-AzRoleAssignment](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azroleassignment) without any parameters.

```azurepowershell
Get-AzRoleAssignment
```

```Example
PS C:\> Get-AzRoleAssignment

RoleAssignmentId   : /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Authorization/roleAssignments/11111111-1111-1111-1111-111111111111
Scope              : /subscriptions/00000000-0000-0000-0000-000000000000
DisplayName        : Alain
SignInName         : alain@example.com
RoleDefinitionName : Storage Blob Data Reader
RoleDefinitionId   : 2a2b9908-6ea1-4ae2-8e65-a410df84e7d1
ObjectId           : 44444444-4444-4444-4444-444444444444
ObjectType         : User
CanDelegate        : False

RoleAssignmentId   : /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/pharma-sales/providers/Microsoft.Authorization/roleAssignments/33333333-3333-3333-3333-333333333333
Scope              : /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/pharma-sales
DisplayName        : Marketing
SignInName         :
RoleDefinitionName : Contributor
RoleDefinitionId   : b24988ac-6180-42a0-ab88-20f7382dd24c
ObjectId           : 22222222-2222-2222-2222-222222222222
ObjectType         : Group
CanDelegate        : False

...
```

## List role assignments for a subscription

To list all role assignments at a subscription scope, use [Get-AzRoleAssignment](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azroleassignment). To get the subscription ID, you can find it on the **Subscriptions** blade in the Azure portal or you can use [Get-AzSubscription](https://learn.microsoft.com/en-us/powershell/module/Az.Accounts/Get-AzSubscription).

```azurepowershell
Get-AzRoleAssignment -Scope /subscriptions/<subscription_id>
```

```Example
PS C:\> Get-AzRoleAssignment -Scope /subscriptions/00000000-0000-0000-0000-000000000000
```

## List role assignments for a user

To list all the roles that are assigned to a specified user, use [Get-AzRoleAssignment](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azroleassignment).

```azurepowershell
Get-AzRoleAssignment -SignInName <email_or_userprincipalname>
```

```Example
PS C:\> Get-AzRoleAssignment -SignInName isabella@example.com | FL DisplayName, RoleDefinitionName, Scope

DisplayName        : Isabella Simonsen
RoleDefinitionName : BizTalk Contributor
Scope              : /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/pharma-sales
```

To list all the roles that are assigned to a specified user and the roles that are assigned to the groups to which the user belongs, use [Get-AzRoleAssignment](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azroleassignment).

```azurepowershell
Get-AzRoleAssignment -SignInName <email_or_userprincipalname> -ExpandPrincipalGroups
```

```Example
Get-AzRoleAssignment -SignInName isabella@example.com -ExpandPrincipalGroups | FL DisplayName, RoleDefinitionName, Scope
```

## List role assignments for a resource group

To list all role assignments at a resource group scope, use [Get-AzRoleAssignment](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azroleassignment).

```azurepowershell
Get-AzRoleAssignment -ResourceGroupName <resource_group_name>
```

```Example
PS C:\> Get-AzRoleAssignment -ResourceGroupName pharma-sales | FL DisplayName, RoleDefinitionName, Scope

DisplayName        : Alain Charon
RoleDefinitionName : Backup Operator
Scope              : /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/pharma-sales

DisplayName        : Isabella Simonsen
RoleDefinitionName : BizTalk Contributor
Scope              : /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/pharma-sales

DisplayName        : Alain Charon
RoleDefinitionName : Virtual Machine Contributor
Scope              : /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/pharma-sales
```

## List role assignments for a management group

To list all role assignments at a management group scope, use [Get-AzRoleAssignment](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azroleassignment). To get the management group ID, you can find it on the **Management groups** blade in the Azure portal or you can use [Get-AzManagementGroup](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azmanagementgroup).

```azurepowershell
Get-AzRoleAssignment -Scope /providers/Microsoft.Management/managementGroups/<group_id>
```

```Example
PS C:\> Get-AzRoleAssignment -Scope /providers/Microsoft.Management/managementGroups/marketing-group
```

## List role assignments for a resource

To list role assignments for a specific resource, use [Get-AzRoleAssignment](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azroleassignment) and the `-Scope` parameter. The scope will be different depending on the resource. To get the scope, you can run `Get-AzRoleAssignment` without any parameters to list all of the role assignments and then find the scope you want to list.

```azurepowershell
Get-AzRoleAssignment -Scope "/subscriptions/<subscription_id>/resourcegroups/<resource_group_name>/providers/<provider_name>/<resource_type>/<resource>
```

This following example shows how to list the role assignments for a storage account. Note that this command also lists role assignments at higher scopes, such as resource groups and subscriptions, that apply to this storage account.

```Example
PS C:\> Get-AzRoleAssignment -Scope "/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/storage-test-rg/providers/Microsoft.Storage/storageAccounts/storagetest0122"
```

If you want to just list role assignments that are assigned directly on a resource, you can use the [Where-Object](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object) command to filter the list.

```Example
PS C:\> Get-AzRoleAssignment | Where-Object {$_.Scope -eq "/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/storage-test-rg/providers/Microsoft.Storage/storageAccounts/storagetest0122"}
```

## List role assignments for classic service administrator and co-administrators

> [!IMPORTANT]
> As of **August 31, 2024**, Azure classic administrator roles (along with Azure classic resources and Azure Service Manager) are retired and no longer supported. Starting in **December 2025**, Azure automatically assigned the Owner role at subscription scope to users in the public cloud who were still assigned the Co-Administrator or Service Administrator role. As of **May 2026**, classic administrator roles are fully retired and you must assign roles in [Azure role-based access control (RBAC)](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles) to manage access.
>
> For more information, see [Azure classic subscription administrators](https://learn.microsoft.com/en-us/azure/role-based-access-control/classic-administrators).

To list role assignments for the classic subscription administrator and co-administrators, use [Get-AzRoleAssignment](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azroleassignment).

```azurepowershell
Get-AzRoleAssignment -IncludeClassicAdministrators
```

## List role assignments for a managed identity

1. Get the object ID of the system-assigned or user-assigned managed identity.

   To get the object ID of a user-assigned managed identity, you can use [Get-AzADServicePrincipal](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azadserviceprincipal).

   ```azurepowershell
   Get-AzADServicePrincipal -DisplayNameBeginsWith "<name> or <vmname>"
   ```

1. To list the role assignments, use [Get-AzRoleAssignment](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azroleassignment).

   ```azurepowershell
   Get-AzRoleAssignment -ObjectId <objectid>
   ```

## Next steps

[Assign Azure roles using Azure PowerShell](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-powershell)
