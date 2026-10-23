# Migrate applications from Okta to Microsoft Entra ID

> Source: https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/migrate-applications-from-okta  
> Microsoft doc last updated: 12/06/2024


In this tutorial, you learn how to migrate your applications from Okta to Microsoft Entra ID.

## Prerequisites

To manage the application in Microsoft Entra ID, you need:

- A Microsoft Entra user account. If you don't already have one, you can [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- One of the following roles: Cloud Application Administrator, Application Administrator, or owner of the service principal.

## Create an inventory of current Okta applications

Before migration, document the current environment and application settings. You can use the Okta API to collect this information. Use an API explorer tool such as [Postman](https://www.postman.com/).

To create an application inventory:

1. With the Postman app, from the Okta admin console, generate an API token.
2. On the API dashboard, under **Security**, select **Tokens** > **Create Token**.

    

3. Enter a token name and then select **Create Token**.

    

4. Record the token value and save it. After you select **OK, got it**, it isn't accessible.

    

5. In the Postman app, in the workspace, select **Import**.

6. On the **Import** page, select **Link**. To import the API, insert the following link:

`https://developer.okta.com/docs/api/postman/example.oktapreview.com.environment`

   

>[!NOTE]
>Don't modify the link with your tenant values.

7. Select **Import**.

    

8. After the API is imported, change the **Environment** selection to **{yourOktaDomain}**.
9. To edit your Okta environment, select the **eye** icon. Then select **Edit**.

    

10. In the **Initial Value** and **Current Value** fields, update the values for the URL and API key. Change the name to reflect your environment. 
11. Save the values.

     

12. [Load the API into Postman](https://app.getpostman.com/run-collection/377eaf77fdbeaedced17).
13. Select **Apps** > **Get List Apps** > **Send**.

>[!NOTE]
>You can print the applications in your Okta tenant. The list is in JSON format.

   

We recommend you copy and convert this JSON list to a CSV format:

- Use a public converter such as [Konklone](https://konklone.io/json/)
- Or for PowerShell, use [ConvertFrom-Json](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertfrom-json) and [ConvertTo-CSV](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertto-csv)

>[!NOTE]
>To have a record of the applications in your Okta tenant, download the CSV.

## Migrate a SAML application to Microsoft Entra ID

To migrate a SAML 2.0 application to Microsoft Entra ID, configure the application in your Microsoft Entra tenant for application access. In this example, we convert a Salesforce instance. 

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator). 
2. Browse to **Entra ID** > **Enterprise apps** > **All applications**, then select **New application**.

3. In **Microsoft Entra Gallery**, search for **Salesforce**, select the application, and then select **Create**.

    

4. After the application is created, on the **Single sign-on (SSO)** tab, select **SAML**.

    

5. Download the **Certificate (Raw)** and **Federation Metadata XML** to import it into Salesforce.

6. On the Salesforce administration console, select **Identity** > **Single Sign-On Settings** > **New from Metadata File**.

    

7. Upload the XML file you downloaded from the Microsoft Entra admin center. Then select **Create**.
8. Upload the certificate you downloaded from Azure. Select **Save**.
9. Record the values in the following fields. The values are in Azure.

   - **Entity ID**
   - **Login URL**
   - **Logout URL**

10. Select **Download Metadata**.
11. To upload the file to the Microsoft Entra admin center, in the Microsoft Entra ID **Enterprise applications** page, in the SAML SSO settings, select **Upload metadata file**.  
12. Ensure the imported values match the recorded values. Select **Save**.

    

13. In the Salesforce administration console, select **Company Settings** > **My Domain**. Go to **Authentication Configuration** and then select **Edit**.

     

14. For a sign-in option, select the new SAML provider you configured. Select **Save**.

     

15. In Microsoft Entra ID, on the **Enterprise applications** page, select **Users and groups**. Then add test users.

     

16. To test the configuration, sign in as a test user. Go to the Microsoft [apps gallery](https://aka.ms/myapps) and then select **Salesforce**.

     

17. To sign in, select the configured identity provider (IdP).

     

>[!NOTE]
>If configuration is correct, the test user lands on the Salesforce home page. For troubleshooting help, see the [debugging guide](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/debug-saml-sso-issues).

18. On the **Enterprise applications** page, assign the remaining users to the Salesforce application, with the correct roles.

>[!NOTE]
>After you add the remaining users to the Microsoft Entra application, users can test the connection to ensure they have access. Test the connection before the next step.

19. On the Salesforce administration console, select **Company Settings** > **My Domain**.

20. Under **Authentication Configuration**, select **Edit**. For authentication service, clear the selection for **Okta**.

    

## Migrate an OpenID Connect or OAuth 2.0 application to Microsoft Entra ID

To migrate an OpenID Connect (OIDC) or OAuth 2.0 application to Microsoft Entra ID, in your Microsoft Entra tenant, configure the application for access. In this example, we convert a custom OIDC app.

To complete the migration, repeat configuration for all applications in the Okta tenant.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator). 
1. Browse to **Entra ID** > **Enterprise apps** > **All applications**.
2. Select **New application**.
3. Select **Create your own application**. 
4. On the menu that appears, name the OIDC app and then select **Register an application you're working on to integrate with Microsoft Entra ID**. 
5. Select **Create**.
6. On the next page, set up the tenancy of your application registration. For more information, see [Tenancy in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/single-and-multi-tenant-apps). Go to **Accounts in any organizational directory (Any Microsoft Entra directory - Multitenant)** > **Register**.

    

7. On the **App registrations** page, under **Microsoft Entra ID**, open the created registration.

>[!NOTE]
>Depending on the [application scenario](https://learn.microsoft.com/en-us/entra/identity-platform/authentication-flows-app-scenarios), there are various configuration actions. Most scenarios require an app client secret.

8. On the **Overview** page, record the **Application (client) ID**. You use this ID in your application.

9. On the left, select **Certificates & secrets**. Then select **+ New client secret**. Name the client secret and set its expiration.

10. Record the value and ID of the secret.

>[!NOTE]
>If you misplace the client secret, you can't retrieve it. Instead, regenerate a secret.

11. On the left, select **API permissions**. Then grant the application access to the OIDC stack.
12. Select **+ Add permission** > **Microsoft Graph** > **Delegated permissions**.
13. In the **OpenId permissions** section, select **email**, **openid**, and **profile**. Then select **Add permissions**.
14. To improve user experience and suppress user consent prompts, select **Grant admin consent for Tenant Domain Name**. Wait for the **Granted** status to appear.

    

15. If your application has a redirect URI, enter the URI. If the reply URL targets the **Authentication** tab, followed by **Add a platform** and **Web**, enter the URL. 
16. Select **Access tokens** and **ID tokens**. 
17. Select **Configure**.
18. If needed, on the **Authentication** menu, under **Advanced settings** and **Allow public client flows**, select **Yes**.

    

19. Before you test, in your OIDC-configured application, import the application ID and client secret. 

>[!NOTE]
>Use the previous steps to configure your application with settings such as Client ID, Secret, and Scopes.

## Migrate a custom authorization server to Microsoft Entra ID

Okta authorization servers map one-to-one to application registrations that [expose an API](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-expose-web-apis#add-a-scope).

Map the default Okta authorization server to Microsoft Graph scopes or permissions.

   

## Next steps

- [Migrate Okta federation to Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/migrate-okta-federation)
- [Migrate Okta sync provisioning to Microsoft Entra Connect-based synchronization](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/migrate-okta-sync-provisioning)
- [Migrate Okta sign-on policies to Microsoft Entra Conditional Access](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/migrate-okta-sign-on-policies-conditional-access)
