# az aks draft

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/draft  
> Microsoft doc last updated: unknown

Commands to build deployment files in a project directory and deploy to an AKS cluster.

Subgroups and commands: `az_aks_draft_create`, `az_aks_draft_generate-workflow`, `az_aks_draft_setup-gh`, `az_aks_draft_up`, `az_aks_draft_update`

## az aks draft create  (extension: aks-preview etc.)

Generate a Dockerfile and the minimum required Kubernetes deployment files (helm, kustomize, manifests) for your project directory.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--app` — Specify the name of the helm release.
- `--change-reference` — The related change reference ID for this resource operation.
- `--create-config` — Specify the path to the configuration file.
- `--deployment-only` — Only generate deployment files (helm, kustomize, manifests) for the Kubernetes deployment.
- `--destination` — Specify the path to the project directory (default is .). Default: ..
- `--dockerfile-only` — Only generate Dockerfile for the Kubernetes deployment.
- `--language` — Specify the language used to create the Kubernetes deployment.
- `--path` — Automatically download and use the Draft binary at the specified location.

*Prompt to generate a Dockerfile and deployment files in the current directory.*
```azurecli
az aks draft create
```

*Generate only the Dockerfile in the current directory.*
```azurecli
az aks draft create --dockerfile-only=true
```

*Generate only the deployment files in the current directory.*
```azurecli
az aks draft create --deployment-only=true
```

*Generate a Dockerfile and an deployment file in a Java project with an app name at a specific project directory.*
```azurecli
az aks draft create --language=java --app=some_app --destination=/projects/some_project
```

## az aks draft generate-workflow  (extension: aks-preview etc.)

Generate a GitHub workflow for automatic build and deploy to AKS.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--branch` — Specify the GitHub branch to automatically deploy from.
- `--change-reference` — The related change reference ID for this resource operation.
- `--cluster-name` — Specify the AKS cluster name.
- `--container-name` — Specify the name of the container image.
- `--destination` — Specify the path to the project directory (default is .).
- `--path` — Automatically download and use the Draft binary at the specified location.
- `--registry-name` — Specify the path to the project directory.
- `--resource-group` — Specify the name of the Azure resource group.

*Prompt to generate a GitHub workflow in the current directory.*
```azurecli
az aks draft generate-workflow
```

*Prompt to generate a GitHub workflow in a specific project directory.*
```azurecli
az aks draft generate-workflow --destination=/projects/some_project
```

*Generate a GitHub workflow with a resource group, an AKS cluster name, a container registry name in a specific project directory.*
```azurecli
az aks draft generate-workflow --resource-group=some_rg --cluster-name=some_cluster --registry-name=some_registry --destination=/projects/some_project
```

*Generate a GitHub workflow that deploys from the main branch with a resource group, an AKS cluster name, a container registry name, and a container image name in a specific project directory.*
```azurecli
az aks draft generate-workflow --branch=main --resource-group=some_rg --cluster-name=some_cluster --registry-name=some_registry --container-name=some_image --destination=/projects/some_project
```

## az aks draft setup-gh  (extension: aks-preview etc.)

Set up GitHub OIDC for your application.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--app` — Specify the Azure Active Directory applicaton name.
- `--change-reference` — The related change reference ID for this resource operation.
- `--gh-repo` — Specify the the GitHub repository (organization/repo_name).
- `--path` — Automatically download and use the Draft binary at the specified location.
- `--provider` — Specify the cloud provider (default is azure). Default: azure.
- `--resource-group` — Specify the name of the Azure resource group.
- `--subscription-id` — Specify the Azure subscription ID.

*Prompt to setup the GitHub OIDC for a repository.*
```azurecli
az aks draft setup-gh
```

*Setup the GitHub OIDC on Azure for a specific repository.*
```azurecli
az aks draft setup-gh --provider=azure --gh-repo=some_organization/some_repo
```

*Setup the GitHub OIDC on Azure with subscription ID and resource group.*
```azurecli
az aks draft setup-gh --provider=azure --subscription-id=some_subscription --resource-group=some_rg
```

*Setup the GitHub OIDC with an application name on Azure with subscription ID and resource group for a specific repository.*
```azurecli
az aks draft setup-gh --app=some_app --provider=azure --subscription-id=some_subscription --resource-group=some_rg --gh-repo=some_organization/some_repo
```

## az aks draft up  (extension: aks-preview etc.)

Run `az aks draft setup-gh` then `az aks draft generate-workflow`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--app` — Specify the name of the application.
- `--branch` — Specify the GitHub branch to automatically deploy from.
- `--change-reference` — The related change reference ID for this resource operation.
- `--cluster-name` — Specify the AKS cluster name.
- `--container-name` — Specify the name of the container image.
- `--destination` — Specify the path to the project directory (default is .).
- `--gh-repo` — Specify the the GitHub repository (organization/repo_name).
- `--path` — Automatically download and use the Draft binary at the specified location.
- `--provider` — Specify the cloud provider (default is azure). Default: azure.
- `--registry-name` — Specify the path to the project directory.
- `--resource-group` — Specify the name of the Azure resource group.
- `--subscription-id` — Specify the Azure subscription ID.

*Prompt to setup the GitHub OIDC then generate a GitHub workflow in the current directory.*
```azurecli
az aks draft up
```

*Prompt to setup the GitHub OIDC then generate a GitHub workflow in a specific project directory.*
```azurecli
az aks draft up --destination=/projects/some_project
```

*Prompt to setup the GitHub OIDC for a specific repository then generate a GitHub workflow in a specific project directory.*
```azurecli
az aks draft up --gh-repo=some_organization/some_repo --destination=/projects/some_project
```

## az aks draft update  (extension: aks-preview etc.)

Update your application to be internet accessible.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--certificate` — Specify the URI of the Keyvault certificate to present.
- `--change-reference` — The related change reference ID for this resource operation.
- `--destination` — Specify the path to the project directory (default is .).
- `--host` — Specify the host of the ingress resource.
- `--path` — Automatically download and use the Draft binary at the specified location.

*Prompt to update the application to be internet accessible.*
```azurecli
az aks draft update
```

*Prompt to update the application to be internet accessible in a specific project directory.*
```azurecli
az aks draft update --destination=/projects/some_project
```

*Update the application to be internet accessible with a host of the ingress resource and a Keyvault certificate in a specific project directory.*
```azurecli
az aks draft update --host=some_host --certificate=some_certificate --destination=/projects/some_project
```
