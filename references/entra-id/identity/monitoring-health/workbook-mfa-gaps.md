# Multifactor Authentication Gaps workbook

> Source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/workbook-mfa-gaps  
> Microsoft doc last updated: 11/04/2024


The Multifactor Authentication Gaps workbook helps with identifying user sign-ins and applications that aren't protected by multifactor authentication (MFA) requirements. This workbook:
* Identifies user sign-ins not protected by MFA requirements.
* Provides further drill down options using various pivots such as applications, operating systems, and location.
* Provides several filters such as trusted locations and device states to narrow down the users/applications. 
* Provides filters to scope the workbook for a subset of users and applications.

This article gives you an overview of the **Multifactor authentication gaps** workbook.

## Prerequisites

To use Azure Workbooks for Microsoft Entra ID, you need:

- A Microsoft Entra tenant with a [Premium P1 license](https://learn.microsoft.com/en-us/entra/fundamentals/get-started-premium)
- A Log Analytics workspace *and* access to that workspace
- The appropriate roles for Azure Monitor *and* Microsoft Entra ID

### Log Analytics workspace

You must create a [Log Analytics workspace](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/quick-create-workspace) *before* you can use Microsoft Entra Workbooks. several factors determine access to Log Analytics workspaces. You need the right roles for the workspace *and* the resources sending the data.

For more information, see [Manage access to Log Analytics workspaces](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/manage-access).

### Azure Monitor roles

Azure Monitor provides [two built-in roles](https://learn.microsoft.com/en-us/azure/azure-monitor/roles-permissions-security#monitoring-reader) for viewing monitoring data and editing monitoring settings. Azure role-based access control (RBAC) also provides two Log Analytics built-in roles that grant similar access.

- **View**:
  - Monitoring Reader
  - Log Analytics Reader

- **View and modify settings**:
  - Monitoring Contributor
  - Log Analytics Contributor

### Microsoft Entra roles
<a name='azure-ad-roles'></a>

Read only access allows you to view Microsoft Entra ID log data inside a workbook, query data from Log Analytics, or read logs in the Microsoft Entra admin center. Update access adds the ability to create and edit diagnostic settings to send Microsoft Entra data to a Log Analytics workspace.

- **Read**:
  - Reports Reader
  - Security Reader
  - Global Reader

- **Update**:
  - Security Administrator

For more information on Microsoft Entra built-in roles, see [Microsoft Entra built-in roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference).

For more information on the Log Analytics RBAC roles, see [Azure built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#log-analytics-contributor).

## How to import the workbook

The **MFA gaps** workbook is currently not available as a template, but you can import it from the Microsoft Entra workbooks GitHub repository.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) using the appropriate combination of roles.
1. Browse to **Entra ID** > **Monitoring & health** > **Workbooks**.
1. Select **+ New**.
1. Select the **Advanced Editor** button from the top of the page. A JSON editor opens.

    

1. Use the following link to access the GitHub repository that contains the JSON file for the **Multifactor Authentication Gaps** workbook:
    - **Direct link to the Multifactor Authentication Gaps JSON file**: https://github.com/microsoft/Application-Insights-Workbooks/blob/master/Workbooks/Azure%20Active%20Directory/MultiFactorAuthenticationGaps/MultiFactorAuthenticationGaps.workbook
    - Make sure you're on the *MultiFactorAuthenticationGaps.workbook* file in the GitHub repository.

1. Copy the entire JSON file from the GitHub repository.

    

1. Return to the workbook Advanced Editor window and paste the JSON file over the existing text.
1. Select the **Apply** button. The workbook might take a few moments to populate.
1. Select **Done Editing** and then select the **Save** button and provide the required information.
    - Provide a **Title**, **Subscription**, **Resource Group** (you must have the ability to save a workbook for the selected Resource Group), and **Location**.
    - Optionally choose to save your workbook content to an [Azure Storage Account](https://learn.microsoft.com/en-us/azure/azure-monitor/visualize/workbooks-bring-your-own-storage).
1. Select the **Apply** button.

## Summary
The summary widget provides a detailed look at sign-ins related to multifactor authentication.

### Sign-ins not protected by MFA requirement by applications

* **Number of users signing-in not protected by multi-factor authentication requirement by application:** This widget provides a time based bar-graph representation of the number of user sign-ins not protected by MFA requirement by applications.
* **Percent of users signing-in not protected by multi-factor authentication requirement by application:** This widget provides a time based bar-graph representation of the percentage of user sign-ins not protected by MFA requirement by applications.
* **Select an application and user to learn more:** This widget groups the top users signed in without MFA requirement by application. Select the application to see a list of the user names and the count of sign-ins without MFA.

### Sign-ins not protected by MFA requirement by users
* **Sign-ins not protected by multi-factor auth requirement by user:** This widget shows top user and the count of sign-ins not protected by MFA requirement.
* **Top users with high percentage of authentications not protected by multi-factor authentication requirements:** This widget shows users with top percentage of authentications that aren't protected by MFA requirements.

### Sign-ins not protected by MFA requirement by Operating Systems
* **Number of sign-ins not protected by multi-factor authentication requirement by operating system:** This widget provides time based bar graph of sign-in counts that aren't protected by MFA by operating system of the devices.
* **Percent of sign-ins not protected by multi-factor authentication requirement by operating system:** This widget provides time based bar graph of sign-in percentages that aren't protected by MFA by operating system of the devices.

### Sign-ins not protected by MFA requirement by locations
* **Number of sign-ins not protected by multi-factor authentication requirement by location:** This widget shows the sign-ins counts that aren't protected by MFA requirement in map bubble chart on the world map.

## Related content

- [How to use the identity workbooks](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-use-workbooks)
- [Conditional Access gap analyzer workbook](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/workbook-conditional-access-gap-analyzer)
