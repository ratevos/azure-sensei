# az aks connection

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/connection  
> Microsoft doc last updated: unknown

Commands to manage aks connections.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_aks_connection_create`, `az_aks_connection_create_app-insights`, `az_aks_connection_create_appconfig`, `az_aks_connection_create_cognitiveservices`, `az_aks_connection_create_confluent-cloud`, `az_aks_connection_create_cosmos-cassandra`, `az_aks_connection_create_cosmos-gremlin`, `az_aks_connection_create_cosmos-mongo`, `az_aks_connection_create_cosmos-sql`, `az_aks_connection_create_cosmos-table`, `az_aks_connection_create_eventhub`, `az_aks_connection_create_keyvault`, `az_aks_connection_create_mongodb-atlas`, `az_aks_connection_create_mysql`, `az_aks_connection_create_mysql-flexible`, `az_aks_connection_create_mysql-flexible(serviceconnector-passwordless)`, `az_aks_connection_create_neon-postgres`, `az_aks_connection_create_postgres`, `az_aks_connection_create_postgres-flexible`, `az_aks_connection_create_postgres-flexible(serviceconnector-passwordless)`, `az_aks_connection_create_redis`, `az_aks_connection_create_redis-enterprise`, `az_aks_connection_create_servicebus`, `az_aks_connection_create_signalr`, `az_aks_connection_create_sql`, `az_aks_connection_create_sql(serviceconnector-passwordless)`, `az_aks_connection_create_storage-blob`, `az_aks_connection_create_storage-file`, `az_aks_connection_create_storage-queue`, `az_aks_connection_create_storage-table`, `az_aks_connection_create_webpubsub`, `az_aks_connection_delete`, `az_aks_connection_list`, `az_aks_connection_list-configuration`, `az_aks_connection_list-support-types`, `az_aks_connection_show`, `az_aks_connection_update`, `az_aks_connection_update_app-insights`, `az_aks_connection_update_appconfig`, `az_aks_connection_update_cognitiveservices`, `az_aks_connection_update_confluent-cloud`, `az_aks_connection_update_cosmos-cassandra`, `az_aks_connection_update_cosmos-gremlin`, `az_aks_connection_update_cosmos-mongo`, `az_aks_connection_update_cosmos-sql`, `az_aks_connection_update_cosmos-table`, `az_aks_connection_update_eventhub`, `az_aks_connection_update_keyvault`, `az_aks_connection_update_mongodb-atlas`, `az_aks_connection_update_mysql`, `az_aks_connection_update_mysql-flexible`, `az_aks_connection_update_neon-postgres`, `az_aks_connection_update_postgres`, `az_aks_connection_update_postgres-flexible`, `az_aks_connection_update_redis`, `az_aks_connection_update_redis-enterprise`, `az_aks_connection_update_servicebus`, `az_aks_connection_update_signalr`, `az_aks_connection_update_sql`, `az_aks_connection_update_storage-blob`, `az_aks_connection_update_storage-file`, `az_aks_connection_update_storage-queue`, `az_aks_connection_update_storage-table`, `az_aks_connection_update_webpubsub`, `az_aks_connection_validate`, `az_aks_connection_wait`

## az aks connection delete  (Preview)

Delete a aks connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--connection` — Name of the aks connection.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Delete a aks connection interactively*
```azurecli
az aks connection delete
```

*Delete a aks connection by connection name*
```azurecli
az aks connection delete -g ClusterRG -n MyCluster --connection MyConnection
```

*Delete a aks connection by connection id*
```azurecli
az aks connection delete --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker}
```

## az aks connection list  (Preview)

List connections of a aks.

**Optional parameters**

- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.

*List aks connections interactively*
```azurecli
az aks connection list
```

*List aks connections by source resource name*
```azurecli
az aks connection list -g ClusterRG -n MyCluster
```

*List aks connections by source resource id*
```azurecli
az aks connection list --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster}
```

## az aks connection list-configuration  (Preview)

List source configurations of a aks connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--connection` — Name of the aks connection.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.

*List a connection's source configurations interactively*
```azurecli
az aks connection list-configuration
```

*List a connection's source configurations by connection name*
```azurecli
az aks connection list-configuration -g ClusterRG -n MyCluster --connection MyConnection
```

*List a connection's source configurations by connection id*
```azurecli
az aks connection list-configuration --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker}
```

## az aks connection list-support-types  (Preview)

List client types and auth types supported by aks connections.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--target-type -t` — The target resource type.

*List all aks supported target resource types and auth types*
```azurecli
az aks connection list-support-types -o table
```

*List aks supported auth types for a specific target resource type*
```azurecli
az aks connection list-support-types --target-type storage-blob -o table
```

## az aks connection show  (Preview)

Get the details of a aks connection.

**Optional parameters**

- `--connection` — Name of the aks connection.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.

*Get a connection interactively*
```azurecli
az aks connection show
```

*Get a connection by connection name*
```azurecli
az aks connection show -g ClusterRG -n MyCluster --connection MyConnection
```

*Get a connection by connection id*
```azurecli
az aks connection show --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker}
```

## az aks connection validate  (Preview)

Validate a aks connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--connection` — Name of the aks connection.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.

*Validate a connection interactively*
```azurecli
az aks connection validate
```

*Validate a connection by connection name*
```azurecli
az aks connection validate -g ClusterRG -n MyCluster --connection MyConnection
```

*Validate a connection by connection id*
```azurecli
az aks connection validate --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker}
```

## az aks connection wait  (Preview)

Place the CLI in a waiting state until a condition of the connection is met.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--connection` — Name of the aks connection.
- `--created` — Wait until created with 'provisioningState' at 'Succeeded'. Default: False.
- `--custom` — Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running'].
- `--deleted` — Wait until deleted. Default: False.
- `--exists` — Wait until the resource exists. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--interval` — Polling interval in seconds. Default: 30.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--timeout` — Maximum wait in seconds. Default: 3600.
- `--updated` — Wait until updated with provisioningState at 'Succeeded'. Default: False.

*Wait until the connection is successfully created.*
```azurecli
az aks connection wait --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --created
```
