# Automated ServiceNow Ticket Creation with Microsoft Entra Entitlement Management Integration

> Source: https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-ticketed-provisioning  
> Microsoft doc last updated: 02/02/2026


Scenario: In this scenario you learn how to use custom extensibility, and a Logic App, to automatically generate ServiceNow tickets for manual provisioning of users who have received assignments and need access to apps.

In this tutorial, you learn:

> * Adding a Logic App Workflow to an existing catalog.
> * Adding a custom extension to a policy within an existing access package.
> * Registering an application in Microsoft Entra ID for resuming Entitlement Management workflow
> * Configuring ServiceNow for Automation Authentication.
> * Requesting access to an access package as an end-user.
> * Receiving access to the requested access package as an end-user.

## Prerequisites

- A Microsoft Entra user account with an active Azure subscription. If you don't already have one, you can [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- One of the following least privileged roles: Cloud Application Administrator, Application Administrator, or owner of the service principal.
- A [ServiceNow instance](https://www.servicenow.com/) of Rome or higher
- SSO integration with ServiceNow. If this isn't already configured, see:[Tutorial: Microsoft Entra single sign-on (SSO) integration with ServiceNow](https://learn.microsoft.com/en-us/entra/identity/saas-apps/servicenow-tutorial) before continuing.

> [!NOTE]
> It's recommended to use a least privilege role when completing these steps.

## Adding Logic App Workflow to an existing Catalog for Entitlement Management

To add a Logic App workflow to an existing catalog use the ARM template for the Logic App creation here: 

[](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fdemos%2Fidentitygovernance-entitlementmanagement-extensibility-servicenow-sample-logicapp%2Fazuredeploy.json).

Provide the resource group details, along with the Catalog ID to associate the Logic App with and select purchase. For more information on how to create a new catalog, see: [Create and manage a catalog of resources in entitlement management](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-catalog-create).

After a catalog is created, you'd add a Logic App workflow by doing the following steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Identity Governance Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#identity-governance-administrator).
    > [!TIP]
    > Other least privilege roles that can complete this task include the Catalog owner and Resource group owner.
1. In the left menu, select **Catalogs**. 

1. Select the catalog for which you want to add a custom extension and then in the left menu, select **Custom Extensions**.

1. In the header navigation bar, select **Add a Custom Extension**.

1. In the **Basics** tab, enter the name of the custom extension and a description of the workflow. These fields show up in the **Custom Extensions** tab of the Catalog.
    
1. Select the **Extension Type** as “**Request workflow**” to correspond with the policy stage of the access package requested being created.
    
1. Select **Launch and wait** in the **Extension Configuration** which will pause the associated access package action until after the Logic App linked to the extension completes its task, and a resume action is sent by the admin to continue the process. For more information on this process, see:  [Configuring custom extensions that pause entitlement management processes](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-logic-apps-integration#configuring-custom-extensions-that-pause-entitlement-management-processes).

1.  In the **Details** tab, choose No in the "*Create new logic App*" field as the Logic App was created in the previous steps. However, you need to provide the Azure subscription and resource group details, along with the Logic App name.
    
1. In **Review and Create**, review the summary of your custom extension and make sure the details for your Logic App call-out are correct. Then select **Create**.

1. Once created, the Logic App is able to be accessed under **Logic App** next to the custom extension on the custom extensions page. You're able to call on this in access package policies.
    

> [!TIP]
> To learn more about custom extension feature that pauses entitlement management processes, see: [Configuring custom extensions that pause entitlement management processes](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-logic-apps-integration#configuring-custom-extensions-that-pause-entitlement-management-processes).

## Adding Custom Extension to a policy in an existing Access Package 

After setting up custom extensibility in the catalog, administrators can create an access package with a policy to trigger the custom extension when the request has been approved. This enables them to define specific access requirements and tailor the access review process to meet their organization's needs.  

1. In the Microsoft Entra portal as at least an [Identity Governance Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#identity-governance-administrator), select **Access packages**.
    > [!TIP]
    > Other least privilege roles that can complete this task include the Catalog owner and Access package manager.
1. Select the access package you want to add a custom extension (Logic App) to from the list of access packages that have already been created.

1. Change to the policy tab, select the policy, and select **Edit**.

1. In the policy settings, go to the **Custom Extensions** tab.

1. In the menu below **Stage**, select the access package event you wish to use as trigger for this custom extension (Logic App). For our scenario, to trigger the custom extension Logic App workflow when access package has been approved, select **Request is approved**.
    > [!NOTE]
    > To create a ServiceNow ticket for an expired assignment that had permission granted previously, add a new stage for "*Assignment is removed*", and then select the LogicApp.
1. In the menu below Custom Extension, select the custom extension (Logic App) you created in the above steps to add to this access package. The action you select executes when the event selected in the *when* field occurs.

1. Select **Update** to add it to an existing access package's policy.
    

> [!NOTE]
> Select **New access package** if you want to create a new access package. For more information about how to create an access package, see: [Create a new access package in entitlement management](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create). For more information about how to edit an existing access package, see: [Change request settings for an access package in Microsoft Entra entitlement management](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-request-policy#open-and-edit-an-existing-policys-request-settings).

## Register an application with secrets in the Microsoft Entra admin center

With Azure, you're able to use [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/secrets/about-secrets) to store application secrets such as passwords. To register an application with secrets within the Microsoft Entra admin center, follow these steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Identity Governance Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#identity-governance-administrator).

1. Browse to **Entra ID** > **App registrations**.

1. Under Manage, select App registrations > New registration.

1. Enter a display Name for your application.

1. Select "Accounts in this organizational directory only" in supported account type.

1. Select Register.

After registering your application, you must add a client secret by following these steps: 

1. Browse to **Entra ID** > **App registrations**.

1. select your application.

1. Select Certificates & secrets > Client secrets > New client secret.

1. Add a description for your client secret.

1. Select an expiration for the secret or specify a custom lifetime.

1. Select Add.

> [!NOTE]
> To find more detailed information on registering an application, see: [Quickstart: Register an app in the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app):

To authorize the created application to call the [MS Graph resume API](https://learn.microsoft.com/en-us/graph/api/accesspackageassignmentrequest-resume) you'd do the following steps:

1. Navigate to the Microsoft Entra admin center [Identity Governance - Microsoft Entra admin center](https://entra.microsoft.com/#view/Microsoft_AAD_ERM/DashboardBlade/~/elmEntitlement)

1. In the left menu, select **Catalogs**.

1. Select the catalog for which you have added the custom extension.

1. Select “Roles and administrators” menu and select “+ Add access package assignment manager”.

1. In the Select members dialog box, search for the application created by name or application Identifier. Select the application and choose the *“Select”* button.

> [!TIP]
> You can find more detailed information on delegation and roles on Microsoft’s official documentation located here: [Delegation and roles in entitlement management](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-delegate).

## Configuring ServiceNow for Automation Authentication

At this point it's time to configure ServiceNow for resuming the entitlement management workflow after the ServiceNow ticket closure:

1. Register a Microsoft Entra application in the ServiceNow Application Registry by following these steps:
    1. Sign in to ServiceNow and navigate to the Application Registry.
    1. Select “*New*” and then select “**Connect to a third party OAuth Provider**”.
    1. Provide a name for the application, and select Client Credentials in the Default Grant type.
    1. Enter the Client Name, ID, Client Secret, Authorization URL, Token URL that were generated when you registered the Microsoft Entra application in the Microsoft Entra admin center.
    1. Submit the application.
        
1. Create a System Web Service REST API message by following these steps: 
    1. Go to the REST API Messages section under System Web Services.
    1. Select the "New" button to create a new REST API message.
    1. Fill in all the required fields, which include providing the Endpoint URL: 
        ``https://learn.microsoft.com/en-us/graph/api/accesspackageassignmentrequest-resume?view=graph-rest-1.0&tabs=http``
    1. For the required header:<br>
         Content Type: `application/json` 
    1. For Authentication, select OAuth2.0 and choose the OAuth profile that was created during the app registration process.
    1. Select the "*Submit*" button to save the changes.
    1. Go back to the REST API Messages section under System Web Services.
    1. Select Http Request and then select "*New*". Enter a name, and select "POST" as the Http method.
    1. In the Http request, add the content for the Http query parameters using the following API Schema:
        ``` http
        {
        "data": {
            "@odata.type": "#microsoft.graph.accessPackageAssignmentRequestCallbackData",
            "customExtensionStageInstanceDetail": "Resuming-Assignment for user",
            "customExtensionStageInstanceId": "${StageInstanceId}",
            "stage": "${Stage}"
                  },
                  "source": "ServiceNow",
                    "type": "microsoft.graph.accessPackageCustomExtensionStage.${Stage}"
                    }
        ```
    1. Select "*Submit*" to save the changes.
         
        
        
1. Modify the request table schema: To modify the request table schema, make changes to the three tables shown in the following image:
    
    Add the four column label and type as string:
    - AccessPackageAssignmentRequestId
    - AccessPackageAssignmentStage
    - StageInstanceId
    - EntraUserObjectId
1. To automate workflow with Flow Designer, you'd do the following steps:
    1. Sign in to ServiceNow and go to Flow Designer.
    1. Select the “*New*” button and create a new action. 
    1. Add an action to invoke the System Web Service REST API message that was created in the previous step.
        
        Script for the action: (Update the script with the Column labels created in previous step):
        ``` 
        (function execute(inputs, outputs) {
            gs.info("AccessPackageAssignmentRequestId: " + inputs['accesspkgassignmentrequestid']);
            gs.info("StageInstanceId: " + inputs['customextensionstageinstanceid'] );
            gs.info("Stage: " + inputs['assignmentstage']);
            var r = new sn_ws.RESTMessageV2('Resume ELM WorkFlow', 'RESUME');
            r.setStringParameterNoEscape('AccessPackageAssignmentRequestId', inputs['accesspkgassignmentrequestid']);
            r.setStringParameterNoEscape('StageInstanceId', inputs['customextensionstageinstanceid'] );
            r.setStringParameterNoEscape('Stage', inputs['assignmentstage']);
            var response = r.execute();
            var responseBody = response.getBody();
            var httpStatus = response.getStatusCode();
            var requestBody =  r.getRequestBody();
            gs.info("requestBody: " + requestBody);
            gs.info("responseBody: " + responseBody);
            gs.info("httpStatus: " + httpStatus);
            })(inputs, outputs); 
        ```
    1. Save the Action
    1. Select the "*New*" button to create a new flow.
    1. Enter flow name, select Run as – System User and select submit.
1. To create triggers within ServiceNow, you'd follow these steps:
    1. Select "*Add Trigger*" and then select "*updated*" trigger and run the trigger for every update.
    1. Add a filter condition by updating the condition as shown in the following image:
        
    1. Select done.
    1. Select add an action
        
    1. Select the Action and then select the action created in the previous step.
        
    1. Drag and drop the newly created columns from the request record to the appropriate action parameters.
    1. Select “Done”, “Save” and then “Activate”. 
        

## Requesting access to an access package as an end-user

When an end user requests access to an access package, the request is sent to the appropriate approver. Once the approver grants approval, Entitlement Management calls the Logic App. The Logic app then calls ServiceNow to create a new request/ticket and Entitlement Management awaits a callback from ServiceNow.

## Receiving access to the requested access package as an end-user 

The IT Support team works on the previous ticket created to do necessary provisions, and close the ServiceNow ticket. When the ticket is closed, ServiceNow triggers a call to resume the Entitlement Management workflow. Once the request is completed, the requestor receives a notification from entitlement management that the request has been fulfilled. This streamlined workflow ensures that access requests are fulfilled efficiently, and users are notified promptly.

> [!NOTE]
> The end user sees "assignment failed" in the MyAccess portal if the ticket isn't closed within 14 days.

## Next steps

Advance to the next article to learn how to create...

> [Trigger Logic Apps with custom extensions in entitlement management](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-logic-apps-integration)
