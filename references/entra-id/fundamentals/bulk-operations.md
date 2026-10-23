# Bulk operations in Microsoft Entra ID (Preview)

> Source: https://learn.microsoft.com/en-us/entra/fundamentals/bulk-operations  
> Microsoft doc last updated: 06/18/2026


## Overview

The new bulk operations experience in Microsoft Entra ID provides enhanced capabilities for managing **Groups**, **Devices, Administrative Unit and Role assignments.** This service enables bulk actions including create, update, and delete operations. The improved service delivers better performance, reduces timeouts, and removes scaling limitations for large tenants.

> [!NOTE] 
> The new bulk operations service currently only supports **Groups**, **Devices**, **Users** export, **Administrative Unit and Role assignment**. Support for additional entities like **Enterprise applications** will be added in a future update. Localization for templates is partially supported (exported CSV doesn't have a localization template, but import and remove are supported). Additionally, guest users cannot initiate bulk operations. The new bulk operations service doesn't support exporting hidden memberships.

For information about limitations and to learn more about the previous Bulk Operations experience, see [Bulk operations service limitations](https://learn.microsoft.com/en-us/entra/fundamentals/bulk-operations-service-limitations).

## Bulk download groups

To download all groups in your organization:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/#view/Microsoft_AAD_IAM/GroupsManagementMenuBlade) and in the left-hand navigation pane, select the **Groups** tab and then **All groups**.

    

2. Select **Download groups**.

    

3. Enter a filename and select **Start bulk operation**.

    

4. Select the **Click here to view the status of each operation** link to navigate to the **Bulk operations** blade. 

    

5. Select the filename to download the CSV file containing all groups with the specified columns.

## Download filtered groups

To download a filtered subset of groups:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/#view/Microsoft_AAD_IAM/GroupsManagementMenuBlade) and in the left-hand navigation pane, select the **Groups** tab.

2. Select **Add filter** to open the **Manage filters** panel. Apply desired filters to narrow down the group list. Only selected columns appear in the CSV file.

    

3. Select **Download groups**.

4. Follow steps 3-5 from [Bulk download groups](#bulk-download-groups).

## Bulk download group members

To download all members of a specific group:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/#view/Microsoft_AAD_IAM/GroupsManagementMenuBlade) and in the left-hand navigation pane, select the **Groups** tab.

2. Select a group from the list and navigate to the **Members** tab.

    

3. On the **Members** page command bar, select **Download members**.

    If you see a **Bulk operations** menu instead, select **Bulk operations** > **Download members**.

4. Enter a filename and select **Start bulk operation**.

5. Follow the download process as described in [Bulk download groups](#bulk-download-groups).

## Bulk import group members in Microsoft Entra ID

To add multiple members to a group:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/#view/Microsoft_AAD_IAM/GroupsManagementMenuBlade) and in the left-hand navigation pane, select the **Groups** tab.

2. Select a group from the list and navigate to the **Members** tab.

3. Select **Bulk operations** > **Import members**.

    

4. Select **Download csv template** to get a template file with the correct column header. The template contains one column: `Member object ID or user principal name [memberObjectIdOrUpn] Required`. Delete the example row and add the Object IDs or UPNs for the members you want to import, one per row. You can use either:
   - **Object ID**: The GUID of the user (for example, `aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb`)
   - **User principal name**: The UPN of the user (for example, `user@contoso.com`)

    

5. Upload the completed CSV file and select **Submit**.

6. Monitor the notification for job completion. Select the **Success!** link to view the operation status. 

> [!IMPORTANT]
> If you add invalid Object IDs in the uploaded CSV file, the bulk operation status shows **Failed** with reason **NotAllRowsSuccessfullyProcessed**. You can select on the filename to download a detailed report showing the status of each object ID.

## Bulk remove group members 

To remove multiple members from a group:

1. Follow steps 1-2 from [Bulk download group members](#bulk-download-group-members).

2. Select **Bulk operations** > **Remove members**.

    

3. Select **Download csv template** to get a template file with the correct column header. The template contains one column: `Member object ID or user principal name [memberObjectIdOrUpn] Required`. Delete the example row and add the Object IDs or UPNs for the members you want to remove, one per row. You can use either:
   - **Object ID**: The GUID of the user (for example, `aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb`)
   - **User principal name**: The UPN of the user (for example, `user@contoso.com`)

4. Upload the completed CSV file and select **Submit**.

    

5. Monitor the notification for job completion. Select the **Success!** link to view the operation status.

6. If the operation shows **Failed** status with reason **NotAllRowsSuccessfullyProcessed**, select the filename to download a detailed report showing the status of each object ID.

7. Verify that the specified members were removed from the group.

## Delete bulk jobs

To delete completed or failed bulk operations:

1. Navigate to the [Bulk Operations (Preview)](https://entra.microsoft.com/?feature.tokencaching=true&feature.internalgraphapiversion=true&enableNewBulkJobsExport=true&enableNewBulkJobsList=true#view/Microsoft_AAD_IAM/BulkJobsList.ReactView) page.

   

2. Select the bulk job you want to delete.

3. Select **Delete**.

    

4. Confirm the deletion. The deleted job is removed from the list.

         

## Devices scenario steps

1. Go to the **All devices** blade.

    

2. Select **Download devices**.

    

3. Enter a filename that matches your naming convention and select **Start bulk operation**.
    

4. Verify the notification message and, if the job was submitted successfully, select the **Success!** or **File is ready! Click here to download** link.

    

5. Select the filename for the bulk job you created to download the CSV file. Verify the CSV contains all devices with the columns you selected when the bulk job was created.

You can bulk export users following the steps in [Download a list of users in Microsoft Entra admin center](https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-download).

## Add users to an administrative unit in a bulk operation

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/) as at least a [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator).

2. Browse to **Entra ID** > **Roles & admins** > **Admin units**.

3. Select the administrative unit you want to add users to.

4. Select **Users** > **Bulk operations** > **Bulk add members**.

    

5. In the **Bulk add members** pane, download the comma-separated values (CSV) template. Update and format the CSV as follows:

    Entries: Object Ids or UPN of members to add to the Admin Unit. Rename the file if desired, then select and upload the edited file.

6. Select **Submit** after successful upload.

    

7. Verify the notification message and ensure the job was submitted successfully.

    

8. Select **Success** to navigate to the bulk jobs list. You can sort by creation time to find your job, then select it to download.

    

    

> [!NOTE]
> Verify that the correct object IDs were added to the admin unit successfully. Refresh the UX if needed to see the updated state; it takes some time to reflect especially when adding groups to Admin Unit.
>
> If the input includes an invalid Object ID or one already assigned to this admin unit, the bulk operation status shows "Failed" instead of "Success" due to not all rows successfully processed. In the results csv, you will see the failure reason as 'The request was malformed or contains invalid parameters'. This is most likely due to the object being already assigned to this admin unit pre-operation. Other valid rows should still be processed successfully, please verify accordingly.

## Remove users from an administrative unit in a bulk operation

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/) as at least a [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator).

2. Browse to **Entra ID** > **Roles & admins** > **Admin units**.

3. Select the administrative unit that you want to remove users from.

4. Select **Users** > **Bulk operations** > **Bulk remove members**.

    

5. In the **Bulk remove members** pane, download the comma-separated values (CSV) template.

6. Don't change the first row of the template, and for each row fill in objectID or UPN of the users/devices/groups that you want to remove.

7. Save your changes and upload the CSV file.

8. Select **Submit**.

## Download Role Assignment

To download all active role assignments across all roles, including built-in and custom roles, follow these steps.

1. On the **Roles and administrators** page, select **All roles**.

2. Select **Download assignments**.

3. Select **Success** to navigate to the bulk jobs list. You can sort by creation time to find your job, then select it to download.

    

    

4. Sample output:

    

> [!NOTE]
> Filters and sorting are **not** supported for this bulk job type; this downloads all role assignments.

## Related content

- [Bulk operations service limitations](https://learn.microsoft.com/en-us/entra/fundamentals/bulk-operations-service-limitations)
- [Add or remove group members using Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-groups)
- [Bulk create users in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-add)
