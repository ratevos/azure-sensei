# Quickstart: Configure Quick Access to private resources

> Source: https://learn.microsoft.com/en-us/entra/global-secure-access/quickstart-quick-access  
> Microsoft doc last updated: 03/13/2026


## Overview

Microsoft Entra Private Access provides a secure, zero-trust access solution for accessing internal resources without requiring a VPN. Configure Quick Access and enable the Private Access traffic forwarding profile to specify the sites and apps you want routed through Microsoft Entra Private Access. At this time, the Global Secure Access client must be installed on end-user devices to use Microsoft Entra Private Access, so that step is included in this section.
 
This quickstart shows you the steps needed to configure Quick Access to private resources. For more information about Global Secure Access, see [What is Global Secure Access?](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access)

> [!NOTE]
> Use Quick Access as a transition phase in your Zero Trust journey. After Quick Access has enabled you to replace your VPN, [configure per-app access](https://learn.microsoft.com/en-us/entra/global-secure-access/quickstart-per-app-access) to achieve application segmentation and per-app granular controls.

> [!VIDEO https://www.youtube-nocookie.com/embed/MfcZ3zQhF-4]

## Prerequisites

Administrators who interact with **Global Secure Access** features must have the [Global Secure Access Administrator role](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference). Some features might also require other roles.

To follow the [Zero Trust principle of least privilege](https://learn.microsoft.com/en-us/security/zero-trust/), consider using [Privileged Identity Management (PIM)](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/pim-configure) to activate just-in-time privileged role assignments.

The product requires licensing. For details, see the licensing section of [What is Global Secure Access?](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access). If needed, you can [purchase licenses or get trial licenses](https://aka.ms/azureadlicense).

## Configure Quick Access to private resources

Set up Quick Access for broader access to your network using Microsoft Entra Private Access.

1. [Configure a Microsoft Entra private network connector and connector group](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-connectors).
1. [Configure Quick Access to your private resources](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-quick-access).
1. [Enable the Private Access traffic forwarding profile](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-manage-private-access-profile).
1. [Install and configure the Global Secure Access Client on end-user devices](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-install-windows-client).

After you complete these four steps, users with the Global Secure Access client installed on a Windows device can connect to private resources, through a Quick Access app and private network connector. 

## Next step
- [Quickstart: Configure per-app access to private resources](https://learn.microsoft.com/en-us/entra/global-secure-access/quickstart-per-app-access)
