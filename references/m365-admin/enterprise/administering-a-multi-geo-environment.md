# Service Behavior in a Multi-Geo Enabled Environment

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/administering-a-multi-geo-environment  
> Microsoft doc last updated: 05/09/2025


Here's a look at how Microsoft 365 services work in a Multi-Geo environment.

## Administrator experience

The SharePoint admin center has a [**Geo locations** tab](https://go.microsoft.com/fwlink/?linkid=2185076) in the left navigation that features a geo locations map where you can view and manage your geo locations. Use this page to add or delete geo locations for your _Tenant_.

## Audit log search

A unified [Audit log](https://support.office.com/article/0d4d0f35-390b-4518-800e-0c7ec95e946c) for all your _Satellite Geography_ locations is available from the Microsoft 365 audit log search page. You can see all the audit log entries from across geo locations, for example, NAM & EUR users' activities will show up in one org view and then you can apply existing filters to see specific user's activities.

## BCS, Secure Store, Apps

BCS, Secure Store, and Apps all have separate instances in each satellite location, and therefore the SharePoint administrator should manage and configure these services separately from each satellite location.

## Compliance admin center

There's one central Microsoft Purview portal for a Multi-Geo _Tenant_: [Microsoft Purview portal](https://purview.microsoft.com/).

## eDiscovery

By default, an eDiscovery Manager or Administrator of a Multi-Geo _Tenant_ will be able to conduct eDiscovery tasks only in the _Primary Provisioned Geography_ of that _Tenant_. A member of the **Organization Management** role group or a user with the **Role Management** role must assign eDiscovery Manager permissions in the Microsoft Purview portal to allow others to perform eDiscovery tasks and assign a "Region" parameter in their applicable Compliance Security Filter to specify the _Geography_ for conducting eDiscovery as _Satellite Geography_ location. Otherwise, no eDiscovery activities will be carried out for the _Satellite Geography_ location. Only one "Region" security filter per user is supported.

See [Assign eDiscovery permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/ediscovery-assign-permissions#before-you-assign-permissions) for more information. To configure the Compliance Security Filter for a Region, see [Configure Office 365 Multi-Geo eDiscovery](https://learn.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-ediscovery-configuration).

## Exchange Online mailboxes

Users' Exchange Online mailboxes are moved automatically if their PDL is changed. When a new mailbox is created, it's provisioned to the user's PDL or to the central location if no value has been set for the user's PDL.

## Information Protection (IP) Data Loss Prevention (DLP) policy

You can set your IP DLP policies for OneDrive, SharePoint, and Exchange Online in the Security and Compliance center, scoping policies as needed to the whole _Tenant_ or to applicable users. For example: If you wish to select a policy for a user in a satellite location, select to apply the policy to a specific OneDrive and enter the user's OneDrive URL. See [Overview of data loss prevention policies](https://support.office.com/article/1966b2a7-d1e2-4d92-ab61-42efbb137f5e) for general guidance in creating DLP policies.

The DLP policies are automatically synchronized based on their applicability to each geo location.

Implementing Information Protection and Microsoft Purview Data Loss Prevention policies to all users in a geo location isn't an option available in the UI, instead you must select the applicable accounts for the policy or apply the policy globally to all accounts.

## Microsoft Power Apps

Power Apps created for the satellite location will use the end point located in the central location for the _Tenant_. Microsoft Power Apps isn't a Multi-Geo service. 

## Microsoft Power Automate

Flows created for the satellite location will use the end point located in the default geo location for the _Tenant_. Microsoft Power Automate isn't a Multi-Geo service. 

## SharePoint storage quota

By default, all geo locations of a multi-geo environment share the available _Tenant_ storage quota. You can also manage the storage quota by allocating a specific quota for a particular geo location. For more information, see [SharePoint storage quotas in multi-geo environments](https://learn.microsoft.com/en-us/microsoft-365/enterprise/sharepoint-multi-geo-storage-quota).

## Sharing

Administrators can set and manage sharing policies for each of their locations. The OneDrive and SharePoint sites in each geo location will honor only the corresponding geo-specific sharing settings. (For example, you can allow [external sharing](https://support.office.com/article/C8A462EB-0723-4B0B-8D0A-70FEAFE4BE85) for your central location, but not for your satellite location or vice versa.) Note that the sharing settings don't allow configuring sharing limitations between geo locations.

## Microsoft Stream

Videos uploaded to Microsoft Stream in a 1:1 chat are stored in the OneDrive of the person uploading. Meeting recordings are stored in the OneDrive of each attendee who records the meeting.

## Taxonomy

We support a unified [taxonomy](https://learn.microsoft.com/en-us/sharepoint/managed-metadata) for enterprise-managed metadata across geo locations, with the master being hosted in the central location for your company. We recommend that you manage your global taxonomy from the central location and only add location-specific terms to the satellite location's Taxonomy. Global taxonomy terms will synchronize to the satellite locations.

See [Manage metadata in a Multi-Geo tenant](https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/multigeo-managedmetadata) for more details and for developer guidance.

## User Profile Application

There's a [user profile application](https://learn.microsoft.com/en-us/sharepoint/manage-user-profiles) in each geo location. Each user's profile information is hosted in their geo location and available to the administrator for that geo location.

If you have custom profile properties, then we recommend that you use the same profile schema across geographies and populate your custom profile properties either in all geo locations or where needed. For guidance regarding how to populate user profile data programmatically, please refer to the [Bulk User Profile Update API](https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/bulk-user-profile-update-api-for-sharepoint-online).

See [Work with user profiles in a Multi-Geo tenant](https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/multigeo-userprofileexperience) for additional details and for developer guidance.

## Viva Engage

Viva Engage isn't a Multi-Geo workload. Viva Engage threads stored in Viva Engage will be placed in the _Tenant's_ central location. Viva Engage is rolling out a file storage change which will store Viva Engage files within SharePoint. Viva Engage files stored in SharePoint will be placed the SharePoint site associated with the Viva Engage group. SharePoint group sites are based on PDL logic as outlined in [SharePoint Sites and Groups](https://learn.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-capabilities-in-onedrive-and-sharepoint-online-in-microsoft-365#sharepoint-sites-and-groups).
