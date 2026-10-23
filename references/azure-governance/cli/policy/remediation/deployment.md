# az policy remediation deployment

> Source: https://learn.microsoft.com/en-us/cli/azure/policy/remediation/deployment  
> Microsoft doc last updated: unknown

Manage resource policy remediation deployments.

Subgroups and commands: `az_policy_remediation_deployment_list`

## az policy remediation deployment list

Lists deployments for a resource policy remediation.

**Required parameters**

- `--name -n` — Name of the remediation.

**Optional parameters**

- `--management-group -m` — Name of management group.
- `--namespace` — Provider namespace (Ex: Microsoft.Provider).
- `--parent` — The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
- `--resource` — Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-type` — Resource type (Ex: resourceTypeC).
