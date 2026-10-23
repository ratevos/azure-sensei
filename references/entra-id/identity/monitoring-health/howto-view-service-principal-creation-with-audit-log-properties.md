# How to investigate why a service principal was created in your tenant

> Source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-view-service-principal-creation-with-audit-log-properties  
> Microsoft doc last updated: 06/05/2026


When a new service principal appears in your tenant, you might want to understand why it was created and who or what initiated the process. The [new audit log properties](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/understand-service-principal-creation-with-new-audit-log-properties) `ServicePrincipalProvisioningType`, `SubscribedSkus`, and `AppOwnerOrganizationId` help you quickly determine whether the service principal was provisioned by Microsoft, created by a user, or added by an external application. The following steps show you how to access these properties in the Microsoft Entra admin center to use them in your investigations. You can also leverage Microsoft Graph API and Log Analytics to access these new properties.

## Prerequisites

To view and use these properties in Microsoft Entra audit logs, you need:

- Access to the Microsoft Entra admin center.
- One of the following roles (or a role with equivalent permissions): [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator), [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader), or [Reports Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#reports-reader).
- Audit logging enabled for your tenant. For more information, see the [Microsoft Entra audit logs overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-audit-logs).

## View audit log properties to understand service principal details

To view audit log properties in the Microsoft Entra admin center:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/).
1. Browse to **Monitoring & health** > **Audit logs**.
1. Set **Category** to **ApplicationManagement** and apply the filter.
1. Filter **Activity** to **Add service principal** and apply the filter.
2. Select an event and expand **Additional details**. Look for these properties `ServicePrincipalProvisioningType`, `SubscribedSkus`, and `AppOwnerOrganizationId`.

If you send audit logs to Log Analytics, Microsoft Sentinel, or another destination, the same properties are available in the **AuditLogs** table under the **AdditionalDetails** JSON. You can parse these fields in your queries to group events by provisioning type, SKU, or owning tenant.

## Investigate the new service principal

Once the new properties are available in your tenant, you can use them to streamline investigations into new service principals in Log Analytics and Microsoft Sentinel:

1. Start with `ServicePrincipalProvisioningType` to distinguish Microsoft-driven provisioning from direct user or app activity in your tenant.
1. When the value is subscription, review `SubscribedSkus` to see which subscriptions or service plans in your tenant made the Microsoft service principal eligible for just-in-time provisioning.
1. Use `AppOwnerOrganizationId` to understand whether the app is homed in your tenant, in a Microsoft services tenant, or in another external tenant.
1. Combine these fields with existing audit log properties such as `initiatedBy` and `targetResources` to get a full picture of who or what created the service principal, without relying on additional API calls.

> [!NOTE]
> The `AppOwnerOrganizationId` property will only show for events where there is a backing application object. The `SubscribedSkus` property will only show for events when `ServicePrincipalProvisioningType` = `Subscription`.

These enhancements are designed to make it easier for you to interpret service principal creation events, quickly understand the meaning of different values, and plug that information into your own alerting and governance workflows. These alerts can categorize service principal creation events as "expected" versus "unexpected" based on your tenant security preferences. 

## Use Microsoft Graph

To retrieve these events programmatically, query the [List directoryAudits](https://learn.microsoft.com/en-us/graph/api/directoryaudit-list?view=graph-rest-1.0&preserve-view=true) operation and filter on the activity name. The new properties are returned in the `additionalDetails` collection of each event.

```http
GET https://graph.microsoft.com/v1.0/auditLogs/directoryAudits?$filter=activityDisplayName eq 'Add service principal'
```

## Related content
[Microsoft Entra audit log categories and activities](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-audit-activities)
