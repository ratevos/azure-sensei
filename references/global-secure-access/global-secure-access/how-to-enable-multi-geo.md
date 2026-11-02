# Multi-Geo for Microsoft Entra Private Access

> Source: https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-enable-multi-geo  
> Microsoft doc last updated: 08/18/2025

Multi-Geo capability can help optimize the traffic flow from Microsoft Entra clients to Microsoft Entra apps through private access. This article explains how to enable the multi-Geo capability for Microsoft Entra Private Access.

## Prerequisites

- You must have a Microsoft Entra Private Access license.
- You must have a Microsoft Entra Private Access connector group. For more information, see [How to configure private network connectors for Microsoft Entra Private Access and Microsoft Entra application proxy](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-connectors).
- You must have the **Global Secure Access Administrator** role or the **Privileged Role Administrator** role. For more information, see [Microsoft Entra Built-in Roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference).

## Overview

Multi-Geo capability helps optimize traffic flow from Microsoft Entra clients to Microsoft Entra apps through private access. Currently, the tenant's default geo location determines the Microsoft Entra routing for private access. For instance, if a tenant's default region is North America, all connector groups must connect to the Microsoft Entra backend in North America, even if some applications and connector groups are in different regions. Multi-Geo support lets customers optimize traffic flow by assigning connector groups according to their preferred geo locations instead of relying solely on the tenant's geo location. Each connector group connects to the SSE backend in the selected area, enhancing overall efficiency. This arrangement provides customers with the flexibility to direct connections to the SSE backend of their choice.

## Enable multi-Geo capability
To enable the multi-Geo capability for Microsoft Entra Private Access, complete the following steps. This procedure involves creating connector group in different geographic region, installing connectors, and adding application segments to the connector group.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as a [Global Secure Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-secure-access-administrator).
1. Browse to **Applications** > **Enterprise applications** > **Private Network connectors**.
1. Create a connector group, associate it with a geographic region of your choice.
    1. Select **+ New Connector Group**.
    1. In the **New Connector Group** pane, enter a name for the connector group.
    1. Under Advanced settings, select the optimized **country/region** for the connector group. The region you select determines the backend that the connector group connects to.
1. Install a connector. The connector installation require working with an admin in the associated region. For more information, see [How to configure private network connectors for Microsoft Entra Private Access and Microsoft Entra application proxy](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-connectors).
1. Add an application segment to the connector group.
    1. Browse to **Global Secure Access** > **Applications** > **Enterprise applications** > **Network access properties**.
    1. Select **+ Add application segment**.
    1. Select the application segment you want to add to the connector group.
    1. Select **Save**.
1. After about 30 minutes, the multi-Geo configuration takes effect and traffic begins flowing.

> [!NOTE]
> - Multi-Geo connectors aren't available through Quick Access. Multi-Geo supports only private enterprise apps.
> - Multi-Geo doesn't support the Domain Name System (DNS) experience.
> - Multi-Geo doesn't support Japan region selection through Microsoft Entra admin center.

## Related content

* [How to configure private network connectors for Microsoft Entra Private Access and Microsoft Entra application proxy](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-connectors)
