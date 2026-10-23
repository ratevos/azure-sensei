# Kubernetes on Azure tutorial - Create an Azure Kubernetes Service (AKS) cluster

> Source: https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster  
> Microsoft doc last updated: 06/23/2026


Kubernetes provides a distributed platform for containerized applications. With Azure Kubernetes Service (AKS), you can quickly create a production-ready Kubernetes cluster.

In this tutorial, you deploy a Kubernetes cluster in AKS. You learn how to:

>
> * Deploy an AKS cluster that can authenticate to an Azure Container Registry (ACR).
> * Install the Kubernetes CLI, `kubectl`.
> * Configure `kubectl` to connect to your AKS cluster.

## Before you begin

In previous tutorials, you created a container image and uploaded it to an ACR instance. Start with [Tutorial 1 - Prepare application for AKS][aks-tutorial-prepare-app] to follow along.

This tutorial creates billable AKS cluster resources and requires an **Owner** or **Azure account administrator** role in your Azure subscription.

* If you're using Azure CLI, this tutorial requires that you're running the Azure CLI version 2.35.0 or later. Check your version with `az --version`. To install or upgrade, see [Install Azure CLI][azure-cli-install].
* If you're using Azure PowerShell, this tutorial requires that you're running Azure PowerShell version 5.9.0 or later. Check your version with `Get-InstalledModule -Name Az`. To install or upgrade, see [Install Azure PowerShell][azure-powershell-install].
* If you're using Azure Developer CLI, this tutorial requires that you're running the Azure Developer CLI version 1.5.1 or later. Check your version with `azd version`. To install or upgrade, see [Install Azure Developer CLI][azure-azd-install].

---

## Create a Kubernetes cluster

AKS clusters can use [Kubernetes role-based access control (Kubernetes RBAC)][k8s-rbac], which allows you to define access to resources based on roles assigned to users. If a user is assigned multiple roles, permissions are combined. Permissions can be scoped to either a single namespace or across the whole cluster.

To learn more about AKS and Kubernetes RBAC, see [Control access to cluster resources using Kubernetes RBAC and Microsoft Entra identities in AKS][aks-k8s-rbac].

### [Azure CLI](#tab/azure-cli)

This tutorial requires Azure CLI version 2.35.0 or later. Check your version with `az --version`. To install or upgrade, see [Install Azure CLI][azure-cli-install]. If you're using the Bash environment in Azure Cloud Shell, the latest version is already installed. 

### [Azure PowerShell](#tab/azure-powershell)

This tutorial requires Azure PowerShell version 5.9.0 or later. Check your version with `Get-InstalledModule -Name Az`. To install or upgrade, see [Install Azure PowerShell][azure-powershell-install]. If you're using Azure Cloud Shell, the latest version is already installed. 

### [Azure Developer CLI](#tab/azure-azd)

This tutorial requires Azure Developer CLI version 1.5.1 or later. Check your version with `azd version`. To install or upgrade, see [Install Azure Developer CLI][azure-azd-install].

---

## Install the Kubernetes CLI

You use the Kubernetes CLI, [`kubectl`][kubectl], to connect to your Kubernetes cluster. If you use the Azure Cloud Shell, `kubectl` is already installed. If you're running the commands locally, you can use the Azure CLI or Azure PowerShell to install `kubectl`.

### [Azure CLI](#tab/azure-cli)

* Install `kubectl` locally using the [`az aks install-cli`][az aks install-cli] command.

    ```azurecli-interactive
    az aks install-cli
    ```

### [Azure PowerShell](#tab/azure-powershell)

* Install `kubectl` locally using the [`Install-AzAksCliTool`][install-azaksclitool] cmdlet.

    ```azurepowershell-interactive
    Install-AzAksCliTool
    ```

### [Azure Developer CLI](#tab/azure-azd)

`azd` environments in a codespace automatically download all dependencies found in `./devcontainer/devcontainer.json`. This includes the Kubernetes CLI along with any Azure Container Registry (ACR) images.

* To install `kubectl` locally, use the [`az aks install-cli`][az aks install-cli] command.

    ```azurecli-interactive
    az aks install-cli
    ```

---

## Create an AKS cluster

AKS clusters can use [Kubernetes role-based access control (Kubernetes RBAC)][k8s-rbac], which allows you to define access to resources based on roles assigned to users. Permissions are combined when users are assigned multiple roles. Permissions can be scoped to either a single namespace or across the whole cluster. For more information, see [Control access to cluster resources using Kubernetes RBAC and Microsoft Entra ID in AKS][aks-k8s-rbac].

### [Azure CLI](#tab/azure-cli)

To allow an AKS cluster to interact with other Azure resources, the Azure platform automatically creates a cluster identity. In this example, the cluster identity is [granted the right to pull images][container-registry-integration] from the ACR instance you created in the previous tutorial. To execute the command successfully, you must have an **Owner** or **Azure account administrator** role in your Azure subscription.

* Create an AKS cluster using the [`az aks create`][az aks create] command. The following example creates a cluster named *myAKSCluster* in the resource group named *myResourceGroup*. This resource group was created in the [previous tutorial][aks-tutorial-prepare-acr] in the *westus2* region. We'll continue to use the environment variable, `$ACRNAME`, that we set in the [previous tutorial][aks-tutorial-prepare-acr]. If you don't have this environment variable set, set it now to the same value you used previously.

Choose one cluster option and run only the matching command block. You have two options to create an AKS cluster. See [here](https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic) for a detailed comparison.

1. **AKS Automatic** (recommended) — a fully managed Kubernetes experience that automates cluster setup, operations, and node management. Choose this option for simplified operations and to use the [AKS Desktop](https://learn.microsoft.com/en-us/azure/aks/aks-desktop-app) application UI with recommended defaults.

    Run this command block only if you chose **AKS Automatic**.
    ```azurecli-interactive
    az aks create \
        --resource-group myResourceGroup \
        --name myAKSCluster \
        --sku automatic \
        --attach-acr $ACRNAME
    
    AKS_ID=$(az aks show --resource-group myResourceGroup --name myAKSCluster --query id -o tsv)
    ENTRA_OBJECT_ID=$(az ad signed-in-user show --query id -o tsv)

    # Grant yourself admin permissions to the cluster using the Azure Kubernetes Service RBAC Cluster Admin role.
    az role assignment create --role "Azure Kubernetes Service RBAC Cluster Admin" \
        --assignee $ENTRA_OBJECT_ID \
        --scope $AKS_ID
    ```
    
1. **AKS Standard** — gives you full control over cluster configuration and node management. Choose this option if you need to customize cluster settings. To use [AKS Desktop](https://learn.microsoft.com/en-us/azure/aks/aks-desktop-app) with Standard clusters, specify [additional cluster options](https://learn.microsoft.com/en-us/azure/aks/aks-desktop-install-cluster-setup#aks-standard-clusters) at creation time.

    Run this command block only if you chose **AKS Standard**.

    > [!IMPORTANT]
    > This tutorial creates a three-node cluster. If you get an error message when trying to create the cluster, then you might need to request a quota increase for your Azure subscription or try a different Azure region. Alternatively, you can use fewer nodes, or omit the node VM size parameter to use the default VM size. For information about AKS resource limits and region availability, see [Quotas, virtual machine size restrictions, and region availability in AKS][quotas-skus-regions].

    ```azurecli-interactive
    az aks create \
        --resource-group myResourceGroup \
        --name myAKSCluster \
        --node-count 3 \
        --node-vm-size standard_l8s_v3 \
        --generate-ssh-keys \
        --attach-acr $ACRNAME
    ```

    > [!NOTE]
    > If you already generated SSH keys, you might encounter an error similar to `linuxProfile.ssh.publicKeys.keyData is invalid`. To proceed, retry the command without the `--generate-ssh-keys` parameter.

To avoid needing an **Owner** or **Azure account administrator** role, you can also manually configure a service principal to pull images from ACR. For more information, see [ACR authentication with service principals](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-auth-service-principal) or [Authenticate from Kubernetes with a pull secret](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-auth-kubernetes). Alternatively, you can use a [managed identity](https://learn.microsoft.com/en-us/azure/aks/use-managed-identity) instead of a service principal for easier management.

### [Azure PowerShell](#tab/azure-powershell)

To allow an AKS cluster to interact with other Azure resources, the Azure platform automatically creates a cluster identity. In this example, the cluster identity is [granted the right to pull images][container-registry-integration] from the ACR instance you created in the previous tutorial. To execute the command successfully, you need to have an **Owner** or **Azure account administrator** role in your Azure subscription.

* Create an AKS cluster using the [`New-AzAksCluster`][new-azakscluster] cmdlet. The following example creates a cluster named *myAKSCluster* in the resource group named *myResourceGroup*. This resource group was created in the [previous tutorial][aks-tutorial-prepare-acr] in the *westus2* region.

    ```azurepowershell-interactive
    New-AzAksCluster -ResourceGroupName myResourceGroup -Name myAKSCluster -NodeCount 3 -NodeVmSize standard_l8s_v3 -GenerateSshKey -AcrNameToAttach $ACRNAME
    ```

    > [!NOTE]
    > If you already generated SSH keys, you might encounter an error similar to `linuxProfile.ssh.publicKeys.keyData is invalid`. To proceed, retry the command without the `-GenerateSshKey` parameter.

To avoid needing an **Owner** or **Azure account administrator** role, you can also manually configure a service principal to pull images from ACR. For more information, see [ACR authentication with service principals](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-auth-service-principal) or [Authenticate from Kubernetes with a pull secret](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-auth-kubernetes). Alternatively, you can use a [managed identity](https://learn.microsoft.com/en-us/azure/aks/use-managed-identity) instead of a service principal for easier management.

### [Azure Developer CLI](#tab/azure-azd)

`azd` packages the deployment of clusters with the application itself using the `azd up` command. This command is covered in the [Deploy containerized application](https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-application) tutorial.

If you're using this path, skip AKS cluster creation commands in this tutorial and continue to the next tutorial.

---

## Connect to cluster using kubectl

### [Azure CLI](#tab/azure-cli)

1. Configure `kubectl` to connect to your Kubernetes cluster using the [`az aks get-credentials`][az aks get-credentials] command. The following example gets credentials for the AKS cluster named *myAKSCluster* in *myResourceGroup*.

    ```azurecli-interactive
    az aks get-credentials --resource-group myResourceGroup --name myAKSCluster
    ```

2. Verify connection to your cluster using the [`kubectl get nodes`][kubectl-get] command, which returns a list of cluster nodes.

    ```azurecli-interactive
    kubectl get nodes
    ```

    The following example output shows a list of the cluster nodes:

    ```output
    NAME                                STATUS   ROLES   AGE   VERSION
    aks-nodepool1-19366578-vmss000000   Ready    agent   47h   v1.30.9
    aks-nodepool1-19366578-vmss000001   Ready    agent   47h   v1.30.9
    aks-nodepool1-19366578-vmss000002   Ready    agent   47h   v1.30.9
    ```

### [Azure PowerShell](#tab/azure-powershell)

1. Configure `kubectl` to connect to your Kubernetes cluster using the [`Import-AzAksCredential`][import-azakscredential] cmdlet. The following example gets credentials for the AKS cluster named *myAKSCluster* in *myResourceGroup*.

    ```azurepowershell-interactive
    Import-AzAksCredential -ResourceGroupName myResourceGroup -Name myAKSCluster
    ```

2. Verify connection to your cluster using the [`kubectl get nodes`][kubectl-get] command, which returns a list of cluster nodes.

    ```azurepowershell-interactive
    kubectl get nodes
    ```

    The following example output shows a list of the cluster nodes.

    ```output
    NAME                                STATUS   ROLES   AGE   VERSION
    aks-nodepool1-19366578-vmss000000   Ready    agent   47h   v1.30.9
    aks-nodepool1-19366578-vmss000001   Ready    agent   47h   v1.30.9
    aks-nodepool1-19366578-vmss000002   Ready    agent   47h   v1.30.9
    ```

### [Azure Developer CLI](#tab/azure-azd)

1. Configure authentication to your cluster using the [`azd auth login`][azd-auth-login] command.

    ```azdeveloper
    azd auth login 
    ```

2. Follow the directions for your auth method.

3. Verify the connection to your cluster using the [`kubectl get nodes`][kubectl-get] command.

    ```azurecli-interactive
    kubectl get nodes
    ```

    The following example output shows a list of the cluster nodes:

    ```output
    NAME                                STATUS   ROLES   AGE   VERSION
    aks-nodepool1-19366578-vmss000000   Ready    agent   47h   v1.30.9
    aks-nodepool1-19366578-vmss000001   Ready    agent   47h   v1.30.9
    aks-nodepool1-19366578-vmss000002   Ready    agent   47h   v1.30.9
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

---

## Next steps

In this tutorial, you deployed a Kubernetes cluster in AKS and configured `kubectl` to connect to the cluster. You learned how to:

>
> * Deploy an AKS cluster that can authenticate to an ACR.
> * Install the Kubernetes CLI, `kubectl`.
> * Configure `kubectl` to connect to your AKS cluster.

In the next tutorial, you learn how to deploy Azure Container Storage on your cluster and create a generic ephemeral volume. If you're using Azure Developer CLI, or if you weren't able to use a storage optimized VM type due to quota issues, proceed directly to the [Deploy containerized application](https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-application) tutorial.

> [Deploy Azure Container Storage][aks-tutorial-acstor]

[kubectl]: https://kubernetes.io/docs/reference/kubectl/
[kubectl-get]: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get
[k8s-rbac]: https://kubernetes.io/docs/reference/access-authn-authz/rbac/

[aks-tutorial-deploy-app]: https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-application
[aks-tutorial-prepare-acr]: https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-prepare-acr
[aks-tutorial-prepare-app]: https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-prepare-app
[aks-tutorial-acstor]: https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-azure-container-storage
[az aks create]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-create
[az aks install-cli]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-install-cli
[az aks get-credentials]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-get-credentials
[azure-azd-install]: https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/install-azd
[azure-cli-install]: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
[container-registry-integration]: https://learn.microsoft.com/en-us/azure/aks/cluster-container-registry-integration
[quotas-skus-regions]: https://learn.microsoft.com/en-us/azure/aks/quotas-skus-regions
[azure-powershell-install]: https://learn.microsoft.com/en-us/powershell/azure/install-az-ps
[new-azakscluster]: https://learn.microsoft.com/en-us/powershell/module/az.aks/new-azakscluster
[install-azaksclitool]: https://learn.microsoft.com/en-us/powershell/module/az.aks/install-azaksclitool
[import-azakscredential]: https://learn.microsoft.com/en-us/powershell/module/az.aks/import-azakscredential
[aks-k8s-rbac]: https://learn.microsoft.com/en-us/azure/aks/kubernetes-rbac-entra-id
[azd-auth-login]: https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/reference#azd-auth-login
