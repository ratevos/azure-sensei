# Govern access for applications in your environment

> Source: https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-applications-prepare  
> Microsoft doc last updated: 11/21/2024


Microsoft Entra ID Governance allows you to balance your organization's need for security and employee productivity with the right processes and visibility. Its features ensure that users and agent IDs have the right access to the right resources in your organization at the right time.

Organizations with compliance requirements or risk management plans have sensitive or business-critical applications. The application sensitivity may be based on its purpose or the data it contains, such as financial information or personal information of the organization's customers. For those applications, only a subset of all the users and agent IDs in the organization will typically be authorized to have access, and access should only be permitted based on documented business requirements. 

As part of your organization's controls for managing access, you can use Microsoft Entra features to:

* set up appropriate access
* provision users to applications
* enforce access checks
* produce reports to demonstrate how those controls are being used to meet your compliance and risk management objectives.

In addition to the application access governance scenario, you can also use Microsoft Entra ID Governance features and the other Microsoft Entra features for other scenarios, such as [reviewing and removing users from other organizations](https://learn.microsoft.com/en-us/entra/id-governance/access-reviews-external-users) or [managing users who are excluded from Conditional Access policies](https://learn.microsoft.com/en-us/entra/id-governance/conditional-access-exclusion). If your organization has multiple administrators in Microsoft Entra ID or Azure, uses B2B or self-service group management, then you should [plan an access reviews deployment](https://learn.microsoft.com/en-us/entra/id-governance/deploy-access-reviews) for those scenarios.

## License requirements
Using this feature requires Microsoft Entra ID Governance or Microsoft Entra Suite licenses. To find the right license for your requirements, see [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).

## Getting started with governing access to applications

Microsoft Entra ID Governance can be integrated with many applications, using [standards](https://learn.microsoft.com/en-us/entra/architecture/auth-sync-overview) such as OpenID Connect, SAML, SCIM, SQL, and LDAP. Through these standards, you can use Microsoft Entra ID  with many popular SaaS applications, on-premises applications, and applications that your organization has developed. 

Once you've prepared your Microsoft Entra environment, as described in the section below, the three step plan covers how to connect an application to Microsoft Entra ID and enable identity governance features to be used for that application.

1. [Define your organization's policies for governing access to the application](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-applications-define)
1. [Integrate the application with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-applications-integrate) to ensure only authorized users can access the application, and review user's existing access to the application to set a baseline of all users having been reviewed. This allows authentication and user provisioning
1. [Deploy those policies](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-applications-deploy) for controlling single sign-on (SSO) and automating access assignments for that application

<a name='prerequisites-before-configuring-azure-ad-for-identity-governance'></a>

## Prerequisites before configuring Microsoft Entra ID and Microsoft Entra ID Governance for identity governance

Before you begin the process of governing application access from Microsoft Entra ID Governance, you should check your Microsoft Entra environment is appropriately configured.

* **Select the appropriate tenant deployment architecture.** If you'll be providing business partners as well as workforce users access to an application, then select a tenant to integrate the application and deploy identity governance capabilities, that will be configured for any collaboration or isolation requirements for the business partner scenario. For more information, see [Microsoft Entra External ID deployment architectures with Microsoft Entra](https://learn.microsoft.com/en-us/entra/architecture/external-identity-deployment-architectures).

* **Ensure your Microsoft Entra ID and Microsoft Online Services environment is ready for the [compliance requirements](https://learn.microsoft.com/en-us/entra/standards/standards-overview) for the applications to be integrated and properly licensed**. Compliance is a shared responsibility among Microsoft, cloud service providers (CSPs), and organizations. To use Microsoft Entra ID to govern access to applications, you must have one of the following [license combinations](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals) in your tenant:

  * **Microsoft Entra ID Governance** and its prerequisite, Microsoft Entra ID P1
  * **Microsoft Entra ID Governance Step Up for Microsoft Entra ID P2** and its prerequisite, either Microsoft Entra ID P2 or Enterprise Mobility + Security (EMS) E5
  * **Microsoft Entra Suite**

   Your tenant needs to have at least as many licenses as the number of member (non-guest) users who are governed, including those users that have or can request access to the applications, approve, or review access to the applications. With an appropriate license for those users, you can then govern access to up to 1500 applications per user. For more information, see [license scenarios](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).

* **If you will be governing guest's access to the application, link your Microsoft Entra tenant to a subscription for MAU billing**. This step is necessary prior to having a guest request or review their access. For more information, see [billing model for Microsoft Entra External ID](https://learn.microsoft.com/en-us/entra/external-id/external-identities-pricing).

* **Check that Microsoft Entra ID is already sending its audit log, and optionally other logs, to Azure Monitor.** Azure Monitor is optional, but useful for governing access to apps, as Microsoft Entra only stores audit events for up to 30 days in its audit log. You can keep the audit data for longer than the default retention period, outlined in [How long does Microsoft Entra ID store reporting data?](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-reports-data-retention), and use Azure Monitor workbooks and custom queries and reports on historical audit data. You can check the Microsoft Entra configuration to see if it's using Azure Monitor, in **Microsoft Entra ID** in the Microsoft Entra admin center, by clicking on **Workbooks**. If this integration isn't configured, and you have an Azure subscription and are in the `Global Administrator` or `Security Administrator` roles, you can [configure Microsoft Entra ID to use Azure Monitor](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-logs-and-reporting).

* **Select an object retention approach.** If your organization requires being able to report on historical Microsoft Entra objects, such as reports that list users and agent IDs who had access to an application in a past year including those who were subsequently deleted from Microsoft Entra, then you should plan to archive objects from Microsoft Entra to a separate repository for retention and reporting purposes. For more information, see [Customized reports in Azure Data Explorer (ADX) using data from Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/id-governance/custom-entitlement-report-with-adx-and-entra-id).

* **Make sure only authorized users are in the highly privileged administrative roles in your Microsoft Entra tenant.** Administrators in the *Global Administrator*, *Identity Governance Administrator*, *User Administrator*, *Application Administrator*, *Cloud Application Administrator*, and *Privileged Role Administrator* can make changes to users and their application role assignments. If the memberships of those roles haven't yet been recently reviewed, you need a user who is in the *Global Administrator* or *Privileged Role Administrator* to ensure that [access review of these directory roles](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-create-roles-and-resource-roles-review) are started. You should also ensure that users in Azure roles in subscriptions that hold the Azure Monitor, Logic Apps, and other resources needed for the operation of your Microsoft Entra configuration have been reviewed.

* **Check your tenant has appropriate isolation.** If your organization is using Active Directory on-premises, and these AD domains are connected to Microsoft Entra ID, then you need to ensure that highly privileged administrative operations for cloud-hosted services are isolated from on-premises accounts. Check that you've [configured your systems to protect your Microsoft 365 cloud environment from on-premises compromise](https://learn.microsoft.com/en-us/entra/architecture/protect-m365-from-on-premises-attacks).

Once you have checked your Microsoft Entra environment is ready, then proceed to [define the governance policies](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-applications-define) for your applications.

## Next steps

- [Define governance policies](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-applications-define)
- [Integrate an application with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-applications-integrate)
- [Deploy governance policies](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-applications-deploy)
