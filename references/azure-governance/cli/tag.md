# az tag

> Source: https://learn.microsoft.com/en-us/cli/azure/tag  
> Microsoft doc last updated: unknown

Tag Management on a resource.

Subgroups and commands: `az_tag_add-value`, `az_tag_create`, `az_tag_delete`, `az_tag_list`, `az_tag_remove-value`, `az_tag_update`

## az tag add-value

Create a tag value.

**Required parameters**

- `--name -n` — The tag name.
- `--value` — The tag value.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Create a tag value.*
```azurecli
az tag add-value --name MyTag --value MyValue
```

## az tag create

Create tags on a specific resource.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--name -n` — The name of the tag to create.
- `--resource-id` — The resource identifier for the entity being tagged. A resource, a resource group or a subscription may be tagged.
- `--tags` — The tags to be applied on the resource.

*Create a tag in the subscription.*
```azurecli
az tag create --name MyTag
```

*Create or update the entire set of tags on a subscription.*
```azurecli
az tag create --resource-id /subscriptions/{subId} --tags Dept=Finance Status=Normal
```

*Create or update the entire set of tags on a resource group.*
```azurecli
az tag create --resource-id /subscriptions/{sub-id}/resourcegroups/{rg} --tags Dept=Finance Status=Normal
```

*Create or update the entire set of tags on a resource.*
```azurecli
az tag create --resource-id /subscriptions/{sub-id}/resourcegroups/{rg}/providers/Microsoft.Compute/virtualMachines/{vmName} --tags Dept=Finance Status=Normal
```

## az tag delete

Delete tags on a specific resource.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--name -n` — The name of the tag to be deleted.
- `--resource-id` — The resource identifier for the entity being tagged. A resource, a resource group or a subscription may be tagged.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Delete a predefined tag from the subscription not associated with a resource or having no tag values.*
```azurecli
az tag delete --name MyTag
```

*Delete the entire set of tags on a subscription.*
```azurecli
az tag delete --resource-id /subscriptions/{sub-id}
```

*Delete the entire set of tags on a resource group.*
```azurecli
az tag delete --resource-id /subscriptions/{sub-id}/resourcegroups/{rg}
```

*Delete the entire set of tags on a resource. (Even using --name along with --resource-id to specify a single tag)*
```azurecli
az tag delete --resource-id /subscriptions/{sub-id}/resourcegroups/{rg}/providers/Microsoft.Compute/virtualMachines/{vmName}
```

## az tag list

List the entire set of tags on a specific resource.

**Optional parameters**

- `--resource-id` — The resource identifier for the entity being tagged. A resource, a resource group or a subscription may be tagged.

*List the entire set of tags on a subscription.*
```azurecli
az tag list --resource-id /subscriptions/{sub-id}
```

*List the entire set of tags on a resource group.*
```azurecli
az tag list --resource-id /subscriptions/{sub-id}/resourcegroups/{rg}
```

*List the entire set of tags on a resource.*
```azurecli
az tag list --resource-id /subscriptions/{sub-id}/resourcegroups/{rg}/providers/Microsoft.Compute/virtualMachines/{vmName}
```

## az tag remove-value

Deletes a predefined tag value for a predefined tag name.

**Required parameters**

- `--name -n` — The tag name.
- `--value` — The tag value.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

## az tag update

Selectively update the set of tags on a specific resource.

**Required parameters**

- `--operation` — The update operation. Options are Merge, Replace and Delete.
- `--resource-id` — The resource identifier for the entity being tagged. A resource, a resource group or a subscription may be tagged.
- `--tags` — The tags to be updated on the resource.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Selectively update the set of tags on a subscription with "merge" Operation.*
```azurecli
az tag update --resource-id /subscriptions/{sub-id} --operation merge --tags key1=value1 key3=value3
```

*Selectively update the set of tags on a resource group with "replace" Operation.*
```azurecli
az tag update --resource-id /subscriptions/{sub-id}/resourcegroups/{rg} --operation replace --tags key1=value1 key3=value3
```

*Selectively update the set of tags on a resource with "delete" Operation.*
```azurecli
az tag update --resource-id /subscriptions/{sub-id}/resourcegroups/{rg}/providers/Microsoft.Compute/virtualMachines/{vmName} --operation delete --tags key1=value1
```
