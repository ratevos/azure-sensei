# Quickstart: Add an enterprise application

> Source: https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/add-application-portal  
> Microsoft doc last updated: 03/31/2025


In this quickstart, you use the Microsoft Entra admin center to add an enterprise application to your Microsoft Entra tenant. Microsoft Entra ID has a gallery that contains thousands of enterprise applications that are already preintegrated. Many of the applications your organization uses are probably already in the gallery. This quickstart uses the application named **Microsoft Entra SAML Toolkit** as an example, but the concepts apply for most [enterprise applications in the gallery](https://learn.microsoft.com/en-us/entra/identity/saas-apps/tutorial-list).

We recommend that you use a nonproduction environment to test the steps in this quickstart.

## Prerequisites

To add an enterprise application to your Microsoft Entra tenant, you need:

- A Microsoft Entra user account. If you don't already have one, you can [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- One of the following roles: Cloud Application Administrator, or Application Administrator.

## Add an enterprise application

To add an enterprise application to your tenant:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator). 
1. Browse to **Entra ID** > **Enterprise apps** > **All applications**.
1. Select **New application**.
1. The **Browse Microsoft Entra Gallery** pane opens and displays tiles for cloud platforms, on-premises applications, and featured applications. Applications listed in the **Featured applications** section have icons indicating whether they support federated single sign-on (SSO) and provisioning. Search for and select the application. In this quickstart, **Microsoft Entra SAML Toolkit** is being used.

    

1. Enter a name that you want to use to recognize the instance of the application. For example, `Microsoft Entra SAML Toolkit 1`.
1. Select **Create**, you're taken to the application that you registered.
1. You should [assign owners to the application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/assign-app-owners#assign-an-owner) as a best practice at this point.

If you choose to install an application that uses OpenID Connect based SSO, instead of seeing a **Create** button, you see a button that redirects you to the application sign-in or sign-up page depending on whether you already have an account there. For more information, see [Add an OpenID Connect based single sign-on application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/add-application-portal-setup-oidc-sso). After sign-in, the application is added to your tenant.

## Clean up resources

If you're planning to complete the next quickstart, keep the enterprise application that you created. Otherwise, you can consider deleting it to clean up your tenant. For more information, see [Delete an application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/delete-application-portal).

## Microsoft Graph API

To add an application from the Microsoft Entra gallery programmatically, use the [applicationTemplate: instantiate](https://learn.microsoft.com/en-us/graph/api/applicationtemplate-instantiate) API in Microsoft Graph.

## Next steps

Learn how to create a user account and assign it to the enterprise application that you added.

> [Create and assign a user account](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/add-application-portal-assign-users)
