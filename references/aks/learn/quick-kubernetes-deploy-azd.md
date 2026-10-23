# Quickstart: Deploy an Azure Kubernetes Service (AKS) cluster using the Azure Developer CLI

> Source: https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-azd  
> Microsoft doc last updated: 03/21/2024


Azure Kubernetes Service (AKS) is a managed Kubernetes service that lets you quickly deploy and manage clusters. In this quickstart, you learn to:

- Download and install the Azure Developer CLI (`azd`).
- Clone applications from an Azure Developer CLI template (`azd` template).
- Deploy an AKS cluster using the Azure Developer CLI (`azd`).
- Run a sample multi-container application with a group of microservices that simulates a retail app.
- Delete and clean up containers made from the `azd` template.

> [!NOTE]
> To get started with quickly provisioning an AKS cluster, this article includes steps to deploy a cluster with default settings for evaluation purposes only. Before deploying a production-ready cluster, we recommend that you familiarize yourself with our [baseline reference architecture][baseline-reference-architecture] to consider how it aligns with your business requirements.

## Before you begin

This quickstart assumes a basic understanding of Kubernetes concepts. For more information, see [Kubernetes core concepts for Azure Kubernetes Service (AKS)][kubernetes-concepts].

- 

- For ease of use, run this sample on Bash or PowerShell in the [Azure Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview). For more information, see [Quickstart for Azure Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/quickstart).

- To use `azd` locally, install version 1.6.1 or later of the [Azure Developer CLI][azd-install].
  - If you're using the [Azure Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview), the latest version of `azd` is already installed.

## Review application code

You can review the application code in the [Azure-Samples/aks-store-demo GitHub repository](https://github.com/Azure-Samples/aks-store-demo).

The quickstart application includes the following Kubernetes deployments and services:

- **Store front**: Web application for customers to view products and place orders.
- **Product service**: Shows product information.
- **Order service**: Places orders.
- **Rabbit MQ**: Message queue for an order queue.

> [!NOTE]
> We don't recommend running stateful containers, such as Rabbit MQ, without persistent storage for production use. These are used here for simplicity, but we recommend using managed services instead, such as Azure Cosmos DB or Azure Service Bus.

## Clone the Azure Developer CLI template

1. Clone the AKS store demo template from the **Azure-Samples** repository using the [`azd init`][azd-init] command with the `--template` parameter.

    ```azdeveloper
    azd init --template Azure-Samples/aks-store-demo
    ```

2. Enter an environment name for your project that uses only alphanumeric characters and hyphens, such as *aks-azdqs-1*.

    ```output
    Enter a new environment name: aks-azdqs-1
    ```

## Sign in to your Azure Cloud account

The `azd` template contains all the code needed to create the services, but you need to sign in to your Azure account in order to host the application on AKS.

1. Sign in to your account using the [`azd auth login`][azd-auth-login] command.

    ```azdeveloper
    azd auth login
    ```

2. Copy the device code that appears in the output and press enter to sign in.

    ```output
    Start by copying the next code: XXXXXXXXX
    Then press enter and continue to log in from your browser...
    ```

    > [!IMPORTANT]
    > If you're using an out-of-network virtual machine or GitHub Codespace, certain Azure security policies cause conflicts when used to sign in with `azd auth login`. If you run into an issue here, you can follow the azd auth workaround provided below, which involves using a `curl` request to the localhost URL you were redirected to after running [`azd auth login`][az-auth-login].

3. Authenticate with your credentials on your organization's sign in page.
4. Confirm that it's you trying to connect from the Azure CLI.
5. Verify the message "Device code authentication completed. Logged in to Azure." appears in your original terminal.

    ```output
    Waiting for you to complete authentication in the browser...
    Device code authentication completed.
    Logged in to Azure.
    ```

### azd auth workaround

This workaround requires you to have the [Azure CLI][install-azure-cli] installed.

1. Open a terminal window and log in with the Azure CLI using the [`az login`][az-login] command with the `--scope` parameter set to `https://graph.microsoft.com/.default`.

    ```azurecli-interactive
    az login --scope https://graph.microsoft.com/.default
    ```

    You should be redirected to an authentication page in a new tab to create a browser access token, as shown in the following example:

    ```output
    https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize?clientid=<your_client_id>.
    ```

2. Copy the localhost URL of the webpage you received after attempting to sign in with `azd auth login`.
3. In a new terminal window, use the following `curl` request to log in. Make sure you replace the `<localhost>` placeholder with the localhost URL you copied in the previous step.

    ```console
    curl <localhost>
    ```

    A successful login outputs an HTML webpage, as shown in the following example:

    ```output
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="refresh" content="60;url=https://docs.microsoft.com/cli/azure/">
        <title>Login successfully</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
    
            code {
                font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;
                display: inline-block;
                background-color: rgb(242, 242, 242);
                padding: 12px 16px;
                margin: 8px 0px;
            }
        </style>
    </head>
    <body>
        <h3>You have logged into Microsoft Azure!</h3>
        <p>You can close this window, or we will redirect you to the <a href="https://docs.microsoft.com/cli/azure/">Azure CLI documentation</a> in 1 minute.</p>
        <h3>Announcements</h3>
        <p>[Windows only] Azure CLI is collecting feedback on using the <a href="https://learn.microsoft.com/windows/uwp/security/web-account-manager">Web Account Manager</a> (WAM) broker for the login experience.</p>
        <p>You may opt-in to use WAM by running the following commands:</p>
        <code>
            az config set core.allow_broker=true<br>
            az account clear<br>
            az login
        </code>
    </body>
    </html>
    ```

4. Close the current terminal and open the original terminal. You should see a JSON list of your subscriptions.
5. Copy the `id` field of the subscription you want to use.
6. Set your subscription using the [`az account set`][az-account-set] command.

    ```azurecli-interactive
    az account set --subscription <subscription_id>
    ```

[install-azure-cli]: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
[az-login]: https://learn.microsoft.com/en-us/cli/azure/#az-login
[az-account-set]: https://learn.microsoft.com/en-us/cli/azure/account#az-account-set

## Create and deploy resources for your cluster

`azd` runs all the hooks inside of the [`azd-hooks` folder][azd-hooks-folder] to preregister, provision, and deploy the application services.

The `azd` template for this quickstart creates a new resource group with an AKS cluster and an Azure key vault. The key vault stores client secrets and runs the services in the `pets` namespace

1. Create all the application resources using the [`azd up`][azd-up] command.

    ```azdeveloper
    azd up
    ```

2. Select an Azure subscription for your billing usage.

    ```output
    ? Select an Azure Subscription to use:  [Use arrows to move, type to filter]
    > 1. My Azure Subscription (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)
    ```

3. Select a region to deploy your application to.

    ```output
    Select an Azure location to use:  [Use arrows to move, type to filter]
      1.  (South America) Brazil Southeast (brazilsoutheast)
      2.  (US) Central US (centralus)
      3.  (US) East US (eastus)
    > 43. (US) East US 2 (eastus2)
      4.  (US) East US STG (eastusstg)
      5.  (US) North Central US (northcentralus)
      6.  (US) South Central US (southcentralus)
    ```

    `azd` automatically runs the preprovisioning and postprovisioning commands to create the resources for your application. This process can take a few minutes to complete. Once complete, you should see an output similar to the following example:

    ```output
    SUCCESS: Your workflow to provision and deploy to Azure completed in 9 minutes 40 seconds.
    ```

## Test the application

When the application runs, a Kubernetes service exposes the application front end to the internet. This process can take a few minutes to complete. To manage a Kubernetes cluster, use the Kubernetes command-line client, [kubectl][kubectl]. `kubectl` is already installed during `azd up`.

1. Set your namespace as the demo namespace `pets` using the [`kubectl set-context`][kubectl-set-context] command.

    ```console
    kubectl config set-context --current --namespace=pets
    ```

2. Check the status of the deployed pods using the [`kubectl get pods`][kubectl-get] command. Make sure all pods are `Running` before proceeding.

    ```console
    kubectl get pods
    ```

3. Check for a public IP address for the store-front application and monitor progress using the [`kubectl get service`][kubectl-get] command with the `--watch` argument.

    ```console
    kubectl get service store-front --watch
    ```

    The **EXTERNAL-IP** output for the `store-front` service initially shows as *pending*:

    ```output
    NAME          TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)        AGE
    store-front   LoadBalancer   10.0.100.10   <pending>     80:30025/TCP   4h4m
    ```

4. Once the **EXTERNAL-IP** address changes from *pending* to an actual public IP address, use `CTRL-C` to stop the `kubectl` watch process.

    The following sample output shows a valid public IP address assigned to the service:

    ```output
    NAME          TYPE           CLUSTER-IP    EXTERNAL-IP    PORT(S)        AGE
    store-front   LoadBalancer   10.0.100.10   20.62.159.19   80:30025/TCP   4h5m
    ```

5. Open a web browser to the external IP address of your service to see the Azure Store app in action.

    

## Delete the cluster

Once you're finished with the quickstart, clean up unnecessary resources to avoid Azure charges.

1. Delete all the resources created in the quickstart using the [`azd down`][azd-down] command.

    ```azdeveloper
    azd down
    ```

2. Confirm your decision to remove all used resources from your subscription by typing `y` and pressing `Enter`.

    ```output
    ? Total resources to delete: 14, are you sure you want to continue? (y/N)
    ```

3. Allow purge to reuse the quickstart variables if applicable by typing `y` and pressing `Enter`.

    ```output
    [Warning]: These resources have soft delete enabled allowing them to be recovered for a period or time after deletion. During this period, their names may not be reused. In the future, you can use the argument --purge to skip this confirmation.

    ? Would you like to permanently delete these resources instead, allowing their names to be reused? (y/N)
    ```

    Once the resources are deleted, you should see an output similar to the following example:

    ```output
    SUCCESS: Your application was removed from Azure in 14 minutes 30 seconds.
    ```

> [!NOTE]
> This sample application is for demo purposes and doesn't represent all the best practices for Kubernetes applications.
> For guidance on creating full solutions with AKS for production, see [AKS solution guidance][aks-solution-guidance].

## Next steps

In this quickstart, you deployed a Kubernetes cluster and then deployed a simple multi-container application to it. This sample application is for demo purposes only and doesn't represent all the best practices for Kubernetes applications. For guidance on creating full solutions with AKS for production, see [AKS solution guidance][aks-solution-guidance].

To learn more about AKS and walk through a complete code-to-deployment example, continue to the Kubernetes cluster tutorial.

> [AKS tutorial][aks-tutorial]

[azd-hooks-folder]: https://github.com/Azure-Samples/aks-store-demo/tree/main/azd-hooks
[kubectl]: https://kubernetes.io/docs/reference/kubectl/
[kubectl-get]: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get
[kubectl-set-context]: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#config-set-context

[aks-tutorial]: https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-prepare-app
[azd-init]: https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/reference#azd-init
[azd-up]: https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/reference#azd-up
[azd-down]: https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/reference#azd-down
[azd-auth-login]: https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/reference#azd-auth-login
[azd-install]: https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/install-azd
[kubernetes-concepts]: https://learn.microsoft.com/en-us/azure/aks/concepts-clusters-workloads
[aks-solution-guidance]: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-start-here?toc=/azure/aks/toc.json&bc=/azure/aks/breadcrumb/toc.json
[baseline-reference-architecture]: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks/baseline-aks?toc=/azure/aks/toc.json&bc=/azure/aks/breadcrumb/toc.json
