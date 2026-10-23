# Recommendation to migrate applications away from AD FS

> Source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/recommendation-migrate-apps-from-adfs-to-azure-ad  
> Microsoft doc last updated: 04/28/2026


[Microsoft Entra recommendations](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations) provides you with personalized insights and actionable guidance to align your tenant with recommended best practices.

This article covers the recommendation to migrate apps from Active Directory Federated Services (AD FS) to Microsoft Entra ID. This recommendation is called `adfsAppsMigration` in the recommendations API in Microsoft Graph.

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

As an admin responsible for managing applications, you want your applications to use the security features of Microsoft Entra ID and maximize their value. This recommendation shows up if your tenant has apps on ADFS that can 100% be migrated to Microsoft Entra ID. For more information, see [Understand the stages of migrating application authentication from AD FS to Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/migrate-adfs-apps-stages).

## Value 

Using Microsoft Entra ID gives you granular per-application access controls to secure access to applications. With Microsoft Entra B2B collaboration, you can increase user productivity. Automated app provisioning automates the user identity lifecycle in cloud SaaS apps such as Dropbox, Salesforce, and more. 

## Action plan

1. [Install Microsoft Entra Connect](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-roadmap) on your AD FS server. 
1. [Review the AD FS application activity report](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/migrate-adfs-application-activity) to get insights about your AD FS applications. 
1. Read the solution guide for [migrating applications to Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/migrate-adfs-apps-stages). 
1. Migrate applications to Microsoft Entra ID. For more information, see the article [Migrate from federation to cloud authentication](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/migrate-from-federation-to-cloud-authentication).

### Guided walkthrough

For a guided walkthrough of many of the recommendations in this article, see the migration guide [Migrate from AD FS to Microsoft Entra ID for identity management](https://go.microsoft.com/fwlink/?linkid=2225005) when signed in to the Microsoft 365 admin center. To review best practices without signing in and activating automated setup features, go to the Microsoft 365 Setup portal.

## Related content

- [Review the Microsoft Entra recommendations overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations)
- [Learn how to use Microsoft Entra recommendations](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-use-recommendations)
- [Explore the Microsoft Graph API properties for recommendations](https://learn.microsoft.com/en-us/graph/api/resources/recommendation)
