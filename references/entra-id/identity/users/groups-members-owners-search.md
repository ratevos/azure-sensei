# Search and filter groups members and owners (preview)

> Source: https://learn.microsoft.com/en-us/entra/identity/users/groups-members-owners-search  
> Microsoft doc last updated: 09/04/2025


## Overview

This article tells you how to search for members and owners of a group and how to use search filters in Microsoft Entra ID, part of Microsoft Entra. Search functions for groups include:

- Groups search capabilities, such as substring search in group names
- Filtering and sorting options on member and owner lists
- Search capabilities for member and owner lists

## Group search and sort

On the **All groups** page, when you enter a search string, you can toggle between **contains** and **starts with** searches on the **All groups** page only.

> [!IMPORTANT]
>The contains search uses tokenized matching, not literal substring matching. This means the system breaks both your query and the stored values into smaller chunks (tokens), usually words or alphanumeric segments, and checks if any query token appears in the stored tokens.

The substring search is done using whole words only, and any special characters are searched for also as an ANDed search. For example, searching for -Name starts a search for the substring "Name" and a search for "-". Substring search is case-sensitive. Object ID or mailNickname properties are also searched.

For example, a search for “policy” returns both "MDM policy – West" and "Policy group." A group named "New_policy" wouldn't be returned. You can sort the **All groups** list by name in ascending or descending order.

## Group member search and filter

### Search group member and owner lists

When you search the members or owners of a group, a tokenized contains search is automatically used. For example, a search for “Scott” returns both Scott Wilkinson and Maya Scott.

### Filter member and owner lists

You can also filter the group members and owners lists by user type. This information is found in the **User Type** column in the members or owners list. You can filter the list to see only members or guests.

The **Members** page includes all the unique members of group including anyone who inherits their group membership from another group.

You can also search and filter the lists individually. Filtering the all members list doesn't affect filters that are applied to the direct members list.

## Group memberships

You can also view group memberships on the **Group memberships** page. The **Group memberships** page supports search, sort, and filter operations that are similar to the other Groups pages.

## Group member counts

The group **Overview** page provides member counts for groups. You can see the total number of direct members for a group and the total membership count (all the unique members of group including inherited memberships) on the **Overview** page.

## Next steps

These articles provide additional information on working with groups in Microsoft Entra ID.

- [Manage Microsoft Entra groups and group membership](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-groups)
- [Manage rules for dynamic membership groups](https://learn.microsoft.com/en-us/entra/identity/users/groups-create-rule)
- [Manage access to resources using groups](https://learn.microsoft.com/en-us/entra/fundamentals/concept-learn-about-groups)
- [Manage access to SaaS apps using groups](https://learn.microsoft.com/en-us/entra/identity/users/groups-saasapps)
- [Manage groups using PowerShell commands](https://learn.microsoft.com/en-us/entra/identity/users/groups-settings-v2-cmdlets)
- [Add an Azure subscription to Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-subscriptions-associated-directory)
