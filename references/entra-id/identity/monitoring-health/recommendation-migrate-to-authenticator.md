# Recommendation to migrate to Microsoft authenticator

> Source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/recommendation-migrate-to-authenticator  
> Microsoft doc last updated: 04/28/2026


[Microsoft Entra recommendations](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations) is a feature that provides you with personalized insights and actionable guidance to align your tenant with recommended best practices.

This article covers the recommendation to migrate users to the Microsoft Authenticator app, which is currently a preview recommendation. This recommendation is called `useAuthenticatorApp` in the recommendations API in Microsoft Graph.

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

Multifactor authentication (MFA) is a key component to improve the security posture of your Microsoft Entra tenant. While SMS text and voice calls were once commonly used for multifactor authentication, they're becoming increasingly less secure. You also don't want to overwhelm your users with lots of MFA methods and messages.

One way to ease the burden on your users is to migrate anyone using SMS or voice call for MFA to use the Microsoft Authenticator app. This strategy also increases the security of their authentication methods.

This recommendation appears if Microsoft Entra ID detects that your tenant has users authenticating using SMS or voice instead of the Microsoft Authenticator app in the past week.

## Value 

Push notifications through the Microsoft Authenticator app provide the least intrusive MFA experience for users. This method is the most reliable and secure option because it relies on a data connection rather than telephony.

The verification code option enables MFA even in isolated environments without data or cellular signals, where SMS and Voice calls might not work.

The Microsoft Authenticator app is available for Android and iOS. Microsoft Authenticator can serve as a traditional MFA factor (one-time passcodes, push notification) and when your organization is ready for Password-less, the Microsoft Authenticator app can be used to sign in to Microsoft Entra ID without a password.

## Action plan

1. Ensure that notification through mobile app and/or verification code from mobile app are available to users as authentication methods. How to Configure Verification Options

2. Educate users on how to add a work or school account. 

## Related content

- [Review the Microsoft Entra recommendations overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations)
- [Learn how to use Microsoft Entra recommendations](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-use-recommendations)
- [Explore the Microsoft Graph API properties for recommendations](https://learn.microsoft.com/en-us/graph/api/resources/recommendation)
