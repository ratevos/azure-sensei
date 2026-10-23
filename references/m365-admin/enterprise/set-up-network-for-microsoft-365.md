# Set up your network for Microsoft 365

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/set-up-network-for-microsoft-365  
> Microsoft doc last updated: 09/23/2025


*This article applies to both Microsoft 365 Enterprise and Office 365 Enterprise.*

An important part of your Microsoft 365 onboarding is to ensure that your network and Internet connections are set up for optimized access. Configuring your on-premises network to access a globally distributed Software-as-a-Service (SaaS) cloud is different from a traditional network that is optimized for traffic to on-premises datacenters and a central Internet connection.

Use these articles to understand the key differences and to modify your edge devices, client computers, and on-premises network to get the best performance for your on-premises users.

## How Microsoft 365 networking works

See these articles for an overview of connectivity for Microsoft 365:

- [Microsoft 365 networking connectivity overview](https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-networking-overview)
- [Microsoft 365 network connectivity principles](https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-network-connectivity-principles)
- [Assessing Microsoft 365 network connectivity](https://learn.microsoft.com/en-us/microsoft-365/enterprise/assessing-network-connectivity)

For advice on enhancing performance, see [Network planning and performance tuning for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/enterprise/network-planning-and-performance).

## Support Microsoft 365 networking as a network equipment vendor

If you are a network equipment vendor, join the [Microsoft 365 Networking Partner Program](https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-networking-partner-program). Enroll in the program to build Microsoft 365 network connectivity principles into your products and solutions.

> [!NOTE]
> The Microsoft 365 Network Provider program is no longer open for new network providers.

## Microsoft 365 endpoints
Endpoints are the set of destination IP addresses, DNS domain names, and URLs for Microsoft 365 traffic on the Internet.

To optimize performance to Microsoft 365 cloud-based services, some endpoints need special handling by your client browsers and the devices in your edge network. These devices include firewalls, SSL Break and Inspect and packet inspection devices, and data loss prevention systems.

See [Managing Microsoft 365 endpoints](https://learn.microsoft.com/en-us/microsoft-365/enterprise/managing-office-365-endpoints) for the details.

There are currently five different Microsoft 365 clouds. This table takes you to the list of endpoints for each one.

| Endpoints | Description |
|:-------|:-----|
| [Worldwide endpoints](https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges) | The endpoints for worldwide Microsoft 365 subscriptions, which include the United States Government Community Cloud (GCC). |
| [U.S. Government DoD endpoints](https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-u-s-government-dod-endpoints) | The endpoints for United States Department of Defense (DoD) subscriptions. |
| [U.S. Government GCC High endpoints](https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-u-s-government-gcc-high-endpoints) | The endpoints for United States Government Community Cloud High (GCC High) subscriptions. |
| [Microsoft 365 operated by 21Vianet endpoints](https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges-21vianet) | The endpoints for Microsoft 365 operated by 21Vianet, which is designed to meet the needs for Microsoft 365 in China. |
|||

To automate getting the latest list of endpoints for your Microsoft 365 cloud, see the [Microsoft 365 IP Address and URL Web service](https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-ip-web-service).

For additional endpoints, see these articles:

- [Additional endpoints not included in the Web service](https://learn.microsoft.com/en-us/microsoft-365/enterprise/additional-office365-ip-addresses-and-urls)
- [Network requests in Office 2016 for Mac](https://learn.microsoft.com/en-us/microsoft-365/enterprise/network-requests-in-office-2016-for-mac)

## Additional topics for Microsoft 365 networking

See these articles for specialized topics in Microsoft 365 networking:

- [Content delivery networks](https://learn.microsoft.com/en-us/microsoft-365/enterprise/content-delivery-networks)
- [IPv6 support in Microsoft 365 services](https://learn.microsoft.com/en-us/microsoft-365/enterprise/ipv6-support)
- [NAT support with Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/enterprise/nat-support-with-microsoft-365)

## ExpressRoute for Microsoft 365

See these articles for information on the use of ExpressRoute for Microsoft 365 traffic:

- [Azure ExpressRoute for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/enterprise/azure-expressroute)

> [!NOTE]
> We **do not recommend** ExpressRoute for Microsoft 365 because it does not provide the best connectivity model for the service in most circumstances. As such, Microsoft authorization is required to use this connectivity model. We review every customer request and authorize ExpressRoute for Microsoft 365 only in the rare scenarios where it is necessary. Please read the [ExpressRoute for Microsoft 365 guide](https://www.microsoft.com/download/details.aspx?id=102899) for more information and following a comprehensive review of the document with your productivity, network, and security teams, work with your Microsoft account team to submit an exception if needed.
