# Phase 4: Plan management and insights

> Source: https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/migrate-adfs-plan-management-insights  
> Microsoft doc last updated: 05/30/2023


Once apps are migrated, you must ensure that:

- Users can securely access and manage
- You can gain the appropriate insights into usage and app health

We recommend taking the following actions as appropriate to your organization.

## Manage your users’ app access

Once you've migrated the apps, consider applying the following suggestions to enrich your user’s experience:

- Make apps discoverable by publishing them to the [Microsoft MyApplications portal](https://support.microsoft.com/account-billing/sign-in-and-start-apps-from-the-my-apps-portal-2f3b1bae-0e5a-4a86-a33e-876fbd2a4510#download-and-install-the-my-apps-secure-sign-in-extension).
- Add [app collections](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/access-panel-collections) so users can locate application based on business function.
- Add their own application bookmarks to the [MyApplications portal](https://support.microsoft.com/account-billing/sign-in-and-start-apps-from-the-my-apps-portal-2f3b1bae-0e5a-4a86-a33e-876fbd2a4510#download-and-install-the-my-apps-secure-sign-in-extension).
- Enable [self-service application access](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/manage-self-service-access) to an app and **let users add apps that you curate**.
- Optionally [hide applications from end-users](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/hide-application-from-user-portal).
- Users can go to [Office.com](https://www.office.com) to **search for their apps and have their most-recently-used apps appear** for them right from where they do work.  
- Users can download the MyApps secure sign-in extension in Chrome, or Microsoft Edge so they can launch applications directly from their browser without having to first navigate to MyApplications.
- Users can access the MyApps portal with Intune-managed browser on their [iOS 7.0](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/hide-application-from-user-portal) or later or [Android](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/hide-application-from-user-portal) devices.

  - For **Android devices**, from the [Google play store](https://play.google.com/store/apps/details?id=com.microsoft.intune)

  - For **Apple devices**, from the [Apple App Store](https://apps.apple.com/us/app/intune-company-portal/id719171358).

> [!VIDEO https://www.youtube.com/embed/8aUIuOXeDxw]

## Secure app access

Microsoft Entra ID provides a centralized access location to manage your migrated apps. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) and enable the following capabilities:

- **Secure user access to apps.** Enable [Conditional Access policies](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview) to secure user access to applications based on device state, location, and more.
- **Automatic provisioning.** Set up [automatic provisioning of users](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/user-provisioning) with various third-party SaaS apps that users need to access. In addition to creating user identities, it includes the maintenance and removal of user identities as status or roles change.
- **Delegate user access** **management**. As appropriate, enable self-service application access to your apps and *assign a business approver to approve access to those apps*. Use [Self-Service Group Management](https://learn.microsoft.com/en-us/entra/identity/users/groups-self-service-management)for groups assigned to collections of apps.
- **Delegate admin access** using **Directory Role** to assign an admin role (such as Application Administrator, Cloud Application Administrator, or Application Developer) to your user.
- **Add applications to Access Packages** to provide governance and attestation.

## Audit and gain insights of your apps

You can also use the [Microsoft Entra admin center](https://entra.microsoft.com) to audit all your apps from a centralized location,

- **Audit your app** using **Enterprise Applications, Audit**, or access the same information from the [Microsoft Entra reporting API](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-configure-prerequisites-for-reporting-api) to integrate into your favorite tools.
- **View the permissions for an app** using **Enterprise Applications, Permissions** for apps using OAuth/OpenID Connect.
- **Get sign-in insights** using **Enterprise Applications, Sign-Ins**. Access the same information from the [Microsoft Entra reporting API.](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-configure-prerequisites-for-reporting-api)
- **Visualize your app’s usage** from the [Microsoft Entra ID Power BI content pack](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-use-workbooks)

## Exit criteria

You're successful in this phase when you:

- Provide secure app access to your users
- Manage to audit and gain insights of the migrated apps

## Do even more with deployment plans

Deployment plans walk you through the business value, planning, implementation steps, and management of Microsoft Entra solutions, including app migration scenarios. They bring together everything that you need to start deploying and getting value out of Microsoft Entra capabilities. The deployment guides include content such as Microsoft recommended best practices, end-user communications, planning guides, implementation steps, test cases, and more.

Many [deployment plans](https://learn.microsoft.com/en-us/entra/architecture/deployment-plans) are available for your use, and we’re always making more!

## Contact support

Visit the following support links to create or track support ticket and monitor health.

- **Azure Support:** You can call [Microsoft Support](https://azure.microsoft.com/support) and open a ticket for any Azure Identity deployment issue depending on your Enterprise Agreement with Microsoft.
- **FastTrack**: If you've purchased Enterprise Mobility and Security (EMS) or Microsoft Entra ID P1 or P2 licenses, you're eligible to receive deployment assistance from the [FastTrack program.](https://learn.microsoft.com/en-us/microsoft-365/fasttrack/introduction)
- **Engage the Product Engineering team:** If you're working on a major customer deployment with millions of users, you're entitled to support from the Microsoft account team or your Cloud Solutions Architect. Based on the project’s deployment complexity, you can work directly with the [Azure Identity Product Engineering team.](https://portal.azure.com/#blade/Microsoft_Azure_Marketplace/MarketplaceOffersBlade/selectedMenuItemId/solutionProviders)

## Next steps

- [Migration process](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/migrate-adfs-apps-stages)
