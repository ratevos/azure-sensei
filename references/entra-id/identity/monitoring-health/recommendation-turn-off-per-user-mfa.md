# Turn off per user MFA in Microsoft Entra ID

> Source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/recommendation-turn-off-per-user-mfa  
> Microsoft doc last updated: 04/28/2026


[Microsoft Entra recommendations](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations) is a feature that provides you with personalized insights and actionable guidance to align your tenant with recommended best practices.

This article covers the recommendation to switch per-user multifactor authentication (MFA) accounts to Conditional Access MFA accounts. This recommendation is called `switchFromPerUserMFA` in the recommendations API in Microsoft Graph.

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

As an admin, you want to maintain security for your company’s resources, but you also want your employees to easily access resources as needed. MFA enables you to enhance the security posture of your tenant.

In your tenant, you can enable MFA on a per-user basis. In this scenario, your users perform MFA each time they sign in. There are some exceptions, such as when they sign in from trusted IP addresses or when the "remember MFA on trusted devices" feature is turned on. While enabling MFA is a good practice, switching per-user MFA to MFA based on [Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview) can reduce the number of times your users are prompted for MFA.

This recommendation shows up if:

- You have per-user MFA configured for at least 5% of your users.
- Conditional Access policies are active for more than 1% of your users (indicating familiarity with Conditional Access policies).

## Value 

This recommendation improves your user's productivity and minimizes the sign-in time with fewer MFA prompts. Conditional Access and MFA used together help ensure that your most sensitive resources can have the tightest controls, while your least sensitive resources can be more freely accessible. For an overview of available functionality in Conditional Access, see [Building a Conditional Access policy](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policies).

## Action plan

1. Require MFA using a Conditional Access policy.
    - [Enable Microsoft Entra multifactor authentication with Conditional Access](https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa).
    - Ensure that you're covering all resources and users you would like to secure with MFA.
1. Ensure that the per-user MFA configuration is turned off.
    1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator).
    1. Browse to **Users** > **All users** and select the **Per-user MFA** button.

    

    1. Select **Disable MFA** for all users who had this option enabled.

    
    
After all users are migrated to Conditional Access MFA accounts, the recommendation status automatically updates the next time the service runs. Continue to review your Conditional Access policies.

## Related content

- [How to use Microsoft Entra recommendations](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-use-recommendations)
- [Microsoft Graph API for recommendations](https://learn.microsoft.com/en-us/graph/api/resources/recommendation)
- [MFA and Conditional Access policy](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-mfa-strength)
- [MFA and Conditional Access policy tutorial](https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa)
