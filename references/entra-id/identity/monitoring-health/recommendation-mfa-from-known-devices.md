# Recommendation to minimize MFA prompts from known devices

> Source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/recommendation-mfa-from-known-devices  
> Microsoft doc last updated: 04/28/2026


[Microsoft Entra recommendations](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations) is a feature that provides you with personalized insights and actionable guidance to align your tenant with recommended best practices.

This article covers the recommendation to minimize multifactor authentication prompts from known devices. This recommendation is called `tenantMFA` in the recommendations API in Microsoft Graph.

> [!NOTE]
> If you have a Microsoft Entra ID P1 or P2 license, Microsoft recommends using [Conditional Access sign-in frequency](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-session-lifetime) to control how often users are prompted for MFA, rather than the **remember multifactor authentication** setting described in this article. For more information, see [Reauthentication prompts and session lifetime for Microsoft Entra multifactor authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/concepts-azure-multi-factor-authentication-prompts-session-lifetime).

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

As an admin, you want to maintain security for your company’s resources, but you also want your employees to easily access resources as needed. While enabling MFA is a good practice, you should try to keep the number of MFA prompts your users have to go through at a minimum. One option you have to accomplish this goal is to **allow users to remember multifactor authentication on trusted devices**.

The *remember multifactor authentication on trusted device* feature sets a persistent cookie on the browser when a user selects the *Don't ask again for X days* option at sign-in. The user isn't prompted again for MFA from that browser until the cookie expires. If the user opens a different browser on the same device or clears the cookies, they're prompted again to verify.

For more information, see [Configure Microsoft Entra multifactor authentication settings](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-mfasettings).

This recommendation shows up if the **remember multifactor authentication** feature is set to less than 30 days.

## Value 

This recommendation improves your user's productivity and minimizes the sign-in time with fewer MFA prompts. Ensure that your most sensitive resources can have the tightest controls, while your least sensitive resources can be more freely accessible.

## Action plan

If you have a Microsoft Entra ID P1 or P2 license, consider migrating to [Conditional Access sign-in frequency](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-session-lifetime) for session management instead of using the **remember multifactor authentication** setting. For tenants that continue to use this setting, complete the following steps to ensure the duration is set to at least 90 days.

1. Review the [How to configure Microsoft Entra multifactor authentication settings](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-mfasettings) article.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator).

1. Browse to **Entra ID** > **Multifactor authentication**.

1. Under the **Configure** heading, select the **Additional cloud-based multifactor authentication settings** link.

    

1. Select the **Service settings** tab.

    

1. Under the **Remember multifactor authentication on trusted device** heading, select the checkbox, and set the number of days to 90.

    

## Related content

- [Review the Microsoft Entra recommendations overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations)
- [Learn how to use Microsoft Entra recommendations](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-use-recommendations)
- [Explore the Microsoft Graph API properties for recommendations](https://learn.microsoft.com/en-us/graph/api/resources/recommendation)
