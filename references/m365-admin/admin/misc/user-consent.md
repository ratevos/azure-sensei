# Managing user consent to apps in Microsoft 365

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/misc/user-consent  
> Microsoft doc last updated: 04/02/2025


This setting controls whether users can give that consent to apps that use OpenID Connect and OAuth 2.0 for sign-in and requests to access data. An app can be created from within your own organization, or it can come from another Microsoft 365 organization or a third-party.

If you turn this setting on, those apps will ask users for permission to access your organization’s data, and users can choose whether to allow it. If you turn this setting off, then admins must consent to those apps before users may use them. In this case, consider setting up an [admin consent workflow](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/configure-admin-consent-workflow) in the Microsoft Entra admin center so users can send a request for admin approval to use any blocked app.

A user can give access only to apps they own that access their Microsoft 365 information. They can't give an app access to any other user's information.

## Turning user consent on or off

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

Contact your Global Administrator to edit the user consent policy in the Microsoft Entra portal by following the steps in [Configure how users consent to applications](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent).

## Related content

[Configure the admin consent workflow](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/configure-admin-consent-workflow) (article)\
[Managing consent to applications and evaluating consent requests](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/manage-consent-requests) (article)
