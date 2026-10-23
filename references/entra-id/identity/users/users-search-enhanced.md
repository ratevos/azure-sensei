# User management enhancements

> Source: https://learn.microsoft.com/en-us/entra/identity/users/users-search-enhanced  
> Microsoft doc last updated: 01/06/2025


## Overview

This article describes how to use the user management enhancements in the Microsoft Entra admin center. In this article, you review the **All users** and **user profile** pages.

Enhancements include:

- Preloaded scrolling so that you no longer have to select **Load more** to view more users.
- More user properties can be added as columns including city, country/region, employee ID, employee type, and external user state.
- More user properties can be filtered on including custom security attributes, on-premises extension attributes, and manager.
- More ways to customize your view, like using drag-and-drop to reorder columns.
- Copy and share your customized All Users view with others.
- An enhanced User Profile experience that gives you quick insights about a user and lets you view and edit more properties.

> [!NOTE]
> These enhancements aren't currently available for Azure AD B2C tenants.

## All users page

The columns and filters available on the **All users** page have been updated. In addition to the existing columns for managing your list of users, the option to add more user properties as columns and filters including employee ID, employee hire date, on-premises attributes, and more has been added.

### Reorder columns

You can customize your list view by reordering the columns on the page in one of two ways. One way is to directly drag and drop the columns on the page. Another way is to select **Columns** to open the column picker and then drag and drop the three-dot "handle" next to any given column.

### Share views

If you want to share your customized list view with another person, you can select **Copy link to current view** in the upper right corner to share a link to the view. 

## User profile enhancements

The user profile page is now organized into three tabs: **Overview**, **Monitoring**, and **Properties**.  

### Overview tab 

The overview tab contains key properties and insights about a user, such as: 

- Properties like user principal name, object ID, created date/time, and user type 
- Selectable aggregate values such as the number of groups that the user is a member of, the number of apps to which they have access, and the number of licenses that are assigned to them 
- Quick alerts and insights about a user such as their current account enabled status, the last time they signed in, whether they can use multifactor authentication, and B2B collaboration options

> [!NOTE] 
> Some insights about a user may not be visible to you unless you have sufficient role permissions.  

### Monitoring tab 

The monitoring tab is the new home for the chart showing user sign-ins over the past 30 days.  

### Properties tab 

The properties tab now contains more user properties. Properties are broken up into categories including Identity, Job information, Contact information, Parental controls, Settings, and On-premises.  

You can edit properties by selecting the pencil icon next to any category, which will then redirect you to a new editing experience. Here, you can search for specific properties or scroll through property categories. You can edit one or many properties, across categories, before selecting **Save**. 

> [!NOTE] 
> Some properties won't be visible or editable if they are read-only or if you don’t have sufficient role permissions to edit them. 

## Next steps

**User operations**

- [Add or change profile information](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-user-profile-info)
- [Add or delete users](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-create-delete-users)

**Bulk operations**

- [Bulk operations service limitations](https://learn.microsoft.com/en-us/entra/fundamentals/bulk-operations-service-limitations)
- [Download list of users](https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-download)
- [Bulk add users](https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-add)
- [Bulk delete users](https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-delete)
- [Bulk restore users](https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-restore)
