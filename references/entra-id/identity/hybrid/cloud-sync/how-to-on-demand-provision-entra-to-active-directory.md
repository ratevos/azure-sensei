# On-demand provisioning - Microsoft Entra ID to Active Directory

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-on-demand-provision-entra-to-active-directory  
> Microsoft doc last updated: 08/24/2026


Microsoft Entra Cloud Sync lets you test configuration changes by applying them to a single user or group before you enable the configuration for all in-scope objects.

Use this test to validate and verify that the changes you made to the configuration were applied properly and that objects are correctly synchronized to Active Directory.

This article covers on-demand provisioning for configurations that provision from Microsoft Entra ID to Active Directory. If you're looking for information about provisioning from Active Directory to Microsoft Entra ID, see [On-demand provisioning - Active Directory to Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-on-demand-provision).

The following is true for on-demand group provisioning:
- On-demand provisioning of groups supports updating up to five members at a time.
- On-demand provisioning doesn't support deleting groups that are deleted from Microsoft Entra ID. Those groups don't appear when you search for a group.
- On-demand provisioning doesn't support nested groups that aren't directly assigned to the application.
- The on-demand provisioning request API can only accept a single group with up to five members at a time.

<a name='verify-a-group'></a>

## Verify a user or group

 1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator).

1. Browse to **Entra ID** > **Entra Connect** > **Cloud sync**.

   

 3. Under **Configuration**, select your configuration.
 4. On the left, select **Provision on demand**.
 5. Select the **Users** or **Groups** tab, depending on which object type you want to test.

    

Then follow the steps for the object type you selected.

# [Users](#tab/users)

1. In **Select a user**, search for the user by name, and then select the user.

   

1. Select **Provision**.

# [Groups](#tab/groups)

1. In **Selected group**, search for the group by name, and then select the group.
1. Under **Selected users**, select **View members only** to choose from the group's current members, or **View all users** to search the whole directory. Then select the members you want to test.

   > [!NOTE]
   > Members aren't provisioned automatically. Select the members you want to test, up to five at a time.

   

1. Select **Provision**.

---

## Review the result

The result lists four steps: importing the object, evaluating it against your scoping filters, matching it against the target system, and performing the action in Active Directory. Select **View details** on any step to see what was evaluated.

A step reports **Success** when it completes, or **Skipped** when there was nothing to do, such as when the object in Active Directory already matches. To run the same test again, select **Retry**. To test a different object, select **Provision another object**.

# [Users](#tab/users)

# [Groups](#tab/groups)

---

## Related content

- [Configure Microsoft Entra ID to Active Directory provisioning](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-configure-entra-to-active-directory)
- [Test and enable provisioning to Active Directory](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-test-and-enable-provisioning-entra-to-active-directory)
- [Group writeback with Microsoft Entra Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/group-writeback-cloud-sync)
- [Govern on-premises Active Directory based apps (Kerberos) using Microsoft Entra ID Governance](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/govern-on-premises-groups)
- [Migrate Microsoft Entra Connect Sync group writeback V2 to Microsoft Entra Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/migrate-group-writeback)
