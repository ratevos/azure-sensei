# Externally determine the approval requirements for an access package using custom extensions

> Source: https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-dynamic-approval  
> Microsoft doc last updated: 11/04/2025


In entitlement management, approvers for access package requests can either be directly assigned, or determined dynamically. Entitlement management natively supports dynamically determining approvers such as the requestors manager, their second-level manager, or a sponsor from a connected organization:

With the introduction of [custom extensions](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-logic-apps-integration) calling out to [Azure Logic Apps](https://learn.microsoft.com/en-us/azure/logic-apps/logic-apps-overview) you are now able to dynamically determine approval requirements for each access package assignment request based on your organizations specific business logic. The access package assignment request process will pause until your business logic hosted in Azure Logic Apps returns a [approval stage](https://learn.microsoft.com/en-us/graph/api/resources/accesspackageapprovalstage) which will then be leveraged in the subsequent approval process via the [My Access portal](https://myaccess.microsoft.com). For example, if access requests must be approved by the department head of the person requesting an access package this feature allows you to query an external system, such as your human resources (HR) system, to on-the-fly look up the current department head and assign them as the approver for the given access request.

This article walks you through making a custom extension, its underlying Azure Logic App, setting its system-assigned identity and role in the catalog, editing the logic app action to perform business logic, and testing to see if it runs successfully.

Want to learn how this feature can use SAP organizational business context for approvals? Check out this episode of the SAP on Azure podcast:

> [!VIDEO https://www.youtube.com/embed/qpEkNQtLLRY?si=ImIiD2jZPE8YTJGq]

## License requirements

Using this feature requires Microsoft Entra ID Governance or Microsoft Entra Suite licenses. To find the right license for your requirements, see [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).

## Prerequisites

- At least the [Entitlement Management Catalog owner](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-delegate#entitlement-management-roles) role of the catalog where the custom extension will be created or exists.
- At least the [Azure built-in role](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles) of [Logic App Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/integration#logic-app-contributor) on the Logic App itself, the resource group, subscription, or management group that the logic app is in.

## Create the custom extension and Azure Logic App

To create a custom extension, and its underlying Azure Logic App, you'd do the following steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Catalog owner](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-delegate#entitlement-management-roles) of the catalog where the custom extension will be located.

1. Browse to **ID Governance** > **Catalogs**.

1. On the Catalogs overview page, select an existing catalog where your custom extension will be located, or create a new catalog.

1. On the specific catalog page where you want to create your custom extension, select **Custom extensions**.
    
1. Select **Add a custom extension** to add a name and description for the custom extension. When finished, select **Next**.
    
1. On the **Extension Type** page, select **Request workflow (triggered when an access package is request, approved, granted, or removed)** and select **Next**.
    
1. On the **Extension Configuration** page, for Behavior select **Launch and wait**, for Response data select **Approval Stage**, and then select **Next**.
    
1. On the **Details** page, choose a subscription, resource group, and name for the logic app being created. Once you've entered this information, select **Create a logic app**. Once the logic app is created, select **Next**.

1. On the **Review + create** page, make sure all your details are correct, then select **Create**.

## Reference the custom extension in an access package assignment policy

Once you've created the custom extension and logic app, you can reference the custom extension in an access package assignment policy by doing the following steps:

1. Select the catalog where the custom extension was created.

1. On the catalog page, select **Access packages**, and select the access package for the policy you want to update.

1. On the access package overview page, select **Policies**, and select the policy to edit.
    
1.  On the **Edit policy** page under **Requests**, set the **Require approval** box to yes, and you're able to add your custom extension as an approver. The example here shows the custom extension being used as the first approver.
  
1. Select **Update**.

Once updated, you can go to the edited policy, and confirm the change by selecting **Approval stage details**.

  

## Set logic app assigned identity and assign its role

With the Azure logic app created, you must enable its system-assigned identity, and give it the proper role by doing the following steps:

1. Sign in to the Azure portal and go to the logic app with the [Azure built-in role](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles) of at least [Logic App Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/integration#logic-app-contributor).

1. On the logic app overview page, go to **Settings** > **Identity**.

1. On the Identity page, enable the system assigned managed identity
    
1. Select **Save**.

1. Back in the Microsoft Entra admin center as at least the role of [Catalog owner](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-delegate#entitlement-management-roles), go to the catalog where you created the custom extension, and select **Roles and administrators**.

1. On the roles and administrators page, select **Add access package assignment manager**, and select the logic app you created.
    

## Configure the logic app and corresponding business logic

With the Azure Logic App given the access package assignment manager role for the catalog, you must now go to logic app to edit it to communicate with Microsoft Entra. To do this, you'd do the following steps:

1. On the logic app created, go to **Development Tools** > **Logic app designer**.

1. On the designer page, remove everything under the **manual** trigger, and select the **Add an action** button.
    
1. On the Add an Action pane, select **HTTP**.

1. On the **HTTP** pane under Parameters, enter the following parameters:
    - URI: `https://graph.microsoft.com/beta@{triggerBody()?['CallbackUriPath']}`
    - Method: POST
    - Authentication Type: Managed identity
    - Managed Identity: System-assigned managed identity
    - Audience: https://graph.microsoft.com
1. Under HTTP Settings, disable **Asynchronous Pattern**.
    
1. After you've made changes to the HTTP trigger, select **Save**.

## Add business logic to the logic app

With the logic app configured for communication with Microsoft Entra, you can now add what you want the app to do. Logic app actions are added to the body of the **HTTP** section you configured for the logic app. To edit this, you do the following:

1. On the logic app created, go to **Development Tools** > **Logic app designer**.

1. On the logic app designer page, select **HTTP**.

1. On the HTTP pane under **Parameters**, scroll down to **Body** and enter your logic data based on the parameters you want to query for. For more information, see: [Call external HTTP or HTTPS endpoints from workflows in Azure Logic Apps](https://learn.microsoft.com/en-us/azure/connectors/connectors-native-http?tabs=standard).
    
    > [!NOTE]
    > For an example of the body action see: [HTTP action example](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-dynamic-approval#http-action-example).
1. When finished adding your business logic, select **save**.

## Verify the extension worked

To verify that the custom extension works, you can request access to the access package, and view the request details via **Requests** on the access package page by following these steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Catalog owner](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-delegate#entitlement-management-roles) of the catalog where the custom extension is located.
    > [!TIP]
    > Other least privilege roles that can complete this task include the Access package manager, Access package assignment manager, and Identity Governance Administrator.
1. Browse to **ID Governance** > **Entitlement management** > **Access package**.

1. On the Access packages page, open the access package you want to view requests of.

1. Select **Requests**.

1. On the requests page, select the request you want to view details of and confirm that the access package was successfully delivered.
    

## HTTP action example

The following example of an action that can be placed in the HTTP body is a logic app that identifies the primary approver. [You have to pass your own variable](https://learn.microsoft.com/en-us/azure/logic-apps/logic-apps-create-variables-store-values?tabs=consumption) into this code where prompted:

```
{
  "data": {
    "@@odata.type": "microsoft.graph.assignmentRequestApprovalStageCallbackData",
    "approvalStage": {
      "durationBeforeAutomaticDenial": "P2D",
      "escalationApprovers": [],
      "fallbackEscalationApprovers": [],
      "fallbackPrimaryApprovers": [],
      "isApproverJustificationRequired": false,
      "isEscalationEnabled": false,
      "primaryApprovers": [
        {
          "@@odata.type": "#microsoft.graph.singleUser",
          "description": "This is the primary approver for the access package requested by the user.",
          "id": "<Dynamically assigned variable>",
          "isBackup": false
        }
      ]
    },
    "customExtensionStageInstanceDetail": "A approval stage from Logic Apps",
    "customExtensionStageInstanceId": "@{triggerBody()?['CustomExtensionStageInstanceId']}",
    "stage": "assignmentRequestDeterminingApprovalRequirements"
  },
  "source": "LogicApps",
  "type": "microsoft.graph.accessPackageCustomExtensionStage.assignmentRequestCreated"
}
```

> [!NOTE]
> Although the example uses a user ID, the primaryApprovers and escalationApprovers section can contain valid [subjectSets](https://learn.microsoft.com/en-us/graph/api/resources/subjectset) supported by Entitlement Management. In Public Preview the resume call must be performed against Microsoft Graph's beta endpoint. However, the [approval stage](https://learn.microsoft.com/en-us/graph/api/resources/accesspackageapprovalstage) provided in the resume call body must follow the [v1.0 convention](https://learn.microsoft.com/en-us/graph/api/resources/accesspackageapprovalstage) and not the [beta convention](https://learn.microsoft.com/en-us/graph/api/resources/approvalstage?view=graph-rest-beta&preserve-view=true).

## Related content

- [Trigger Logic Apps with custom extensions in entitlement management](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-logic-apps-integration)
- [Tutorial: Integrating Microsoft Entra Entitlement Management with Microsoft Teams using Custom Extensibility and Logic Apps](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-custom-teams-extension)
