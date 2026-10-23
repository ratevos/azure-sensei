# Bulk add group members by uploading a CSV file

> Source: https://learn.microsoft.com/en-us/entra/identity/users/groups-bulk-import-members  
> Microsoft doc last updated: 06/18/2026


## Overview

You can add multiple members to a group by using a comma-separated values (CSV) file to bulk import group members in the portal for Microsoft Entra ID.

## Understand the CSV template

Download and fill in the bulk upload CSV template to successfully add Microsoft Entra group members in bulk. Use the template that you download for the group member import operation. The current group member template starts with the column header, not a `version:v1.0` row.

### CSV template structure

The rows in a downloaded CSV template are:

- **Column headings**: Preserve the full downloaded column header exactly as-is. The property name in brackets is only one part of the header, so don't replace the full header with only `memberObjectIdOrUpn`. The current group member import header is `Member object ID or user principal name [memberObjectIdOrUpn] Required`. For group membership changes, you can use either the member object ID or the user principal name (UPN) in the rows under this header.
- **Examples row**: If the template includes a row of example values, such as `Example: 9832aad8-e4fe-496b-a604-95c6eF01ae75`, remove the examples row and replace it with your own entries.

> [!NOTE]
> CSV template formats vary by operation and can change. Download the latest template for your operation from the Microsoft Entra admin center. Preserve the column headers exactly as downloaded. If the template includes a version row, preserve it. If the template doesn't include a version row, don't add one. Follow the operation-specific instructions for handling the examples row.

### More guidance

- Preserve the column headers exactly as downloaded. If the template includes a version row, preserve it.
- The required columns are listed first.
- We don't recommend adding new columns to the template. Any additional columns you add are ignored and not processed.
- We recommend that you download the latest version of the CSV template as often as possible.

- Add at least two users' UPNs or object IDs to successfully upload the file.
- Enter one member per row. Don't use semicolons or other delimiters to separate multiple members in a single row.

### Example CSV file

Here's an example of a completed CSV file ready for upload, matching the current group member import template format. This example uses user principal names (UPNs):

```csv
Member object ID or user principal name [memberObjectIdOrUpn] Required
alain@contoso.com
isabella@contoso.com
joseph@contoso.com
chaya@contoso.com
```

Alternatively, you can use object IDs instead of UPNs:

```csv
Member object ID or user principal name [memberObjectIdOrUpn] Required
00aa00aa-bb11-cc22-dd33-44ee44ee44ee
11bb11bb-cc22-dd33-ee44-55ff55ff55ff
22cc22cc-dd33-ee44-ff55-66aa66aa66aa
```

> [!TIP]
> To find a user's object ID, go to **Identity** > **Users** > **All users**, select the user, and copy the **Object ID** from the user's profile page.

## Bulk import group members

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Groups Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#groups-administrator).
1. Navigate to **Identity**.
    > [!NOTE]
    > Group owners can also bulk import members of groups they own.
1. Select **Groups** > **All groups**.
1. Open the group to which you're adding members and then select **Members**.
1. On the **Members** page, select **Bulk operations** and then choose **Import members**.
1. On the **Bulk import group members** page, select **Download** to get the CSV file template with required group member properties.

    

1. Open the CSV file and add a line for each group member you want to import into the group. For each member, enter either their **User principal name** (UPN, such as `user@contoso.com`) or their **Object ID** (a GUID like `aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb`). Enter one member per row. Then save the file.

1. On the **Bulk import group members** page, under **Upload your csv file**, browse to the file. When you select the file, validation of the CSV file starts.
1. When the file contents are validated, the bulk import page displays **File uploaded successfully**. If there are errors, you must fix them before you can submit the job.
1. When your file passes validation, select **Submit** to start the bulk operation that imports the group members to the group.
1. When the import operation finishes, a notification states that the bulk operation succeeded.

If you experience errors, you can download and view the results file on the **Bulk operation results** page. The file contains the reason for each error. The file submission must match the provided template and include the exact column names.

For more information about bulk operations limitations, see [Bulk import service limits](#bulk-import-service-limits).

## Check import status

You can see the status of all of your pending bulk requests in the **Bulk operation results** page.

1. Navigate to **Identity** > **Users** > **Bulk operation results**.
1. Find your bulk operation in the list. The **Status** column shows whether the operation is **In Progress**, **Succeeded**, or **Failed**.

    

For details about each line item within the bulk operation, select the values under the **# Success**, **# Failure**, or **Total Requests** columns. If failures occurred, the reasons for failure are listed.

### Download the results file

To download detailed results:

1. On the **Bulk operation results** page, select the operation you want to review.
1. Select **Download** to get a CSV file containing the status of each row from your original upload.
1. Open the CSV file to see which members were added successfully and which failed, along with specific error messages.

Common errors include:
- **Member not found**: The UPN or object ID doesn't exist in your directory.
- **Member already exists**: The user is already a member of the group.
- **Invalid format**: The UPN or object ID format is incorrect.

## Bulk import service limits

> [!NOTE]
> When performing bulk operations, such as import or create, you can encounter a problem if the bulk operation doesn't complete within the hour. To work around this issue, we recommend splitting the number of records processed per batch. For example, before starting an export you could limit the result set by filtering on a group type or user name to reduce the size of the results. By refining your filters, essentially you limit the data returned by the bulk operation. For more information, see [Bulk operations service limitations](https://learn.microsoft.com/en-us/entra/fundamentals/bulk-operations-service-limitations).

## Next steps

- [Bulk remove group members](https://learn.microsoft.com/en-us/entra/identity/users/groups-bulk-remove-members)
- [Download members of a group](https://learn.microsoft.com/en-us/entra/identity/users/groups-bulk-download-members)
- [Download a list of all groups](https://learn.microsoft.com/en-us/entra/identity/users/groups-bulk-download)
