# Relocate your Azure Functions app to another Azure region

> Source: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-functions  
> Microsoft doc last updated: 09/15/2025


This article describes how to move an Azure Functions-hosted function app to another Azure region.

There are various reasons why you may want to move your existing Azure resources from one region to another. You may want to:

- Take advantage of a new Azure region.
- Deploy features or services available in specific regions only.
- Meet internal policy and governance requirements.
- Align with company mergers and acquisitions
- Meet capacity planning requirements.

The Azure resources that host your function app are region-specific and can't be moved across regions. Instead, you must create a copy of your existing function app resources in the target region, and then redeploy your functions code over to the new app.

You can move these same resources to another resource group or subscription, as long as they remain in the same region. For more information, see [Move App Service resources to a new resource group or subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-limitations/app-service-move-limitations).

## Prerequisites

- Make sure that the target region supports Azure Functions and any related service whose resources you want to move.
- Make sure that you have privileges to create the resources needed in the new region.

## Prepare

Identify all the function app resources used on the source region, which potentially includes:

- Function app
- [Hosting plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale#overview-of-plans)
- [Deployment slots](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-slots)
- [Custom domains purchased in Azure](https://learn.microsoft.com/en-us/azure/app-service/manage-custom-dns-buy-domain)
- [TLS/SSL certificates and settings](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-certificate)
- [Configured networking options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options)
- [Managed identities](https://learn.microsoft.com/en-us/azure/app-service/overview-managed-identity)
- [Configured application settings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings)
- [Scaling configurations](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale#scale)

When preparing to move your app to a new region, there are a few parts of the architecture that require special consideration and planning.

### Function app name

Function app names must be globally unique across all Azure apps. This means that your new function app can't have the same name and URL as the original one. This is even true when using a custom DNS, because the underlying `<APP_NAME>.azurewebsites.net` must still be unique. You might need to update any clients that connect to HTTP endpoints on your function app. These clients need to use the new URL when making requests.

### Source code

Ideally, you maintain your source code in a code repository of some kind, or in a container repository if running in a Linux container. If you're using continuous deployment, plan to switch the repository or container deployment connection to the new function app address. If, for some reason, you no longer have the source code, you can [download the currently running package](https://learn.microsoft.com/en-us/azure/azure-functions/deployment-zip-push#download-your-function-app-files) from the original function app. We recommend storing your source files in a code repository and [using continuous deployment for updates](https://learn.microsoft.com/en-us/azure/azure-functions/functions-continuous-deployment).

### Default storage account

The Functions host requires an Azure Storage account. For more information, see [Storage account requirements](https://learn.microsoft.com/en-us/azure/azure-functions/storage-considerations#storage-account-requirements). For best performance, your function app should [use a storage account in the same region](https://learn.microsoft.com/en-us/azure/azure-functions/storage-considerations#storage-account-location). When you create a new app with a new storage account in your new region, your app gets a new set of [function access keys](https://learn.microsoft.com/en-us/azure/azure-functions/function-keys-how-to) and the state of any triggers (such as timer triggers) is reset.

### Persisted local storage

Functions executions are [intended to be stateless](https://learn.microsoft.com/en-us/azure/azure-functions/performance-reliability#write-functions-to-be-stateless). However, we don't prevent you from writing data to the local file system. It's possible to store data generated and used by your application on the `%HOME%\site` virtual drive, but this data shouldn't be state-related. If your scenario requires you to maintain state between function executions, consider instead using [Durable Functions](https://learn.microsoft.com/en-us/azure/durable-task/durable-functions/durable-functions-overview).

If your application persists data to the app's shared storage path, make sure to plan how you're going to manage that state during a resource move. Keep in mind that for Dedicated (App Service) plan apps, the share is part of the site. For Consumption and Premium plans, the share is, by default, an Azure Files share in the default storage account. Apps running on Linux might be using an [explicitly mounted share](https://learn.microsoft.com/en-us/azure/azure-functions/storage-considerations#mount-file-shares) for persisted storage.

### Connected services

Your functions might connect to Azure Services and other resources using either a service SDK or triggers and bindings. Any connected service might be negatively impacted when the app moves to a new region. If latency or throughout are issues, consider moving any connected service to the new region as well. To learn how to move those resources across regions, see the documentation for the respective services. When moving an app with connected services, you might want to consider a [cross-region disaster recovery and business continuity](https://learn.microsoft.com/en-us/azure/reliability/reliability-functions#cross-region-disaster-recovery-and-business-continuity) strategy during the move.

Changes to connected services might require you to update the values stored in your application settings, which are used to connect to those services.

### Configuration

- You can capture a snapshot of the existing app settings and connection strings from the Azure portal. Expand **Settings** > **Environment variables**, select **Advanced edit** under either **App settings** or **Connections strings** and save the JSON output that contains the existing settings or connections. You need to recreate these settings in the new region, but the values themselves are likely to change as a result of subsequent region changes in the connected services.

- Existing [Key Vault references](https://learn.microsoft.com/en-us/azure/app-service/app-service-key-vault-references) can't be exported across an Azure geographical boundary. You must recreate any required references in the new region.

- Your app configuration might be managed by [Azure App Configuration](https://learn.microsoft.com/en-us/azure/azure-app-configuration/overview) or from some other central (downstream) database dependency. Review any App Configuration store or similar stores for environment and region-specific settings that might require modifications.

### Custom domains

If your function app uses a custom domain, [bind it preemptively to the target app](https://learn.microsoft.com/en-us/azure/app-service/manage-custom-dns-migrate-domain#bind-the-domain-name-preemptively). Verify and [enable the domain in the target app](https://learn.microsoft.com/en-us/azure/app-service/manage-custom-dns-migrate-domain#enable-the-domain-for-your-app). After the move, you must remap the domain name.

### Virtual networks

Azure Functions lets you integrate your apps with virtual network resources, and even run them in a virtual network. For more information, see [Azure Functions networking options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options). When moving to a new region, you must first move or recreate all required virtual network and subnet resources before deploying your app. This includes moving or recreating any private endpoints and service endpoints.

### Identities

- You need to recreate any system assigned managed identities along with your app in the new target region. Typically, an automatically created Microsoft Entra ID app, used by EasyAuth, defaults to the app resource name.

- User-assigned managed identities also can't be moved across regions. To keep user-assigned managed identities in the same resource group with your app, you must recreate them in the new region. For more information, see [Relocate managed identities for Azure resources to another region](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-to-managed-identity-regional-move).

- Grant the managed identities the same permissions in your relocated services as the original identities that they're replacing, including Group memberships.

### Certificates

App Service certificate resources can be moved to a new resource group or subscription but not across regions. Certificates that can be exported can also be imported into the app or into Key Vault in the new region. This export and import process is equivalent to a move between regions.

There are different types of certificates that need to be taken into consideration as you plan your service relocation:

| Certificate type | Exportable | Comments |
| ----- | ----- | ----- |
| [App Service managed](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-certificate#import-an-app-service-certificate) | No | Recreate these certificates in the new region. | 
| [Azure Key Vault managed](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-certificate#import-a-certificate-from-key-vault) | Yes | These certificates can be [exported from Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/certificates/how-to-export-certificate) and then [imported into Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/certificates/tutorial-import-certificate) in the new region. |
| Private key (self-managed)  | Yes | Certificates you acquired outside of Azure can be exported from App Service and then imported either into the new app or [into Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/certificates/tutorial-import-certificate) in the new region. |
| Public key | No | Your app might have certificates with only a public key and no secret, which are used to access other secured endpoints. Obtain the required public key certificate files and import them into the app in the new region. |

### Access keys

Functions uses access keys to make it more difficult to access HTTP endpoints in your function app. These keys are maintained encrypted in the default storage account. When you create a new app in the new region, a new set of keys get created. You must update any existing clients that use access keys to use the new keys in the new region. While you should use the new keys, it's possible to recreate the old keys in the new app. For more information, see [Work with access keys in Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/function-keys-how-to#work-with-access-keys-in-azure-functions).

### Downtime

If minimal downtime is a requirement, consider running your function app in both regions as recommended to implement a disaster recovery architecture. The specific architecture you implement depends on the trigger types in your function app. For more information, see [Reliability in Azure Functions](https://learn.microsoft.com/en-us/azure/reliability/reliability-functions#cross-region-disaster-recovery-and-business-continuity).

### Durable Functions

The Durable Functions extension lets you define orchestrations, where state is maintained in your function executions using stateful entities. Ideally, you should allow running orchestrations to complete before migrating your Durable Functions app, especially when you plan to switch to a new storage account in the new region. When migrating your Durable Functions apps, consider using one of these [disaster recovery and geo-distribution strategies](https://learn.microsoft.com/en-us/azure/durable-task/durable-functions/durable-functions-disaster-recovery-geo-distribution).

## Relocate

Recreating your function app in a new region requires you to first recreate the Azure infrastructure of an App Service plan, function app instance, and related resources, such as virtual networks, identities, and slots. You also must reconnect or, in the new region, recreate the Azure resources required by the app. These resources might include the default Azure Storage account and the Application Insights instance.

Then you can package and redeploy the actual application source code or container to the function app running in the new region.

### Recreate your Azure infrastructure

There are several ways to create a function app and related resources in Azure at the target region:

- **Deployment templates**: If you originally deployed your function app using infrastructure-as-code (IaC) files (Bicep, ARM templates, or Terraform), you can update those previous deployments to target the new region and use them to recreate resources in the new region. If you no longer have these deployment files, you can always [download an ARM template for your existing resource group from the Azure portal](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/export-template-portal).
- **Azure CLI/PowerShell scripts**: If you originally deployed your function app using Azure CLI or Azure PowerShell scripts, you can update these scripts to instead target the new region and run them again. If you no longer have these scripts, then you can also [download an ARM template for your existing resource group from the Azure portal](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/export-template-portal).  
- **Azure portal**: If you created your function app in the portal originally or don't feel comfortable using scripts or IaC files, you can just recreate everything in the portal. Make sure to use the same [hosting plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale#overview-of-plans), [language runtime](https://learn.microsoft.com/en-us/azure/azure-functions/supported-languages), and language version as your original app.

### Review configured resources

Review and configure the resources identified in the [Prepare](#prepare) step above in the target region if they weren't configured during the deploy. If you're using continuous deployment with managed identity authentication, make sure the required identities and role mappings exist in the new function app.

### Redeploy your source code

Now that you have the infrastructure in place, you can repackage and redeploy the source code to the function app. This is a good time to move your source code or container image to a repository and [enable continuous deployment](https://learn.microsoft.com/en-us/azure/azure-functions/functions-continuous-deployment) from that repository.

You can also use any other publishing method supported by Functions. Most tool-based publishing requires you to [enable basic authentication on the `scm` endpoint](https://learn.microsoft.com/en-us/azure/azure-functions/functions-continuous-deployment#enable-basic-authentication-for-deployments), which isn't recommended for production apps.

### Relocation considerations

- Remember to verify your configuration and test your functions in the target region.
- If you had custom domain configured, [remap the domain name](https://learn.microsoft.com/en-us/azure/app-service/manage-custom-dns-migrate-domain#4-remap-the-active-dns-name).
- For a function app running in a Dedicated (App Service) plan, also review the [App Service Migration Plan](https://learn.microsoft.com/en-us/azure/app-service/manage-move-across-regions) when the plan is shared with one or more web apps.

## Clean up

After the move is complete, delete the function app and hosting plan from the source region. You pay for function apps in Premium or Dedicated plans, even when the app itself isn't running. If you have recreated other services in the new region, you should also delete the older services after you're certain that they're no longer needed.

## Related resources

Review the [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/browse/?expanded=azure&products=azure-functions) for examples of function apps running in multiple regions as part of more advanced and geo-redundant solution architectures.
