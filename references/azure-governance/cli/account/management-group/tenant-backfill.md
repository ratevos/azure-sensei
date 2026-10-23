# az account management-group tenant-backfill

> Source: https://learn.microsoft.com/en-us/cli/azure/account/management-group/tenant-backfill  
> Microsoft doc last updated: unknown

Backfill Tenant Subscription Operations for Management Groups.

Subgroups and commands: `az_account_management-group_tenant-backfill_get`, `az_account_management-group_tenant-backfill_start`

## az account management-group tenant-backfill get

Get the backfill status for a tenant.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Get the backfill status for a tenant.*
```azurecli
az account management-group tenant-backfill get
```

## az account management-group tenant-backfill start

Start backfilling subscriptions for a tenant.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Start backfilling subscriptions for a tenant.*
```azurecli
az account management-group tenant-backfill start
```
