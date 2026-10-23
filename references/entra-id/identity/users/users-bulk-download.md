# Download a list of users in the Azure portal (Preview)

> Source: https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-download  
> Microsoft doc last updated: 08/19/2025


## Overview

Microsoft Entra ID, part of Microsoft Entra, supports bulk user list download operations.

## Required permissions

Both admin and standard users can download user lists.

## To download a list of users

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).
1. Select Microsoft Entra ID.
1. Select **Users** > **All users** > **Download users**. By default, all user profiles are exported.
1. On the **Download users** page, select **Start** to receive a CSV file listing user profile properties. If there are errors, you can download and view the results file on the **Bulk operation results** page. The file contains the reason for each error.

    

> [!NOTE]
> The download file will contain the filtered list of users based on the scope of the filters applied.

The following user attributes are included:

- `userPrincipalName`
- `displayName`
- `surname`
- `mail`
- `givenName`
- `objectId`
- `userType`
- `jobTitle`
- `department`
- `accountEnabled`
- `usageLocation`
- `streetAddress`
- `state`
- `country`
- `physicalDeliveryOfficeName`
- `city`
- `postalCode`
- `telephoneNumber`
- `mobile`
- `authenticationAlternativePhoneNumber`
- `authenticationEmail`
- `alternateEmailAddress`
- `ageGroup`
- `consentProvidedForMinor`
- `legalAgeGroupClassification`

## Check status

You can see the status of your pending bulk requests in the **Bulk operation results** page.

If you experience errors, you can download and view the results file on the **Bulk operation results** page. The file contains the reason for each error. The file submission must match the provided template and include the exact column names. For more information about bulk operations limitations, see [Bulk download service limits](#bulk-download-service-limits).

## Bulk download service limits

> [!NOTE]
> When performing bulk operations, such as import or create, you can encounter a problem if the bulk operation doesn't complete within the hour. To work around this issue, we recommend splitting the number of records processed per batch. For example, before starting an export you could limit the result set by filtering on a group type or user name to reduce the size of the results. By refining your filters, essentially you limit the data returned by the bulk operation. For more information, see [Bulk operations service limitations](https://learn.microsoft.com/en-us/entra/fundamentals/bulk-operations-service-limitations).

## Improved bulk user download in Microsoft Entra admin center (Preview)

The enhanced bulk user download experience includes: 

**Customizable columns for export**: Previously, user exports included only a fixed set of predefined attributes. With this update, admins can customize their User List View columns, and the export will mirror those selected columns. This gives IT admins greater control and relevance in the data they download.

**Expanded attribute coverage**: 27 new user attributes are now added to the exportable list, enabling deeper insights and more tailored exports. See full list of these newly exportable attributes:

1. Assigned licenses
1. Authorization info
1. Employee ID
1. Employee hire date
1. Employee org data
1. Employee type
1. Extension attributes
1. External user state change date time
1. Fax number
1. IM addresses
1. Last password change date time
1. Last interactive sign-in date
1. Last non-interactive sign-in date
1. On-premises SAM account name
1. On-premises distinguished name
1. On-premises domain name
1. On-premises immutable ID
1. On-premises last sync date time
1. On-premises provisioning errors
1. On-premises security identifier
1. On-premises user principal name
1. Password policies
1. Password profile
1. Preferred data location
1. Preferred language
1. Proxy addresses
1. Sign in sessions valid from date time

> [!NOTE]
> Columns derived from complex properties are exported as the entire complex property. For example, downloading the **Last interactive sign-in date** column results in the entire signInActivity property, along with all its related data fields, to be included in the CSV file.

### Performance improvements

The bulk download process is now up to 12 to 15 times faster, improving experience and efficiency for large user lists. This improvement also eliminates the service limitation that exists today which creates issues if the bulk operation doesn’t complete within 1 hour.

### User experience

1. Select the **Download users (Preview)** button from the command bar on the **All users** page.

    

1. When the context pane opens, select **Start download** and when that succeeds, select **File is ready! Click here to download** to download the CSV.

    

1. On the left menu, go to **Bulk operation results (Preview)** to view the status of your bulk download request. Only the preview download results will appear in this preview tab.

    

## Next steps

- [Bulk add users](https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-add)
- [Bulk delete users](https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-delete)
- [Bulk restore users](https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-restore)
