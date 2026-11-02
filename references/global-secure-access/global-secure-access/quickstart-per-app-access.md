# Quickstart: Configure per-app access to private resources

> Source: https://learn.microsoft.com/en-us/entra/global-secure-access/quickstart-per-app-access  
> Microsoft doc last updated: 03/13/2026


## Overview

This quickstart shows you the steps needed to configure per-app access to private resources. For more information about Global Secure Access, see [What is Global Secure Access?](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access)

## Prerequisites

Administrators who interact with **Global Secure Access** features must have the [Global Secure Access Administrator role](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference). Some features might also require other roles.

To follow the [Zero Trust principle of least privilege](https://learn.microsoft.com/en-us/security/zero-trust/), consider using [Privileged Identity Management (PIM)](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/pim-configure) to activate just-in-time privileged role assignments.

The product requires licensing. For details, see the licensing section of [What is Global Secure Access?](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access). If needed, you can [purchase licenses or get trial licenses](https://aka.ms/azureadlicense).
## Configure per-app access to private resources

Create specific private apps for granular segmented access to private access resources using Microsoft Entra Private Access.

1. [Configure a private network connector and connector group](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-connectors).
1. [Create a private Global Secure Access application](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-per-app-access).
1. [Enable the Private Access traffic forwarding profile](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-manage-private-access-profile).
1. [Install and configure the Global Secure Access Client on end-user devices](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-install-windows-client).

After you complete these steps, users with the Global Secure Access client installed on a Windows device can connect to your private resources through a Global Secure Access app and private network connector.

Optionally:

- [Secure Quick Access applications with Conditional Access policies](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-target-resource-private-access-apps).
- [Review the Global Secure Access logs](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-global-secure-access-logs-monitoring).

## Next step
- [Understand Microsoft Entra Internet Access](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-internet-access)
- [Understand Microsoft Entra Private Access](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-private-access)
