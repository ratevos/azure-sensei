# az ad app

> Source: https://learn.microsoft.com/en-us/cli/azure/ad/app  
> Microsoft doc last updated: unknown

Manage Microsoft Entra applications.

Subgroups and commands: `az_ad_app_create`, `az_ad_app_credential`, `az_ad_app_credential_delete`, `az_ad_app_credential_list`, `az_ad_app_credential_reset`, `az_ad_app_delete`, `az_ad_app_federated-credential`, `az_ad_app_federated-credential_create`, `az_ad_app_federated-credential_delete`, `az_ad_app_federated-credential_list`, `az_ad_app_federated-credential_show`, `az_ad_app_federated-credential_update`, `az_ad_app_list`, `az_ad_app_owner`, `az_ad_app_owner_add`, `az_ad_app_owner_list`, `az_ad_app_owner_remove`, `az_ad_app_permission`, `az_ad_app_permission_add`, `az_ad_app_permission_admin-consent`, `az_ad_app_permission_delete`, `az_ad_app_permission_grant`, `az_ad_app_permission_list`, `az_ad_app_permission_list-grants`, `az_ad_app_show`, `az_ad_app_update`

## az ad app create

Create an application.

**Required parameters**

- `--display-name` — The display name of the application.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--app-roles` — The collection of roles assigned to the application. With app role assignments, these roles can be assigned to users, groups, or service principals associated with other applications. Should be JSON file path or in-line JSON string. See examples for details.
- `--change-reference` — The related change reference ID for this resource operation.
- `--enable-access-token-issuance` — Specifies whether this web application can request an access token using the OAuth 2.0 implicit flow.
- `--enable-id-token-issuance` — Specifies whether this web application can request an ID token using the OAuth 2.0 implicit flow.
- `--end-date` — Date or datetime after which credentials expire (e.g. '2017-12-31T11:59:59+00:00' or '2017-12-31'). Default value is one year after current time.
- `--identifier-uris` — Space-separated values. Also known as App ID URI, this value is set when an application is used as a resource app. The identifierUris acts as the prefix for the scopes you'll reference in your API's code, and it must be globally unique. You can use the default value provided, which is in the form `a
- `--is-fallback-public-client` — Specifies the fallback application type as public client, such as an installed application running on a mobile device. The default value is false which means the fallback application type is confidential client such as a web app.
- `--key-display-name` — Friendly name for the key.
- `--key-type` — The type of the key credentials associated with the application. Default: AsymmetricX509Cert.
- `--key-usage` — The usage of the key credentials associated with the application. Default: Verify.
- `--key-value` — The value for the key credentials associated with the application.
- `--optional-claims` — Application developers can configure optional claims in their Microsoft Entra applications to specify the claims that are sent to their application by the Microsoft security token service. For more information, see https://learn.microsoft.com/azure/active-directory/develop/active-directory-optional-
- `--public-client-redirect-uris` — Space-separated values. Specifies the URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent.
- `--requested-access-token-version` — Specifies the access token version expected by this resource. This changes the version and format of the JWT produced independent of the endpoint or client used to request the access token.
- `--required-resource-accesses` — Specifies the resources that the application needs to access. This property also specifies the set of delegated permissions and application roles that it needs for each of those resources. This configuration of access to the required resources drives the consent experience. Should be JSON file path 
- `--service-management-reference` — References application or service contact information from a Service or Asset Management database.
- `--sign-in-audience` — Specifies the Microsoft accounts that are supported for the current application.
- `--start-date` — Date or datetime at which credentials become valid (e.g. '2017-01-01T01:00:00+00:00' or '2017-01-01'). Default value is current time.
- `--web-home-page-url` — Home page or landing page of the application.
- `--web-redirect-uris` — Space-separated values. Specifies the URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent.

*Create an application.*
```azurecli
az ad app create --display-name mytestapp
```

*Create an application that can fall back to public client with Microsoft Graph delegated permission User.Read*
```azurecli
az ad app create --display-name my-public --is-fallback-public-client --required-resource-accesses @manifest.json
("manifest.json" contains the following content)
[{
    "resourceAppId": "00000003-0000-0000-c000-000000000000",
    "resourceAccess": [
        {
            "id": "e1fe6dd8-ba31-4d61-89e7-88639da4683d",
            "type": "Scope"
        }
   ]
}]
```

*Create an application with a role*
```azurecli
az ad app create --display-name mytestapp --identifier-uris https://mytestapp.websites.net --app-roles @manifest.json
("manifest.json" contains the following content)
[{
    "allowedMemberTypes": [
      "User"
    ],
    "description": "Approvers can mark documents as approved",
    "displayName": "Approver",
    "isEnabled": "true",
    "value": "approver"
}]
```

*Create an application with optional claims*
```azurecli
az ad app create --display-name mytestapp --optional-claims @manifest.json
("manifest.json" contains the following content)
{
    "idToken": [
        {
            "name": "auth_time",
            "essential": false
        }
    ],
    "accessToken": [
        {
            "name": "ipaddr",
            "essential": false
        }
    ],
    "saml2Token": [
        {
            "name": "upn",
            "essential": false
        },
        {
            "name": "extension_ab603c56068041afb2f6832e2a17e237_skypeId",
            "source": "user",
            "essential": false
        }
    ]
}
```

## az ad app delete

Delete an application.

**Required parameters**

- `--id` — Identifier uri, application id, or object id.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Delete an application. (autogenerated)*
```azurecli
az ad app delete --id 00000000-0000-0000-0000-000000000000
```

## az ad app list

List applications.

**Optional parameters**

- `--all` — List all entities, expect long delay if under a big organization.
- `--app-id` — Application id.
- `--display-name` — The display name of the application.
- `--filter` — OData filter, e.g. --filter "displayname eq 'test' and servicePrincipalType eq 'Application'".
- `--identifier-uri` — Graph application identifier, must be in uri format.
- `--show-mine` — List entities owned by the current user.

## az ad app show

Get the details of an application.

**Required parameters**

- `--id` — Identifier uri, application id, or object id.

*Get the details of an application with appId.*
```azurecli
az ad app show --id 00000000-0000-0000-0000-000000000000
```

*Get the details of an application with id.*
```azurecli
az ad app show --id 00000000-0000-0000-0000-000000000000
```

*Get the details of an application with identifier URI.*
```azurecli
az ad app show --id api://myapp
```

## az ad app update

Update an application.

**Required parameters**

- `--id` — Identifier uri, application id, or object id.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--add` — Add an object to a list of objects by specifying a path and key value pairs. Example: `--add property.listProperty <key=value, string or JSON string>`. Default: [].
- `--app-roles` — The collection of roles assigned to the application. With app role assignments, these roles can be assigned to users, groups, or service principals associated with other applications. Should be JSON file path or in-line JSON string. See examples for details.
- `--change-reference` — The related change reference ID for this resource operation.
- `--display-name` — The display name of the application.
- `--enable-access-token-issuance` — Specifies whether this web application can request an access token using the OAuth 2.0 implicit flow.
- `--enable-id-token-issuance` — Specifies whether this web application can request an ID token using the OAuth 2.0 implicit flow.
- `--end-date` — Date or datetime after which credentials expire (e.g. '2017-12-31T11:59:59+00:00' or '2017-12-31'). Default value is one year after current time.
- `--force-string` — When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON. Default: False.
- `--identifier-uris` — Space-separated values. Also known as App ID URI, this value is set when an application is used as a resource app. The identifierUris acts as the prefix for the scopes you'll reference in your API's code, and it must be globally unique. You can use the default value provided, which is in the form `a
- `--is-fallback-public-client` — Specifies the fallback application type as public client, such as an installed application running on a mobile device. The default value is false which means the fallback application type is confidential client such as a web app.
- `--key-display-name` — Friendly name for the key.
- `--key-type` — The type of the key credentials associated with the application. Default: AsymmetricX509Cert.
- `--key-usage` — The usage of the key credentials associated with the application. Default: Verify.
- `--key-value` — The value for the key credentials associated with the application.
- `--optional-claims` — Application developers can configure optional claims in their Microsoft Entra applications to specify the claims that are sent to their application by the Microsoft security token service. For more information, see https://learn.microsoft.com/azure/active-directory/develop/active-directory-optional-
- `--public-client-redirect-uris` — Space-separated values. Specifies the URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent.
- `--remove` — Remove a property or an element from a list. Example: `--remove property.list <indexToRemove>` OR `--remove propertyToRemove`. Default: [].
- `--requested-access-token-version` — Specifies the access token version expected by this resource. This changes the version and format of the JWT produced independent of the endpoint or client used to request the access token.
- `--required-resource-accesses` — Specifies the resources that the application needs to access. This property also specifies the set of delegated permissions and application roles that it needs for each of those resources. This configuration of access to the required resources drives the consent experience. Should be JSON file path 
- `--service-management-reference` — References application or service contact information from a Service or Asset Management database.
- `--set` — Update an object by specifying a property path and value to set. Example: `--set property1.property2=<value>`. Default: [].
- `--sign-in-audience` — Specifies the Microsoft accounts that are supported for the current application.
- `--start-date` — Date or datetime at which credentials become valid (e.g. '2017-01-01T01:00:00+00:00' or '2017-01-01'). Default value is current time.
- `--web-home-page-url` — Home page or landing page of the application.
- `--web-redirect-uris` — Space-separated values. Specifies the URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent.

*Update an application with Microsoft Graph delegated permission User.Read*
```azurecli
az ad app update --id e042ec79-34cd-498f-9d9f-123456781234 --required-resource-accesses @manifest.json
("manifest.json" contains the following content)
[{
    "resourceAppId": "00000003-0000-0000-c000-000000000000",
    "resourceAccess": [
        {
            "id": "e1fe6dd8-ba31-4d61-89e7-88639da4683d",
            "type": "Scope"
        }
   ]
}]
```

*declare an application role*
```azurecli
az ad app update --id e042ec79-34cd-498f-9d9f-123456781234 --app-roles @manifest.json
("manifest.json" contains the following content)
[{
    "allowedMemberTypes": [
      "User"
    ],
    "description": "Approvers can mark documents as approved",
    "displayName": "Approver",
    "isEnabled": "true",
    "value": "approver"
}]
```

*update optional claims*
```azurecli
az ad app update --id e042ec79-34cd-498f-9d9f-123456781234 --optional-claims @manifest.json
("manifest.json" contains the following content)
{
    "idToken": [
        {
            "name": "auth_time",
            "essential": false
        }
    ],
    "accessToken": [
        {
            "name": "ipaddr",
            "essential": false
        }
    ],
    "saml2Token": [
        {
            "name": "upn",
            "essential": false
        },
        {
            "name": "extension_ab603c56068041afb2f6832e2a17e237_skypeId",
            "source": "user",
            "essential": false
        }
    ]
}
```

*update an application's group membership claims to "All"*
```azurecli
az ad app update --id e042ec79-34cd-498f-9d9f-123456781234 --set groupMembershipClaims=All
```
