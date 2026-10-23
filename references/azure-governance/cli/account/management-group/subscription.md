# az account management-group subscription

> Source: https://learn.microsoft.com/en-us/cli/azure/account/management-group/subscription  
> Microsoft doc last updated: unknown

Subscription operations for Management Groups.

Subgroups and commands: `az_account_management-group_subscription_add`, `az_account_management-group_subscription_remove`, `az_account_management-group_subscription_show`, `az_account_management-group_subscription_show-sub-under-mg`

## az account management-group subscription add

Add a subscription to a management group.

**Required parameters**

- `--name -n` — Name of the management group.
- `--subscription -s` — Subscription Id or Name.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Add a subscription to a management group.*
```azurecli
az account management-group subscription add --name GroupName --subscription Subscription
```

## az account management-group subscription remove

Remove an existing subscription from a management group.

**Required parameters**

- `--name -n` — Name of the management group.
- `--subscription -s` — Subscription Id or Name.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Remove an existing subscription from a management group.*
```azurecli
az account management-group subscription remove --name GroupName --subscription Subscription
```

## az account management-group subscription show

Show the details of a subscription under a known management group.

**Required parameters**

- `--name -n` — Name of the management group.
- `--subscription -s` — Subscription Id or Name.

*Show the details of a subscription under a known management group.*
```azurecli
az account management-group subscription show --name GroupName --subscription Subscription
```

## az account management-group subscription show-sub-under-mg

Get the subscription under a management group.

**Required parameters**

- `--name -n` — Name of the management group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Get the subscription under a management group.*
```azurecli
az account management-group subscription show-sub-under-mg --name GroupName
```
