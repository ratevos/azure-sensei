# Quickstart: Create a remote network, apply Conditional Access, and review the logs

> Source: https://learn.microsoft.com/en-us/entra/global-secure-access/quickstart-remote-network  
> Microsoft doc last updated: 03/13/2026


## Overview

Microsoft Entra Internet Access isolates the traffic for Microsoft applications and resources, such as Exchange Online and SharePoint Online. Users can access these resources by connecting to the Global Secure Access client or through a remote network, such as in a branch office location.
 
This quickstart shows you the steps needed to create a remote network and start acquiring Microsoft traffic. For more information about Global Secure Access, see [What is Global Secure Access?](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access)

## Prerequisites

Administrators who interact with **Global Secure Access** features must have the [Global Secure Access Administrator role](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference). Some features might also require other roles.

To follow the [Zero Trust principle of least privilege](https://learn.microsoft.com/en-us/security/zero-trust/), consider using [Privileged Identity Management (PIM)](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/pim-configure) to activate just-in-time privileged role assignments.

The product requires licensing. For details, see the licensing section of [What is Global Secure Access?](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access). If needed, you can [purchase licenses or get trial licenses](https://aka.ms/azureadlicense).

## Create a remote network, apply Conditional Access, and review the logs

1. [Create a remote network](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-manage-remote-networks).
1. [Target the Microsoft traffic profile with Conditional Access policy](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-target-resource-microsoft-profile).
1. [Review the Global Secure Access logs](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-global-secure-access-logs-monitoring).

After you complete these optional steps, users can connect to Microsoft services without the Global Secure Access client if they're connecting through the remote network you created *and* if they meet the conditions you added to the Conditional Access policy.

## Next step
- [Quickstart: Configure Quick Access to your primary private resources](https://learn.microsoft.com/en-us/entra/global-secure-access/quickstart-quick-access)
