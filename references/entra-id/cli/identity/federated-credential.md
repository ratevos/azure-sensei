# az identity federated-credential

> Source: https://learn.microsoft.com/en-us/cli/azure/identity/federated-credential  
> Microsoft doc last updated: unknown

Manage federated identity credentials under user assigned identities.

Subgroups and commands: `az_identity_federated-credential_create`, `az_identity_federated-credential_delete`, `az_identity_federated-credential_list`, `az_identity_federated-credential_show`, `az_identity_federated-credential_update`

## az identity federated-credential create

Create a federated identity credential under an existing user assigned identity.

**Required parameters**

- `--identity-name` — The name of the identity resource.
- `--name -n` — The name of the federated identity credential resource.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--audiences` — The aud value in the token sent to Azure for getting the user-assigned managed identity token. The value configured in the federated credential and the one in the incoming token must exactly match for Azure to issue the access token. Support shorthand-syntax, json-file and yaml-file. Try "??" to sho Default: ['api://AzureADTokenExchange'].
- `--change-reference` — The related change reference ID for this resource operation.
- `--claims-matching-expression-value --cme-value` — The wildcard-based expression for matching incoming claims. Cannot be used with --subject.
- `--claims-matching-expression-version --cme-version` — Specifies the version of the claims matching expression used in the expression.
- `--issuer` — The openId connect metadata URL of the issuer of the identity provider that Azure AD would use in the token exchange protocol for validating tokens before issuing a token as the user-assigned managed identity.
- `--subject` — The sub value in the token sent to Azure AD for getting the user-assigned managed identity token. The value configured in the federated credential and the one in the incoming token must exactly match for Azure AD to issue the access token. Either 'subject' or 'claimsMatchingExpression' must be defin

*Create a federated identity credential under a specific user assigned identity using subject.*
```azurecli
az identity federated-credential create --name myFicName --identity-name myIdentityName --resource-group myResourceGroup --issuer myIssuer --subject mySubject --audiences myAudiences
```

*Create a federated identity credential under a specific user assigned identity using claimsMatchingExpression.*
```azurecli
az identity federated-credential create --name myFicName --identity-name myIdentityName --resource-group myResourceGroup --issuer myIssuer --claims-matching-expression-version 1 --claims-matching-expression-value "claims['sub'] eq 'foo'" --audiences myAudiences
```

## az identity federated-credential delete

Delete a federated identity credential under an existing user assigned identity.

**Required parameters**

- `--identity-name` — The name of the identity resource.
- `--name -n` — The name of the federated identity credential resource.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Delete a federated identity credential under a specific user assigned identity.*
```azurecli
az identity federated-credential delete --name myFicName --identity-name myIdentityName --resource-group myResourceGroup
```

## az identity federated-credential list

List all federated identity credentials under an existing user assigned identity.

**Required parameters**

- `--identity-name` — The name of the identity resource.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--max-items` — Total number of items to return in the command's output. If the total number of items available is more than the value specified, a token is provided in the command's output. To resume pagination, provide the token value in `--next-token` argument of a subsequent command.
- `--next-token` — Token to specify where to start paginating. This is the token value from a previously truncated response.
- `--skiptoken` — A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls.
- `--top` — Number of records to return.

*List all federated identity credentials under an existing user assigned identity.*
```azurecli
az identity federated-credential list --identity-name myIdentityName --resource-group myResourceGroup
```

## az identity federated-credential show

Show a federated identity credential under an existing user assigned identity.

**Required parameters**

- `--identity-name` — The name of the identity resource.
- `--name -n` — The name of the federated identity credential resource.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*Show a federated identity credential under a specific user assigned identity.*
```azurecli
az identity federated-credential show --name myFicName --identity-name myIdentityName --resource-group myResourceGroup
```

## az identity federated-credential update

Update a federated identity credential under an existing user assigned identity.

**Required parameters**

- `--identity-name` — The name of the identity resource.
- `--name -n` — The name of the federated identity credential resource.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--add` — Add an object to a list of objects by specifying a path and key value pairs. Example: `--add property.listProperty <key=value, string or JSON string>`.
- `--audiences` — The aud value in the token sent to Azure for getting the user-assigned managed identity token. The value configured in the federated credential and the one in the incoming token must exactly match for Azure to issue the access token. Support shorthand-syntax, json-file and yaml-file. Try "??" to sho
- `--change-reference` — The related change reference ID for this resource operation.
- `--claims-matching-expression-value --cme-value` — The wildcard-based expression for matching incoming claims. Cannot be used with --subject.
- `--claims-matching-expression-version --cme-version` — Specifies the version of the claims matching expression used in the expression.
- `--force-string` — When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
- `--issuer` — The openId connect metadata URL of the issuer of the identity provider that Azure AD would use in the token exchange protocol for validating tokens before issuing a token as the user-assigned managed identity.
- `--remove` — Remove a property or an element from a list. Example: `--remove property.list <indexToRemove>` OR `--remove propertyToRemove`.
- `--set` — Update an object by specifying a property path and value to set. Example: `--set property1.property2=<value>`.
- `--subject` — The sub value in the token sent to Azure AD for getting the user-assigned managed identity token. The value configured in the federated credential and the one in the incoming token must exactly match for Azure AD to issue the access token. Either 'subject' or 'claimsMatchingExpression' must be defin

*Update a federated identity credential under a specific user assigned identity using subject.*
```azurecli
az identity federated-credential update --identity-name myIdentityName --name myFicName --resource-group myResourceGroup --issuer myIssuer --subject mySubject --audiences myAudiences
```

*Update a federated identity credential under a specific user assigned identity using claimsMatchingExpression.*
```azurecli
az identity federated-credential update --identity-name myIdentityName --name myFicName --resource-group myResourceGroup --issuer myIssuer --claims-matching-expression-version 1 --claims-matching-expression-value "claims['sub'] eq 'foo'" --audiences myAudiences
```
