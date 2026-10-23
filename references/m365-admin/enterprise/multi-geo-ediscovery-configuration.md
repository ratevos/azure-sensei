# Configure Microsoft 365 Multi-Geo eDiscovery

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-ediscovery-configuration  
> Microsoft doc last updated: 12/02/2025


[eDiscovery premium features](https://learn.microsoft.com/en-us/purview/edisc) allow a Multi-Geo eDiscovery administrator to search all of the _Geographies_ without needing to use a "Region" security filter. Data is exported to the Azure instance of the _Primary Provisioned Geography_ location of the multi-geo _Tenant_.

Without eDiscovery premium features enabled, an eDiscovery manager or administrator of a Multi-Geo _Tenant_ can conduct eDiscovery only in the _Primary Provisioned Geography_ location of that _Tenant_. To support the ability to conduct eDiscovery for _Satellite Geography_ locations, a new compliance security filter parameter named "Region" is available through PowerShell. This parameter can be used by _Tenants_ whose _Primary Provisioned Geography_ location is in North America, Europe, or Asia Pacific. eDiscovery with premium features is required for _Tenants_ whose _Primary Provisioned Geography_ location isn't in North America, Europe, or Asia Pacific and who need to perform eDiscovery across _Satellite Geography_ locations.

A member of the **Organization Management** role group or a user with the **Role Management** role must assign eDiscovery Manager permissions in the Microsoft Purview portal to allow others to perform eDiscovery tasks and assign a "Region" parameter in their applicable Compliance Security Filter to specify the _Geography_ for conducting eDiscovery as _Satellite Geography_ location. Otherwise, no eDiscovery activities occur for the _Satellite Geography_ location. Only one "Region" security filter per user is supported. See [Assign eDiscovery permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/edisc-permissions) for more information.

When you set the eDiscovery Manager or Administrator role for a particular _Satellite Geography_ location, the eDiscovery Manager or Administrator can only perform eDiscovery search actions against the SharePoint sites and OneDrive sites located in that _Satellite Geography_ location. If an eDiscovery Manager or Administrator attempts to search SharePoint or OneDrive sites outside the specified _Satellite Geography_ location, no results are returned. Also, when the eDiscovery Manager or Administrator for a _Satellite Geography_ location triggers an export, data is exported to the Azure instance of that region. This helps organizations stay in compliance by not allowing content to be exported across controlled borders.

> [!NOTE]
> If an eDiscovery Manager needs to search across multiple SharePoint _Satellite Geography_ locations, create another user account for the eDiscovery Manager that specifies the alternate _Satellite Geography_ location where the OneDrive or SharePoint sites are located.

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

To set the Compliance Security Filter for a Region:

1. [Connect to Microsoft 365 Security & Compliance PowerShell](https://learn.microsoft.com/en-us/powershell/exchange/connect-to-scc-powershell)

1. Use the following syntax:

   ```powershell
   New-ComplianceSecurityFilter -Action All -FilterName <TheNameYouWantToAssign> -Region <RegionValue> -Users <UserPrincipalName>
   ```

   For example:

   ```powershell
   New-ComplianceSecurityFilter -Action All -FilterName "NAM eDiscovery Managers" -Region NAM -Users adwood@contoso.onmicrosoft.com
   ```

See the [New-ComplianceSecurityFilter](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/new-compliancesecurityfilter) article for more parameters and syntax.
