# Troubleshoot resource access denied in Privileged Identity Management

> Source: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-troubleshoot  
> Microsoft doc last updated: 04/23/2026


## Overview

If you're experiencing issues with Privileged Identity Management (PIM) in Microsoft Entra ID, the information included in this article can help you resolve these issues.

## Access to Azure resources denied

### Problem

As an active owner or user access administrator for an Azure resource, you're able to see your resource inside Privileged Identity Management but can't perform any actions such as making an eligible assignment or viewing a list of role assignments from the resource overview page. Any of these actions results in an authorization error.

### Cause

This issue can occur when the User Access Administrator role for the PIM service principal was accidentally removed from the subscription. For the Privileged Identity Management service to access Azure resources, the MS-PIM service principal should always have the [User Access Administrator role](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator) assigned.

### Resolution

Assign the User Access Administrator role to the Privileged Identity Management service principal name (MS–PIM) at the subscription level. This assignment allows the Privileged Identity Management service to access the Azure resources. Assign the role at a management group level or at the subscription level, depending on your requirements. For more information about service principals, see [Assign an application to a role](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal#assign-a-role-to-the-application).

## Next steps

- [License requirements to use Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals)
- [Securing privileged access for hybrid and cloud deployments in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-planning.md?toc=/azure/active-directory/privileged-identity-management/toc.json)
- [Deploy Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-deployment-plan)
