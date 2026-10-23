# az aks app

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/app  
> Microsoft doc last updated: unknown

Commands to manage AKS app.

Subgroups and commands: `az_aks_app_up`

## az aks app up  (Preview; extension: aks-preview etc.)

Deploy to AKS via GitHub actions.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--acr` — Name of the Azure Container Registry to be used for pushing the image.
- `--aks-cluster` — Name of the cluster to select for deployment.
- `--branch-name` — New branch name to be created to check in files and raise a PR.
- `--change-reference` — The related change reference ID for this resource operation.
- `--do-not-wait` — Do not wait for workflow completion. Default: False.
- `--port` — Port on which your application runs. Default is 8080.
- `--repository -r` — GitHub repository URL e.g. https://github.com/azure/azure-cli.
