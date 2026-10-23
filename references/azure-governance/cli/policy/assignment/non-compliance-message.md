# az policy assignment non-compliance-message

> Source: https://learn.microsoft.com/en-us/cli/azure/policy/assignment/non-compliance-message  
> Microsoft doc last updated: unknown

Manage non-compliance message used by the policy assignment.

Subgroups and commands: `az_policy_assignment_non-compliance-message_create`, `az_policy_assignment_non-compliance-message_delete`, `az_policy_assignment_non-compliance-message_list`, `az_policy_assignment_non-compliance-message_show`, `az_policy_assignment_non-compliance-message_update`

## az policy assignment non-compliance-message create

Create a non-compliance message.

**Required parameters**

- `--message -m` — A custom non-compliance message.
- `--name -n` — The name of the policy assignment.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--policy-definition-reference-id -r` — The policy definition reference ID.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--scope` — The scope of the policy assignment.

*Add a non-compliance message to a policy assignment*
```azurecli
az policy assignment non-compliance-message create -g MyResourceGroup -n MyPolicyAssignment -m 'Resources must follow naming standards'
```

*Add a non-compliance message for a specific policy in an assigned policy set definition*
```azurecli
az policy assignment non-compliance-message create -g MyResourceGroup -n MyPolicySetAssignment -m 'Resources must use allowed SKUs' --policy-definition-reference-id SkuPolicyRefId
```

## az policy assignment non-compliance-message delete

Delete a non-compliance message.

**Required parameters**

- `--message -m` — A custom non-compliance message.
- `--name -n` — The name of the policy assignment.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--policy-definition-reference-id -r` — The policy definition reference ID.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--scope` — The scope of the policy assignment.

*Remove non-compliance messages from a policy assignment that contain a specific message and no policy definition reference ID*
```azurecli
az policy assignment non-compliance-message delete -g MyResourceGroup -n MyPolicyAssignment -m 'Resources must follow naming standards'
```

*Remove non-compliance messages from a policy assignment that contain a specific message and a specific policy definition reference ID*
```azurecli
az policy assignment non-compliance-message delete -g MyResourceGroup -n MyPolicySetAssignment -m 'Resources must use allowed SKUs' --policy-definition-reference-id SkuPolicyRefId
```

## az policy assignment non-compliance-message list

Retrieve non-compliance messages.

**Required parameters**

- `--name -n` — The name of the policy assignment.

**Optional parameters**

- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--scope` — The scope of the policy assignment.

*List the non-compliance messages for a policy assignment*
```azurecli
az policy assignment non-compliance-message list -g MyResourceGroup -n MyPolicyAssignment
```

## az policy assignment non-compliance-message show

Retrieve a non-compliance message.

**Required parameters**

- `--message -m` — A custom non-compliance message.
- `--name -n` — The name of the policy assignment.

**Optional parameters**

- `--policy-definition-reference-id -r` — The policy definition reference ID.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--scope` — The scope of the policy assignment.

*Show the non-compliance message from a policy assignment that contains a specific message and policy definition reference ID*
```azurecli
az policy assignment non-compliance-message show -g MyResourceGroup -n MyPolicySetAssignment -m 'Resources must use allowed SKUs' --policy-definition-reference-id SkuPolicyRefId
```

## az policy assignment non-compliance-message update

Update a non-compliance message.

**Required parameters**

- `--message -m` — A custom non-compliance message.
- `--name -n` — The name of the policy assignment.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--add` — Add an object to a list of objects by specifying a path and key value pairs. Example: `--add property.listProperty <key=value, string or JSON string>`.
- `--change-reference` — The related change reference ID for this resource operation.
- `--force-string` — When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
- `--policy-definition-reference-id -r` — The policy definition reference ID.
- `--remove` — Remove a property or an element from a list. Example: `--remove property.list <indexToRemove>` OR `--remove propertyToRemove`.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--scope` — The scope of the policy assignment.
- `--set` — Update an object by specifying a property path and value to set. Example: `--set property1.property2=<value>`.

*Update the non-compliance message for a specific policy in an assigned policy set definition*
```azurecli
az policy assignment non-compliance-message update -g MyResourceGroup -n MyPolicySetAssignment -m 'Resources may only use SKUs from [preferredSKU, anotherGoodSKU]' --policy-definition-reference-id SkuPolicyRefId
```
