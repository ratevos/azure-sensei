# az ad signed-in-user

> Source: https://learn.microsoft.com/en-us/cli/azure/ad/signed-in-user  
> Microsoft doc last updated: unknown

Show graph information about current signed-in user in CLI.

Subgroups and commands: `az_ad_signed-in-user_list-owned-objects`, `az_ad_signed-in-user_show`

## az ad signed-in-user list-owned-objects

Get the list of directory objects that are owned by the user.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--type -t` — Object type filter, e.g. "application", "servicePrincipal" "group", etc.

## az ad signed-in-user show

Get the details for the currently logged-in user.
