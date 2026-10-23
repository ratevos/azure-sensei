# Microsoft Entra ID Governance licensing fundamentals

> Source: https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals  
> Microsoft doc last updated: 07/29/2026

This article discusses Microsoft Entra ID Governance licensing for employees. It's intended for IT decision makers, IT administrators, and IT professionals who are considering Microsoft Entra ID Governance services for their organizations.

For governance licensing for guest users, see [Microsoft Entra ID Governance licensing for guest users](https://learn.microsoft.com/en-us/entra/id-governance/microsoft-entra-id-governance-licensing-for-guest-users). For agent identity licensing requirements, see [Governing agent identities](https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview#license-requirements). For licensing that applies to Tenant Governance administrators and features, see [Licensing for Microsoft Entra Tenant Governance](https://learn.microsoft.com/en-us/entra/id-governance/tenant-governance/licensing).

## Types of licenses

The following licenses are available for use with Microsoft Entra ID Governance in the commercial and government clouds. The choice of licenses you need in a tenant depends on the features you're using in that tenant.

- **Free** - Included with Microsoft cloud subscriptions such as Microsoft Azure, Microsoft 365, and others.
- **Microsoft Entra ID P1** - Microsoft Entra ID P1 is available as a standalone product or included with Microsoft 365 E3, E5 or E7 for enterprise customers and Microsoft 365 Business Premium for small to medium businesses.
- **Microsoft Entra ID P2** - Microsoft Entra ID P2 is available as a standalone product or included with Microsoft 365 E5 or E7 for enterprise customers.
- **Microsoft Entra ID Governance** - Microsoft Entra ID Governance is an advanced set of identity governance capabilities available for Microsoft Entra ID P1 and P2 customers. Microsoft Entra ID Governance is available as six products **Microsoft Entra ID Governance**, **Microsoft Entra ID Governance Step Up for Microsoft Entra ID P2**, **Entra ID Governance Frontline Worker**, **Microsoft Entra ID Governance Step up for Microsoft Entra ID F2**, **Microsoft Entra ID Governance for Government** and **Microsoft Entra ID Governance Add-on for Microsoft Entra ID P2 for Government**. These six products differ only in their prerequisites; they contain both the entitlement management, privileged identity management and access reviews capabilities that were in Microsoft Entra ID P2, and additional advanced identity governance capabilities. The following section goes into more detail on the different prerequisites of these products.
- **Microsoft Entra Suite** - Microsoft Entra Suite is a complete cloud-based solution for workforce access, available for Microsoft Entra ID P1 and P2 customers. Microsoft Entra Suite brings together **Microsoft Entra Private Access**, **Microsoft Entra Internet Access**, **Microsoft Entra ID Governance**, **Microsoft Entra ID Protection**, and **Microsoft Entra Verified ID**. The Microsoft Entra ID Governance portion provides the same identity governance capabilities as the **Microsoft Entra ID Governance** product. The difference is that they have different prerequisites.
- **Microsoft Agent 365** - Microsoft Agent 365 provides identity governance capabilities for agent identities, providing access governance for agents and service principals via Entra's Entitlement Management, additional automations via Lifecycle workflows as well as end user experiences for sponsors to manage agent identity and access lifecycle. The following section goes into more detail on the prerequisites and capabilities. For more information about Microsoft Agent 365, see: [Microsoft Agent 365](https://www.microsoft.com/licensing/faqs/122).

>[!NOTE]
>Some Microsoft Entra ID Governance scenarios can be configured to depend upon other features that aren't covered by Microsoft Entra ID Governance. These features might have additional licensing requirements. For more information on governance scenarios using other features, see the [Identity Governance overview](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview) page.

The Microsoft Entra ID Governance for Government and Microsoft Entra ID Governance Add-on for Microsoft Entra ID P2 for Government products are available in the US Government community cloud (GCC), GCC-High, and Department of Defense cloud environments.

### Governance products and prerequisites

The Microsoft Entra ID Governance capabilities are currently available in six standalone products. These six products provide the same identity governance capabilities. The difference between the six products is that they have different prerequisites.

- A subscription to **Microsoft Entra ID Governance** or **Microsoft Entra ID Governance for Government**, listed in the product terms as the **Microsoft Entra ID Governance (User SL)** product, requires that the tenant also have an active subscription to another product, one that contains the `AAD_PREMIUM` or `AAD_PREMIUM_P2` service plan. Examples of products meeting this prerequisite include **Microsoft Entra ID P1**, **Microsoft 365 E3/E5/A3/A5/G3/G5** or **Enterprise Mobility + Security E3/E5**.
- A subscription to **Microsoft Entra ID Governance Step Up for Microsoft Entra ID P2** or **Microsoft Entra ID Governance Add-on for Microsoft Entra ID P2 for Government**, listed in the product terms as the **Microsoft Entra ID Governance P2** product, requires that the tenant also have an active subscription to another product, one that contains the `AAD_PREMIUM_P2` service plan. Examples of products meeting this prerequisite include **Microsoft Entra ID P2**, **Microsoft 365 E5/A5/G5**, **Enterprise Mobility + Security E5**, **Microsoft 365 E5/F5 Security** or **Microsoft 365 F5 Security + Compliance**.
- A subscription to the **Entra ID Governance Frontline Worker (User SL)** product requires that the tenant also have an active subscription to another product, one that contains the `AAD_PREMIUM` or `AAD_PREMIUM_P2` service plan. Examples of products meeting this prerequisite include **Microsoft Entra ID P1**, **Microsoft 365 E3/E5/A3/A5/G3/G5**, **Enterprise Mobility + Security E3/E5** or **Microsoft 365 F1/F3**.
- A subscription to **Microsoft Entra ID Governance Step up for Microsoft Entra ID F2**, listed in the product terms as the **Microsoft Entra ID Governance F2** or **Microsoft Entra ID Governance Step-Up for Microsoft Entra ID F2 for Frontline Worker (User SL)** product, requires that the tenant also have an active subscription to another product, one that contains the `AAD_PREMIUM_P2` service plan. Examples of products meeting this prerequisite include **Microsoft Entra ID F2**.
- A subscription to **Microsoft Agent 365** requires that the tenant also have an active subscription to another product, one that contains the `AAD_PREMIUM` service plan. Examples of products meeting this prerequisite include **Microsoft Entra ID P1** or **Microsoft 365 E3**.

Microsoft Entra ID Governance capabilities are also included in the Microsoft Entra Suite and in Microsoft 365 E7. The available Microsoft Entra Suite products include **Microsoft Entra Suite (User SL)**, **Microsoft Entra Suite Add-on for Microsoft Entra ID F2 for FLW (User SL)**, **Microsoft Entra Suite Add-on for Microsoft Entra ID P2 (User SL)**, **Microsoft Entra Suite Add-on for Microsoft Entra ID P2 EDU (User SL)**, **Microsoft Entra Suite FLW (User SL)**, and **Microsoft Entra Suite for EDU (User SL)**.

The [product names and service plan identifiers for licensing](https://learn.microsoft.com/en-us/entra/identity/users/licensing-service-plan-reference) lists additional products that include the prerequisite service plans.

>[!NOTE]
>A subscription to a prerequisite for a Microsoft Entra ID Governance product must be active in the tenant. If a prerequisite isn't present, or the subscription expires, then Microsoft Entra ID Governance scenarios might not function as expected.  

To check if the prerequisite products for a Microsoft Entra ID Governance product are present in a tenant, you can use the Microsoft Entra admin center or the Microsoft 365 admin center to view the list of products.

1. Sign into the [Microsoft Entra admin center](https://entra.microsoft.com) as a [License Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#license-administrator).

1. Browse to **Billing** > **Licenses**.

1. In the **Manage** menu, select **Licensed features**. The information bar indicates the current Microsoft Entra ID license plan.

1. To view the existing products in the tenant, in the **Manage** menu, select **All products**.

Governance of guest users requires an Azure subscription be selected for guest billing. For more information, see: [Microsoft Entra ID Governance licensing for guest users](https://learn.microsoft.com/en-us/entra/id-governance/microsoft-entra-id-governance-licensing-for-guest-users).

## Starting a trial

A Global Administrator in a commercial tenant that has an appropriate prerequisite product, such as Microsoft Entra ID P1, already purchased, and isn't already using or has previously trialed Microsoft Entra ID Governance, can request a trial of Microsoft Entra ID Governance in their tenant.

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com/AdminPortal/Home) as a [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator)

1. In the **Billing** menu, select **Purchase services**.

1. In the **Search all product categories** box, type `"Microsoft Entra ID Governance"`.

1. Select **Details** below **Microsoft Entra ID Governance** to view the trial and purchase information for the product. If your tenant has Microsoft Entra ID P2, then select  **Details** below **Microsoft Entra ID Governance Step-Up for Microsoft Entra ID P2**.

1. In the product details page, select **Start free trial**.

## Microsoft Entra ID Governance features

The following table shows the licensing requirements for Microsoft Entra ID Governance features for member users. Microsoft Entra Suite includes all features of Microsoft Entra ID Governance. Microsoft 365 E7 also includes all ID Governance features through the Entra Suite and Agent 365. Licensing information for Entitlement management, Access reviews, and Lifecycle Workflows are provided following the table.

### Features by license

The following table shows what features associated with identity governance are available with each license. For more information on other features, see [Microsoft Entra plans and pricing](https://www.microsoft.com/security/business/microsoft-entra-pricing). Not all features are available in all clouds; see [Microsoft Entra feature availability](https://learn.microsoft.com/en-us/entra/identity/authentication/feature-availability) for Azure Government.

|Feature|Free|Microsoft Entra ID P1|Microsoft Entra ID P2|Microsoft Entra ID Governance|Microsoft Entra Suite|Microsoft Agent 365|Microsoft 365 E7|
|-----|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|**Provisioning**||||||||
|[API-driven provisioning](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/inbound-provisioning-api-concepts)|| :white_check_mark:  | :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[HR-driven provisioning](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/what-is-hr-driven-provisioning)|| :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[Account Discovery](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/how-to-account-discovery)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[Automated user provisioning to SaaS apps](https://learn.microsoft.com/en-us/entra/identity/saas-apps/tutorial-list)| :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[Automated group provisioning to SaaS apps](https://learn.microsoft.com/en-us/entra/identity/saas-apps/tutorial-list)|| :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[Automated provisioning to on-premises apps](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/on-premises-application-provisioning-architecture)|| :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[Cross-tenant synchronization for users (same cloud)](https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-configure.md?pivots=cross-cloud-synchronization)|| :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[Cross-tenant synchronization for groups (same cloud)](https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-configure.md?pivots=cross-cloud-synchronization)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[Cross-cloud synchronization](https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-configure.md?pivots=cross-cloud-synchronization)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|**Lifecycle Workflows (LCW)**|**Free**|**Microsoft Entra ID P1**|**Microsoft Entra ID P2**|**Microsoft Entra ID Governance**| **Microsoft Entra Suite** | **Microsoft Agent 365** |**Microsoft 365 E7**|
|[Lifecycle Workflows](https://learn.microsoft.com/en-us/entra/id-governance/what-are-lifecycle-workflows)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[LCW + Custom Extensions (Logic Apps)](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-extensibility)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[LCW + Agent Sponsorship tasks](https://learn.microsoft.com/en-us/entra/id-governance/agent-sponsor-tasks)|||||| :white_check_mark: | :white_check_mark: |
|**Access reviews (AR)**|**Free**|**Microsoft Entra ID P1**|**Microsoft Entra ID P2**|**Microsoft Entra ID Governance**| **Microsoft Entra Suite** | **Microsoft Agent 365** | **Microsoft 365 E7**|
|[AR - Capabilities previously generally available in Microsoft Entra ID P2](https://learn.microsoft.com/en-us/entra/id-governance/access-reviews-overview)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[AR - PIM For Groups (Preview)](https://learn.microsoft.com/en-us/entra/id-governance/create-access-review-pim-for-groups)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[AR - Reviews scoped to inactive users without active users in the review](https://learn.microsoft.com/en-us/entra/id-governance/create-access-review#scope)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[AR - Reviews scoped to active and inactive users with review decision helpers for inactive users for the reviewer](https://learn.microsoft.com/en-us/entra/id-governance/review-recommendations-access-reviews#inactive-user-recommendations)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[AR - Machine learning assisted access certifications and reviews](https://learn.microsoft.com/en-us/entra/id-governance/review-recommendations-access-reviews#user-to-group-affiliation)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[AR - Catalog Access Reviews](https://learn.microsoft.com/en-us/entra/id-governance/catalog-access-reviews)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[AR - Custom data provided resource](https://learn.microsoft.com/en-us/entra/id-governance/custom-data-resource-access-reviews)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|**Entitlement management (EM)**|**Free**|**Microsoft Entra ID P1**|**Microsoft Entra ID P2**|**Microsoft Entra ID Governance**| **Microsoft Entra Suite** | **Microsoft Agent 365** |**Microsoft 365 E7**|
|[EM - Capabilities previously generally available in Microsoft Entra ID P2](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-overview)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Users assigned to access packages](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create#allow-users-service-principals-and-agent-identities-in-your-directory-to-request-the-access-package)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Agents and service principals assigned to access packages](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create#allow-users-service-principals-and-agent-identities-in-your-directory-to-request-the-access-package)|||||| :white_check_mark: | :white_check_mark: |
|[EM - Users request access for themselves](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-overview)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Admins directly assign a user assignments(including guests)](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-assignments#directly-assign-an-identity)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Admins directly assign agents and service principals](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-assignments#directly-assign-any-identity)|||||| :white_check_mark: | :white_check_mark: |
|[EM - Admins directly assign any user - via email address for users not yet in your directory](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-assignments#directly-assign-any-identity)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Managers requesting on behalf of employees](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-request-behalf)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Owners and sponsors request access on behalf of their agents or service principals](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-request-behalf#scenarios-for-requesting-on-behalf-of-agent-identities)|||||| :white_check_mark: | :white_check_mark: |
|**EM - Supported resources**|**Free**|**Microsoft Entra ID P1**|**Microsoft Entra ID P2**|**Microsoft Entra ID Governance**| **Microsoft Entra Suite** | **Microsoft Agent 365** |**Microsoft 365 E7**|
|[EM - Groups and teams in access packages](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-resources#add-a-group-or-team-resource-role)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Eligible group ownerships and memberships in access packages (PIM for Groups)](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-eligible)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Applications in access packages](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-resources#add-an-application-resource-role)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - SharePoint sites in access packages](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-resources#add-a-sharepoint-site-resource-role)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Microsoft Entra Roles (Preview)](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-roles)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - SAP Identity Access Governance (IAG) business roles (Preview)](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-sap-integration)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - API permissions in access packages](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-resources#add-an-api-permission)|||||| :white_check_mark: | :white_check_mark: |
|**EM - Approval options**|**Free**|**Microsoft Entra ID P1**|**Microsoft Entra ID P2**|**Microsoft Entra ID Governance**| **Microsoft Entra Suite** | **Microsoft Agent 365** |**Microsoft 365 E7**|
|[EM - Multi-stage approvals with alternate approvers if no action is taken](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-approval-policy)||| :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
|[EM - Specific approvers](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-approval-policy)||| :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
|[EM - Managers as approvers](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-approval-policy)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Internal sponsors as approvers (from assignees' connected organizations)](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-approval-policy)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - External sponsors as approvers (from assignees' connected organizations)](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-approval-policy)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Sponsors as approvers (from assignees' user profile)](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-approval-policy)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Agent Sponsors as approvers](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-approval-policy)|||||| :white_check_mark: | :white_check_mark: |
|[EM - Externally determine approval requirements using custom extensions](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-dynamic-approval)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Collect additional requestor information for approval](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-approval-policy#collect-additional-requestor-information-for-approval)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|**EM - Lifecycle**|**Free**|**Microsoft Entra ID P1**|**Microsoft Entra ID P2**|**Microsoft Entra ID Governance**| **Microsoft Entra Suite** | **Microsoft Agent 365** |**Microsoft 365 E7**|
|[EM - Expiration of access package assignments](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-lifecycle-policy)||| :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
|[EM - Manage the lifecycle of external users](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-external-users#manage-the-lifecycle-of-external-users)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Mark guest as governed](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-manage-lifecycle)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|**EM - Additional capabilities**|**Free**|**Microsoft Entra ID P1**|**Microsoft Entra ID P2**|**Microsoft Entra ID Governance**| **Microsoft Entra Suite** | **Microsoft Agent 365** |**Microsoft 365 E7**|
|[EM - Separation of duties](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-incompatible)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Custom Extensions (Logic Apps)](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-logic-apps-integration)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Auto Assignment Policies](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-auto-assignment-policy)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Verified ID integration](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-verified-id-settings)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Microsoft Entra ID Protection integration](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-configure-id-protection-approvals)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Microsoft Purview Insider Risk Management integration](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-configure-insider-risk-management-approvals)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Conditional Access Scoping](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-external-users#review-your-conditional-access-policies)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|**My Access**|**Free**|**Microsoft Entra ID P1**|**Microsoft Entra ID P2**|**Microsoft Entra ID Governance**| **Microsoft Entra Suite** | **Microsoft Agent 365** |**Microsoft 365 E7**|
|[My Access portal](https://learn.microsoft.com/en-us/entra/id-governance/my-access-portal-overview)||| :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
|[EM - My Access Search](https://learn.microsoft.com/en-us/entra/id-governance/my-access-portal-overview)||| :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
|[EM - Suggested access packages in My Access](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-suggested-access-packages)||| | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Configure whether requestors can see approver details in My Access (Preview)](https://learn.microsoft.com/en-us/entra/id-governance/my-access-approver-details)||| | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[EM - Delegate approvals in My Access (Preview)](https://learn.microsoft.com/en-us/entra/id-governance/my-access-portal-overview)||| | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|**Privileged Identity Management (PIM)**|**Free**|**Microsoft Entra ID P1**|**Microsoft Entra ID P2**|**Microsoft Entra ID Governance**| **Microsoft Entra Suite** | **Microsoft Agent 365** |**Microsoft 365 E7**|
|[Privileged Identity Management (PIM)](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[PIM For Groups](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/concept-pim-for-groups)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[PIM Conditional Access Controls](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings#on-activation-require-microsoft-entra-conditional-access-authentication-context)||| :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[PIM - Custom extensions for role activation (Preview)](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/privileged-identity-management-custom-extensions)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|**Other**|**Free**|**Microsoft Entra ID P1**|**Microsoft Entra ID P2**|**Microsoft Entra ID Governance**| **Microsoft Entra Suite** | **Microsoft Agent 365** |**Microsoft 365 E7**|
|[Identity governance dashboard](https://learn.microsoft.com/en-us/entra/id-governance/governance-dashboard)| | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[Insights and reporting - Inactive guest accounts](https://learn.microsoft.com/en-us/entra/identity/users/clean-up-stale-guest-accounts)|||| :white_check_mark: | :white_check_mark: || :white_check_mark: |
|[Conditional Access - Terms of use attestation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/terms-of-use)|| :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: || :white_check_mark: |

### Entitlement Management

Using this feature requires a Microsoft Entra ID Governance subscription for your organization's member users. Some capabilities within this feature can operate with a Microsoft Entra ID P2 subscription. Some capabilities within this feature require guest billing.

### Access reviews

Using this feature requires a Microsoft Entra ID Governance subscription for your organization's member users, including for all employees who are reviewing access or having their access reviewed. Some capabilities within this feature might operate with a Microsoft Entra ID P2 subscription. Some capabilities within this feature require guest billing.

### Lifecycle Workflows

With Microsoft Entra ID Governance licenses for Lifecycle Workflows, you can:

- Create, manage, and delete workflows up to the total limit of 50 workflows.
- Trigger on-demand and scheduled workflow execution.
- Manage and configure existing tasks to create workflows that are specific to your needs.
- Create up to 100 custom task extensions to be used in your workflows.

Using this feature requires a Microsoft Entra ID Governance subscription for your organization's member users. Some capabilities within this feature require guest billing.

## Privileged Identity Management

To use Microsoft Entra Privileged Identity Management, a tenant must have a valid license. This article describes the license requirements to use Privileged Identity Management. To use Privileged Identity Management, you must have one of the following licenses:

### Valid licenses for PIM

You need either Microsoft Entra ID Governance licenses or Microsoft Entra ID P2 licenses to use PIM and all of its settings. Currently, you can scope an access review to service principals with access to Microsoft Entra ID, resource roles with a Microsoft Entra ID P2 or users with Microsoft Entra ID Governance edition active in your tenant. 

### Licenses you must have for PIM

Ensure that your directory has Microsoft Entra ID P2 or Microsoft Entra ID Governance licenses for the following categories of users:

- Users with eligible and/or time-bound assignments to Microsoft Entra ID or Azure roles managed using PIM
- Users with eligible and/or time-bound assignments as members or owners of PIM for Groups
- Users able to approve or reject activation requests in PIM
- Users assigned to an access review
- Users who perform access reviews

### When a license expires for PIM

If a Microsoft Entra ID P2, Microsoft Entra ID Governance, or trial license expires, Privileged Identity Management features are no longer available in your directory:

- Permanent role assignments to Microsoft Entra roles are unaffected.
- The Privileged Identity Management service in the Microsoft Entra admin center, and the Graph API cmdlets and PowerShell interfaces of Privileged Identity Management, will no longer be available for users to activate privileged roles, manage privileged access, or perform access reviews of privileged roles.
- Eligible role assignments of Microsoft Entra roles are removed, as users will no longer be able to activate privileged roles.
- Any ongoing access reviews of Microsoft Entra roles ends, and Privileged Identity Management configuration settings are removed.
- Privileged Identity Management no longer sends emails on role assignment changes.

## API-driven provisioning

This feature is available with Microsoft Entra ID P1, P2, and Microsoft Entra ID Governance subscriptions. A subscription license is required with enough seats for every identity that is sourced using the [/bulkUpload](https://learn.microsoft.com/en-us/graph/api/synchronization-synchronizationjob-post-bulkupload) API and provisioned to either on-premises Active Directory or Microsoft Entra ID.

### License scenarios

|Customer License  |Usage limits enforced at tenant level for API-driven provisioning  |
|---------|---------|
|Microsoft Entra ID P1 or P2      |   Daily usage quota (number of user records that can be uploaded over 24-hour period): **100K user records (2000 /bulkUpload API calls with each request containing max of 50 records)**.<br><br>Max number of API-driven provisioning jobs for each flow: 2<br>o Max 2 apps for API-driven provisioning to on-premises Active Directory.<br>o Max 2 apps for API-driven provisioning to Microsoft Entra ID.      |
|Microsoft Entra ID Governance alongside Microsoft Entra ID P1 or P2     | Daily usage quota (number of user records that can be uploaded over 24-hour period): **300K user records  (6000 /bulkUpload API calls with each request containing max of 50 records)**.<br><br>Max number of API-driven provisioning jobs for each flow: 20<br>o Max 20 apps for API-driven provisioning to on-premises Active Directory.<br>o Max 20 apps for API-driven provisioning to Microsoft Entra ID.        |

## Account Discovery

Account Discovery requires the Microsoft Entra ID Governance add-on or Microsoft Entra Suite. This feature allows administrators to discover existing user accounts in target applications and identify which users have matching Entra accounts or are orphan accounts. For more information, see [Discover identities in target applications with Account Discovery](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/how-to-account-discovery).

## Licensing FAQs

### Do licenses need to be assigned to users to use Identity Governance features?

Users don't need to be assigned a Microsoft Entra ID Governance license, but there needs to be as many licenses to include all member users in scope of, or who configures, the Identity Governance features. In addition, the guest billing model must be enabled if there are guest users to be governed, as described in the next answer.

### How can I license usage of Microsoft Entra ID Governance features for business guests?

Microsoft Entra ID Governance utilizes Monthly Active User (MAU) licensing for guest users which is different than licensing for employees and requires an Azure subscription.
 
Under the guest billing model, guests are identified by a *userType* of Guest regardless of where the user authenticates. A *userType* of Guest is the default userType for all B2B invitation methods and can also be set by an Identity administrator. The bill for each month includes a record for each guest user with one or more governance actions in that month. See the Azure pricing page for pricing details.

For more information, see: [Microsoft Entra ID Governance licensing for guest users](https://learn.microsoft.com/en-us/entra/id-governance/microsoft-entra-id-governance-licensing-for-guest-users).

### What happens to PIM when a license expires?

If a Microsoft Entra ID P2 or Microsoft Entra ID Governance license expires or trial ends, Privileged Identity Management features will no longer be available in your directory. The following changes listed are applicable to PIM for Microsoft Entra roles, PIM for Azure resources, and PIM for Groups.

- Active permanent assignments aren't affected.
- Active time-bound assignments become active permanent, which means they'll no longer expire at a designated time.
- Eligible role assignments are removed, as users will no longer be able to activate privileged roles.
- Privileged Identity Management blades on Microsoft Entra admin center or Azure portal, API, and PowerShell interfaces of Privileged Identity Management, will no longer be available for users to activate roles, manage assignments, or perform access reviews of privileged roles.
- Any ongoing access reviews of Microsoft Entra roles end, and Privileged Identity Management configuration settings are removed.
- Privileged Identity Management will no longer send emails on role assignment changes and PIM Alerts.

<a name='will-any-iga-features-and-capabilities-be-added-under-the-entra-id-p2-license'></a>

### Will any IGA features and capabilities be added under the Microsoft Entra ID P2 License?

All currently Generally Available features in Microsoft Entra ID P2 will remain, but no new Identity Governance & Administration (IGA) features or capabilities will be added to the Microsoft Entra ID P2 SKU.

## Next steps

- [What is Microsoft Entra ID Governance?](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview)
