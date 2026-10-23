# Lifecycle Workflows templates and categories

> Source: https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-templates  
> Microsoft doc last updated: 04/25/2026


Lifecycle Workflows allows you to automate the lifecycle management process for your organization by creating workflows that contain both built-in tasks, and custom task extensions. These workflows, and the tasks within them, all fall into categories based on the Joiner-Mover-Leaver(JML) model of lifecycle management. To make this process even more efficient, Lifecycle Workflows also provide you with templates, which you can use to accelerate the setup, creation, and configuration of common lifecycle management processes. You can create workflows based on these templates as is, or you can customize them even further to match the requirements for users within your organization. In this article, you get the complete list of workflow templates, common template parameters, default template parameters for specific templates, and the list of compatible tasks for each template. For full task definitions, see [Lifecycle Workflow tasks and definitions](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-tasks).

## Lifecycle Workflows built-in templates

Lifecycle Workflows currently have 14 built-in templates you can use or customize:

The list of templates is as follows:

- [Onboard pre-hire employee](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-templates#onboard-pre-hire-employee)
- [Onboard new hire employee](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-templates#onboard-new-hire-employee)
- [Post-Onboarding of an employee](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-templates#post-onboarding-of-an-employee)
- [Real-time employee change](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-templates#real-time-employee-change)
- [Real-time employee termination](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-templates#real-time-employee-termination)  
- [Pre-Offboarding of an employee](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-templates#pre-offboarding-of-an-employee)
- [Offboard an employee](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-templates#offboard-an-employee)
- [Post-Offboarding of an employee](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-templates#post-offboarding-of-an-employee)
- [Employee group membership changes](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-templates#employee-group-membership-changes)
- [Employee job profile change](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-templates#employee-job-profile-change)
- [Pre-Offboard inactive users](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-templates#pre-offboard-inactive-users)
- [Offboard inactive users](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-templates#offboard-inactive-users)
- [Transition agent sponsorships when a sponsor leaves](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-templates#transition-agent-sponsorships-when-a-sponsor-leaves)
- [Transition agent sponsorships when a sponsor changes roles](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-templates#transition-agent-sponsorships-when-a-sponsor-changes-roles)

For a complete guide on creating a new workflow from a template, see: [Tutorial: On-boarding users to your organization using Lifecycle workflows with the Microsoft Entra admin center](https://learn.microsoft.com/en-us/entra/id-governance/tutorial-onboard-custom-workflow-portal).

> [!NOTE]
> Lifecycle workflows enhances Microsoft Entra ID Governance's [HR-driven provisioning](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/what-is-hr-driven-provisioning) by automating routine processes. While HR provisioning manages the creation and attribute updates of user accounts, lifecycle workflows provide additional automation of tasks.

### Onboard pre-hire employee

 The **Onboard pre-hire employee** template is designed to configure tasks that must be completed before an employee's start date.

The default specific parameters and properties for the **Onboard pre-hire employee** template are as follows:

|Parameter  |Description  |Customizable  |
|---------|---------|---------|
|Category     |  Joiner       |  ❌       |
|Trigger Type     | Time based attribute, Attribute changes, Group Membership change        |  ✔️       |
|Trigger details     | Depends on trigger type selection. <br> • **Time based**:  Days from event, Event timing, Event user attribute<br> • **Attribute changes**: Trigger attribute <br>• **Group membership changes**: Added to group/Remove from group    |   ✔️      |
|Days from event     | -7        | ✔️        |
|Event timing     | Before        |  ❌       |
|Event User attribute     | EmployeeHireDate        |   ❌      |
|Scope     | Depends on trigger. <br> **Rule based**: Time based attribute, Attribute changes.<br> **Group membership change**: Group based.         | ✔️        |
|Tasks     | **Generate TAP And Send Email**     |  ✔️       |

For a tutorial on setting up a workflow that uses the **Onboard pre-hire employee** template, see: [Automate employee onboarding tasks before their first day of work with the Microsoft Entra admin center](https://learn.microsoft.com/en-us/entra/id-governance/tutorial-onboard-custom-workflow-portal).

### Onboard new hire employee

The **Onboard new-hire employee** template is designed to configure tasks that are completed on an employee's start date.

The default specific parameters for the **Onboard new hire employee** template are as follows:

|Parameter  |Description  |Customizable  |
|---------|---------|---------|
|Category     |  Joiner       |  ❌       |
|Trigger Type     | Time based attribute, Attribute changes, Group Membership change          |  ✔️       |
|Trigger details     | Depends on trigger type selection. <br> • **Time based**:  Days from event, Event timing, Event user attribute<br> • **Attribute changes**: Trigger attribute <br>• **Group membership changes**: Added to group/Remove from group    |   ✔️      |
|Days from event     | 0        | ❌        |
|Event timing     | On        |  ❌       |
|Event User attribute     | EmployeeHireDate, createdDateTime        |   ✔️      |
|Scope     | Depends on trigger. <br> **Rule based**: Time based attribute, Attribute changes.<br> **Group membership change**: Group based.         | ✔️        |
|Tasks     | **Add User To Group**, **Enable User Account**, **Send Welcome Email**      |  ✔️       |

### Post-Onboarding of an employee

The **Post-Onboarding of an employee** template is designed to configure tasks that are completed after an employee's start, or creation, date.

The default specific parameters for the **Post-Onboarding of an employee** template are as follows:

|Parameter  |Description  |Customizable  |
|---------|---------|---------|
|Category     |  Joiner       |  ❌       |
|Trigger Type     | Time based attribute, Attribute changes, Group Membership change       |  ✔️       |
|Trigger details     | Depends on trigger type selection. <br> • **Time based**:  Days from event, Event timing, Event user attribute<br> • **Attribute changes**: Trigger attribute <br>• **Group membership changes**: Added to group/Remove from group     |   ✔️      |
|Days from event     | 7       | ✔️        |
|Event timing     | After        |  ❌       |
|Event User attribute     | EmployeeHireDate, createdDateTime        |   ✔️      |
|Scope     | Depends on trigger. <br> **Rule based**: Time based attribute, Attribute changes.<br> **Group membership change**: Group based.         | ✔️        |
|Tasks     | **Add User To Group**, **Add user to selected teams**    |  ✔️       |

### Real-time employee change

The **Real-time employee change** template is designed to configure tasks that are completed immediately when an employee changes roles.

The default specific parameters for the **Real-time employee change** template are as follows:

|Parameter  |Description  |Customizable  |
|---------|---------|---------|
|Category     |  Mover       |  ❌       |
|Trigger Type     | On-demand        |  ❌       |
|Tasks     | **Run a Custom Task Extension**, **Remove all access package assignments for user** (scheduled removal defaulting to 15 days)    |  ✔️       |

> [!NOTE]
> As this template is designed to run on-demand, no execution condition is present.

### Real-time employee termination

The **Real-time employee termination** template is designed to configure tasks that are completed immediately when an employee is terminated.

The default specific parameters for the **Real-time employee termination** template are as follows:

|Parameter  |Description  |Customizable  |
|---------|---------|---------|
|Category     |  Leaver       |  ❌       |
|Trigger Type     | On-demand        |  ❌       |
|Tasks     | **Remove user from all groups**, **Delete User Account**, **Remove user from all Teams**      |  ✔️       |

> [!NOTE]
> As this template is designed to run on-demand, no execution condition is present.

### Pre-Offboarding of an employee

The **Pre-Offboarding of an employee** template is designed to configure tasks that are completed before an employee's last day of work.

The default specific parameters for the **Pre-Offboarding of an employee** template are as follows:

|Parameter  |Description  |Customizable  |
|---------|---------|---------|
|Category     |  Leaver       |  ❌       |
|Trigger Type     | Time based attribute, Attribute changes, Group Membership change         |  ✔️       |
|Trigger details     | Depends on trigger type selection. <br> • **Time based**:  Days from event, Event timing, Event user attribute<br> • **Attribute changes**: Trigger attribute <br>• **Group membership changes**: Added to group/Remove from group    |   ✔️      |
|Days from event     | 7        | ✔️        |
|Event timing     | Before        |  ❌       |
|Event User attribute     | employeeLeaveDateTime        |   ❌      |
|Scope     | Depends on trigger. <br> **Rule based**: Time based attribute, Attribute changes.<br> **Group membership change**: Group based.         | ✔️        |
|Tasks     | **Remove user from selected groups**, **Remove user from selected Teams**     |  ✔️       |

### Offboard an employee

The **Offboard an employee** template is designed to configure tasks that are completed on an employee's last day of work.

The default specific parameters for the **Offboard an employee** template are as follows:

|Parameter  |Description  |Customizable  |
|---------|---------|---------|
|Category     |  Leaver       |  ❌       |
|Trigger Type     | Time based attribute, Attribute changes, Group Membership change        |  ✔️       |
|Trigger details     | Depends on trigger type selection. <br> • **Time based**:  Days from event, Event timing, Event user attribute<br> • **Attribute changes**: Trigger attribute <br>• **Group membership changes**: Added to group/Remove from group    |   ✔️      |
|Days from event     | 0        | ✔️        |
|Event timing     | On        |  ❌       |
|Event User attribute     | employeeLeaveDateTime      |   ❌      |
|Scope     | Depends on trigger. <br> **Rule based**: Time based attribute, Attribute changes.<br> **Group membership change**: Group based.         | ✔️        |
|Tasks     | **Disable User Account**, **Remove user from all groups**, **Remove user from all Teams**     |  ✔️       |

### Post-Offboarding of an employee

The **Post-Offboarding of an employee** template is designed to configure tasks that are completed after an employee's last day of work.

The default specific parameters for the **Post-Offboarding of an employee** template are as follows:

|Parameter  |Description  |Customizable  |
|---------|---------|---------|
|Category     |  Leaver       |  ❌       |
|Trigger Type     | Time based attribute, Attribute changes, Group Membership change        |  ✔️       |
|Trigger details     | Depends on trigger type selection. <br> • **Time based**:  Days from event, Event timing, Event user attribute<br> • **Attribute changes**: Trigger attribute <br>• **Group membership changes**: Added to group/Remove from group     |   ✔️      |
|Event User attribute     | employeeLeaveDateTime      |   ❌      |
|Scope     | Depends on trigger. <br> **Rule based**: Time based attribute, Attribute changes.<br> **Group membership change**: Group based.         | ✔️        |
|Tasks     | **Remove all licenses for user**, **Remove user from all Teams**, **Delete User Account**     |  ✔️       |

For a tutorial on setting up a workflow that uses the **Post-Offboarding of an employee** template, see: [Automate employee offboarding tasks after their last day of work with the Microsoft Entra admin center](https://learn.microsoft.com/en-us/entra/id-governance/tutorial-scheduled-leaver-portal).

### Employee group membership changes

The **Employee group membership changes** template is designed to configure tasks that are completed when an employee has a change in a group membership.

The default specific parameters for the **Employee group membership changes** template are as follows:

|Parameter  |Description  |Customizable  |
|---------|---------|---------|
|Category     |  mover       |  ❌       |
|Trigger Type     | Attribute changes, Group Membership change        |  ✔️       |
|Trigger details     | Depends on trigger type selection. <br> • **Attribute changes**: Trigger attribute <br>• **Group membership changes**: Added to group/Remove from group    |   ✔️      |
|Scope     | Depends on trigger. <br> **Rule based**: Attribute changes.<br> **Group membership change**: Group based.       | ✔️        |
|Tasks     | **Remove all access package assignments for user** (scheduled removal defaulting to 15 days), **Remove user from selected Teams**, **Send email to notify manager of user move**     |  ✔️       |

### Employee job profile change

The **Employee job profile change** template is designed to configure tasks that are completed when an employee has a change in job title.

The default specific parameters for the **Employee job profile change** template are as follows:

|Parameter  |Description  |Customizable  |
|---------|---------|---------|
|Category     |  mover       |  ❌       |
|Trigger Type     | Attribute changes, Group Membership change        |  ✔️       |
|Trigger details     | Depends on trigger type selection. <br> • **Attribute changes**: Trigger attribute <br>• **Group membership changes**: Added to group/Remove from group    |   ✔️      |
|Scope     | Depends on trigger. <br> **Rule based**: Attribute changes.<br> **Group membership change**: Group based.         | ✔️        |
|Tasks     | **Send email to notify manager of user move**, **Remove all access package assignments for user** (scheduled removal defaulting to 15 days), **Remove user from selected groups**, **Remove user from selected Teams**, **Request user access package assignment**    |  ✔️       |

For a tutorial on setting up a workflow that uses the **Employee job profile change** template, see: [Automate employee mover tasks when they change jobs using the Microsoft Entra admin center](https://learn.microsoft.com/en-us/entra/id-governance/tutorial-mover-custom-workflow-portal).

### Pre-Offboard inactive users

The **Pre-Offboard inactive users** template is designed to configure tasks that must be completed before offboarding inactive users.

The default specific parameters for the **Pre-Offboard inactive users** template are as follows:

|Parameter  |Description  |Customizable  |
|---------|---------|---------|
|Category     |  Leaver       |  ❌       |
|Trigger Type     | Sign-in inactivity, Attribute changes, Group Membership change      |  ✔️       |
|Trigger details     | Depends on trigger type selection. <br> • **Sign-in inactivity**:  Days of inactivity<br> • **Attribute changes**: Trigger attribute <br>• **Group membership changes**: Added to group/Remove from group    |   ✔️      |
|Days of inactivity     | 90       | ✔️        |
|Event timing     | Before        |  ❌       |
|Event User attribute     | lastSuccessfulSignInDateTime        |   ❌      |
|Scope     | Depends on trigger. <br> **Rule based**: Time based attribute, Attribute changes.<br> **Group membership change**: Group based.         | ✔️        |
|Tasks     | **Disable user account**, **Send inactivity notification email**     |  ✔️       |

### Offboard inactive users

The **Offboard inactive users** template is designed to configure tasks that must be completed to offboard inactive users.

The default specific parameters for the **Offboard inactive users** template are as follows:

|Parameter  |Description  |Customizable  |
|---------|---------|---------|
|Category     |  Leaver       |  ❌       |
|Trigger Type     | Sign-in inactivity, Attribute changes, Group Membership change         |  ✔️       |
|Trigger details     | Depends on trigger type selection. <br> • **Sign-in inactivity**:  Days of inactivity <br> • **Attribute changes**: Trigger attribute <br>• **Group membership changes**: Added to group/Remove from group    |   ✔️      |
|Days from event     | 120        | ✔️        |
|Event timing     | After        |  ❌       |
|Event User attribute     | lastSuccessfulSignInDateTime        |   ❌      |
|Scope     | Depends on trigger. <br> **Rule based**: Time based attribute, Attribute changes<br> **Group membership change**: Group based.         | ✔️        |
|Tasks     | **Disable user account**, **Send inactivity notification email**     |  ✔️       |

### Transition agent sponsorships when a sponsor leaves

The **Transition agent sponsorships when a sponsor leaves** template is designed to configure tasks that transition agent sponsorships when a sponsor leaves the organization. This template is available for tenants with the Microsoft Agent 365 license. For more information, see: [Microsoft Agent 365 Documentation](https://aka.ms/entraagent365).

The default specific parameters for the **Transition agent sponsorships when a sponsor leaves** template are as follows:

|Parameter  |Description  |Customizable  |
|---------|---------|---------|
|Category     |  Leaver       |  ❌       |
|Trigger Type     | Time based attribute, Attribute changes, Group Membership change        |  ✔️       |
|Trigger details     | Depends on trigger type selection. <br> • **Time based**:  Days from event, Event timing, Event user attribute<br> • **Attribute changes**: Trigger attribute <br>• **Group membership changes**: Added to group/Remove from group    |   ✔️      |
|Days from event     | 0        | ✔️        |
|Event timing     | On        |  ❌       |
|Event User attribute     | employeeLeaveDateTime        |   ❌      |
|Scope     | Depends on trigger. <br> **Rule based**: Time based attribute, Attribute changes.<br> **Group membership change**: Group based.         | ✔️        |
|Tasks     | **Send email to manager about sponsorship changes**, **Send email to co-sponsors about sponsor changes**, **Transfer agent sponsorships to manager**     |  ✔️       |

### Transition agent sponsorships when a sponsor changes roles

The **Transition agent sponsorships when a sponsor changes roles** template is designed to configure tasks that transition agent sponsorships when a sponsor changes roles within the organization. This template is available for tenants with the Microsoft Agent 365 license. For more information, see: [Microsoft Agent 365 Documentation](https://aka.ms/entraagent365).

The default specific parameters for the **Transition agent sponsorships when a sponsor changes roles** template are as follows:

|Parameter  |Description  |Customizable  |
|---------|---------|---------|
|Category     |  Mover       |  ❌       |
|Trigger Type     | Attribute changes, Group Membership change        |  ✔️       |
|Trigger details     | Depends on trigger type selection. <br> • **Attribute changes**: Trigger attribute <br>• **Group membership changes**: Added to group/Remove from group    |   ✔️      |
|Scope     | Depends on trigger. <br> **Rule based**: Attribute changes.<br> **Group membership change**: Group based.         | ✔️        |
|Tasks     | **Send email to manager about sponsorship changes**, **Send email to co-sponsors about sponsor changes**, **Transfer agent sponsorships to manager**     |  ✔️       |

## Next steps

- [`workflowTemplate` resource type](https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-workflowtemplate?view=graph-rest-beta&preserve-view=true)
- [Lifecycle Workflow tasks and definitions](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-tasks)
- [Create a Lifecycle workflow](https://learn.microsoft.com/en-us/entra/id-governance/create-lifecycle-workflow)
- [Custom task extensions for workflows beyond built-in templates](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-extensibility)
- [Trigger Logic Apps based on custom task extensions](https://learn.microsoft.com/en-us/entra/id-governance/trigger-custom-task)
