# Bulk delete users in Microsoft Entra ID

> Source: https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-delete  
> Microsoft doc last updated: 09/25/2026


Using the admin center in Microsoft Entra ID, part of Microsoft Entra, you can remove a large number of users by using a comma-separated values (CSV) file to bulk delete users.

## Prerequisites

To bulk delete users in the Microsoft Entra admin center, sign in as at least a User Administrator.

## Bulk delete users

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator).
1. Select **Microsoft Entra ID**.
1. Select **Users** > **All users** > **Bulk operations** > **Bulk delete**.

    

1. On the **Bulk delete user** page, select **Download** to download the latest version of the CSV template.
1. Open the CSV file, preserve the column header exactly as downloaded, and add a line for each user you want to delete. For each user, enter either the **User principal name** or **Object ID**. Save the file.
1. On the **Bulk delete user** page, under **Upload your csv file**, browse to the file. When you select the file and select **Submit**, validation of the CSV file starts.
1. When the file contents are validated, you’ll see **File uploaded successfully**. If there are errors, you must fix them before you can submit the job.
1. When your file passes validation, select **Submit** to start the bulk operation that deletes the users.
1. When the deletion operation completes, you see a notification that the bulk operation succeeded.

If you experience errors, you can download and view the results file on the **Bulk operation results** page. The file contains the reason for each error. The file submission must match the provided template and include the exact column names.

For more information about bulk operations limitations, see [Bulk delete service limits](#bulk-delete-service-limits).

## CSV template structure

The rows in the example downloaded CSV template below are as follows:

- **Column headings**: Preserve `UserPrincipalName or Object ID [UPN or objectId] Required` exactly as downloaded.
- **Examples row**: You can keep the examples row in the CSV file. Add the users that you want to delete on the following rows. For each user, enter a user principal name (UPN) or object ID.

### Example CSV file

Here's an example of a completed CSV file ready for upload:

```csv
UserPrincipalName or Object ID [UPN or objectId] Required
chris@contoso.com
alain@contoso.com
00aa00aa-bb11-cc22-dd33-44ee44ee44ee
```

### Additional guidance for the CSV template

- Preserve the column headers exactly as downloaded. If the template includes a version row, preserve it.
- The required columns are listed first.
- We don't recommend adding new columns to the template. Any additional columns you add are ignored and not processed.
- We recommend that you download the latest version of the CSV template as often as possible.

- Enter one user per row.

## Check status

You can see the status of all of your pending bulk requests in the **Bulk operation results** page.

Next, you can check to see that the users you deleted exist in the Microsoft Entra organization either in the portal or by using PowerShell.

## Verify deleted users

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator).
1. Select **Microsoft Entra ID**.
1. Select **All users** only and verify that the users you deleted are no longer listed.

### Verify deleted users with PowerShell

Run the following command:

``` PowerShell
Get-MgUser -Filter "UserType eq 'Member'"
```

Verify that the users that you deleted are no longer listed.

## Bulk delete service limits

> [!NOTE]
> When performing bulk operations, such as import or create, you can encounter a problem if the bulk operation doesn't complete within the hour. To work around this issue, we recommend splitting the number of records processed per batch. For example, before starting an export you could limit the result set by filtering on a group type or user name to reduce the size of the results. By refining your filters, essentially you limit the data returned by the bulk operation. For more information, see [Bulk operations service limitations](https://learn.microsoft.com/en-us/entra/fundamentals/bulk-operations-service-limitations).

## Related content

- [Bulk add users](https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-add)
- [Download list of users](https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-download)
- [Bulk restore users](https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-restore)
