# az policy metadata

> Source: https://learn.microsoft.com/en-us/cli/azure/policy/metadata  
> Microsoft doc last updated: unknown

Get policy metadata resources.

Subgroups and commands: `az_policy_metadata_list`, `az_policy_metadata_show`

## az policy metadata list

List policy metadata resources.

**Optional parameters**

- `--top` — Maximum number of records to return.

*Get all policy metadata resources.*
```azurecli
az policy metadata list
```

*Get policy metadata resources, limit the output to 5 resources.*
```azurecli
az policy metadata list --top 5
```

## az policy metadata show

Get a single policy metadata resource.

**Required parameters**

- `--name -n` — The name of the metadata resource.

*Get the policy metadata resource with the name 'ACF1000'.*
```azurecli
az policy metadata show --name ACF1000
```
