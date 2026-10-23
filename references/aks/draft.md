# Draft extension for Azure Kubernetes Service (AKS) (preview)

> Source: https://learn.microsoft.com/en-us/azure/aks/draft  
> Microsoft doc last updated: 06/22/2023


[Draft](https://github.com/Azure/draft) is an open-source project that streamlines Kubernetes development by taking a non-containerized application and generating the Dockerfiles, Kubernetes manifests, Helm charts, Kustomize configurations, and other artifacts associated with a containerized application. Draft can also create a GitHub Action workflow file to quickly build and deploy applications onto any Kubernetes cluster.

## How it works

Draft has the following commands to help ease your development on Kubernetes:

- `draft create`: Creates the Dockerfile and the proper manifest files.
- `draft setup-gh`: Sets up your GitHub OIDC.
- `draft generate-workflow`: Generates the GitHub Action workflow file for deployment onto your cluster.
- `draft up`: Sets up your GitHub OIDC and generates a GitHub Action workflow file, combining the previous two commands.

## Prerequisites

- If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.
- Install the latest version of the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows) and the *aks-preview* extension.
- If you don't have one already, you need to create an [AKS cluster][deploy-cluster] and an Azure Container Registry instance.

### Install the `aks-preview` Azure CLI extension

1. Install the `aks-preview` extension using the [`az extension add`][az-extension-add] command.

    ```azurecli-interactive
    az extension add --name aks-preview
    ```

2. Update the extension to make sure you have the latest version using the [`az extension update`][az-extension-update] command.

    ```azurecli-interactive
    az extension update --name aks-preview
    ```

## Create artifacts using `draft create`

You can use `draft create` to create Dockerfiles, Helm charts, Kubernetes manifests, or Kustomize files needed to deploy your application onto an AKS cluster.

- Create an artifact using the [`az aks draft create`][az-aks-draft-create] command.

    ```azure-cli-interactive
    az aks draft create
    ```

  - You can also run the command on a specific directory using the `--destination` flag, as shown in the following example:

    ```azure-cli-interactive
    az aks draft create --destination /Workspaces/ContosoAir
    ```

## Set up GitHub OIDC using `draft setup-gh`

To use Draft, you have to register your application with GitHub using `draft setup-gh`. This step only needs to be done once per repository.

- Register your application with GitHub using the [`az aks draft setup-gh`][az-aks-draft-setup-gh] command.

    ```azure-cli-interactive
    az aks draft setup-gh
    ```

## Generate a GitHub Action workflow file for deployment using `draft generate-workflow`

After you create your artifacts and set up GitHub OIDC, you can use `draft generate-workflow` to generate a GitHub Action workflow file, creating an action that deploys your application onto your AKS cluster. Once your workflow file is generated, you must commit it into your repository in order to initiate the GitHub Action.

- Generate a GitHub Action workflow file using the [`az aks draft generate-workflow`][az-aks-draft-generate-workflow] command.

    ```azure-cli-interactive
    az aks draft generate-workflow
    ```

  - You can also run the command on a specific directory using the `--destination` flag, as shown in the following example:

    ```azure-cli-interactive
    az aks draft generate-workflow --destination /Workspaces/ContosoAir
    ```

## Set up GitHub OpenID Connect (OIDC) and generate a GitHub Action workflow file using `draft up`

`draft up` is a single command to accomplish GitHub OIDC setup and generate a GitHub Action workflow file for deployment. It effectively combines the `draft setup-gh` and `draft generate-workflow` commands, meaning it's most commonly used when getting started in a new repository for the first time, and only needs to be run once. Subsequent updates to the GitHub Action workflow file can be made using `draft generate-workflow`.

- Set up GitHub OIDC and generate a GitHub Action workflow file using the [`az aks draft up`][az-aks-draft-up] command.

    ```azure-cli-interactive
    az aks draft up
    ```

  - You can also run the command on a specific directory using the `--destination` flag, as shown in the following example:

    ```azure-cli-interactive
    az aks draft up --destination /Workspaces/ContosoAir
    ```

## Use Application Routing with Draft to make your application accessible over the internet

[Application Routing][app-routing] is the easiest way to get your web application up and running in Kubernetes securely. Application Routing removes the complexity of ingress controllers and certificate and DNS management, and it offers configuration for enterprises looking to bring their own. Application Routing offers a managed ingress controller based on nginx that you can use without restrictions and integrates out of the box with Open Service Mesh to secure intra-cluster communications.

- Set up Draft with Application Routing using the [`az aks draft update`][az-aks-draft-update] and pass in the DNS name and Azure Key Vault-stored certificate when prompted.

    ```azure-cli-interactive
    az aks draft update
    ```

  - You can also run the command on a specific directory using the `--destination` flag, as shown in the following example:

    ```azure-cli-interactive
    az aks draft update --destination /Workspaces/ContosoAir
    ```

[deploy-cluster]: https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster
[app-routing]: https://learn.microsoft.com/en-us/azure/aks/app-routing
[az-extension-add]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-add
[az-extension-update]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-update
[az-aks-draft-update]: https://learn.microsoft.com/en-us/cli/azure/aks/draft#az-aks-draft-update
[az-aks-draft-up]: https://learn.microsoft.com/en-us/cli/azure/aks/draft#az-aks-draft-up
[az-aks-draft-create]: https://learn.microsoft.com/en-us/cli/azure/aks/draft#az-aks-draft-create
[az-aks-draft-setup-gh]: https://learn.microsoft.com/en-us/cli/azure/aks/draft#az-aks-draft-setup-gh
[az-aks-draft-generate-workflow]: https://learn.microsoft.com/en-us/cli/azure/aks/draft#az-aks-draft-generate-workflow
