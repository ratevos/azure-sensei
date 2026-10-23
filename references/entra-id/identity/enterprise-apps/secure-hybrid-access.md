# Secure hybrid access, protect legacy apps with Microsoft Entra ID

> Source: https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/secure-hybrid-access  
> Microsoft doc last updated: 01/17/2023


In this article, learn to protect your on-premises and cloud legacy authentication applications by connecting them to Microsoft Entra ID.

* **[Application Proxy](#secure-hybrid-access-with-application-proxy)**:
  * [Remote access to on-premises applications through Microsoft Entra application proxy](https://learn.microsoft.com/en-us/entra/identity/app-proxy)
  * Protect users, apps, and data in the cloud and on-premises 
  * [Use it to publish on-premises web applications externally](https://learn.microsoft.com/en-us/entra/identity/app-proxy/overview-what-is-app-proxy)
  
* **[Secure hybrid access through Microsoft Entra ID partner integrations](#partner-integrations-for-apps-on-premises-and-legacy-authentication)**:

  * [Pre-built solutions](#secure-hybrid-access-through-azure-ad-partner-integrations)
  * [Apply Conditional Access policies per application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/secure-hybrid-access-integrations#apply-conditional-access-policies)
 
In addition to Application Proxy, you can strengthen your security posture with [Microsoft Entra Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview) and [Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection). 

<a name='single-sign-on-and-multi-factor-authentication'></a>

## Single sign-on and multifactor authentication

With Microsoft Entra ID as an identity provider (IdP), you can use modern authentication and authorization methods like [single sign-on (SSO)](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/what-is-single-sign-on) and [Microsoft Entra multifactor authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-howitworks) to secure legacy, on-premises applications.

## Secure hybrid access with Application Proxy

Use Application Proxy to protect users, apps, and data in the cloud, and on premises. Use this tool for secure remote access to on-premises web applications. Users don’t need to use a virtual private network (VPN); they connect to applications from devices with SSO. 

Learn more:

* [Remote access to on-premises applications through Microsoft Entra application proxy](https://learn.microsoft.com/en-us/entra/identity/app-proxy)
* [Tutorial: Add an on-premises application for remote access through Application Proxy in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/app-proxy/application-proxy-add-on-premises-application)
* [How to configure SSO to an Application Proxy application](https://learn.microsoft.com/en-us/entra/identity/app-proxy/how-to-configure-sso)
* [Using Microsoft Entra application proxy to publish on-premises apps for remote users](https://learn.microsoft.com/en-us/entra/identity/app-proxy/overview-what-is-app-proxy)

### Application publishing and access management

Use Application Proxy remote access as a service to publish applications to users outside the corporate network. Help improve your cloud access management without requiring modification to your on-premises applications. Plan a [Microsoft Entra application proxy deployment](https://learn.microsoft.com/en-us/entra/identity/app-proxy/conceptual-deployment-plan).

## Partner integrations for apps: on-premises and legacy authentication

Microsoft partners with various companies that deliver pre-built solutions for on-premises applications, and applications that use legacy authentication. The following diagram illustrates a user flow from sign-in to secure access to apps and data.

   

<a name='secure-hybrid-access-through-azure-ad-partner-integrations'></a>

<a name='secure-hybrid-access-through-microsoft-entra-partner-integrations'></a>

### Secure hybrid access through Microsoft Entra ID partner integrations

The following partners offer solutions to support [Conditional Access policies per application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/secure-hybrid-access-integrations#apply-conditional-access-policies). Use the tables in the following sections to learn about the partners and Microsoft Entra integration documentation.

|Partner|Integration documentation|
|---|---|
|Akamai Technologies|[Tutorial: Microsoft Entra SSO integration with Akamai](https://learn.microsoft.com/en-us/entra/identity/saas-apps/akamai-tutorial)|
|Citrix Systems, Inc.|[Tutorial: Microsoft Entra SSO integration with Citrix ADC SAML Connector for Microsoft Entra ID (Kerberos-based authentication)](https://learn.microsoft.com/en-us/entra/identity/saas-apps/citrix-netscaler-tutorial)|
|Cloudflare, Inc.|[Tutorial: Configure Cloudflare with Microsoft Entra ID for secure hybrid access](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/cloudflare-integration)|
|Datawiza|[Tutorial: Configure Secure Hybrid Access with Microsoft Entra ID and Datawiza](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/datawiza-configure-sha)|
|F5, Inc.|[Integrate F5 BIG-IP with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/f5-integration)</br>[Tutorial: Configure F5 BIG-IP SSL-VPN for Microsoft Entra SSO](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/f5-passwordless-vpn)|
|Progress Software Corporation, Progress Kemp|[Tutorial: Microsoft Entra SSO integration with Kemp LoadMaster Microsoft Entra integration](https://learn.microsoft.com/en-us/entra/identity/saas-apps/kemp-tutorial)|
|Perimeter 81 Ltd.|[Tutorial: Microsoft Entra SSO integration with Perimeter 81](https://learn.microsoft.com/en-us/entra/identity/saas-apps/perimeter-81-tutorial)|
|Silverfort|[Tutorial: Configure Secure Hybrid Access with Microsoft Entra ID and Silverfort](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/silverfort-integration)|
|Strata Identity, Inc.|[Integrate Microsoft Entra SSO with Maverics Identity Orchestrator SAML Connector](https://learn.microsoft.com/en-us/entra/identity/saas-apps/maverics-identity-orchestrator-saml-connector-tutorial)|

#### Partners with pre-built solutions and integration documentation

|Partner|Integration documentation|
|---|---|
|Amazon Web Service, Inc.|[Tutorial: Microsoft Entra SSO integration with AWS ClientVPN](https://learn.microsoft.com/en-us/entra/identity/saas-apps/aws-clientvpn-tutorial)|
|Check Point Software Technologies Ltd.|[Tutorial: Microsoft Entra single SSO integration with Check Point Remote Secure Access VPN](https://learn.microsoft.com/en-us/entra/identity/saas-apps/check-point-remote-access-vpn-tutorial)|
|Cisco Systems, Inc.|[Tutorial: Microsoft Entra SSO integration with Cisco Secure Firewall - Secure Client](https://learn.microsoft.com/en-us/entra/identity/saas-apps/cisco-secure-firewall-secure-client)|
|Fortinet, Inc.|[Tutorial: Microsoft Entra SSO integration with FortiGate SSL VPN](https://learn.microsoft.com/en-us/entra/identity/saas-apps/fortigate-ssl-vpn-tutorial)|
|Palo Alto Networks|[Tutorial: Microsoft Entra SSO integration with Palo Alto Networks Admin UI](https://learn.microsoft.com/en-us/entra/identity/saas-apps/paloaltoadmin-tutorial)|
|Pulse Secure|[Tutorial: Microsoft Entra SSO integration with Pulse Connect Secure (PCS)](https://learn.microsoft.com/en-us/entra/identity/saas-apps/pulse-secure-pcs-tutorial)</br>[Tutorial: Microsoft Entra SSO integration with Pulse Secure Virtual Traffic Manager](https://learn.microsoft.com/en-us/entra/identity/saas-apps/pulse-secure-virtual-traffic-manager-tutorial)|
|Zscaler, Inc.|[Tutorial: Integrate Zscaler Private Access with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/saas-apps/zscalerprivateaccess-tutorial)|

## Next steps 
Select a partner in the tables mentioned to learn how to integrate their solution with Microsoft Entra ID.
