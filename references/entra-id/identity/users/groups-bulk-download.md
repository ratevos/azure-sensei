# Download a list of groups in the Azure portal

> Source: https://learn.microsoft.com/en-us/entra/identity/users/groups-bulk-download  
> Microsoft doc last updated: 12/05/2025


## Overview

You can download a list of all the groups in your organization to a comma-separated values (CSV) file in the portal for Microsoft Entra ID. All admins and nonadmin users can download group lists.

## Bulk download groups

To download all groups in your organization:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/#view/Microsoft_AAD_IAM/GroupsManagementMenuBlade) and in the left-hand navigation pane, select the **Groups** tab and then **All groups**.

    

1. Select **Download groups**.

    

1. Enter a filename and select **Start bulk operation**.

    

1. A **Success!** notification appears when the job is submitted. The notification says "Bulk operation download groups submission successful. Click on the title for more information."

1. Select the **Success!** notification title to open the job details, then select the filename to download the CSV file. A **Download successful** notification confirms when the file has been downloaded.

> [!TIP]
> You can also select **Click here to view the status of each operation** in the download dialog to navigate directly to the **Bulk operation results** page, where you can monitor all pending and completed bulk operations.

### Downloaded CSV file format

The downloaded CSV file contains information about each group, including:

| Column | Description |
|--------|-------------|
| Object ID | The unique identifier (GUID) of the group |
| Display name | The display name of the group |
| Mail | The email address associated with the group (if applicable) |
| Group type | Security or Microsoft 365 |
| Membership type | Assigned or Dynamic |

> [!TIP]
> You can use the downloaded CSV file to get object IDs that you need for other bulk operations, such as adding members to groups.

## Download filtered groups

To download a filtered subset of groups:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/#view/Microsoft_AAD_IAM/GroupsManagementMenuBlade) and in the left-hand navigation pane, select the **Groups** tab.
1. Select **Manage filters** to edit the column filters.
1. Select **Download groups**.
1. Follow steps 3-5 from [Bulk download groups](#bulk-download-groups).

> [!NOTE]
> When filtering groups, only the selected columns appear in the CSV file after editing filters.

If you experience errors, you can download and view the results file on the **Bulk operation results** page. The file contains the reason for each error. The file submission must match the provided template and include the exact column names. For more information about bulk operations limitations, see [Bulk download service limits](#bulk-download-service-limits).

## Check download status

You can see the status of all of your pending bulk requests in the **Bulk operation results** page.

## Bulk download service limits

> [!NOTE]
> When performing bulk operations, such as import or create, you can encounter a problem if the bulk operation doesn't complete within the hour. To work around this issue, we recommend splitting the number of records processed per batch. For example, before starting an export you could limit the result set by filtering on a group type or user name to reduce the size of the results. By refining your filters, essentially you limit the data returned by the bulk operation. For more information, see [Bulk operations service limitations](https://learn.microsoft.com/en-us/entra/fundamentals/bulk-operations-service-limitations).

## Next steps

- [Bulk remove group members](https://learn.microsoft.com/en-us/entra/identity/users/groups-bulk-remove-members)
- [Download members of a group](https://learn.microsoft.com/en-us/entra/identity/users/groups-bulk-download-members)
