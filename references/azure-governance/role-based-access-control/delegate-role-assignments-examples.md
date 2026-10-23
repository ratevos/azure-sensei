# Examples to delegate Azure role assignment management with conditions - Azure ABAC

> Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/delegate-role-assignments-examples  
> Microsoft doc last updated: 04/15/2024


This article lists examples of how to delegate Azure role assignment management to other users with conditions.

## Prerequisites

For information about the prerequisites to add or edit role assignment conditions, see [Conditions prerequisites](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-prerequisites).

## Example: Constrain roles

This condition allows a delegate to only add or remove role assignments for the [Backup Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-contributor) or [Backup Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-reader) roles.

You must add this condition to any role assignments for the delegate that include the following actions.

- `Microsoft.Authorization/roleAssignments/write`
- `Microsoft.Authorization/roleAssignments/delete`

# [Template](#tab/template)

Here are the settings to add this condition using the Azure portal and a condition template.

> | Condition | Setting |
> | --- | --- |
> | Template | Constrain roles |
> | Roles | [Backup Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-contributor)<br/>[Backup Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-reader) |

# [Condition editor](#tab/condition-editor)

Here are the settings to add this condition using the Azure portal and the condition editor.

To target both the add and remove role assignment actions, notice that you must add two conditions. You must add two conditions because the attribute source is different for each action. If you try to target both actions in the same condition, you won't be able to add an expression. For more information, see [Symptom - No options available error](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-troubleshoot#symptom---no-options-available-error).

> | Condition #1 | Setting |
> | --- | --- |
> | Actions | [Create or update role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#create-or-update-role-assignments) |
> | Attribute source | Request |
> | Attribute | [Role definition ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#role-definition-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Roles | [Backup Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-contributor)<br/>[Backup Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-reader) |

> | Condition #2 | Setting |
> | --- | --- |
> | Actions | [Delete a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#delete-a-role-assignment) |
> | Attribute source | Resource |
> | Attribute | [Role definition ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#role-definition-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Roles | [Backup Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-contributor)<br/>[Backup Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-reader) |

```
(
 (
  !(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})
 )
 OR 
 (
  @Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {5e467623-bb1f-42f4-a55d-6e525e11384b, a795c7a0-d4a2-40c1-ae25-d81f01202912}
 )
)
AND
(
 (
  !(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})
 )
 OR 
 (
  @Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {5e467623-bb1f-42f4-a55d-6e525e11384b, a795c7a0-d4a2-40c1-ae25-d81f01202912}
 )
)
```

# [Azure PowerShell](#tab/azure-powershell)

Here's how to add this condition using Azure PowerShell.

```azurepowershell
$roleDefinitionId = "f58310d9-a9f6-439a-9e8d-f62e7b41a168"
$principalId = "<principalId>"
$scope = "/subscriptions/<subscriptionId>"
$condition = "((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {5e467623-bb1f-42f4-a55d-6e525e11384b, a795c7a0-d4a2-40c1-ae25-d81f01202912})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {5e467623-bb1f-42f4-a55d-6e525e11384b, a795c7a0-d4a2-40c1-ae25-d81f01202912}))"
$conditionVersion = "2.0"
New-AzRoleAssignment -ObjectId $principalId -Scope $scope -RoleDefinitionId $roleDefinitionId -Condition $condition -ConditionVersion $conditionVersion
```

---

## Example: Constrain roles and principal types

This condition allows a delegate to only add or remove role assignments for the [Backup Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-contributor) or [Backup Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-reader) roles. Also, the delegate can only assign these roles to principals of type user or group.

You must add this condition to any role assignments for the delegate that include the following actions.

- `Microsoft.Authorization/roleAssignments/write`
- `Microsoft.Authorization/roleAssignments/delete`

# [Template](#tab/template)

Here are the settings to add this condition using the Azure portal and a condition template.

> | Condition | Setting |
> | --- | --- |
> | Template | Constrain roles and principal types |
> | Roles | [Backup Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-contributor)<br/>[Backup Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-reader) |
> | Principal types | Users<br/>Groups |

# [Condition editor](#tab/condition-editor)

Here are the settings to add this condition using the Azure portal and the condition editor.

To target both the add and remove role assignment actions, notice that you must add two conditions. You must add two conditions because the attribute source is different for each action. If you try to target both actions in the same condition, you won't be able to add an expression. For more information, see [Symptom - No options available error](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-troubleshoot#symptom---no-options-available-error).

> | Condition #1 | Setting |
> | --- | --- |
> | Actions | [Create or update role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#create-or-update-role-assignments) |
> | Attribute source | Request |
> | Attribute | [Role definition ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#role-definition-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Roles | [Backup Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-contributor)<br/>[Backup Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-reader) |
> | Operator | And |
> | **Expression 2** |  |
> | Attribute source | Request |
> | Attribute | [Principal type](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#principal-type) |
> | Operator | [ForAnyOfAnyValues:StringEqualsIgnoreCase](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Value | User<br/>Group |

> | Condition #2 | Setting |
> | --- | --- |
> | Actions | [Delete a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#delete-a-role-assignment) |
> | Attribute source | Resource |
> | Attribute | [Role definition ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#role-definition-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Roles | [Backup Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-contributor)<br/>[Backup Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-reader) |
> | Operator | And |
> | **Expression 2** |  |
> | Attribute source | Resource |
> | Attribute | [Principal type](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#principal-type) |
> | Operator | [ForAnyOfAnyValues:StringEqualsIgnoreCase](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Value | User<br/>Group |

```
(
 (
  !(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})
 )
 OR 
 (
  @Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {5e467623-bb1f-42f4-a55d-6e525e11384b, a795c7a0-d4a2-40c1-ae25-d81f01202912}
  AND
  @Request[Microsoft.Authorization/roleAssignments:PrincipalType] ForAnyOfAnyValues:StringEqualsIgnoreCase {'User', 'Group'}
 )
)
AND
(
 (
  !(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})
 )
 OR 
 (
  @Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {5e467623-bb1f-42f4-a55d-6e525e11384b, a795c7a0-d4a2-40c1-ae25-d81f01202912}
  AND
  @Resource[Microsoft.Authorization/roleAssignments:PrincipalType] ForAnyOfAnyValues:StringEqualsIgnoreCase {'User', 'Group'}
 )
)
```

# [Azure PowerShell](#tab/azure-powershell)

Here's how to add this condition using Azure PowerShell.

```azurepowershell
$roleDefinitionId = "f58310d9-a9f6-439a-9e8d-f62e7b41a168"
$principalId = "<principalId>"
$scope = "/subscriptions/<subscriptionId>"
$condition = "((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {5e467623-bb1f-42f4-a55d-6e525e11384b, a795c7a0-d4a2-40c1-ae25-d81f01202912} AND @Request[Microsoft.Authorization/roleAssignments:PrincipalType] ForAnyOfAnyValues:StringEqualsIgnoreCase {'User', 'Group'})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {5e467623-bb1f-42f4-a55d-6e525e11384b, a795c7a0-d4a2-40c1-ae25-d81f01202912} AND @Resource[Microsoft.Authorization/roleAssignments:PrincipalType] ForAnyOfAnyValues:StringEqualsIgnoreCase {'User', 'Group'}))"
$conditionVersion = "2.0"
New-AzRoleAssignment -ObjectId $principalId -Scope $scope -RoleDefinitionId $roleDefinitionId -Condition $condition -ConditionVersion $conditionVersion
```

---

## Example: Constrain roles and specific groups

This condition allows a delegate to only add or remove role assignments for the [Backup Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-contributor) or [Backup Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-reader) roles. Also, the delegate can only assign these roles to specific groups named Marketing (28c35fea-2099-4cf5-8ad9-473547bc9423) or Sales (86951b8b-723a-407b-a74a-1bca3f0c95d0).

You must add this condition to any role assignments for the delegate that include the following actions.

- `Microsoft.Authorization/roleAssignments/write`
- `Microsoft.Authorization/roleAssignments/delete`

# [Template](#tab/template)

Here are the settings to add this condition using the Azure portal and a condition template.

> | Condition | Setting |
> | --- | --- |
> | Template | Constrain roles and principals |
> | Roles | [Backup Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-contributor)<br/>[Backup Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-reader) |
> | Principals | Marketing<br/>Sales |

# [Condition editor](#tab/condition-editor)

Here are the settings to add this condition using the Azure portal and the condition editor.

To target both the add and remove role assignment actions, notice that you must add two conditions. You must add two conditions because the attribute source is different for each action. If you try to target both actions in the same condition, you won't be able to add an expression. For more information, see [Symptom - No options available error](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-troubleshoot#symptom---no-options-available-error).

> | Condition #1 | Setting |
> | --- | --- |
> | Actions | [Create or update role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#create-or-update-role-assignments) |
> | Attribute source | Request |
> | Attribute | [Role definition ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#role-definition-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Roles | [Backup Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-contributor)<br/>[Backup Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-reader) |
> | Operator | And |
> | **Expression 2** |  |
> | Attribute source | Request |
> | Attribute | [Principal ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#principal-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Principals | Marketing<br/>Sales |

> | Condition #2 | Setting |
> | --- | --- |
> | Actions | [Delete a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#delete-a-role-assignment) |
> | Attribute source | Resource |
> | Attribute | [Role definition ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#role-definition-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Roles | [Backup Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-contributor)<br/>[Backup Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-reader) |
> | Operator | And |
> | **Expression 2** |  |
> | Attribute source | Resource |
> | Attribute | [Principal ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#principal-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Principals | Marketing<br/>Sales |

```
(
 (
  !(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})
 )
 OR 
 (
  @Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {5e467623-bb1f-42f4-a55d-6e525e11384b, a795c7a0-d4a2-40c1-ae25-d81f01202912}
  AND
  @Request[Microsoft.Authorization/roleAssignments:PrincipalId] ForAnyOfAnyValues:GuidEquals {28c35fea-2099-4cf5-8ad9-473547bc9423, 86951b8b-723a-407b-a74a-1bca3f0c95d0}
 )
)
AND
(
 (
  !(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})
 )
 OR 
 (
  @Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {5e467623-bb1f-42f4-a55d-6e525e11384b, a795c7a0-d4a2-40c1-ae25-d81f01202912}
  AND
  @Resource[Microsoft.Authorization/roleAssignments:PrincipalId] ForAnyOfAnyValues:GuidEquals {28c35fea-2099-4cf5-8ad9-473547bc9423, 86951b8b-723a-407b-a74a-1bca3f0c95d0}
 )
)
```

# [Azure PowerShell](#tab/azure-powershell)

Here's how to add this condition using Azure PowerShell.

```azurepowershell
$roleDefinitionId = "f58310d9-a9f6-439a-9e8d-f62e7b41a168"
$principalId = "<principalId>"
$scope = "/subscriptions/<subscriptionId>"
$condition = "((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {5e467623-bb1f-42f4-a55d-6e525e11384b, a795c7a0-d4a2-40c1-ae25-d81f01202912} AND @Request[Microsoft.Authorization/roleAssignments:PrincipalId] ForAnyOfAnyValues:GuidEquals {28c35fea-2099-4cf5-8ad9-473547bc9423, 86951b8b-723a-407b-a74a-1bca3f0c95d0})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {5e467623-bb1f-42f4-a55d-6e525e11384b, a795c7a0-d4a2-40c1-ae25-d81f01202912} AND @Resource[Microsoft.Authorization/roleAssignments:PrincipalId] ForAnyOfAnyValues:GuidEquals {28c35fea-2099-4cf5-8ad9-473547bc9423, 86951b8b-723a-407b-a74a-1bca3f0c95d0}))"
$conditionVersion = "2.0"
New-AzRoleAssignment -ObjectId $principalId -Scope $scope -RoleDefinitionId $roleDefinitionId -Condition $condition -ConditionVersion $conditionVersion
```

---

## Example: Constrain virtual machine management

This condition allows a delegate to only add or remove role assignments for the [Virtual Machine Administrator Login](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#virtual-machine-administrator-login) or [Virtual Machine User Login](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#virtual-machine-user-login) roles. Also, the delegate can only assign these roles to a specific user named Dara (ea585310-c95c-4a68-af22-49af4363bbb1).

This condition is useful when you want to allow a delegate to assign a virtual machine login role to themselves for a virtual machine they've just created.

You must add this condition to any role assignments for the delegate that include the following actions.

- `Microsoft.Authorization/roleAssignments/write`
- `Microsoft.Authorization/roleAssignments/delete`

# [Template](#tab/template)

Here are the settings to add this condition using the Azure portal and a condition template.

> | Condition | Setting |
> | --- | --- |
> | Template | Constrain roles and principals |
> | Roles | [Virtual Machine Administrator Login](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#virtual-machine-administrator-login)<br/>[Virtual Machine User Login](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#virtual-machine-user-login) |
> | Principals | Dara |

# [Condition editor](#tab/condition-editor)

Here are the settings to add this condition using the Azure portal and the condition editor.

To target both the add and remove role assignment actions, notice that you must add two conditions. You must add two conditions because the attribute source is different for each action. If you try to target both actions in the same condition, you won't be able to add an expression. For more information, see [Symptom - No options available error](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-troubleshoot#symptom---no-options-available-error).

> | Condition #1 | Setting |
> | --- | --- |
> | Actions | [Create or update role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#create-or-update-role-assignments) |
> | Attribute source | Request |
> | Attribute | [Role definition ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#role-definition-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Roles | [Virtual Machine Administrator Login](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#virtual-machine-administrator-login)<br/>[Virtual Machine User Login](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#virtual-machine-user-login) |
> | Operator | And |
> | **Expression 2** |  |
> | Attribute source | Request |
> | Attribute | [Principal ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#principal-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Principals | Dara |

> | Condition #2 | Setting |
> | --- | --- |
> | Actions | [Delete a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#delete-a-role-assignment) |
> | Attribute source | Resource |
> | Attribute | [Role definition ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#role-definition-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Roles | [Virtual Machine Administrator Login](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#virtual-machine-administrator-login)<br/>[Virtual Machine User Login](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#virtual-machine-user-login) |
> | Operator | And |
> | **Expression 2** |  |
> | Attribute source | Resource |
> | Attribute | [Principal ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#principal-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Principals | Dara |

```
(
 (
  !(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})
 )
 OR 
 (
  @Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {1c0163c0-47e6-4577-8991-ea5c82e286e4, fb879df8-f326-4884-b1cf-06f3ad86be52}
  AND
  @Request[Microsoft.Authorization/roleAssignments:PrincipalId] ForAnyOfAnyValues:GuidEquals {ea585310-c95c-4a68-af22-49af4363bbb1}
 )
)
AND
(
 (
  !(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})
 )
 OR 
 (
  @Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {1c0163c0-47e6-4577-8991-ea5c82e286e4, fb879df8-f326-4884-b1cf-06f3ad86be52}
  AND
  @Resource[Microsoft.Authorization/roleAssignments:PrincipalId] ForAnyOfAnyValues:GuidEquals {ea585310-c95c-4a68-af22-49af4363bbb1}
 )
)
```

# [Azure PowerShell](#tab/azure-powershell)

Here's how to add this condition using Azure PowerShell.

```azurepowershell
$roleDefinitionId = "f58310d9-a9f6-439a-9e8d-f62e7b41a168"
$principalId = "<principalId>"
$scope = "/subscriptions/<subscriptionId>"
$condition = "((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {1c0163c0-47e6-4577-8991-ea5c82e286e4, fb879df8-f326-4884-b1cf-06f3ad86be52} AND @Request[Microsoft.Authorization/roleAssignments:PrincipalId] ForAnyOfAnyValues:GuidEquals {ea585310-c95c-4a68-af22-49af4363bbb1})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {1c0163c0-47e6-4577-8991-ea5c82e286e4, fb879df8-f326-4884-b1cf-06f3ad86be52} AND @Resource[Microsoft.Authorization/roleAssignments:PrincipalId] ForAnyOfAnyValues:GuidEquals {ea585310-c95c-4a68-af22-49af4363bbb1}))"
$conditionVersion = "2.0"
New-AzRoleAssignment -ObjectId $principalId -Scope $scope -RoleDefinitionId $roleDefinitionId -Condition $condition -ConditionVersion $conditionVersion
```

---

## Example: Constrain AKS cluster management

This condition allows a delegate to only add or remove role assignments for the [Azure Kubernetes Service RBAC Admin](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-kubernetes-service-rbac-admin), [Azure Kubernetes Service RBAC Cluster Admin](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-kubernetes-service-rbac-cluster-admin), [Azure Kubernetes Service RBAC Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-kubernetes-service-rbac-reader), or [Azure Kubernetes Service RBAC Writer](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-kubernetes-service-rbac-writer) roles. Also, the delegate can only assign these roles to a specific user named Dara (ea585310-c95c-4a68-af22-49af4363bbb1).

This condition is useful when you want to allow a delegate to assign Azure Kubernetes Service (AKS) cluster data plane authorization roles to themselves for a cluster they've just created.

You must add this condition to any role assignments for the delegate that include the following actions.

- `Microsoft.Authorization/roleAssignments/write`
- `Microsoft.Authorization/roleAssignments/delete`

# [Template](#tab/template)

Here are the settings to add this condition using the Azure portal and a condition template.

> | Condition | Setting |
> | --- | --- |
> | Template | Constrain roles and principals |
> | Roles | [Azure Kubernetes Service RBAC Admin](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-kubernetes-service-rbac-admin)<br/>[Azure Kubernetes Service RBAC Cluster Admin](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-kubernetes-service-rbac-cluster-admin)<br/>[Azure Kubernetes Service RBAC Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-kubernetes-service-rbac-reader)<br/>[Azure Kubernetes Service RBAC Writer](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-kubernetes-service-rbac-writer) |
> | Principals | Dara |

# [Condition editor](#tab/condition-editor)

Here are the settings to add this condition using the Azure portal and the condition editor.

To target both the add and remove role assignment actions, notice that you must add two conditions. You must add two conditions because the attribute source is different for each action. If you try to target both actions in the same condition, you won't be able to add an expression. For more information, see [Symptom - No options available error](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-troubleshoot#symptom---no-options-available-error).

> | Condition #1 | Setting |
> | --- | --- |
> | Actions | [Create or update role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#create-or-update-role-assignments) |
> | Attribute source | Request |
> | Attribute | [Role definition ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#role-definition-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Roles | [Azure Kubernetes Service RBAC Admin](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-kubernetes-service-rbac-admin)<br/>[Azure Kubernetes Service RBAC Cluster Admin](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-kubernetes-service-rbac-cluster-admin)<br/>[Azure Kubernetes Service RBAC Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-kubernetes-service-rbac-reader)<br/>[Azure Kubernetes Service RBAC Writer](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-kubernetes-service-rbac-writer) |
> | Operator | And |
> | **Expression 2** |  |
> | Attribute source | Request |
> | Attribute | [Principal ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#principal-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Principals | Dara |

> | Condition #2 | Setting |
> | --- | --- |
> | Actions | [Delete a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#delete-a-role-assignment) |
> | Attribute source | Resource |
> | Attribute | [Role definition ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#role-definition-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Roles | [Azure Kubernetes Service RBAC Admin](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-kubernetes-service-rbac-admin)<br/>[Azure Kubernetes Service RBAC Cluster Admin](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-kubernetes-service-rbac-cluster-admin)<br/>[Azure Kubernetes Service RBAC Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-kubernetes-service-rbac-reader)<br/>[Azure Kubernetes Service RBAC Writer](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-kubernetes-service-rbac-writer) |
> | Operator | And |
> | **Expression 2** |  |
> | Attribute source | Resource |
> | Attribute | [Principal ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#principal-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Principals | Dara |

```
(
 (
  !(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})
 )
 OR 
 (
  @Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {3498e952-d568-435e-9b2c-8d77e338d7f7, b1ff04bb-8a4e-4dc4-8eb5-8693973ce19b, 7f6c6a51-bcf8-42ba-9220-52d62157d7db, a7ffa36f-339b-4b5c-8bdf-e2c188b2c0eb}
  AND
  @Request[Microsoft.Authorization/roleAssignments:PrincipalId] ForAnyOfAnyValues:GuidEquals {ea585310-c95c-4a68-af22-49af4363bbb1}
 )
)
AND
(
 (
  !(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})
 )
 OR 
 (
  @Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {3498e952-d568-435e-9b2c-8d77e338d7f7, b1ff04bb-8a4e-4dc4-8eb5-8693973ce19b, 7f6c6a51-bcf8-42ba-9220-52d62157d7db, a7ffa36f-339b-4b5c-8bdf-e2c188b2c0eb}
  AND
  @Resource[Microsoft.Authorization/roleAssignments:PrincipalId] ForAnyOfAnyValues:GuidEquals {ea585310-c95c-4a68-af22-49af4363bbb1}
 )
)
```

# [Azure PowerShell](#tab/azure-powershell)

Here's how to add this condition using Azure PowerShell.

```azurepowershell
$roleDefinitionId = "f58310d9-a9f6-439a-9e8d-f62e7b41a168"
$principalId = "<principalId>"
$scope = "/subscriptions/<subscriptionId>"
$condition = "((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {3498e952-d568-435e-9b2c-8d77e338d7f7, b1ff04bb-8a4e-4dc4-8eb5-8693973ce19b, 7f6c6a51-bcf8-42ba-9220-52d62157d7db, a7ffa36f-339b-4b5c-8bdf-e2c188b2c0eb} AND @Request[Microsoft.Authorization/roleAssignments:PrincipalId] ForAnyOfAnyValues:GuidEquals {ea585310-c95c-4a68-af22-49af4363bbb1})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {3498e952-d568-435e-9b2c-8d77e338d7f7, b1ff04bb-8a4e-4dc4-8eb5-8693973ce19b, 7f6c6a51-bcf8-42ba-9220-52d62157d7db, a7ffa36f-339b-4b5c-8bdf-e2c188b2c0eb} AND @Resource[Microsoft.Authorization/roleAssignments:PrincipalId] ForAnyOfAnyValues:GuidEquals {ea585310-c95c-4a68-af22-49af4363bbb1}))"
$conditionVersion = "2.0"
New-AzRoleAssignment -ObjectId $principalId -Scope $scope -RoleDefinitionId $roleDefinitionId -Condition $condition -ConditionVersion $conditionVersion
```

---

## Example: Constrain ACR management

This condition allows a delegate to only add or remove role assignments for the [AcrPull](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#acrpull) role. Also, the delegate can only assign these roles to principals of type service principal.

This condition is useful when you want to allow a developer to assign the AcrPull role to a managed identity themselves so that it can pull images from the Azure Container Registry (ACR).

You must add this condition to any role assignments for the delegate that include the following actions.

- `Microsoft.Authorization/roleAssignments/write`
- `Microsoft.Authorization/roleAssignments/delete`

# [Template](#tab/template)

Here are the settings to add this condition using the Azure portal and a condition template.

> | Condition | Setting |
> | --- | --- |
> | Template | Constrain roles and principal types |
> | Roles | [AcrPull](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#acrpull) |
> | Principal types | Service principals |

# [Condition editor](#tab/condition-editor)

Here are the settings to add this condition using the Azure portal and the condition editor.

To target both the add and remove role assignment actions, notice that you must add two conditions. You must add two conditions because the attribute source is different for each action. If you try to target both actions in the same condition, you won't be able to add an expression. For more information, see [Symptom - No options available error](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-troubleshoot#symptom---no-options-available-error).

> | Condition #1 | Setting |
> | --- | --- |
> | Actions | [Create or update role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#create-or-update-role-assignments) |
> | Attribute source | Request |
> | Attribute | [Role definition ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#role-definition-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Roles | [AcrPull](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#acrpull) |
> | Operator | And |
> | **Expression 2** |  |
> | Attribute source | Request |
> | Attribute | [Principal type](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#principal-type) |
> | Operator | [ForAnyOfAnyValues:StringEqualsIgnoreCase](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Value | ServicePrincipal |

> | Condition #2 | Setting |
> | --- | --- |
> | Actions | [Delete a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#delete-a-role-assignment) |
> | Attribute source | Resource |
> | Attribute | [Role definition ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#role-definition-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Roles | [Backup Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-contributor)<br/>[Backup Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-reader) |
> | Operator | And |
> | **Expression 2** |  |
> | Attribute source | Resource |
> | Attribute | [Principal type](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#principal-type) |
> | Operator | [ForAnyOfAnyValues:StringEqualsIgnoreCase](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Value | ServicePrincipal |

```
(
 (
  !(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})
 )
 OR 
 (
  @Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {7f951dda-4ed3-4680-a7ca-43fe172d538d}
  AND
  @Request[Microsoft.Authorization/roleAssignments:PrincipalType] ForAnyOfAnyValues:StringEqualsIgnoreCase {'ServicePrincipal'}
 )
)
AND
(
 (
  !(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})
 )
 OR 
 (
  @Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {7f951dda-4ed3-4680-a7ca-43fe172d538d}
  AND
  @Resource[Microsoft.Authorization/roleAssignments:PrincipalType] ForAnyOfAnyValues:StringEqualsIgnoreCase {'ServicePrincipal'}
 )
)
```

# [Azure PowerShell](#tab/azure-powershell)

Here's how to add this condition using Azure PowerShell.

```azurepowershell
$roleDefinitionId = "f58310d9-a9f6-439a-9e8d-f62e7b41a168"
$principalId = "<principalId>"
$scope = "/subscriptions/<subscriptionId>"
$condition = "((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {7f951dda-4ed3-4680-a7ca-43fe172d538d} AND @Request[Microsoft.Authorization/roleAssignments:PrincipalType] ForAnyOfAnyValues:StringEqualsIgnoreCase {'ServicePrincipal'})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {7f951dda-4ed3-4680-a7ca-43fe172d538d} AND @Resource[Microsoft.Authorization/roleAssignments:PrincipalType] ForAnyOfAnyValues:StringEqualsIgnoreCase {'ServicePrincipal'}))"
$conditionVersion = "2.0"
New-AzRoleAssignment -ObjectId $principalId -Scope $scope -RoleDefinitionId $roleDefinitionId -Condition $condition -ConditionVersion $conditionVersion
```

---

## Example: Constrain add role assignments

This condition allows a delegate to only add role assignments for the [Backup Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-contributor) or [Backup Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-reader) roles. The delegate can remove any role assignments.

You must add this condition to any role assignments for the delegate that include the following action.

- `Microsoft.Authorization/roleAssignments/write`

# [Template](#tab/template)

None

# [Condition editor](#tab/condition-editor)

Here are the settings to add this condition using the Azure portal and the condition editor.

> | Condition #1 | Setting |
> | --- | --- |
> | Actions | [Create or update role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#create-or-update-role-assignments) |
> | Attribute source | Request |
> | Attribute | [Role definition ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#role-definition-id) |
> | Operator | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
> | Comparison | Value |
> | Roles | [Backup Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-contributor)<br/>[Backup Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#backup-reader) |

```
(
 (
  !(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})
 )
 OR 
 (
  @Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {5e467623-bb1f-42f4-a55d-6e525e11384b, a795c7a0-d4a2-40c1-ae25-d81f01202912}
 )
)
```

# [Azure PowerShell](#tab/azure-powershell)

Here's how to add this condition using Azure PowerShell.

```azurepowershell
$roleDefinitionId = "f58310d9-a9f6-439a-9e8d-f62e7b41a168"
$principalId = "<principalId>"
$scope = "/subscriptions/<subscriptionId>"
$condition = "((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals {5e467623-bb1f-42f4-a55d-6e525e11384b, a795c7a0-d4a2-40c1-ae25-d81f01202912}))"
$conditionVersion = "2.0"
New-AzRoleAssignment -ObjectId $principalId -Scope $scope -RoleDefinitionId $roleDefinitionId -Condition $condition -ConditionVersion $conditionVersion
```

---

## Example: Allow most roles, but don't allow others to assign roles

This condition allows a delegate to add or remove role assignments for all roles except the [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner), [Role Based Access Control Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator), and [User Access Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator) roles.

This condition is useful when you want to allow a delegate to assign most roles, but not allow the delegate to allow others to assign roles.

> [!NOTE]
> This condition should be used with caution. If a new built-in or custom role is later added that includes the permission to create role assignments, this condition would not prevent the delegate from assigning roles. The condition would have to be updated to include the new built-in or custom role.

You must add this condition to any role assignments for the delegate that include the following actions.

- `Microsoft.Authorization/roleAssignments/write`
- `Microsoft.Authorization/roleAssignments/delete`

# [Template](#tab/template)

Here are the settings to add this condition using the Azure portal and a condition template.

> | Condition | Setting |
> | --- | --- |
> | Template | Allow all except specific roles |
> | Exclude roles | [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner)<br/>[Role Based Access Control Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator)<br/>[User Access Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator) |

# [Condition editor](#tab/condition-editor)

Here are the settings to add this condition using the Azure portal and the condition editor.

To target both the add and remove role assignment actions, notice that you must add two conditions. You must add two conditions because the attribute source is different for each action. If you try to target both actions in the same condition, you won't be able to add an expression. For more information, see [Symptom - No options available error](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-troubleshoot#symptom---no-options-available-error).

> | Condition #1 | Setting |
> | --- | --- |
> | Actions | [Create or update role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#create-or-update-role-assignments) |
> | Attribute source | Request |
> | Attribute | [Role definition ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#role-definition-id) |
> | Operator | [ForAnyOfAllValues:GuidNotEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofallvalues) |
> | Comparison | Value |
> | Roles | [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner)<br/>[Role Based Access Control Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator)<br/>[User Access Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator) |

> | Condition #2 | Setting |
> | --- | --- |
> | Actions | [Delete a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#delete-a-role-assignment) |
> | Attribute source | Resource |
> | Attribute | [Role definition ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#role-definition-id) |
> | Operator | [ForAnyOfAllValues:GuidNotEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofallvalues) |
> | Comparison | Value |
> | Roles | [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner)<br/>[Role Based Access Control Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator)<br/>[User Access Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator) |

```
(
 (
  !(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})
 )
 OR 
 (
  @Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAllValues:GuidNotEquals {8e3af657-a8ff-443c-a75c-2fe8c4bcb635, f58310d9-a9f6-439a-9e8d-f62e7b41a168, 18d7d88d-d35e-4fb5-a5c3-7773c20a72d9}
 )
)
AND
(
 (
  !(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})
 )
 OR 
 (
  @Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAllValues:GuidNotEquals {8e3af657-a8ff-443c-a75c-2fe8c4bcb635, f58310d9-a9f6-439a-9e8d-f62e7b41a168, 18d7d88d-d35e-4fb5-a5c3-7773c20a72d9}
 )
)
```

# [Azure PowerShell](#tab/azure-powershell)

Here's how to add this condition using Azure PowerShell.

```azurepowershell
$roleDefinitionId = "f58310d9-a9f6-439a-9e8d-f62e7b41a168"
$principalId = "<principalId>"
$scope = "/subscriptions/<subscriptionId>"
$condition = "((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAllValues:GuidNotEquals {8e3af657-a8ff-443c-a75c-2fe8c4bcb635, f58310d9-a9f6-439a-9e8d-f62e7b41a168, 18d7d88d-d35e-4fb5-a5c3-7773c20a72d9})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAllValues:GuidNotEquals {8e3af657-a8ff-443c-a75c-2fe8c4bcb635, f58310d9-a9f6-439a-9e8d-f62e7b41a168, 18d7d88d-d35e-4fb5-a5c3-7773c20a72d9}))"
$conditionVersion = "2.0"
New-AzRoleAssignment -ObjectId $principalId -Scope $scope -RoleDefinitionId $roleDefinitionId -Condition $condition -ConditionVersion $conditionVersion
```

---

## Next steps

- [Authorization actions and attributes](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes)
- [Azure role assignment condition format and syntax](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format)
- [Troubleshoot Azure role assignment conditions](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-troubleshoot)
