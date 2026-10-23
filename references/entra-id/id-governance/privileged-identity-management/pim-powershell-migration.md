# PIM PowerShell for Azure resources migration guidance

> Source: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-powershell-migration  
> Microsoft doc last updated: 04/23/2026


## Overview

The following table provides guidance on using the new PowerShell cmdlets in the newer Azure PowerShell module.

## New cmdlets in the Azure PowerShell module

|Old AzureADPreview cmd|New Az cmd equivalent|Description|
|-----|-----|-----|
|Get-AzureADMSPrivilegedResource|[Get-AzResource](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azresource)|Get resources|
|Get-AzureADMSPrivilegedRoleDefinition|[Get-AzRoleDefinition](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azroledefinition)| Get role definitions|
|Get-AzureADMSPrivilegedRoleSetting|[Get-AzRoleManagementPolicy](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azrolemanagementpolicy)|Get the specified role management policy for a resource scope|
|Set-AzureADMSPrivilegedRoleSetting|[Update-AzRoleManagementPolicy](https://learn.microsoft.com/en-us/powershell/module/az.resources/update-azrolemanagementpolicy)| Update a rule defined for a role management policy|
|Open-AzureADMSPrivilegedRoleAssignmentRequest|[New-AzRoleAssignmentScheduleRequest](https://learn.microsoft.com/en-us/powershell/module/az.resources/new-azroleassignmentschedulerequest)|Used for Assignment Requests<br>Create role assignment schedule request|
|Open-AzureADMSPrivilegedRoleAssignmentRequest|[New-AzRoleEligibilityScheduleRequest](https://learn.microsoft.com/en-us/powershell/module/az.resources/new-azroleeligibilityschedulerequest)|Used for Eligibility Requests<br>Create role eligibility schedule request|

## Next steps

- [Microsoft Entra Privileged Identity Management API reference](https://learn.microsoft.com/en-us/graph/api/resources/privilegedidentitymanagementv3-overview)
