# Learn about the audit logs in Microsoft Entra ID

> Source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-audit-logs  
> Microsoft doc last updated: 06/05/2026


Microsoft Entra activity logs include audit logs, which is a comprehensive report on every logged event in Microsoft Entra ID. Changes to applications, groups, users, and licenses are all captured in the Microsoft Entra audit logs.

Three other activity logs are also available to help monitor the health of your tenant:

- **[Sign-ins](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-ins)** – Information about sign-ins and how your resources are used by your users.
- **[Sign-ups (preview)](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-ups)** - For [external tenants](https://learn.microsoft.com/en-us/entra/external-id/tenant-configurations) only, information about all self-service sign-up attempts, including successful sign-ups and failed attempts.
- **[Provisioning](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-provisioning-logs)** – Activities performed by the provisioning service, such as the creation of a group in ServiceNow or a user imported from Workday.

This article gives you an overview of the audit logs, such as the information they provide and what kinds of questions they can answer.

## What can you do with audit logs?

Audit logs in Microsoft Entra ID provide access to system activity records, often needed for compliance. You can get answers to questions related to users, groups, and applications.

**Users:**

- What types of changes were recently applied to users?
- How many users were changed?
- How many passwords were changed?

**Groups:**

- What groups were recently added?
- Have the owners of group been changed?
- What licenses are to a group or a user?

**Applications:**

- What applications were, updated, or removed?
- Has a service principal for an application changed?
- Who or what created a service principal, and why was it created?
- Have the names of applications been changed?

**Custom security attributes:**

- What changes were made to [custom security attribute](https://learn.microsoft.com/en-us/entra/fundamentals/custom-security-attributes-overview) definitions or assignments?
- What updates were made to attribute sets?
- What custom attribute values were assigned to a user?

**Agents:**

- What operations were performed by a specific agent?
- What changes were made to an agent service principal?
- What details of an agent ID were changed?

> [!NOTE]
> Entries in the audit logs are system generated and can't be changed or deleted.

## What do the logs show?

Audit logs display several valuable details on the activities in your tenant. Key details are visible at-a-glance in the table, with more details available by selecting a specific log entry. The Microsoft Entra admin center defaults to the **Directory** tab, which displays the following information:

- Date and time of the occurrence
- Service that logged the occurrence
- Category and name of the activity
- Status of the activity

By selecting a specific log entry, you get even more details, such as:

- Correlation ID for troubleshooting
- Details about the actor or target resource associated with the activity
- Where applicable, old and new values for the changed properties

> [!NOTE]
> In the audit log details, the IP address reflects the OAuth client's IP address. The IP address is the TCP peer of the service's endpoint.

A second tab for **Custom Security** displays audit logs for custom security attributes. To view data on this tab, you must have the [Attribute Log Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#attribute-log-administrator) or [Attribute Log Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#attribute-log-reader) role. This audit log shows all activities related to custom security attributes. For more information, see [What are custom security attributes](https://learn.microsoft.com/en-us/entra/fundamentals/custom-security-attributes-overview).

For a full list of the available audit activities, see [Audit activity reference](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-audit-activities).

## Microsoft 365 activity logs

You can view Microsoft 365 activity logs from the [Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/admin-overview/admin-center-overview). Even though Microsoft 365 activity and Microsoft Entra activity logs share many directory resources, only the Microsoft 365 admin center provides a full view of the Microsoft 365 activity logs.

You can also access the Microsoft 365 activity logs programmatically by using the [Office 365 Management APIs](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-apis-overview).

Most standalone or bundled Microsoft 365 subscriptions have back-end dependencies on some subsystems within the Microsoft 365 datacenter boundary. The dependencies require some information write-back to keep directories in sync and essentially to help enable hassle-free onboarding in a subscription opt-in for Exchange Online. For these write-backs, audit log entries show actions taken by "Microsoft Substrate Management." These audit log entries refer to create/update/delete operations executed by Exchange Online to Microsoft Entra ID. The entries are informational and don't require any action.

## Related content

- [Audit activity reference](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-audit-activities)
- [Understand why a service principal was created in your tenant](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/understand-service-principal-creation-with-new-audit-log-properties)
- [Access activity logs](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)
- [Customize and filter activity logs](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-customize-filter-logs)
