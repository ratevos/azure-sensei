# How to configure routers for remote networks

> Source: https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-customer-premises-equipment  
> Microsoft doc last updated: 03/25/2026


## Overview

IPSec tunnel is a bidirectional communication. One side of the communication is established when [adding a device link to a remote network](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-manage-remote-network-device-links) in Global Secure Access. During that process, you enter your public IP address and border gateway protocol (BGP) addresses in the Microsoft Entra admin center to tell us about your network configurations.

This article provides the steps to set up the other side of the communication channel.

## Prerequisites

To configure your customer premises equipment (CPE), you must have:

- A **Global Secure Access Administrator** role in Microsoft Entra ID.
- The product requires licensing. For details, see the licensing section of [What is Global Secure Access](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access). If needed, you can [purchase licenses or get trial licenses](https://aka.ms/azureadlicense).
- To configure your CPE, you must have completed the Global Secure Access onboarding process.

## How to configure your customer premises equipment

You can set up the CPE using the Microsoft Entra admin center or using the Microsoft Graph API. When you create a remote network and add your device link information, configuration details are generated. These details are needed to configure your CPE.

## [Microsoft Entra admin center](#tab/microsoft-entra-admin-center)

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as a **Global Secure Access Administrator**.
1. Browse to **Global Secure Access** > **Connect** > **Remote networks**.
1. Select **View configuration** for the remote network you need to configure.

    

1. Locate and save Microsoft's public IP address `endpoint` from the panel that opens.

    

1. In the preferred interface for *your CPE*, enter the IP address you saved in the previous step. This step completes the IPSec tunnel configuration.

The following diagram highlights each of the major sections of the device configuration details. Text descriptions of each section follow the diagram. 

- The `branchId` and `branchName` represent the remote network details.
- The `displayName` is the device link name.
- The `endpoint`, `asn`, `bgpAddress`, and `region` represent the Microsoft connectivity details. Enter these details on your CPE.
- For zone redundant device links, a second set of details are generated.
- `PeerConfiguration` and the subsequent details represent the CPE connectivity details. 
- If you've configured more devices, their details follow.
 
> [!IMPORTANT]
>The crypto profile you specified for the device link should match with what you specify on your CPE. If you chose the "default" IKE policy when configuring the device link, use the configurations described in the **[Remote network configurations](https://learn.microsoft.com/en-us/entra/global-secure-access/reference-remote-network-configurations)** article.

## [Microsoft Graph API](#tab/microsoft-graph-api)

Follow these instructions to download the connectivity information for your remote network. 

1. Sign in to [Graph Explorer](https://aka.ms/ge).
1. Select **GET** as the HTTP method from the dropdown.
1. Set the API version to **beta**.
1. Run the following query to list your remote networks and their device links:

    ``` http
    GET https://graph.microsoft.com/beta/networkaccess/connectivity/branches
    ```
1. Run the following query to get the connectivity information, replacing `{branchSiteId}` with the ID of your remote network and `{deviceLinkId}` with the ID of your device link:

    ``` http
    GET https://graph.microsoft.com/beta/networkAccess/connectivity/branches/{branchSiteId}/deviceLinks/{deviceLinkId}
    ```

The details in the response are similar to the device configuration details found in the Microsoft Entra admin center. 

---

## Next steps

- [How to manage remote networks](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-manage-remote-networks)
- [How to manage remote network device links](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-manage-remote-network-device-links)
