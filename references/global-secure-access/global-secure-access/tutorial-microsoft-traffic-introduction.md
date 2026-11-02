# Tutorial: Get started with Microsoft traffic labs

> Source: https://learn.microsoft.com/en-us/entra/global-secure-access/tutorial-microsoft-traffic-introduction  
> Microsoft doc last updated: 06/22/2026


This learning lab series provides hands-on experience with the Microsoft traffic profile in Global Secure Access. The Microsoft traffic profile is part of Microsoft Entra Internet Access for Microsoft services. It routes supported Microsoft service traffic through Global Secure Access so you can apply identity-aware controls to Microsoft traffic.

In this tutorial, you learn how to:

> - Recognize what the Microsoft traffic profile is and how it works.
> - Review the key use cases the Microsoft traffic profile supports.
> - Navigate the learning progression for the lab series.

## What is the Microsoft traffic profile?

The Microsoft traffic profile routes supported Microsoft service traffic through Microsoft's security service edge (SSE). The profile uses preconfigured fully qualified domain names (FQDNs) and IP ranges that are required for supported Microsoft services.

The Microsoft traffic profile is optimized for Microsoft traffic. Traffic available for acquisition in the Microsoft traffic profile can only be acquired in the Microsoft traffic profile. Even if the Internet Access profile is the one profile enabled, Microsoft traffic isn't acquired by the Internet Access profile.

For more information, see [Microsoft traffic profile overview](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-microsoft-traffic-profile).

## Key use cases

Use the Microsoft traffic profile when you want to improve access controls and observability for supported Microsoft service traffic.

| Use case | Recommended configuration |
| --- | --- |
| Preserve the original user source IP in Microsoft Entra sign-in logs. | Configure [source IP restoration](https://learn.microsoft.com/en-us/entra/global-secure-access/tutorial-microsoft-traffic-source-ip-restoration). |
| Require users to connect through your tenant's Global Secure Access service before accessing apps integrated with Microsoft Entra ID. | Configure the [compliant network check](https://learn.microsoft.com/en-us/entra/global-secure-access/tutorial-microsoft-traffic-compliant-network). |
| Restrict sign-ins to authorized external tenants from managed devices and networks. | Configure [universal tenant restrictions](https://learn.microsoft.com/en-us/entra/global-secure-access/tutorial-microsoft-traffic-tenant-restrictions). |

## How to run the lab exercises

This series covers the fundamentals of the Microsoft traffic profile. Follow the exercises in order. Some exercises depend on earlier configuration. For example, the compliant network check depends on Global Secure Access signaling for Conditional Access.

## Prerequisites

To complete this tutorial series, you need:

- A Microsoft Entra ID tenant with Microsoft Entra ID P1 or Microsoft Entra ID P2 licenses. Microsoft Entra Internet Access for Microsoft services capabilities are included in Microsoft Entra ID P1 and Microsoft Entra ID P2.
- Either the Global Administrator role or both of the following roles:
    - Global Secure Access Administrator.
    - Security Administrator.
- The Application Administrator role for exercises that assign users or groups to a traffic forwarding profile.
- The Conditional Access Administrator role for exercises that create or manage Conditional Access policies.
- A Windows 11 device that's Microsoft Entra joined or hybrid joined and has internet access.

## Learning progression

Each lab builds on the previous one and follows a logical progression.

| Exercise | What you learn |
| --- | --- |
| [Enable the Microsoft traffic profile](https://learn.microsoft.com/en-us/entra/global-secure-access/tutorial-microsoft-traffic-enable-profile) | How the Microsoft traffic profile works and how to route Microsoft 365 and Microsoft Entra ID traffic through Global Secure Access. |
| [Enable source IP restoration](https://learn.microsoft.com/en-us/entra/global-secure-access/tutorial-microsoft-traffic-source-ip-restoration) | How to preserve the original client IP in Microsoft Entra sign-in logs for accurate policy evaluation and investigation. |
| [Enable the compliant network check](https://learn.microsoft.com/en-us/entra/global-secure-access/tutorial-microsoft-traffic-compliant-network) | How to require traffic to flow through Global Secure Access before granting access to apps integrated with Microsoft Entra ID. |
| [Configure universal tenant restrictions](https://learn.microsoft.com/en-us/entra/global-secure-access/tutorial-microsoft-traffic-tenant-restrictions) | How to block sign-ins to unauthorized external tenants from managed devices. |

## Next step

> [Enable the Microsoft traffic profile](https://learn.microsoft.com/en-us/entra/global-secure-access/tutorial-microsoft-traffic-enable-profile)
