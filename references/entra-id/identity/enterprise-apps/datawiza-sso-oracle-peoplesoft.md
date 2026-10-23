# Configure Microsoft Entra multifactor authentication and SSO for Oracle PeopleSoft applications using Datawiza Access Proxy

> Source: https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/datawiza-sso-oracle-peoplesoft  
> Microsoft doc last updated: 01/30/2024


In this tutorial, learn how to enable Microsoft Entra single sign-on (SSO) and Microsoft Entra multifactor authentication for an Oracle PeopleSoft application using Datawiza Access Proxy (DAP).

Learn more: [Datawiza Access Proxy](https://www.datawiza.com/)

Benefits of integrating applications with Microsoft Entra ID using DAP:

* [Embrace proactive security with Zero Trust](https://www.microsoft.com/security/business/zero-trust) - a security model that adapts to modern environments and embraces hybrid workplace, while it protects people, devices, apps, and data
* [Microsoft Entra single sign-on](https://azure.microsoft.com/solutions/active-directory-sso/#overview) - secure and seamless access for users and apps, from any location, using a device
* [How it works: Microsoft Entra multifactor authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-howitworks) - users are prompted during sign-in for forms of identification, such as a code on their cellphone or a fingerprint scan
* [What is Conditional Access?](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview) - policies are if-then statements, if a user wants to access a resource, then they must complete an action
* [Easy authentication and authorization in Microsoft Entra ID with no-code Datawiza](https://www.microsoft.com/security/blog/2022/05/17/easy-authentication-and-authorization-in-azure-active-directory-with-no-code-datawiza/) - use web applications such as: Oracle JDE, Oracle E-Business Suite, Oracle Siebel, and home-grown apps
* Use the [Datawiza Cloud Management Console (DCMC)](https://console.datawiza.com) - manage access to applications in public clouds and on-premises

## Scenario description

This scenario focuses on Oracle PeopleSoft application integration using HTTP authorization headers to manage access to protected content.

In legacy applications, due to the absence of modern protocol support, a direct integration with Microsoft Entra SSO is difficult. Datawiza Access Proxy (DAP) bridges the gap between the legacy application and the modern ID control plane, through protocol transitioning. DAP lowers integration overhead, saves engineering time, and improves application security.

## Scenario architecture

The scenario solution has the following components:

* **Microsoft Entra ID** - identity and access management service that helps users sign in and access external and internal resources
* **Datawiza Access Proxy (DAP)** - container-based reverse-proxy that implements OpenID Connect (OIDC), OAuth, or Security Assertion Markup Language (SAML) for user sign-in flow. It passes identity transparently to applications through HTTP headers.
* **Datawiza Cloud Management Console (DCMC)** - administrators manage DAP with UI and RESTful APIs to configure DAP and access control policies
* **Oracle PeopleSoft application** - legacy application to be protected by Microsoft Entra ID and DAP

Learn more: [Datawiza and Microsoft Entra authentication architecture](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/datawiza-configure-sha#datawiza-with-azure-ad-authentication-architecture)

## Prerequisites

Ensure the following prerequisites are met.

* An Azure subscription
  * If you don't have one, you can get an [Azure free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn)
* A Microsoft Entra tenant linked to the Azure subscription
  * See, [Quickstart: Create a new tenant in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/create-new-tenant)
* Docker and Docker Compose
  * Go to docs.docker.com to [Get Docker](https://docs.docker.com/get-docker) and [Install Docker Compose](https://docs.docker.com/compose/install)
* User identities synchronized from an on-premises directory to Microsoft Entra ID, or created in Microsoft Entra ID and flowed back to an on-premises directory
  * See, [Microsoft Entra Connect Sync: Understand and customize synchronization](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-whatis)
* An account with Microsoft Entra ID and the Application Administrator role
  * See, [Microsoft Entra built-in roles, all roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator)
* An Oracle PeopleSoft environment
* (Optional) An SSL web certificate to publish services over HTTPS. You can use default Datawiza self-signed certs for testing.

## Getting started with DAP

To integrate Oracle PeopleSoft with Microsoft Entra ID:

1. Sign in to [Datawiza Cloud Management Console (DCMC)](https://console.datawiza.com/).
2. The Welcome page appears.
3. Select the orange **Getting started** button.
  
   

4. In the **Name** and **Description** fields, enter information.

   

5. Select **Next**.
6. The Add Application dialog appears.
7. For **Platform**, select **Web**.
8. For **App Name**, enter a unique application name.
9. For **Public Domain**, for example use `https://ps-external.example.com`. For testing, you can use localhost DNS. If you aren't deploying DAP behind a load balancer, use the Public Domain port.
10. For **Listen Port**, select the port that DAP listens on.
11. For **Upstream Servers**, select the Oracle PeopleSoft implementation URL and port to be protected. 
12. Select **Next**.
13. On the **Configure IdP** dialog, enter information.

   >[!Note]
   >DCMC has one-click integration to help complete Microsoft Entra configuration. DCMC calls the Microsoft Graph API to create an application registration on your behalf in your Microsoft Entra tenant. Learn more at docs.datawiza.com in [One Click Integration with Microsoft Entra ID](https://docs.datawiza.com/tutorial/web-app-azure-one-click.html#preview)

14. Select **Create**.

   

15. The DAP deployment page appears.
16. Make a note of the deployment Docker Compose file. The file includes the DAP image, the Provisioning Key and Provision Secret, which pulls the latest configuration and policies from DCMC.

## SSO and HTTP headers

DAP gets user attributes from the identity provider (IdP) and passes them to the upstream application with a header or cookie.

The Oracle PeopleSoft application needs to recognize the user. Using a name, the application instructs DAP to pass the values from the IdP to the application through the HTTP header.

1. In Oracle PeopleSoft, from the left navigation, select **Applications**.
2. Select the **Attribute Pass** subtab.
3. For **Field**, select **email**.
4. For **Expected**, select **PS_SSO_UID**.
5. For **Type**, select **Header**.

   

   >[!Note]
   >This configuration uses Microsoft Entra user principal name as the sign-in username for Oracle PeopleSoft. To use another user identity, go to the **Mappings** tab.

   

## SSL Configuration

1. Select the **Advanced tab**.

   

2. Select **Enable SSL**.
3. From the **Cert Type** dropdown, select a type.

   

4. For testing the configuration, there's a self-signed certificate.

   

   >[!Note]
   >You can upload a certificate from a file.

   

5. Select **Save**.

<a name='enable-azure-ad-multi-factor-authentication'></a>

## Enable Microsoft Entra multifactor authentication

To provide more security for sign-ins, you can enforce Microsoft Entra multifactor authentication. 

Learn more: [Tutorial: Secure user sign-in events with Microsoft Entra multifactor authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa)

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as an [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator).
2. Browse to **Entra ID** > **Overview** > **Properties** tab.
3. Under **Security defaults**, select **Manage security defaults**.
4. On the **Security defaults** pane, toggle the dropdown menu to select **Enabled**.
5. Select **Save**.

## Enable SSO in the Oracle PeopleSoft console

To enable SSO in the Oracle PeopleSoft environment:

1. Sign in to the PeopleSoft Console `http://{your-peoplesoft-fqdn}:8000/psp/ps/?cmd=start` using Admin credentials, for example, PS/PS.
2. Add a default public access user to PeopleSoft.
3. From the main menu, navigate to **PeopleTools > Security > User Profiles > User Profiles > Add a New Value**.
4. Select **Add a new value**.
5. Create user **PSPUBUSER**.
6. Enter the password.

    

7. Select the **ID** tab.
8. For **ID Type**, select **None**.

    

3. Navigate to **PeopleTools > Web Profile > Web Profile Configuration > Search > PROD > Security**.
4. Under **Public Users**, select the **Allow Public Access** box.
5. For **User ID**, enter **PSPUBUSER**.
6. Enter the password.

    

7. Select **Save**.
8. To enable SSO, navigate to **PeopleTools > Security > Security Objects > Signon PeopleCode**.
9. Select the **Sign on PeopleCode** page.
10. Enable **OAMSSO_AUTHENTICATION**.
11. Select **Save**.
12. To configure PeopleCode using the PeopleTools application designer, navigate to **File > Open > Definition: Record > Name: `FUNCLIB_LDAP`**.
13. Open **FUNCLIB_LDAP**.

    

14. Select the record.
15. Select **LDAPAUTH > View PeopleCode**.
16. Search for the `getWWWAuthConfig()` function `Change &defaultUserId = ""; to &defaultUserId = PSPUBUSER`.
17. Confirm the user Header is `PS_SSO_UID` for `OAMSSO_AUTHENTICATION` function. 
18. Save the record definition.

    

## Test an Oracle PeopleSoft application

To test an Oracle PeopleSoft application, validate application headers, policy, and overall testing. If needed, use header and policy simulation to validate header fields and policy execution.

To confirm Oracle PeopleSoft application access occurs correctly, a prompt appears to use a Microsoft Entra account for sign-in. Credentials are checked and the Oracle PeopleSoft appears.

## Next steps

- Video: [Enable SSO and MFA for Oracle JD Edwards with Microsoft Entra ID via Datawiza](https://www.youtube.com/watch?v=_gUGWHT5m90)
- [Tutorial: Configure Secure Hybrid Access with Microsoft Entra ID and Datawiza](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/datawiza-configure-sha)
- Go to docs.datawiza.com for Datawiza [User Guides](https://docs.datawiza.com/)
