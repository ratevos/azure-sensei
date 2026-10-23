# Manage workflow properties

> Source: https://learn.microsoft.com/en-us/entra/id-governance/manage-workflow-properties  
> Microsoft doc last updated: 03/12/2026


Managing workflows can be accomplished in one of two ways:  
   - Updating the basic properties of a workflow without creating a new version of it
   - Creating a new version of the updated workflow

You can update the following basic information without creating a new workflow.
   - display name
   - description
   - [Administrative Unit Scope](https://learn.microsoft.com/en-us/entra/id-governance/manage-delegate-workflow)
   - whether or not it's enabled
   - whether or not workflow schedule is enabled
   - task name
   - task description

If you change any other parameters, a new version is required to be created as outlined in the [Managing workflow versions](https://learn.microsoft.com/en-us/entra/id-governance/manage-workflow-tasks) article.

If done via the Microsoft Entra admin center, the new version is created automatically. If done using Microsoft Graph, you must manually create a new version of the workflow.  For more information, see [Edit the properties of a workflow using Microsoft Graph](#edit-the-properties-of-a-workflow-using-microsoft-graph).

## Edit the properties of a workflow using the Microsoft Entra admin center

To edit the properties of a workflow using the Microsoft Entra admin center, you do the following steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Lifecycle Workflows Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#lifecycle-workflows-administrator).

1. Browse to **ID Governance** > **Lifecycle workflows** > **workflows**.

1. Here you see a list of all of your current workflows. Select the workflow that you want to edit.
    
    

6. To change the display name, description, or the Administrative unit scope, select **Properties**.

    

7. Update the desired properties. 
> [!NOTE]
> Display names cannot be the same as other existing workflows. They must have their own unique name.

8. Select **save**.

## Edit the properties of a workflow using Microsoft Graph

To update a workflow via API using Microsoft Graph, see: [Update workflow](https://learn.microsoft.com/en-us/graph/api/identitygovernance-workflow-update)

## Next steps

- [Manage workflow versions](https://learn.microsoft.com/en-us/entra/id-governance/manage-workflow-tasks)
- [Check status of a workflow](https://learn.microsoft.com/en-us/entra/id-governance/check-status-workflow)
