# Authentication prompts analysis workbook

> Source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/workbook-authentication-prompts-analysis  
> Microsoft doc last updated: 11/04/2024


As an IT Pro, you want the right information about authentication prompts in your environment so you can detect unexpected prompts and investigate further. Providing you with this type of information is the goal of the **Authentication Prompts Analysis** workbook. 

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

## Description

Have you recently received complaints from your users about getting too many authentication prompts?

Over-prompting users can affect productivity and can lead to users getting phished for multifactor authentication (MFA). To be clear, we aren't talking about *if* you should require MFA but *how frequently you should prompt your users*.

The following factors can cause over prompting:

- Misconfigured applications
- Over aggressive prompts policies 
- Cyber-attacks 
 
The authentication prompts analysis workbook identifies various types of authentication prompts. The types are based on different factors including users, applications, operating system, processes, and more.

You can use this workbook in the following scenarios:

- To research feedback of users getting too many prompts.
- To detect over-prompting attributed to one specific authentication method, policy application, or device.
- To view authentication prompt counts of high-profile users.
- To track legacy TLS and other authentication process details.

## How to access the workbook

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) using the appropriate combination of roles.

1. Browse to **Entra ID** > **Monitoring & health** > **Workbooks**.

1. Select the **Authentication Prompts Analysis** workbook from the **Usage** section.

## Workbook sections

This workbook breaks down authentication prompts by: 

- Method
- Device state
- Application
- User
- Status
- Operating System
- Process detail
- Policy

In many environments, the most used apps are business productivity apps. Anything that isn’t expected should be investigated. The following charts show authentication prompts by application.

The **prompts by application list view** shows additional information such as timestamps, and request IDs that help with investigations.

Additionally, you get a summary of the average and median prompts count for your tenant. 

This workbook also helps track impactful ways to improve your users’ experience and reduce prompts and the relative percentage.  

 
## Filters

Take advantage of the filters for more granular views of the data: 

Filtering for a specific user that has many authentication requests or only showing applications with sign-in failures can also lead to interesting findings to continue to remediate. 

## Best practices

- If data isn't showing up or seems to be showing up incorrectly, confirm that you set the **Log Analytics Workspace** and **Subscriptions** on the proper resources.

    

- If the visuals are taking too much time to load, try reducing the Time filter to 24 hours or less.

    

- To understand more about the different policies that affect MFA prompts, see [Optimize reauthentication prompts and understand session lifetime for Microsoft Entra multifactor authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/concepts-azure-multi-factor-authentication-prompts-session-lifetime). 

- To learn how to move users from telecom-based methods to the Authenticator app, see [How to run a registration campaign to set up Microsoft Authenticator - Microsoft Authenticator app](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-mfa-registration-campaign).

## Related content

- [How to use the identity workbooks](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-use-workbooks)
- [Manage the 'Stay signed in?' prompt](../../fundamentals/how-to-manage-stay-signed-in-prompt.yml)
- [How MFA works](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-howitworks)
