# Microsoft 365 Usage Analytics Data Model

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/usage-analytics/usage-analytics-data-model  
> Microsoft doc last updated: 03/12/2026


## Data for the Microsoft 365 usage analytics tables

The Microsoft 365 usage analytics data model connects to an API that exposes multidimensional data about service usage and adoption. The APIs that Microsoft 365 usage analytics uses to generate its data come from various generally available Graph APIs. The Microsoft 365 usage analytics API itself isn't generally available.

> [!NOTE]
>
> For more information, see [Working with Microsoft 365 usage reports in Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/resources/report).

This API provides information about the monthly trend of usage of the various Microsoft 365 services. For the exact data returned by the API, see the table in the following section.

## Data tables returned by the Microsoft 365 reporting API

| **Table name**                      | **Information in the table** | **Date range** |
| ----------------------------------  | ---------------------------- | -------------- |
| **Tenant Product Usage**            | Monthly totals of:<ul><li>Enabled users.</li><li>Active users.</li><li>Month-over-month retained users.</li><li>First-time users.</li><li>Cumulative active users.</li></ul> | Monthly aggregated data for a rolling 12‑month period, including the current partial month. |
| **Tenant Product Activity**         | Monthly totals of activities and active user counts for product activities.<br><br>For more information about the activities returned in this table, see [Active user in Microsoft 365 usage reports](https://learn.microsoft.com/en-us/microsoft-365/admin/usage-analytics/active-user-in-usage-reports). | Monthly aggregated data for a rolling 12‑month period, including the current partial month. |
| **Tenant Office Licenses**          | Number of Microsoft Office subscriptions assigned to users. | End‑of‑month state data for a rolling 12‑month period, including the current partial month. |
| **Tenant Mailbox Usage**            | Mailbox data, including:<ul><li>Total mailbox count.</li><li>Storage usage.</li></ul> | End‑of‑month state data for a rolling 12‑month period, including the current partial month. |
| **Tenant Client Usage**             | Number of users actively using specific clients or devices to connect to:<ul><li>Exchange Online.</li><li>Teams.</li><li>Viva Engage.</li></ul> | Monthly aggregated data for a rolling 12‑month period, including the current partial month. |
| **Tenant SharePoint Usage**         | SharePoint site data, including:<ul><li>Total sites (Teams or Groups sites).</li><li>Number of documents.</li><li>File count by activity type.</li><li>Storage used.</li></ul> | End‑of‑month state data for a rolling 12‑month period, including the current partial month. |
| **Tenant OneDrive Usage**           | OneDrive account data, including:<ul><li>Number of accounts.</li><li>Number of documents across OneDrives.</li><li>Storage used.</li><li>File count by activity type.</li></ul> | End‑of‑month state data for a rolling 12‑month period, including the current partial month. |
| **Tenant Microsoft 365 Groups Usage** | Microsoft 365 Groups usage data, including:<ul><li>Mailbox.</li><li>SharePoint.</li><li>Viva Engage.</li></ul> | End‑of‑month state data for a rolling 12‑month period, including the current partial month. |
| **Tenant Office Activation**        | Office subscription activation data, including:<ul><li>Total activations.</li><li>Activations per device (Android, iOS, Mac, PC).</li><li>Activations by service plan (for example, Microsoft 365 Apps for enterprise, Visio, Project).</li></ul> | End‑of‑month state data for a rolling 12‑month period, including the current partial month. |
| **User State**                      | User metadata, including:<ul><li>Display name.</li><li>Assigned products.</li><li>Location.</li><li>Department.</li><li>Title.</li><li>Company.</li></ul>Includes users who were assigned a license during the last complete month. Each user has a unique user ID. | Users who had a license assigned during the last complete month. |
| **User Activity**                   | Per-user activity data for licensed users.<br><br>For more information about the activities returned in this table, see [Active user in Microsoft 365 usage reports](https://learn.microsoft.com/en-us/microsoft-365/admin/usage-analytics/active-user-in-usage-reports). | Users who performed an activity in any service during the last complete month. |

To see the detailed information for each data table, see the following sections.

### Data table - User State

The **User State** table provides user-level details for all users who have a license assigned during the last complete month. It brings in data from Microsoft Entra ID.

| **Name**                  | **Description**                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **UserId**                | Unique user ID that represents a user and enables joining with other data tables within the data set.                     |
| **Timeframe**             | Month value for which this table has data.                                                                                |
| **UPN**                   | User principal name (UPN) that uniquely identifies the user to join with other external data sources.                     |
| **DisplayName**           | User's display name.                                                                                                      |
| **IDType**                | Account user used to sign in. Values can be: <ul><li>1 if the user is a Viva Engage user who connects using their Viva Engage ID.</li><li>0 if the user connects to Viva Engage using their Microsoft 365 ID.</li></ul>                                                                    |
| **HasLicenseEXO**         | Set to true if the user is assigned a license and enabled to use Exchange on the last day of the month.                   |
| **HasLicenseODB**         | Set to true if the user is assigned a license and enabled to use OneDrive on the last day of the month.                   |
| **HasLicenseSPO**         | Set to true if the user is assigned a license and enabled to use SharePoint on the last day of the month.                 |
| **HasLicenseYAM**         | Set to true if the user is assigned a license and enabled to use Viva Engage on the last day of the month.                |
| **HasLicenseSFB**         | Set to true if the user is assigned a license and enabled to use Teams on the last day of the month.         |
| **HasLicenseTeams**       | Set to true if the user is assigned a license and enabled to use Microsoft Teams on the last day of the month.            |
| **Company**               | Company data represented in Microsoft Entra ID for this user.                                                             |
| **Department**            | Department data represented in Microsoft Entra ID for this user.                                                          |
| **LocationCity**          | City data represented in Microsoft Entra ID for this user.                                                                |
| **LocationCountry**       | Country/region data represented in Microsoft Entra ID for this user.                                                      |
| **LocationState**         | State data represented in Microsoft Entra ID for this user.                                                               |
| **LocationOffice**        | User's office.                                                                                                            |
| **Title**                 | Title data represented in Microsoft Entra ID for this user.                                                               |
| **Deleted**               | True if the user was deleted from Microsoft 365 in the last complete month.                                               |
| **DeletedDate**           | Date when the user was deleted from Microsoft 365.                                                                        |
| **YAM_State**             | State of the user in the Viva Engage system. Values can be: <ul><li>Active.</li><li>Deleted.</li><li>Suspended.</li></ul> |
| **YAM_ActivationDate**    | Date the user entered the state of being active in Viva Engage.                                                           |
| **YAM_DeletionDate**      | Date the user entered the state of being deleted in Viva Engage.                                                          |
| **YAM_SuspensionDate**    | Date the user entered the state of being suspended in Viva Engage.                                                        |

### Data table - User Activity

The **User Activity** table contains data about each user who had an activity in any of the services in the previous month.

| **Name**                          | **Description**                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **UserID**                        | Unique user ID that represents a user and enables joining with other data tables within the data set. |
| **Timeframe**                     | Month value for which this table represents data.                                                     |
| **EXO_EmailSent**                 | Number of emails sent.                                                                                |
| **EXO_EmailReceived**             | Number of emails received.                                                                            |
| **EXO_EmailRead**                 | Number of email read activities performed by the user. Includes:<ul><li>Multiple reads of the same email.</li><li>Emails received in previous periods.</li></ul> |
| **EXO_AppointmentCreated**        | Number of appointments created.                                                                       |
| **EXO_MeetingAccepted**           | Number of meetings accepted.                                                                          |
| **EXO_MeetingCancelled**          | Number of meetings canceled.                                                                          |
| **EXO_MeetingDeclined**           | Number of meetings declined.                                                                          |
| **EXO_MeetingSent**               | Number of meetings sent.                                                                              |
| **ODB_FileViewedModified**        | Number of files the user interacted with on any OneDrive. Includes the following actions:<ul><li>Create.</li><li>Update.</li><li>Delete.</li><li>View.</li><li>Download.</li></ul> |
| **ODB_FileSynched**               | Number of files the user synchronized on any OneDrive.                                                |
| **ODB_FileSharedInternally**      | Number of files shared internally from any OneDrive including sharing with users within groups.       |
| **ODB_FileSharedExternally**      | Number of files the user shared externally from any OneDrive.                                         |
| **ODB_AccessedByOwner**           | Number of OneDrive sites the user interacted with that they own.                                      |
| **ODB_AccessedByOthers**          | Number of OneDrive sites owned by another user that the user interacted with.                         |
| **SPO_GroupFileViewedModified**   | Number of files the user interacted with on any group site.                                           |
| **SPO_GroupFileSynched**          | Number of files the user synchronized on any group site.                                              |
| **SPO_GroupFileSharedInternally** | Number of files shared internally from any group site including sharing within groups.                |
| **SPO_GroupFileSharedExternally** | Number of files the user shared externally from any group site.                                       |
| **SPO_GroupAccessedByOwner**      | Number of group sites the user interacted with that they own.                                         |
| **SPO_GroupAccessedByOthers**     | Number of group sites owned by another user that the user interacted with.                            |
| **SPO_OtherFileViewedModified**   | Number of files the user interacted with on any other site.                                           |
| **SPO_OtherFileSynched**          | Number of files the user synchronized from any other site.                                            |
| **SPO_OtherFileSharedInternally** | Number of files shared internally from any other site including sharing within groups.                |
| **SPO_OtherFileSharedExternally** | Number of files the user shared externally from any other site.                                       |
| **SPO_OtherAccessedByOwner**      | Number of other sites the user interacted with that they own.                                         |
| **SPO_OtherAccessedByOthers**     | Number of other sites owned by another user that the user interacted with.                            |
| **SPO_TeamFileViewedModified**    | Number of files the user interacted with on any team site.                                            |
| **SPO_TeamFileSynched**           | Number of files the user synchronized from any team site.                                             |
| **SPO_TeamFileSharedInternally**  | Number of files shared internally from any team site including sharing within groups.                 |
| **SPO_TeamFileSharedExternally**  | Number of files the user shared externally from any team site.                                        |
| **SPO_TeamAccessedByOwner**       | Number of team sites the user interacted with that they own.                                          |
| **SPO_TeamAccessedByOthers**      | Number of team sites owned by another user that the user interacted with.                             |
| **Teams_ChatMessages**            | Number of chat messages sent.                                                                         |
| **Teams_ChannelMessage**          | Number of messages posted to channels.                                                                |
| **Teams_CallParticipate**         | Number of calls the user participated in.                                                             |
| **Teams_MeetingParticipate**      | Number of meetings the user joined.                                                                   |
| **Teams_HasOtherAction**          | Boolean value indicating whether the user performed other actions in Microsoft Teams. The user is considered active but has a zero value for the following items: <ul><li>Chat Messages.</li><li>1:1 calls.</li><li>Channel Messages.</li><li>Total Meetings.</li><li>Meetings organized.</li></ul> |
| **YAM_MessagePost**               | Number of Viva Engage messages the user posted.                                                       |
| **YAM_MessageLiked**              | Number of Viva Engage messages the user liked.                                                        |
| **YAM_MessageRead**               | Number of Viva Engage messages the user read.                                                         |
| **SFB_P2PSummary**                | Number of peer-to-peer sessions the user took part in.                                                |
| **SFB_ConfOrgSummary**            | Number of conference sessions the user organized.                                                     |
| **SFB_ConfPartSummary**           | Number of conference sessions the user participated in.                                               |

### Data table - Tenant Product Usage

The **Tenant Product Usage** table provides month-over-month adoption data in terms of the following types of user for each product within Microsoft 365:

- Enabled.
- Active.
- Returning
- First-time users.

The Microsoft 365 values represent active usage in any of the products.

| **Name**                  | **Description**                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Product**               | Name of products for which the usage information is summarized.<ul><li>The Microsoft 365 value represents activity across any of the products.</li></ul> |
| **Timeframe**             | Month value.<ul><li>One row per product per month.</li><li>Includes the last 12 months, including the current partial month.</li></ul>      |
| **EnabledUsers**          | Number of users enabled to use the product for the timeframe value.<ul><li>Users enabled for any portion of the month are counted.</li></ul>|
| **ActiveUsers**           | Number of users who performed an intentional activity in the product for the timeframe value.<ul><li>A user is counted as active if they performed one of the key product activities.</li><li>Key activities are listed in the **Tenant Product Activity** table.</li></ul> |
| **CumulativeActiveUsers** | Number of users enabled to use the product.<ul><li>Includes users who used the product at least once since data collection started.</li><li>Calculated up to and including the timeframe month.</li></ul> |
| **MoMReturningUsers**     | Number of users active in the timeframe month.<ul><li>Users must also be active during the previous month.</li></ul>                        |
| **FirstTimeUsers**        | Number of users who became active in the timeframe month for the first time.<ul><li>Activity is measured from the start of data collection in the new usage system.</li><li>Once a user is counted as a first-time user, the user is never counted again.</li></ul> |
| **Content Date**          | If the timeframe is:<ul><li> The current month, the latest date with available data.</li><li>A previous month, the last date of that month.</li></ul> |

### Data table - Tenant Product Activity

The **Tenant Product Activity** table provides monthly totals of activity and active user count for various activities within the products.

| **Name**                     | **Description**                                                                                                                                       |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Timeframe**                | Month value.<ul><li>One row per product per month.</li><li>Includes the last 12 months, including the current partial month.</li></ul>                |
| **Product**                  | Name of the product within Microsoft 365 for which usage data is available.                                                                           |
| **Activity**                 | Name of the activity in a product that is used to showcase active use of the product.                                                                 |
| **ActivityCount**            | Total number of actions counted for each activity across all active users.<ul><li>For SharePoint and OneDrive activities, this value represents the number of distinct documents users interacted with.</li></ul> |
| **ActiveUserCount**          | Number of users who performed the activity within the product.                                                                                        |
| **TotalDurationInMinute**    | Total duration, in minutes, across all active users.<ul><li>Applies to audio or video sessions in applicable Microsoft Teams activities.</li></ul>    |
| **Content Date**             | If the timeframe is:<ul><li> The current month, the latest date with available data.</li><li>A previous month, the last date of that month.</li></ul> |

### Data table - Tenant Mailbox Usage

The **Tenant Mailbox Usage** table shows summary data for all licensed Exchange Online users with a user mailbox. It shows the end of month state for all user mailboxes. You can't add the data in this table across multiple months. The latest month's data in this table shows the most recent state.

| **Name**                            | **Description**                                                                 |
| ----------------------------------- |-------------------------------------------------------------------------------- |
| **TotalMailboxes**                  | Number of user mailboxes for the Microsoft 365 subscription.                    |
| **IssueWarningQuota**               | Total quota for issuing warnings across all user mailboxes.                     |
| **ProhibitSendQuota**               | Total quota for prohibiting send actions across all user mailboxes.             |
| **ProhibitSendReceiveQuota**        | Total quota for prohibiting send and receive actions across all user mailboxes. |
| **TotalItemBytes**                  | Amount of storage used across all user mailboxes, in bytes.                     |
| **MailboxesNoWarning**              | Number of user mailboxes that are under the storage warning limit.              |
| **MailboxesIssueWarning**           | Number of user mailboxes that were issued a storage quota warning.              |
| **MailboxesExceedSendQuota**        | Number of user mailboxes that exceeded the send quota.                          |
| **MailboxesExceedSendReceiveQuota** | Number of user mailboxes that exceeded the send and receive quota.              |
| **DeletedMailboxes**                | Number of user mailboxes deleted in the timeframe.                              |
| **Timeframe**                       | Month value.                                                                    |
| **Content Date**                    | If the timeframe is:<ul><li> The current month, the latest date with available data.</li><li>A previous month, the last date of that month.</li></ul> |

### Data table - Tenant Client Usage

The **Tenant Client Usage** table provides month-over-month summary data about the clients that users use to connect to:

- Exchange Online.
- Microsoft Teams.
- Viva Engage.

This table doesn't yet have client use data for SharePoint and OneDrive.

| **Name**         | **Description**                                                                    |
| ---------------- | ---------------------------------------------------------------------------------- |
| **Product**      | Name of the product within Microsoft 365 for which client usage data is available. |
| **ClientId**     | Name of each device used to connect to the product.                                |
| **UserCount**    | Number of users who used each client for each product.                             |
| **Timeframe**    | Month value.                                                                       |
| **Content Date** | If the timeframe is:<ul><li> The current month, the latest date with available data.</li><li>A previous month, the last date of that month.</li></ul> |

### Data table - Tenant SharePoint Usage

The **Tenant SharePoint Usage** table shows month-over-month summary data about the usage or activity of SharePoint sites. The data in this table only covers Team Sites and Group sites and represents the end‑of‑month state of SharePoint sites:

- The values reflect the final totals at the end of the month, not interim activity.
- During the month, users might create, delete, and add files.
- Only the state at the end of the month is recorded.

In the following example, the resulting values shown are seven documents and 5 MB, which represent the end‑of‑month state:

- A user creates five documents that use 10 MB of storage.
- The user then deletes some files and adds others.
- At the end of the month, the site contains seven documents that use 5 MB of storage.

To avoid duplicate counts of aggregations, this table is hidden. It's used as a source to create two reference tables.

| **Name**                        | **Description**                                                                                   |
|-------------------------------- | ------------------------------------------------------------------------------------------------- |
| **SiteType**                    | Site type value. Possible values are:<ul><li>Any: Represents either team or group sites.</li><li>Team.</li><li>Group.</li></ul> |
| **TotalSites**                  | Number of sites that existed at the end of the timeframe.                                         |
| **DocumentCount**               | Total number of documents that existed on the site at the end of the timeframe.                   |
| **DiskUsed**                   | Total storage used, summed across all sites at the end of the timeframe.                           |
| **ActivityType**                | Number of sites that recorded specific types of file activity. Represents any file activity that was performed. For example:<ul><li>Any activity.</li><li>Active files.</li><li>Files shared externally.</li><li>Files shared internally.</li><li>Files synchronized.</li></ul> |
| **SitesWithOwnerActivities**    | Number of active sites where the site owner performed a file activity on their own site.<ul><li>The site owner is the person responsible for the site.</li><li>The site owner can be identified using the PowerShell command `get-sposite`.</li></ul> |
| **SitesWithNonOwnerActivities** | Number of active sites summed up for the month where users other than the site owner performed a file activity.<ul><li>The site owner is the person responsible for the site.</li><li>The site owner can be identified using the PowerShell command `get-sposite`.</li></ul> |
| **ActivityTotalSites**          | Number of sites that recorded any activity during the timeframe.<ul><li>Sites deleted by the end of the timeframe are still counted if they had activity earlier in the timeframe.</li></ul> |
| **Timeframe**                   | Date value.<ul><li>Used as a many‑to‑one relationship with the Calendar table.</li></ul>          |
| **Content Date**                | If the timeframe is:<ul><li> The current month, the latest date with available data.</li><li>A previous month, the last date of that month.</li></ul> |

### Data table - Tenant OneDrive Usage

The **Tenant OneDrive Usage** table provides data about the OneDrive accounts. For example:

- Number of accounts.
- Number of documents across OneDrive accounts.
- Storage used.
- File count by activity type.

The table also shows the end‑of‑month state of OneDrive accounts:

- The values reflect the final state at the end of the month, not changes made during the month.
- Users might create, delete, and add files throughout the month.
- Only the end‑of‑month totals are recorded in this table.

In the following example, the table records seven files and 5 MB, which represent the end‑of‑month state:

- A user creates five documents that use 10 MB of storage.
- During the month, the user deletes some files and adds others.
- By the end of the month, the account contains seven files that use 5 MB of storage.

| **Name**                        | **Description**                                                                                            |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **SiteType**                    | Value is <code>OneDrive</code>.                                                                            |
| **TotalSites**                  | Number of OneDrive accounts that exist at the end of the timeframe.                                        |
| **DocumentCount**               | Total number of documents that exist across all OneDrive accounts at the end of the timeframe.             |
| **DiskUsed**                   | Total storage used, summed across all OneDrive accounts at the end of the timeframe.                        |
| **ActivityType**                | Number of accounts that recorded specific types of file activity. For example:<ul><li>Any activity.</li><li>Active files.</li><li>Files shared externally.</li><li>Files shared internally.</li><li>Files synchronized.</li></ul> |
| **SitesWithOwnerActivities**    | Number of active OneDrive accounts where the account owner performed a file activity on their own account. |
| **SitesWithNonOwnerActivities** | Number of OneDrive accounts with file activity by users other than the owner.                              |
| **ActivityTotalSites**          | Number of OneDrive accounts that recorded any activity during the timeframe.<ul><li>Accounts deleted by the end of the timeframe are still counted if they had activity earlier in the timeframe.</li></ul> |
| **Timeframe**                   | Date value.<ul><li>Used as a many‑to‑one relationship with the Calendar table.</li></ul>                   |
| **Content Date**                | If the timeframe is:<ul><li> The current month, the latest date with available data.</li><li>A previous month, the last date of that month.</li></ul> |

### Data table - Tenant Microsoft 365 Groups Usage

The **Tenant Microsoft 365 Groups Usage** table provides data about how Microsoft 365 Groups is used across the organization.

| **Name**                                 | **Description**                                                                                                  |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------  |
| **TimeFrame**                            | Month value. There's one row per product per month for the last 12 months, including the current partial month.  |
| **GroupType**                            | Type of group (private, public, or any).                                                                         |
| **TotalGroups**                          | Number of groups in each group type.                                                                             |
| **ActiveGroups**                         | Number of active groups.                                                                                         |
| **MBX_TotalGroups**                      | Number of mailbox groups.                                                                                        |
| **MBX_ActiveGroups**                     | Number of active mailbox groups.                                                                                 |
| **MBX_TotalActivities**                  | Number of mailbox activities.                                                                                    |
| **MBX_TotalItems**                       | Number of mailbox items.                                                                                         |
| **MBX_StorageUsed**                      | Quantity of mailbox storage used.                                                                                |
| **SPO_TotalGroups**                      | Number of SharePoint groups.                                                                                     |
| **SPO_ActiveGroups**                     | Number of active SharePoint groups.                                                                              |
| **SPO_FileAccessedActiveGroups**         | Number of SharePoint groups that have file accessed activities.                                                  |
| **SPO_FileSyncedActiveGroups**           | Number of SharePoint groups that have file synchronized activities.                                              |
| **SPO_FileSharedInternallyActiveGroups** | Number of SharePoint groups that shared activities internally, or with groups that might include external users. |
| **SPO_FileSharedExternallyActiveGroups** | Number of SharePoint groups that shared activities externally.                                                   |
| **SPO_TotalActivities**                  | Number of SharePoint activities.                                                                                 |
| **SPO_FileAccessedActivities**           | Number of SharePoint file accessed activities.                                                                   |
| **SPO_FileSyncedActivities**             | Number of SharePoint file synchronized activities.                                                               |
| **SPO_FileSharedInternallyActivities**   | Number of SharePoint file shared activities internally, or with groups that might include external members.      |
| **SPO_FileSharedExternallyActivities**   | Number of SharePoint file shared activities externally.                                                          |
| **SPO_TotalFiles**                       | Number of SharePoint files.                                                                                      |
| **SPO_ActiveFiles**                      | Number of active SharePoint files.                                                                               |
| **SPO_StorageUsed**                      | Quantity of SharePoint storage used.                                                                             |
| **YAM_TotalGroups**                      | Number of Viva Engage groups.                                                                                    |
| **YAM_ActiveGroups**                     | Number of active Viva Engage groups.                                                                             |
| **YAM_LikedActiveGroups**                | Number of Viva Engage groups with like activity.                                                                 |
| **YAM_PostedActiveGroups**               | Number of Viva Engage groups with post activity.                                                                 |
| **YAM_ReadActiveGroups**                 | Number of Viva Engage groups with read activity.                                                                 |
| **YAM_TotalActivities**                  | Number of Viva Engage activities.                                                                                |
| **YAM_LikedActivities**                  | Number of Viva Engage like activities.                                                                           |
| **YAM_PostedActivities**                 | Number of Viva Engage post activities.                                                                           |
| **YAM_ReadActivities**                   | Number of Viva Engage read activities.                                                                           |

### Data table - Tenant Office Licenses

The **Tenant Office Licenses** table provides month-over-month summary data about the license assignment for users.

| **Name**          | **Description**              |
| ----------------- | ---------------------------- |
| **LicenseName**   | Name of the license.         |
| **AssignedCount** | Number of assigned licenses. |
| **Timeframe**     | Month value.                 |

### Data table - Tenant Office Activation

The **Tenant Office Activation** table provides data about the number of Office subscription activations across the service plans. For example:

- Microsoft 365 Apps for enterprises.
- Visio.
- Project.

It also provides data about the number of activations per device (Android, iOS, Mac, or PC).

| **Name**                | **Description**                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------- |
| **ServicePlanName**     | Name of the service plan.                                                                         |
| **TotalEnabled**        | Number of users enabled for the service plan by the end of the timeframe.                         |
| **TotalActivatedUsers** | Number of users who activated the service plan by the end of the timeframe.                       |
| **AndroidCount**        | Number of activations for the service plan on Android devices by the end of the timeframe.        |
| **iOSCount**            | Number of activations for the service plan on iOS devices by the end of the timeframe.            |
| **MacCount**            | Number of activations for the service plan on Mac devices by the end of the timeframe.            |
| **PcCount**             | Number of activations for the service plan on PC devices by the end of the timeframe.             |
| **WinRtCount**          | Number of activations for the service plan on Windows Mobile devices by the end of the timeframe. |
| **Timeframe**           | <ul><li>Date value.</li><li>Used as a many-to-one relationship with the Calendar table.</li></ul> |
| **Content Date**        | If the timeframe is:<ul><li> The current month, the latest date with available data.</li><li>A previous month, the last date of that month.</li></ul> |
