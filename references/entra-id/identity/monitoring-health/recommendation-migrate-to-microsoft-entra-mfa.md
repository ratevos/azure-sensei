# Recommendation to migrate to Microsoft Entra MFA

> Source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/recommendation-migrate-to-microsoft-entra-mfa  
> Microsoft doc last updated: 04/28/2026


[Microsoft Entra recommendations](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations) provide you with personalized insights and actionable guidance to align your tenant with recommended best practices.

This article covers the recommendation to migrate from MFA server to Microsoft Entra MFA. This recommendation is called `mfaServerDeprecation` in the recommendations API in Microsoft Graph.

## Prerequisites

There are different role requirements for viewing or updating a recommendation. Use the least-privileged role for the type of access needed. For a full list of roles, see [Least privileged roles by task](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/delegate-by-task#monitoring-and-health---recommendations-least-privileged-roles).

| Microsoft Entra role | Access type |
|---- |---- |
| Reports Reader | Read-only |
| Security Reader | Read-only |
| Global Reader | Read-only |
| Authentication Policy Administrator | Update and read |
| Exchange Administrator | Update and read |
| Security Administrator | Update and read |
| `DirectoryRecommendations.Read.All` | Read-only in Microsoft Graph |
| `DirectoryRecommendations.ReadWrite.All` | Update and read in Microsoft Graph |

Some recommendations might require a P2 or other license. For more information, see the [Recommendations overview table](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations#recommendations-overview-table).

## Description

Azure Multi-Factor Authentication Server (MFA Server) was scheduled for retirement on September 30th, 2024. To help organizations migrate to Microsoft Entra MFA, this Microsoft Entra recommendation identifies tenants with MFA server activity. This recommendation identifies tenants with active users and MFA attempts for MFA Server in the last seven days. MFA Server client integrations, including a list of affected clients are also surfaced as a part of this recommendation.

## Value 

MFA Server is a component for deploying and managing MFA on-premises. In 2019, Microsoft stopped allowing new deployments of MFA Server and investing in feature enhancements. In September 2022, [Microsoft formally announced the deprecation of MFA Server](https://techcommunity.microsoft.com/t5/microsoft-entra-blog/microsoft-entra-change-announcements-september-2022-train/ba-p/2967454).

Cloud-based, Microsoft Entra multifactor authentication offers better resiliency, availability, and data compliancy. Migrating to Microsoft Entra MFA helps you improve your security posture by giving you access to the latest phishing-resistant authentication methods and more fine-grained access controls. It also helps reduce cost and deployment complexity by no longer having to maintain an on-premises component. 

## Action plan

1. [Learn how to migrate MFA Server to Microsoft Entra MFA](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-migrate-mfa-server-to-mfa-user-authentication).

1. Migrate MFA user information from on-premises to Microsoft Entra.
    - You can either migrate this information manually or use the MFA Server Migration Utility (recommended).
    - [How to use the MFA Server Migration Utility](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-mfa-server-migration-utility).

1. Use [Staged Rollout](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-mfa-server-migration-utility#enable-staged-rollout) to reroute users to authenticate against Microsoft Entra instead of MFA Server.  

1. Identify and migrate any MFA Server dependencies, such as applications using [RADIUS or LDAP authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-mfa-server-migration-utility#authentication-services). 

1. Update domain federation settings and decommission MFA Server. 

## Related content

- [Review the Microsoft Entra recommendations overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations)
- [Learn how to use Microsoft Entra recommendations](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-use-recommendations)
- [Explore the Microsoft Graph API properties for recommendations](https://learn.microsoft.com/en-us/graph/api/resources/recommendation)
