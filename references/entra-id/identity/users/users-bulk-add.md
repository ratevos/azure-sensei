# Bulk create users in the Azure portal

> Source: https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-add  
> Microsoft doc last updated: 09/25/2026


Microsoft Entra ID, part of Microsoft Entra, supports bulk user create and delete operations and supports downloading lists of users. Just fill out the comma-separated values (CSV) template you can download from Microsoft Entra ID.

## Prerequisites

To bulk create users in the Microsoft Entra admin center, sign in as at least a User Administrator.

## Understand the CSV template

Download and fill in the bulk upload CSV template to help you successfully create Microsoft Entra users in bulk. The CSV template you download might look like this example:

> [!WARNING]
> Ensure that you add the `.csv` file extension and remove any leading spaces before `userPrincipalName` and `passwordProfile`.

### CSV template structure

The rows in a downloaded CSV template are as follows:

- **Column headings**: Preserve the column headings exactly as downloaded. The required columns are `Name [displayName] Required`, `User name [userPrincipalName] Required`, and `Initial password [passwordProfile] Required`.
- **Examples row**: You can keep the examples row in the CSV file. Add the users that you want to create on the following rows.

### Additional guidance

- Preserve the column headers exactly as downloaded. If the template includes a version row, preserve it.
- The required columns are listed first.
- We don't recommend adding new columns to the template. Any additional columns you add are ignored and not processed.
- We recommend that you download the latest version of the CSV template as often as possible.

- Make sure to check there is no unintended whitespace before/after any field. For **User principal name**, having such whitespace would cause import failure.
- Ensure that values in **Initial password** comply with the currently active [password policy](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-policy#username-policies).
- Enter one user per row.

### Example CSV file

Here's an example of a completed CSV file ready for upload:

```csv
Name [displayName] Required,User name [userPrincipalName] Required,Initial password [passwordProfile] Required
Chris Green,chris@contoso.com,Example-Password-Only!1
Alain Charon,alain@contoso.com,Example-Password-Only!1
Isabella Simonsen,isabella@contoso.com,Example-Password-Only!1
Joseph Price,joseph@contoso.com,Example-Password-Only!1
```

> [!IMPORTANT]
> Only **Name**, **User name**, and **Initial password** are required. All other columns are optional and can be left empty.

## Create users in bulk

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator).
1. Browse to **Entra ID** > **Users** > **Bulk create**.
1. On the **Bulk create user** page, select **Download** to receive a valid comma-separated values (CSV) file of user properties, and then add users you want to create.

    

1. Open the CSV file, preserve the column headers exactly as downloaded, and add a line for each user you want to create. The only required values are **Name**, **User name**, and **Initial password**. Then save the file.

1. On the **Bulk create user** page, under Upload your CSV file, browse to the file. When you select the file and select **Submit**, validation of the CSV file starts.
1. After the file contents are validated, you’ll see **File uploaded successfully**. If there are errors, you must fix them before you can submit the job.
1. When your file passes validation, select **Submit** to start the bulk operation that imports the new users.
1. When the import operation completes, you see a notification of the bulk operation job status.

> [!NOTE]
> The bulk create operation creates internal member accounts with the passwords specified in the CSV file. No invitation emails are sent to the new users. You must communicate the sign-in credentials to the users through your own process. To bulk invite external guest users and send invitation emails, see [Bulk invite B2B users](https://learn.microsoft.com/en-us/entra/external-id/tutorial-bulk-invite).

If you experience errors, you can download and view the results file on the **Bulk operation results** page. The file contains the reason for each error. The file submission must match the provided template and include the exact column names.

For more information about bulk operations limitations, see [Bulk import service limits](#bulk-import-service-limits).

## Check status

You can see the status of all of your pending bulk requests in the **Bulk operation results** page.

Next, you can check to see that the users you created exist in the Microsoft Entra organization either in the Microsoft Entra admin center or by using PowerShell.

## Verify users

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator).
1. Select Microsoft Entra ID.
1. Select **Users** > **All users**.
1. Under **Show**, select **All users** and verify that the users you created are listed.

### Verify users with PowerShell

Run the following command:

``` PowerShell
Get-MgUser -Filter "UserType eq 'Member'"
```

You should see that the users that you created are listed.

## Bulk import service limits

> [!NOTE]
> When performing bulk operations, such as import or create, you can encounter a problem if the bulk operation doesn't complete within the hour. To work around this issue, we recommend splitting the number of records processed per batch. For example, before starting an export you could limit the result set by filtering on a group type or user name to reduce the size of the results. By refining your filters, essentially you limit the data returned by the bulk operation. For more information, see [Bulk operations service limitations](https://learn.microsoft.com/en-us/entra/fundamentals/bulk-operations-service-limitations).

## Related content

- [Bulk delete users](https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-delete)
- [Download list of users](https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-download)
- [Bulk restore users](https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-restore)
