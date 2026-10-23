# az aks oidc-issuer

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/oidc-issuer  
> Microsoft doc last updated: unknown

Oidc issuer related commands.

Subgroups and commands: `az_aks_oidc-issuer_rotate-signing-keys`

## az aks oidc-issuer rotate-signing-keys

Rotate oidc issuer service account signing keys.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.
