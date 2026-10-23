# Reprocess assignments for an access package in entitlement management

> Source: https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-reprocess-access-package-assignments  
> Microsoft doc last updated: 07/15/2024


As an access package manager, you can automatically reevaluate and enforce users’ original assignments in an access package using the reprocess functionality. Reprocessing eliminates the need for users to repeat the access package request process if their access to resources was impacted by changes outside of Entitlement Management.

For example, a user could have been removed from a group manually, thereby causing that user to lose access to necessary resources. 

Entitlement Management doesn't block outside updates to the access package’s resources, so the Entitlement Management UI wouldn't accurately display this change. Therefore, the user’s assignment status would be shown as “Delivered” even though the user doesn't have access to the resources anymore. However, if the user’s assignment is reprocessed, they're added to the access package’s resources again. Reprocessing ensures that the access package assignments are up to date, that users have access to necessary resources, and that assignments are accurately reflected in the UI.

This article describes how to reprocess assignments in an existing access package.

> [!NOTE]
> Reprocessing access package assignments in the Microsoft Entra admin center requires the signed-in user to be able to access the admin center. Entitlement management roles, such as Access package assignment manager, authorize assignment-management actions within entitlement management, but they don't by themselves change tenant-wide access settings for the admin center. If the **Restrict access to Microsoft Entra administration portal** user setting is enabled, verify that the delegated user can access the admin center, or use an authorized programmatic method. For more information about this setting, see [Default user permissions](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions).

## Prerequisites

To use entitlement management and assign users to access packages, you must have one of the following licenses:

- Microsoft Entra ID P2 or Microsoft Entra ID Governance
- Enterprise Mobility + Security (EMS) E5 license

## Open an existing access package and reprocess user assignments

If you have users who are in the "Delivered" state but don't have access to resources that are a part of the access package, you'll likely need to reprocess the assignments to reassign those users to the access package's resources. Follow these steps to reprocess assignments for an existing access package:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Identity Governance Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#identity-governance-administrator).
    > [!TIP]
    > Other least privilege roles that can complete this task include the Catalog owner, Access package manager, and Access package assignment manager.
1. Browse to **ID Governance** > **Entitlement management** > **Access package**.

1. On the Access packages page, open the access package with the user assignment you want to reprocess.

1. Underneath **Manage** on the left side, select **Assignments**.

    

1. Select all users whose assignments you wish to reprocess.

1. Select **Reprocess**.

## Next steps

- [View, add, and remove assignments for an access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-assignments)
- [View reports and logs](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-reports)
