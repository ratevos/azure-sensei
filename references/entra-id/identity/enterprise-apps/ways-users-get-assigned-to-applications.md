# Understand how users are assigned to apps

> Source: https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/ways-users-get-assigned-to-applications  
> Microsoft doc last updated: 01/07/2021


This article helps you to understand how users get assigned to an application in your tenant.

<a name='how-do-users-get-assigned-an-application-in-azure-ad'></a>

## How do users get assigned an application in Microsoft Entra ID?

There are several ways a user can be assigned an application. Assignment can be performed by an administrator, a business delegate, or sometimes, the user themselves. Below describes the ways users can get assigned to applications:

* An administrator [assigns a user](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/assign-user-or-group-access-portal) to the application directly
* An administrator [assigns a group](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/assign-user-or-group-access-portal) that the user is a member of to the application, including:

  * A group that was synchronized from on-premises
  * A static security group created in the cloud
  * A [dynamic security group](https://learn.microsoft.com/en-us/entra/identity/users/groups-dynamic-membership) created in the cloud
  * A Microsoft 365 group created in the cloud
  * The [All Users](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-groups) group
* An administrator enables [Self-service Application Access](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/manage-self-service-access) to allow a user to add an application using [My Apps](https://support.microsoft.com/account-billing/sign-in-and-start-apps-from-the-my-apps-portal-2f3b1bae-0e5a-4a86-a33e-876fbd2a4510) **Add App** feature **without business approval**
* An administrator enables [Self-service Application Access](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/manage-self-service-access) to allow a user to add an application using [My Apps](https://support.microsoft.com/account-billing/sign-in-and-start-apps-from-the-my-apps-portal-2f3b1bae-0e5a-4a86-a33e-876fbd2a4510) **Add App** feature, but only **with prior approval from a selected set of business approvers**
* An administrator enables [Self-service Group Management](https://learn.microsoft.com/en-us/entra/identity/users/groups-self-service-management) to allow a user to join a group that an application is assigned to **without business approval**
* An administrator enables [Self-service Group Management](https://learn.microsoft.com/en-us/entra/identity/users/groups-self-service-management) to allow a user to join a group that an application is assigned to, but only **with prior approval from a selected set of business approvers**
* One of the application's roles is included in an [entitlement management access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-resources), and a user requests or is assigned to that access package
* An administrator assigns a license to a user directly, for a Microsoft service such as [Microsoft 365](https://www.microsoft.com/microsoft-365)
* An administrator assigns a license to a group that the user is a member of, for a Microsoft service.
* A user [consents to an application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/user-admin-consent-overview#user-consent) on behalf of themselves.

## Next steps

* [Quickstart Series on Application Management](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/view-applications-portal)
* [What is application management?](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/what-is-application-management)
* [What is single sign-on?](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/what-is-single-sign-on)
