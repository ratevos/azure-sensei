# az ad user

> Source: https://learn.microsoft.com/en-us/cli/azure/ad/user  
> Microsoft doc last updated: unknown

Manage Microsoft Entra users.

Subgroups and commands: `az_ad_user_create`, `az_ad_user_delete`, `az_ad_user_get-member-groups`, `az_ad_user_list`, `az_ad_user_show`, `az_ad_user_update`

## az ad user create

Create a user.

**Required parameters**

- `--display-name` — Object's display name or its prefix.
- `--password` — The password that should be assigned to the user for authentication.
- `--user-principal-name` — The user principal name (someuser@contoso.com). It must contain one of the verified domains for the tenant.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--force-change-password-next-sign-in` — Marks this user as needing to update their password the next time they authenticate. If omitted, false will be used. Default: False.
- `--immutable-id` — This property is used to associate an on-premises Active Directory user account to their Microsoft Entra user object. This property must be specified when creating a new user account in the Graph if you're using a federated domain for the user's userPrincipalName (UPN) property. NOTE: The $ and _ ch
- `--mail-nickname` — Mail alias. Defaults to user principal name.

*Create a user*
```azurecli
az ad user create --display-name myuser --password password --user-principal-name myuser@contoso.com
```

## az ad user delete

Delete a user.

**Required parameters**

- `--id` — The object ID or principal name of the user for which to get information.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Delete a user.*
```azurecli
az ad user delete --id myuser@contoso.com
```

## az ad user get-member-groups

Get groups of which the user is a member.

**Required parameters**

- `--id` — The object ID or principal name of the user for which to get information.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--security-enabled-only` — True to specify that only security groups that the entity is a member of should be returned; false to specify that all groups and directory roles that the entity is a member of should be returned. Default: False.

*Get groups of which the user is a member*
```azurecli
az ad user get-member-groups --id myuser@contoso.com
```

## az ad user list

List users.

**Optional parameters**

- `--display-name` — Object's display name or its prefix.
- `--filter` — OData filter, e.g. --filter "displayname eq 'test' and servicePrincipalType eq 'Application'".
- `--upn` — User principal name, e.g. john.doe@contoso.com.

*List all users.*
```azurecli
az ad user list
```

## az ad user show

Get the details of a user.

**Required parameters**

- `--id` — The object ID or principal name of the user for which to get information.

*Show a user.*
```azurecli
az ad user show --id myuser@contoso.com
```

## az ad user update

Update a user.

**Required parameters**

- `--id` — The object ID or principal name of the user for which to get information.

**Optional parameters**

- `--account-enabled` — Enable the user account.
- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--display-name` — Object's display name or its prefix.
- `--force-change-password-next-sign-in` — If the user must change her password on the next login.
- `--mail-nickname` — Mail alias. Defaults to user principal name.
- `--password` — User password.

*Update a user.*
```azurecli
az ad user update --id myuser@contoso.com --display-name username2
```
