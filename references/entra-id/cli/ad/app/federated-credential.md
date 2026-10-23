# az ad app federated-credential

> Source: https://learn.microsoft.com/en-us/cli/azure/ad/app/federated-credential  
> Microsoft doc last updated: unknown

Manage application federated identity credentials.

Subgroups and commands: `az_ad_app_federated-credential_create`, `az_ad_app_federated-credential_delete`, `az_ad_app_federated-credential_list`, `az_ad_app_federated-credential_show`, `az_ad_app_federated-credential_update`

## az ad app federated-credential create

Create application federated identity credential.

**Required parameters**

- `--id` — Application's appId, identifierUri, or id (formerly known as objectId).
- `--parameters` — Parameters for creating federated identity credential. Should be JSON file path or in-line JSON string. See examples for details.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Create application federated identity credential.*
```azurecli
az ad app federated-credential create --id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --parameters credential.json
("credential.json" contains the following content)
{
    "name": "Testing",
    "issuer": "https://token.actions.githubusercontent.com/",
    "subject": "repo:octo-org/octo-repo:environment:Production",
    "description": "Testing",
    "audiences": [
        "api://AzureADTokenExchange"
    ]
}
```

## az ad app federated-credential delete

Delete application federated identity credential.

**Required parameters**

- `--federated-credential-id` — ID or name of the federated identity credential.
- `--id` — Application's appId, identifierUri, or id (formerly known as objectId).

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Delete application federated identity credential.*
```azurecli
az ad app federated-credential delete --id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --federated-credential-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

## az ad app federated-credential list

List application federated identity credentials.

**Required parameters**

- `--id` — Application's appId, identifierUri, or id (formerly known as objectId).

*List application federated identity credentials.*
```azurecli
az ad app federated-credential list --id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

## az ad app federated-credential show

Show application federated identity credential.

**Required parameters**

- `--federated-credential-id` — ID or name of the federated identity credential.
- `--id` — Application's appId, identifierUri, or id (formerly known as objectId).

*Show application federated identity credential with id*
```azurecli
az ad app federated-credential show --id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --federated-credential-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

*Show application federated identity credential with name*
```azurecli
az ad app federated-credential show --id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --federated-credential-id Testing
```

## az ad app federated-credential update

Update application federated identity credential.

**Required parameters**

- `--federated-credential-id` — ID or name of the federated identity credential.
- `--id` — Application's appId, identifierUri, or id (formerly known as objectId).
- `--parameters` — Parameters for creating federated identity credential. Should be JSON file path or in-line JSON string. See examples for details.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Update application federated identity credential. Note that 'name' property cannot be changed.*
```azurecli
az ad app federated-credential update --id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --federated-credential-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --parameters credential.json
("credential.json" contains the following content)
{
    "issuer": "https://token.actions.githubusercontent.com/",
    "subject": "repo:octo-org/octo-repo:environment:Production",
    "description": "Updated description",
    "audiences": [
        "api://AzureADTokenExchange"
    ]
}
```
