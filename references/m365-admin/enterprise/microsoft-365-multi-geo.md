# Microsoft 365 Multi-Geo

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-multi-geo  
> Microsoft doc last updated: 09/26/2025


The _Microsoft 365 Multi-Geo Capabilities add-on_ ("_Multi-Geo_") provides enterprise customers with the ability to expand their Microsoft 365 presence to multiple geographic regions ("_Geographies_") within a single existing Microsoft 365 _Tenant_. Customers must license _Multi-Geo_ through the Enterprise Agreement, Web Direct, or CSP channels.

_Multi-Geo_ is intended for enterprise customers who need to store data in multiple _Geographies_ to satisfy data residency requirements, while retaining single-tenant administration and full-fidelity collaboration experiences between users as necessary.

_Multi-Geo_ enables customers to manage and store in-scope data at a user level for _Microsoft 365 Core Services_ including Exchange Online, SharePoint/OneDrive, Microsoft Teams, and Microsoft 365 Copilot and Copilot Chat. In addition, _Multi-Geo_ can be used with shared resources including SharePoint sites, Microsoft 365 Groups, Shared Mailboxes, eDiscovery, or Microsoft Teams teams.

Customers that utilize Microsoft Purview eDiscovery Standard or Premium should refer to [Microsoft 365 Multi-Geo eDiscovery configuration](https://learn.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-ediscovery-configuration) and [Set up compliance boundaries for eDiscovery investigations](https://learn.microsoft.com/en-us/purview/ediscovery-set-up-compliance-boundaries#searching-and-exporting-content-in-multi-geo-environments) for additional information on region usage and data storage as it relates to Microsoft Purview eDiscovery.

Customers that require performance optimization for Microsoft 365 should refer to [Network planning and performance tuning for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/enterprise/network-planning-and-performance) or contact their Support group.

> [!NOTE]
> Exchange Online, SharePoint, OneDrive, Microsoft Teams, and Microsoft 365 Copilot and Copilot Chat are available for _Multi-Geo_ configuration. For more information about data residency commitments, see [Exchange Online](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-service-exo), [SharePoint and OneDrive](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-service-spo), [Microsoft Teams](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-service-teams#data-residency-commitments-available), and [Microsoft 365 Copilot and Copilot Chat](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-service-copilot) for more details.

For a video introduction on _Microsoft 365 Multi-Geo_, see [SharePoint and OneDrive Multi-Geo to control where your data resides](https://www.youtube.com/watch?v=Do9U3JuROhk).

## Multi-Geo architecture

In a _Multi-Geo_ environment, a Microsoft 365 _Tenant_ consists of a _Primary Provisioned Geography_ (where a customer's Microsoft 365 subscription was originally provisioned) _and_ one or more _Satellite Geography_ locations. In a _Multi-Geo_ enabled _Tenant_, the information about _Geography_ locations, groups, and user information, is mastered in _Microsoft Entra ID_. Because a customer's _Tenant_ information is mastered centrally and synchronized into each _Geography_ location, sharing and experiences involving anyone from a customer's organization contain global awareness.

## Licensing

_Microsoft 365 Multi-Geo_ is available as an add-on to the following Microsoft 365 subscription plans:

- Microsoft 365 F1, F3, E3, or E5 (including SKUs without Microsoft Teams)
- Office 365 F3, E1, E3, or E5 (including SKUs without Microsoft Teams)
- Exchange Online Plan 1 or Plan 2
- OneDrive Plan 1 or Plan 2
- SharePoint Plan 1 or Plan 2
- Microsoft Teams Enterprise, EEA, or Essentials

### Minimum Licensing

Enterprise Agreement customers must purchase a quantity of _Multi-Geo_ licenses _equal to or greater than_ 5% of their total eligible Microsoft 365 users. Similarly, CSP partners must purchase and assign a quantity of _Multi-Geo_ licenses _equal to or greater than_ 5% of their customers' total eligible Microsoft 365 users. For enterprise customers, user subscription licenses must be on the same Enterprise Agreement as the Multi-Geo Services licenses. Customers should contact their Microsoft account team for details.

**Note that Small Business products do not currently qualify for _Multi-Geo_, even if they contain elements of the above list.**

_Multi-Geo Capabilities_ in Microsoft 365 is a user-level add-on license. Customers need a license for each user that they want to host in a _Satellite Geography_ location. Customers can add more licenses over time as they add users in _Satellite Geography_ locations.

There are no _Multi-Geo_ licenses specific to shared resources such as SharePoint Sites, Microsoft 365 Groups, Shared Mailboxes, or Microsoft Teams teams. If enough _Multi-Geo_ user licenses have been acquired, then customers are eligible to use _Multi-Geo_ with shared resources without limitation.

## Microsoft 365 Multi-Geo availability

_Microsoft 365 Multi-Geo_ is currently offered in these _Geographies_:

| Microsoft 365 Geography | PreferredDataLocation (PDL) Value |
|:-|:-|
| South Korea, Japan, Singapore, Malaysia, Hong Kong Special Administrative Region | APC |
| Australia | AUS |
| Austria | AUT |
| Brazil | BRA |
| Canada | CAN |
| Chile | CHL |
| Denmark | DNK |
| France, Netherlands, Ireland, Norway, Switzerland, Austria, Finland, Sweden, Germany | EUR |
| France | FRA |
| Germany | DEU |
| India | IND |
| Indonesia | IDN |
| Israel | ISR |
| Italy | ITA |
| Japan | JPN |
| Korea | KOR |
| Malaysia | MYS |
| Mexico | MEX |
| New Zealand | NZL |
| Norway | NOR |
| Poland | POL |
| Qatar | QAT |
| South Africa | ZAF |
| Spain | ESP |
| Sweden | SWE |
| Switzerland | CHE |
| Taiwan | TWN |
| United Arab Emirates | ARE |
| United Kingdom | GBR |
| United States | NAM |

> [!NOTE]
> To use a security filter for Italy, New Zealand, Spain, or Sweden in eDiscovery, you must have [premium features in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-settings-general) enabled.

To learn more about the definition of each _Geography_, such as what countries or cities contain the data centers, see [Overview and Definitions](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-overview).

## Getting started

Whether you are a CSP partner managing your customer’s Microsoft 365 subscriptions or an Enterprise Agreement customer managing your own subscriptions, you can follow these steps to get started with _Multi-Geo_:

1. Ensure that you purchase _Multi-Geo_ for at least 5% of the total eligible users in your Microsoft 365 subscription. Remember that you'll need a license for each user you want to host in a _Satellite Geography_ location.

2. Before you can start using _Microsoft 365 Multi-Geo_, Microsoft needs to configure your _Tenant_ for _Multi-Geo_ support. This one-time automatic configuration process is triggered after you order the _Multi-Geo Capabilities_ in Microsoft 365 and the licenses show up in your _Tenant_. You'll receive service-specific notifications in the [Microsoft 365 message center](https://support.office.com/article/38FB3333-BFCC-4340-A37B-DEDA509C2093) once the _Tenant_ has completed the configuration process for each service, and then you may begin configuring and using your _Microsoft 365 Multi-Geo Capabilities_. The time required to configure a _Tenant_ for _Multi-Geo_ support varies from _Tenant_ to _Tenant_, but most _Tenants_ finish within a month after receipt of the feature licenses. Larger or more complex _Tenants_ may require more time to complete the configuration process.

3. Read [Plan your multi-geo environment](https://learn.microsoft.com/en-us/microsoft-365/enterprise/plan-for-multi-geo).

4. Learn about [administering a multi-geo environment](https://learn.microsoft.com/en-us/microsoft-365/enterprise/administering-a-multi-geo-environment) and [how your users will experience the environment](https://learn.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-user-experience).

5. When you're ready to set up Microsoft 365 Multi-Geo, [configure your tenant for multi-geo](https://learn.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-tenant-configuration).

6. [Set up search](https://learn.microsoft.com/en-us/microsoft-365/enterprise/configure-search-for-multi-geo).
  
> [!NOTE]
> For more information on the Microsoft 365 services that support _Multi-Geo_, see the [EXO](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-service-exo), [ODSP](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-service-spo), [Teams](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-service-teams), and [Microsoft 365 Copilot and Copilot Chat](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-service-copilot) service data residency pages for more details.

## See also

[Multi-Geo in Exchange Online and OneDrive](https://Aka.ms/GoMultiGeo)

[Multi-Geo Capabilities in OneDrive and SharePoint](https://learn.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-capabilities-in-onedrive-and-sharepoint-online-in-microsoft-365)

[Multi-Geo Capabilities in Exchange Online](https://learn.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-capabilities-in-exchange-online)

[Teams experience in a multi-geo environment](https://learn.microsoft.com/en-us/microsoftteams/teams-experience-o365odb-spo-multi-geo)
